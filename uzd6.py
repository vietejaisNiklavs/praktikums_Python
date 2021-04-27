"""
Uzrakstiet programmu Python,
lai aprēķinātu dienu skaitu starp diviem datumiem.
"""

from datetime import date
datums1 = date(2021, 3, 22)
datums2 = date(2021, 2, 13)
dienas = abs(datums1 - datums2)
print(f'starp šiem datumiem ir {dienas.days} dienas')