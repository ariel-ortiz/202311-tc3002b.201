import re

m = re.search(r'(?P<inicial>\w)(?P<resto>\w*)', 'hola')
if m:
    print(m.group('inicial'))
    print(m.group('resto'))
