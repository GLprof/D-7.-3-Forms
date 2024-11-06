from django import template

register = template.Library()

BALLS = {
    'рублей': 'P',
    'доляры': '$',
}

@register.filter()

def curs(value, code='рублей'):
    """
    valuue: cost_p
    code: рублей
    """
    postfix = BALLS[code]
    return f'{value} {postfix}'
