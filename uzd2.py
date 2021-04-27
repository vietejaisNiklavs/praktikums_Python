""" 
Uzrakstiet programmu, kas ielasa vienu vārdu 
un izvada uz ekrāna sveicienu sekojošā formātā:
"Labdien, vards, pimrdienā!"
Ja ievadīts nav jūsu vards, tiek izdrukāts teksts - Uzredzēšanos!
Pārbaudiet programmas darbību ar dažādiem ievaddatiem.
"""

vards=str(input("Ievadi vārdu: "))
mans_vards="Niklāvs"
if vards== mans_vards:
    print(f"Labrīt, {vards} ,pirmdienā!")
else:
    print("Uz redzēšanos!")
