def inputyear():
    year = int(input('ป้อนชั้นปี : '))
    return year

def textWelcome():
    year = inputyear()
    if year == 1:
        print('Welcome Freshman')
    elif year == 2 :
        print('Welcome Sophomore')
    elif year == 3 :
        print('Welcome Junior') 
    else :
        print("Welcome Senior")

def show():
    textWelcome()

show()
