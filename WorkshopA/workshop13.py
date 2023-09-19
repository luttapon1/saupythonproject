def academicresults():
    numberschool = input('ป้อนรหัสประจำตัวนักเรียน : ')
    name = input('ป้อนชื่อนักเรียน : ')
    grade = float(input('ป้อนเกรดเฉลี่ยนักเรียน : '))
    return numberschool,name,grade

def Numberofstudent():
    numberstudent = int(input('ป้อนจำนวนที่ต้องการตรวจสอบนักเรียน : '))
    return numberstudent

    
    


def gradestudent():
    numberstudent = Numberofstudent()
    x = 1
    numberschool,name,grade = academicresults()
    if grade >= 2.00 :
            print('สอบผ่าน')
    else:
            print('สอบไม่ผ่าน') 
    while x <= numberstudent :
        numberschool,name,grade = academicresults()
        if grade >= 2.00 :
            print('สอบผ่าน')
        else:
            print('สอบไม่ผ่าน') 
        x = x + 1


gradestudent()