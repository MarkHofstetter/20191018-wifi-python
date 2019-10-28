import re

address = 'Schulgasse 234; 1090 gars am kamp, Stiege 27'

data = re.search(r'(\w+gasse)', address)
print(data.group(1))

data = re.search(r'(\d{2})(\d{2})', address)
print(data.group(1))
print(data.group(2))
