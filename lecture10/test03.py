# เขียนข้อมูลลงไฟล์
f_dti = open('myfile02.txt' , 'x' , encoding='utf-8') #เขียนทับไฟล์เดิมไม่ได้
f_dti.write('SAU.....')
f_dti.write('DTI.....\n')
f_dti.write('สวัสดีทุกคน....\n')

f_dti.close

print('บันทึกข้อมูลลงไฟล์เรียบร้อยแล้ว')