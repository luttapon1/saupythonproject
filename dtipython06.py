# คำสั่ง return ที่ไม่มีอะไรต่อท้าย หมายถึง การบ่งบอกการทำงานนั้นๆ ว่าเสร็จแล้ว
def examolet():
    print(111)
    print(222)
    return
    print(3333)
    print(5555)
    return


# Default Parameter
def dtiTest(x, y, z = 20, a = 10):
    print(f'{x} + {y} + {z} + {a} = {x+y+z+a}')

dtiTest(5,100)