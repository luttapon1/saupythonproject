# เขียนข้อมูลลงไฟล์
f_dti1 = open('myfile01.txt' , 'w' , encoding='utf-8') #เปิดไฟล์เพื่อเขียนข้อมูลลงไฟล์
f_dti1.write('Hello.....')
f_dti1.write('Hi.....\n')
f_dti1.write('สวัสดีทุกคน....\n')

f_dti1.close

print('บันทึกข้อมูลลงไฟล์เรียบร้อยแล้ว')