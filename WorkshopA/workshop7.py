def inputnumber():
    number = int(input('ป้อนเลขที่ต้องการ : '))
    return number 

def text():
    t = 'Correct, You are the winner'
    f = 'Not correct !!!.'
    return t,f

def check(number,t,f):
    if number == 25:
        print(t)
    else:
        print(f)


number = inputnumber()
t,f = text()
check(number, t,f)
