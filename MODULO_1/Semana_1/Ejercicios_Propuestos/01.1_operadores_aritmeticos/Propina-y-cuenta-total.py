# Cálculo de propina y cuenta total

costocomida = float(input("¿Cuánto costó la comida? $"))

propina10 = costocomida * 0.10
propina15 = costocomida * 0.15
propina20 = costocomida * 0.20

total10 = costocomida + propina10
total15 = costocomida + propina15
total20 = costocomida + propina20

print("Propina del 10%: $", round(propina10, 2))
print("Propina del 15%: $", round(propina15, 2))
print("Propina del 20%: $", round(propina20, 2))

print("Total a pagar con propina del 10%: $", round(total10, 2))
print("Total a pagar con propina del 15%: $", round(total15, 2))
print("Total a pagar con propina del 20%: $", round(total20, 2))
