from django import template
 
register = template.Library()

@register.filter(name='censor')
def censor(text):
    censors_words = ["успешным", "дольше", "следующем", "плохая", "ужасная", "сумасшедшая"]
    for word in censors_words:
        text = text.replace(word, '*' * len(word))
    return text