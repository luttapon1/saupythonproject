
wide = float(input("กรอกความกว้างของกล่อง(ซม.):"))
long = float(input("กรอกความยาวของกล่อง(ซม.):"))
high = float(input("กรอกความสูงของกล่อง(ซม.):"))
total_area = round((wide*long*2)+(wide*high*2)+(long*high*2)/5)
print("---------------")

print("กล่องที่กว้าง",wide,"ยาว",long,"สูง","ต้องใช้จำนวนสี",total_area,"แกลอน")
print("กล่องที่กว้าง"+" "+str(wide)+" "+"ยาว"+" "+str(long)+" "+"สูง"+" "+"ต้องใช้จำนวนสี"+" "+str(total_area)+" "+"แกลอน")
print("กล่องที่กว้าง {} ยาว {} สูง ต้องใช้จำนวนสี {} แกลแน".format(wide , long , total_area))
print(f'กล่องที่กว้าง {wide} ยาว {long} สูง ต้องใช้จำนวนสี {total_area} แกลอน')




