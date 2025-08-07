# qa_platform/templatetags/custom_filters.py

from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(value, arg):
    """
    Adds a CSS class to a form field.
    """
    css_classes = value.field.widget.attrs.get('class', '')
    if css_classes:
        css_classes = css_classes.split(' ')
    else:
        css_classes = []
    
    args = arg.split(' ')
    for cls in args:
        if cls not in css_classes:
            css_classes.append(cls)
            
    return value.as_widget(attrs={'class': ' '.join(css_classes)})
