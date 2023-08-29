emp_name = input('ป้อนชื่อพนักงาน : ')
sale_price = input('ป้อนยอดขาย : ')
print('--------------')
#ฟังก์ชันแปลง String เป็น number -> int( ), float( )
commission = float(sale_price) * 10/100

print(f'คุณ {emp_name} ยอดขาย {float(sale_price):.2f} บาท ได้ค่าคอม {commission:.2f} บาท')

print('คุณ',emp_name,'ยอดขาย',format(float(sale_price),".2f"),'บาทได้ค่าคอม',format(commission,".2f"),'บาท') 
#,
print('คุณ'+' '+emp_name+' '+'ยอดขาย'+' '+str(format(float(sale_price),".2f"))+' '+'บาทได้ค่าคอม'+' '+str(format(float(commission), ' .2f'))+' '+'บาท')
#+
print('คุณ {} ยอดขาย {} บาท ได้ค่าคอม {} บาท'.format(emp_name, format(float(sale_price), ".2f"), format(commission,".2f")))
#format
