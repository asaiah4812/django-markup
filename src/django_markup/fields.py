from django.db.models.fields import CharField, TextField
from django.utils.translation import ugettext_lazy
from django.core.exceptions import ImproperlyConfigured
from django_markup.markup import formatter

class MarkupField(CharField):
    def __init__(self, default=None, formatter=formatter, *args, **kwargs):
        # Check that the default value is a valid filter
        if default and default not in formatter.filter_list:
            raise ImproperlyConfigured("'%s' is not a registered markup filter. Registered filters are: %s." %
                                      (default, ', '.join(formatter.filter_list.iterkeys())))

        kwargs.setdefault('max_length', 255)
        kwargs.setdefault('choices', formatter.choices())
        kwargs.setdefault('verbose_name', ugettext_lazy('markup'))
        CharField.__init__(self, default, *args, **kwargs)