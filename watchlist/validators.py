from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _, ngettext_lazy
from django.core.validators import BaseValidator


@deconstructible
class MaxValueValidator(BaseValidator):
    message = _('Ensure this value is less than or equal to %(limit_value)s.')
    code = 'max_value'

    def compare(self, a, b):
        return a > b


@deconstructible
class MinValueValidator(BaseValidator):
    message = _('Ensure this value is greater than or equal to %(limit_value)s.')
    code = 'min_value'

    def compare(self, a, b):
        return a < b


@deconstructible
class MinLengthValidator(BaseValidator):
    message = ngettext_lazy(
        'Ensure this value has at least %(limit_value)d character (it has %(show_value)d).',
        'Ensure this value has at least %(limit_value)d characters (it has %(show_value)d).',
        'limit_value')
    code = 'min_length'

    def compare(self, a, b):
        return a < b

    def clean(self, x):
        return len(x)


@deconstructible
class MaxLengthValidator(BaseValidator):
    message = ngettext_lazy(
        'Ensure this value has at most %(limit_value)d character (it has %(show_value)d).',
        'Ensure this value has at most %(limit_value)d characters (it has %(show_value)d).',
        'limit_value')
    code = 'max_length'

    def compare(self, a, b):
        return a > b

    def clean(self, x):
        return len(x)
