def inputpersonnel ():
    on = input('ป้อนรหัสประจำตัว : ')
    name = input('ป้อนชื่อ : ')
    return on , name

def inputsales():
    sales = int(input('ป้อนยอดขาย : '))
    return sales

def Commissions():
    sales = inputsales()

    if sales < 1000 :
        print('No Commission')
    elif sales > 1001 and sales < 2000 :
        Commissionsales = sales + (sales/100)
        print(f'Commission {Commissionsales}')
    elif sales > 2001 and sales < 3000 :
        Commissionsales = sales + ((sales*3)/100)
        print(f'Commission {Commissionsales}')
    else :
        Commissionsales = sales + ((sales*5)/100)
        print(f'Commission {Commissionsales}')

on , name = inputpersonnel()
Commissions()
print(on , name)

        

