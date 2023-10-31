# คุณสมบัติ Encapsulation (ห่อหุ้ม)
class DtiTest05:
    # data
    infoA = 10 #ไม่ได้ห่อหุ้ม
    __infoB = 20 #Encap ดูจาก__ ---> เป็นการกำหนด access_modifier เป็น private

    def __init__(self , infoC , infoD):
        self.infoC = infoC
        self.__infoD = infoD

    # เมื่อใดก็ตาม Encap จะต้องมีเมธอด 2 ตัวเสมอ คือ get , set ของ data ตัวนั้น
    def setInfoB(self , infoB) :
        self.__infoB = infoB

    def getInfoB(self) :
        return self.__infoB
    
    def setInfoD(self , infoD) :
        self.__infoD = infoD

    def getInfoD(self) :
        return self.__infoD

    def showInfo(self):
        print(self.infoA, end='')
        print(self.__infoB, end='')
        print(self.infoC, end='')
        print(self.__infoD)
        print('-------------')


ob1 = DtiTest05(30 ,40)
ob2 = DtiTest05(30 ,100)
ob1.showInfo()
ob1.InfoA = 555
# ob1.__infoB = 999  ไม่เปลี่ยนค่า เพราะมันถูก Encap
ob1.setInfoB(999)
ob1.showInfo()
# print(ob1.__infoB + ob1.__infoD) มันถูก Encap ถ้าจะเอาค่าที่เก็บมาใช้งานต้องใช้เมธอด get
print(ob1.getInfoB() + ob1.getInfoD())
        