# โปรแกรมคำนวณหาพื้นที่วงกลม เส้นรอบวง และปริมาณทรงกลม จากรัศมีที่ป้อนให้ดดยผู้ใช้ทางแป้นพิมพ์ และแสดงผลพื้นที่ เส้นรอบ และปริมาตรทางหน้าจอ
# ขอ 5 ฟังก์ชัน
import math

# inputRadius
def radius():
    r = float(input('ป้อนรัศมี : '))
    return r


# calAreaCircle
def areacircle(r):
    area = math.pi * math.pow(r,2)
    return math.pi * math.pow(r,2)

# calRoundCirle 2 * PI * r
def roundcirle(r):
    round = 2 * math.pi * r
    return 2 * math.pi * r

# calCubeCirle 4 / 3 * PI * r ** 3 
def cubecirle(r):
    cube = 4 / 3 * math.pi * r ** 3
    return 4 / 3 * math.pi * r ** 3

# showResul
def show(r):
    print(f'วงกลมที่มีรัศมี {r} ซม. มีพื้นที่ {areacircle(r):.2f} ซม. เส้นรอบวง {roundcirle(r):.2f} ซม. และปริมาตร {cubecirle(r):.2f} ซม.' )

r = radius()
show(r)


