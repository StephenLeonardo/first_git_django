from django import template
import re
register = template.Library()


@register.filter(name='cut')
def cut(value, arg):
    """
    This cuts out all values of arg from the string
    """

    return value.replace(arg, '')
