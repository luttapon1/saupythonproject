# เขียนข้อมูลลงไฟล์
f_dti = open('myfile01.txt' , 'a' , encoding='utf-8') #เขียนต่อจากไฟล์เดิม
f_dti.write('EEEEE....\n')
f_dti.write('FFFFF.....\n')

f_dti.close()

print('บันทึกข้อมูลลงไฟล์เรียบร้อยแล้ว')