#-*- coding: utf-8 -*-
"""

.. moduleauthor:: Martí Congost <marti.congost@whads.com>
"""
from cocktail.events import when
from cocktail.translations import translations
from woost.admin.sections import Folder, CRUD, Settings
from woost.admin.sections.contentsection import ContentSection
from woost.extensions.googleanalytics.view import View

translations.load_bundle("woost.extensions.googleanalytics.admin.sections")


class GoogleAnalyticsSection(Folder):

    icon_uri = (
        "woost.extensions.googleanalytics.admin.ui://"
        "images/google-analytics.svg"
    )

    def _fill(self):
        self.append(GoogleAnalyticsSettings("settings"))
        self.append(CRUD("views", model = View))


class GoogleAnalyticsSettings(Settings):

    icon_uri = (
        "woost.extensions.googleanalytics.admin.ui://"
        "images/google-analytics.svg"
    )

    members = [
        "x_googleanalytics_account",
        "x_googleanalytics_domain",
        "x_googleanalytics_language",
        "x_googleanalytics_custom_definitions"
    ]


@when(ContentSection.declared)
def fill(e):
    e.source.append(GoogleAnalyticsSection("google-analytics"))

