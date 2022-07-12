import string


values = {'var': 'foo'}

t = string.Template('$var is here but $missing is not provided')

try:
    print('substitute()     :', t.substitute(values))
except KeyError as key_error:
    print('ERROR:', str(key_error))
