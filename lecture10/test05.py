# อ่านข้อมูลจากไฟล์ทั้งหมด

f_dti = open('myfile01.txt' , 'r' , encoding='utf-8') 

try :
    data = f_dti.read()

    print(data)

except Exception :
    print('ติดต่อ Admin')
finally :
    f_dti.close()
