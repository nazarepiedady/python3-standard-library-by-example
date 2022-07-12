import string


values = { 'var': 'foo' }

t = string.Template('''
Variable        : $var
Escape          : $$
Variable in Text: ${var}iable
''')

print('TEMPLATE:', t.substitute(values))
