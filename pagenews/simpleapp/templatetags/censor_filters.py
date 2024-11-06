from django import template

register = template.Library()

CENSURA = ['яндекс', 'попса',]

@register.filter()
def censura(value):
    """
    value: text_p
    """
    words = value.split()
    for i in range(len(words)):
        if words[i].lower() in CENSURA:
            words[i] = words[i][0] + '*' * (len(words[i]) - 1)

    return ' '.join(words)
