from django import template

register=template.Library()

def swap(value):
    return value.swapcase()

def count(value,sc):
    return value.lower().count(sc.lower())

@register.filter()
def delete(value,dc):
    return value.lower().replace(dc,'')


register.filter('swap',swap)
register.filter('count',count)
