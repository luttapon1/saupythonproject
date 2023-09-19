def inputborrowmoney():
    name = input('ป้อนชื่อ : ')
    return name


def inputmoney():
    money = int(input('ป้อนจำนวนเงินที่กู้ : '))
    return money


def interest(name , money):
    if money < 1000:
         interestT = ((money*2.5)/100)
         print(f'ชื่อ {name} คิดดอกเบี้ย {interestT}')
    else:
        interestF = ((money*5.5)/100)
        print(f'ชื่อ {name} โดนคิดดอกเบี้ย {interestF}')


name = inputborrowmoney()
money = inputmoney()
interest(name , money)

    