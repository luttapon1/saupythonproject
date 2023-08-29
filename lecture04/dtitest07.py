number = input("กรอกรหัสพนักงาน")
name = input("กรอกชื่อพนักงาน")
salary = float(input("กรอกเงินเดือนของพนักงาน"))
net_slary = (salary)-((salary*7)/100)-500
print(f'พนักงาน {name} รหัสประจำตัว {number} จะมีเงินเดือนสุทธิ {net_slary}')