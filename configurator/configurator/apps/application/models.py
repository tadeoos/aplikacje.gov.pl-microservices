from django.db import models

from configurator.apps.resource.models import Resource


class AppResource(Resource):
    """An installed application."""
    required_resource = models.ForeignKey(
        Resource,
        blank=True, null=True,
        related_name='required_by_apps'
    )

    def requirements(self):
        return frozenset([self.required_resource])

    def optional_requirements(self):
        return frozenset()
