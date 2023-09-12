# โปรแกรมตรวจสอบน้ำหนักรถบรรทุกของด่านชั่งน้ำหนักว่ารถบรรทุกนั้นมีผ่านเกณฑ์หรือไม่
# หากเกิน 1000 kg ให้แสดงว่า 'รถน้ำหนักไม่ผ่านเกณฑ์' 
# หากน้ำหนักน้อยกว่า 1000 kg ให้แสดงว่า 'รถน้ำหนักผ่านเกณฑ์' 
# โดยป้อนทะเบียนรถและน้ำหนักทางแป้นพิมพ์

# วิเคราะห์
# มองหา feature การทำงานว่ามีอะไรบ้าง เพื่อสร้าง function
# รับค่าทะเบียนรถ น้ำหนักรถ -> inputCarDetial
# ตรวจสอบน้ำหนักรถ แสดงผล -> checkCarAndShowWeight

def inputCarDetial():
    carNO = input('ป้อนทะเบียนรถ : ')
    carWeight = float(input('ป้อนน้ำหนักรถ : '))
    return carNO , carWeight

def checkCarAndShowWeight(carNo,carWeight):
    if carWeight > 1000:
        print(f'รถบรรทุกทะเบียน {carNo} รถน้ำหนักไม่ผ่านเกณฑ์')
    else:
        print(f'รถบรรทุกทะเบียน {carNo} รถน้ำหนักผ่านเกณฑ์')

print('---------------------------')
print('--* Truck Checker ')
print('---------------------------')
carNo , carWeight = inputCarDetial()
print('---------------------------')
checkCarAndShowWeight(carNo,carWeight)
print('---------------------------')
