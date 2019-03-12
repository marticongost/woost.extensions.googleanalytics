"""

.. moduleauthor:: Martí Congost <marti.congost@whads.com>
"""
import json
from cocktail.translations import translations
from cocktail.events import Event
from woost import app
from woost.models import (
    Configuration,
    Publishable,
    get_setting
)
from .utils import get_ga_custom_values


class Tracker:

    declaring_tracker = Event()

    inclusion_code = """
        <script type="text/javascript">
          (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
          (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
          m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
          })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
          %(create_tracker_command)s
          %(initialization)s
          %(commands)s
        </script>
        """

    @classmethod
    def get_analytics_script(cls, publishable = None, commands = None):

        config = Configuration.instance

        if publishable is None:
            publishable = app.publishable

        event = cls.declaring_tracker(
            publishable = publishable,
            account = get_setting("x_googleanalytics_account"),
            tracker_parameters = {},
            domain = get_setting("x_googleanalytics_domain"),
            template = cls.inclusion_code,
            values = {},
            commands = commands or []
        )

        if not event.account:
            return ""

        commands = event.commands
        parameters = {}

        if event.domain:
            event.tracker_parameters["cookieDomain"] = event.domain

        parameters["create_tracker_command"] = \
            cls._serialize_commands([(
                "create",
                event.account,
                event.tracker_parameters
            )])

        if event.values:
            commands.insert(0, ("set", event.values))

        parameters["initialization"] = (
            "woost.ga.setCustomDefinitions(%s);\n"
            "ga('set', woost.ga.getEventData(document.documentElement));" % (
                json.dumps(
                    dict(
                        (custom_def.identifier, {
                            "index": i + 1,
                            "type": custom_def.definition_type
                        })
                        for i, custom_def
                        in enumerate(config.x_googleanalytics_custom_definitions)
                        if custom_def.identifier
                    )
                )
            )
        )
        parameters["commands"] = cls._serialize_commands(commands)
        return event.template % parameters

    @classmethod
    def get_analytics_page_hit_script(cls, publishable = None):
        return cls.get_analytics_script(
            publishable = publishable,
            commands = [("send", "pageview")]
        )

    @classmethod
    def _serialize_commands(cls, commands):
        return "\n".join(
            "ga(%s);" % (", ".join(json.dumps(arg) for arg in cmd))
            for cmd in commands
        )

