"""
Izveidot funkciju, kura atgriež skaitļu kvadrātus, lietotāja norādītā apgabalā.
"""
a=int(input("ievadi skaitļu apgabala sākumu: "))
b=int(input("ievadi skaitļu apgabala beigas: "))

kvadrati = []

for i in range(a, b):
    kvadrats = i * i
    kvadrati.append(kvadrats)

print(kvadrati)