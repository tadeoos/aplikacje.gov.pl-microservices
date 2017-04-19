from django.db import models


class Resource(models.Model):
    """Abstract resource."""

    name = models.CharField(max_length=200)
    description = models.TextField()

    def requirements(self):
        """Frozenset of resources directly required by this resource."""
        raise NotImplementedError()

    def optional_requirements(self):
        """Frozenset of resources directly optionally required by this
        resource."""
        raise NotImplementedError()

    def __str__(self):
        return self.name


class StringResource(Resource):
    value = models.TextField()

    def requirements(self):
        return frozenset()

    def optional_requirements(self):
        return frozenset()


class IntResource(Resource):
    value = models.IntegerField()

    def requirements(self):
        return frozenset()

    def optional_requirements(self):
        return frozenset()


class ListResource(Resource):
    """List of resources. All of them should be same type."""
    value = models.ManyToManyField(Resource, related_name='member_of_lists')

    def requirements(self):
        return frozenset()

    def optional_requirements(self):
        return frozenset(self.value.all())


class DictResource(Resource):
    """Dictionary of which keys are strings and values are resources."""
    def requirements(self):
        return frozenset(entry.value for entry in self.entries)

    def optional_requirements(self):
        return frozenset()

    def as_dict(self):
        return {entry.key: entry.value for entry in self.entries}


class DictResourceEntry(models.Model):
    """Single mapping string -> resource in dictionary of resources."""
    dictionary = models.ForeignKey(DictResource, related_name='entries')
    key = models.TextField()
    value = models.ForeignKey(Resource)

    def __str__(self):
        return '{} : {}'.format(self.dictionary, self.value)
