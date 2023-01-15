MENU = [
        [ "Salade Niçoise", 15 ],
        [ "Salade Lyonnaise", 14 ],
        [ "Salade de foie de volaille", 16 ],
        [ "Salade verte", 10 ],
    ]

def menu():
    print(" Notre menu : \n")
    for plat in MENU:
        desc = plat.pop(0)
        prix = plat.pop(0)
        print(" %30s : %5.2f euros" % (desc, prix))


if __name__ == '__main__':
    menu()

