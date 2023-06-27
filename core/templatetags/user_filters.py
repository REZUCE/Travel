# core/templatetags/user_filters.py
from django import template
from django.utils.safestring import SafeString

# В template.Library зарегистрированы все встроенные теги и фильтры шаблонов;
# добавляем к ним и наш фильтр.
register = template.Library()


@register.filter
def addclass(field, css):
    return field.as_widget(attrs={'class': css})


# Чтобы фильтр был доступен в шаблоне — предварительно
# загрузите его в шаблон тегом {% load user_filters %}.
# {{ form.field_name|addclass:"form-control" }}
# синтаксис @register... , под который описана функция addclass() -
# это применение "декораторов", функций, меняющих поведение функций
