menuList = []
priceList = []

def showBill():
    Total = 0
    print("---- My Food ----")
    for number in range(len(menuList)):
        print(menuList[number],priceList[number],"บาท")
        Total += priceList[number]
    print("Total: ", Total)


while True:
    menuName = input("Please Enter Menu: ")
    if menuName.lower() == "e":
        break
    else:
        menuPrice = int(input("Price: "))
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()