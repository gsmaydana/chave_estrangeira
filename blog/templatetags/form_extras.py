from django import template

register = template.Library()

@register.filter
def add_class(value, class_name):
    existing_classes = value.field.widget.attrs.get('class', '')
    new_classes = f"{existing_classes} {class_name}".strip()
    return value.as_widget(attrs={'class': new_classes})