
print(" Boucle avec break ")
for x in range(0,10):
    print(x)
    if x == 5:
        break

print(" Boucle avec continue ")
for x in range(0,10):
    if x == 5:
        print(" Ici continue")
        continue
    print(x)
