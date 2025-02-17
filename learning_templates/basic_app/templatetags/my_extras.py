from django import template

register = template.Library()

@register.filter(name='cut') # 1st Option
def cut(value,arg):
    # This cut out all values of args from the string!
    return value.replace(arg,'')

# register.filter('cut',cut) # 2nd Option
 