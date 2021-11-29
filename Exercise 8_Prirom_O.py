Username = "ihunz"
Password = "4321"


print("----IHUNZ SHOP----")
print("กรุณาล็อคอินเพื่อเข้าสู่ระบบร้านค้า")
if Username == input("ชื่อผู้ใช้งาน: "):
    if Password == input("รหัสผ่าน: "):
        print("เข้าสู่ระบบสำเร็จ")
        print("----รายการสินค้า----")
        print("1.) Apple 30THB")
        Apple = 30
        print("2.) Banana 20THB")
        Banana = 20
        print("-----------------")
        List = input("กรุณาเลือกสินค้าที่ต้องการซื้อ: ")
        if List == "1" or "Apple" or "apple" :
            print("ซื้อ Apple")
            Amount = int(input("จำนวนสินค้า: "))
            print("----------------------")
            print("ยอดรวมราคาสินค้า:", Apple * Amount, "บาท")
            print("----------------------")
        elif List == "2" or "Banana" or "banana":
            print("ซื้อ Banana")
            Amount = int(input("จำนวนสินค้า: "))
            print("----------------------")
            print("ยอดรวมราคาสินค้า:", Banana * Amount, "บาท")
            print("----------------------")
        print("")
        print("----IHUNZ SHOP----")
        print("ขอบคุณที่มาอุดหนุน")
    else:
        print("รหัสผ่านไม่ถูกต้อง ออกจากระบบ")
else:
    print("ไม่มีชื่อผู้ใช้งาน ออกจากระบบ!")