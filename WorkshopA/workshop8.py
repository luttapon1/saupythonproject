def inputprovince():
    province = input('ป้อนชื่อจังหวัด : ')
    return province
    
def inputPH():
    PH = int(input('ป้อนค่าPH : '))
    return PH

def checkPH():
    PH = inputPH()
    if PH >= 7 and PH < 9 :
        print('Result is Normal')
    elif PH > 8 :
        print('Result is Acid')
    else :
        print('Result is Alkali')

province = inputprovince()
checkPH()
print(province)






