# """
# Uzrakstiet Python programmu, lai iegūtu sfēras
#  ar lietotāja norādītu rādiusu tilpumu.
#  """

from math import pi

radiuss=float(input("ievadi rādiusu: "))
v=(4*pi*radiuss**3)/3

if v > 0:
    print(f'Lodes tilpums ir {v}')
else:
    print('neiespējams rādiuss')
