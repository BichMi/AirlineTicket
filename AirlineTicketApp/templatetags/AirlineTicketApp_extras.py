from django import template
from datetime import datetime, date, time, timedelta

register = template.Library()

@register.filter(name='filbookinfo')
def filbookinfo(value, arg):
    return value.replace(arg, '')

@register.filter(name='formatdate')
def formatdate(date):
    date = datetime.strptime(date, '%Y-%m-%d')
    return date.isoformat()


