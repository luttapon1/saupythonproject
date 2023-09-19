def Tourgroupleader():
    leadername = input('ป้อนชื่อหัวหน้ากรุ๊ปทัวร์ : ')
    phonenumber = input('ป้อนเบอร์โทรศัพท์ : ')
    return leadername, phonenumber

def Numberofpeople():
    numberpeople = int(input('ป้อนจำนวนคน : '))
    if numberpeople >= 1 and numberpeople <=2 :
        price = numberpeople*300
    elif numberpeople >= 3 and numberpeople <=5 :
        price = numberpeople*250
    elif numberpeople >= 6 and numberpeople <=10 :
        price = numberpeople*210
    else :
        price = numberpeople*150
    return numberpeople,price


def show():
    leadername , phonenumber = Tourgroupleader()
    numberpeople , price = Numberofpeople()
    print(f'หัวหน้ากรุ๊ปทัวร์ {leadername} เบอร์โทรศัพท์ {phonenumber} จำนวนคน {numberpeople} ต้องจ่ายเงิน {price}')


show()