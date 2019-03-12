"""

.. moduleauthor:: Martí Congost <marti.congost@whads.com>
"""
from cocktail.events import when
from woost.controllers.cmscontroller import CMSController
from .reportcontroller import ReportController
from .tracker import Tracker

@when(CMSController.producing_output)
def handle_producing_output(e):
    publishable = e.output.get("publishable")
    if (
        publishable is None
        or getattr(publishable, "x_googleanalytics_tracking_should_track", lambda: True)()
    ):
        html = e.output.get("head_end_html", "")
        if html:
            html += " "
        html += Tracker.get_analytics_page_hit_script(publishable)
        e.output["head_end_html"] = html

CMSController.ga_report = ReportController

