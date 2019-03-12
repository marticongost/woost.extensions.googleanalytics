"""

.. moduleauthor:: Martí Congost <marti.congost@whads.com>
"""
from cocktail.translations import translations
from woost.models import Permission

translations.load_bundle("woost.extensions.googleanalytics.readreportspermission")


class ReadReportsPermission(Permission):
    pass

