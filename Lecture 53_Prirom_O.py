def vatCalculate(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result

totalPrice = int(input("ใส่ราคาสินค้า: "))
print(vatCalculate(totalPrice))