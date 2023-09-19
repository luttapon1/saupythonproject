def inputpersonnel():
    on = input('ป้อนเลขประจำตัว :')
    personnel = input('ป้อนชื่อ : ')
    return on , personnel

def salarys():
    salary = int(input('ป้อนเงินเดือน : '))
    return salary


def netsalary(on , personnel , salary):
    netsalary = (salary + ((salary*7)/100))-500
    print(f'เลขประจำตัว {on} ชื่อ {personnel} ได้เงินเดือนสุทธิ {netsalary} ')

on , personnel = inputpersonnel()
salary = salarys()
netsalary(on , personnel , salary)
