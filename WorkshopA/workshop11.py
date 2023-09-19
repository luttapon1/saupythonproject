def inputname():
    name = input('ป้อนชื่อ : ')
    return name 

def inputnumber():
    number = (input('ป้อนเบอร์โทรศัพท์ : '))
    time = int(input('ป้อนเวลาที่ใช้ไป : '))
    return number ,time

def Callprices():
    name = inputname()
    number,time = inputnumber()
    if time > 1 and time < 16 :
        callpeice = time*5
        print(f'คุณ {name} เบอร์ {number} เสียค่าโทร {callpeice}' )
    elif time > 15 and time < 31 :
        callpeice = time*3
        print(f'คุณ {name} เบอร์ {number} เสียค่าโทร {callpeice}' )
    else :
        callpeice = time*1.5
        print(f'คุณ {name} เบอร์ {number} เสียค่าโทร {callpeice}' )


Callprices()

