class DtiTest03 :
    # data
    infoA = 10
    # constructor จะเป็นตัวทำให้ OBject ที่สร้างจากคล่สเดียวกันไม่จำเป็นต้องเหมือนกัน
    # constructor จะทำงานทุกครั้งที่สร้าง Object
    
    def __init__(self , infoB , infoC):
        self.infoB = infoB
        self.infoC = infoC
        print('Wow wow wow......')

    # method
    def showMIxAndInfo(self, mix) :
        print(self.infoA + self.infoB + self.infoC + mix)


sau1 = DtiTest03(20,30)
sau2 = DtiTest03(10,100)
sau3 = DtiTest03(20,30)