#-*- coding: utf-8 -*-
"""

.. moduleauthor:: Martí Congost <marti.congost@whads.com>
"""
from woost.models import ExtensionAssets, Configuration, Role
from .customdefinition import CustomDefinition
from .readreportspermission import ReadReportsPermission


def create_default_custom_definitions():

    assets = ExtensionAssets("googleanalytics")

    Configuration.instance.x_googleanalytics_custom_definitions = [
        assets.require(
            CustomDefinition,
            "default_custom_definitions.locale",
            title = assets.TRANSLATIONS,
            identifier = "woost.locale",
            initialization =
                "from cocktail.translations import get_language\n"
                "value = get_language()"
        ),
        assets.require(
            CustomDefinition,
            "default_custom_definitions.roles",
            title = assets.TRANSLATIONS,
            identifier = "woost.roles",
            initialization =
                "from woost import app\n"
                "value = set(app.user.iter_roles())"
        ),
        assets.require(
            CustomDefinition,
            "default_custom_definitions.path",
            title = assets.TRANSLATIONS,
            identifier = "woost.path",
            initialization =
                "value = reversed(list(publishable.ascend_tree(True)))"
        ),
        assets.require(
            CustomDefinition,
            "default_custom_definitions.publishable",
            title = assets.TRANSLATIONS,
            identifier = "woost.publishable",
            initialization =
                "value = publishable"
        ),
        assets.require(
            CustomDefinition,
            "default_custom_definitions.type",
            title = assets.TRANSLATIONS,
            identifier = "woost.type",
            initialization =
                "from woost.models import Publishable\n"
                "value = [\n"
                "   cls\n"
                "   for cls in publishable.__class__.__mro__\n"
                "   if cls is not Publishable and issubclass(cls, Publishable)\n"
                "]"
        ),
        assets.require(
            CustomDefinition,
            "default_custom_definitions.target",
            title = assets.TRANSLATIONS,
            identifier = "woost.target",
            initialization =
                "value = publishable"
        )
    ]

def grant_read_reports_permission():
    for role_qname in (
        "woost.administrators",
        "woost.editors"
    ):
        role = Role.get_instance(qname = role_qname)
        if role:
            role.permissions.append(ReadReportsPermission.new())

def install():
    """Creates the assets required by the googleanalytics extension."""
    create_default_custom_definitions()
    grant_read_reports_permission()

