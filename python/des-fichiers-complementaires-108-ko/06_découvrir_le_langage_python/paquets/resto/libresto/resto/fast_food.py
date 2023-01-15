MENU = [
        [ "Hamburger", 10 ],
        [ "CheeseBurger", 10 ],
        [ "Frites", 3 ],
        [ "Ketchup", 0 ]
    ]

def menu():
    print(" Notre menu : \n")
    for plat in MENU:
        desc = plat.pop(0)
        prix = plat.pop(0)
        print(" %20s : %5.2f euros" % (desc, prix))


if __name__ == '__main__':
    menu()

