#-*- coding: utf-8 -*-
u"""

.. moduleauthor:: Martí Congost <marti.congost@whads.com>
"""
from cocktail.translations import translations
from cocktail import schema
from woost.models import Document

translations.load_bundle("woost.extensions.googleanalytics.document")

Document.add_member(
    schema.Boolean("x_googleanalytics_tracking_enabled",
        default = True,
        required = True,
        listed_by_default = False,
        member_group = "meta"
    )
)

Document.x_googleanalytics_tracking_should_track = \
    lambda self: self.x_googleanalytics_tracking_enabled

