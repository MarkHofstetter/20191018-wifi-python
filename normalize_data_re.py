import re

address = ' Schulg.    234;       1090    gars am kamp, Stiege 27  '
address = address.strip()
address = re.sub(r'\s+', ' ', address)
address = re.sub(r'g\.', 'gasse', address)

print("[%s]" % (address))
