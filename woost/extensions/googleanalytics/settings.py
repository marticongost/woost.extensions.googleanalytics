#-*- coding: utf-8 -*-
"""

.. moduleauthor:: Martí Congost <marti.congost@whads.com>
"""
from cocktail import schema
from cocktail.translations import translations
from woost.models import add_setting, LocaleMember
from .customdefinition import CustomDefinition

translations.load_bundle("woost.extensions.googleanalytics.settings")

add_setting(
    schema.String(
        "x_googleanalytics_account",
        text_search = False,
    )
)

add_setting(
    schema.String(
        "x_googleanalytics_domain",
        text_search = False,
    )
)

add_setting(
    LocaleMember(
        "x_googleanalytics_language"
    )
)

add_setting(
    schema.Collection(
        "x_googleanalytics_custom_definitions",
        items = schema.Reference(type = CustomDefinition)
    )
)

