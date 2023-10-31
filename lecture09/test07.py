import test06
import math
# import test08
from test08 import calCircleArea , calSquareArea ,calTriangleArea


print(f'ผลรวมของ 10 + 20 = {test06.sumnumber(10,20)}')

test06.showHi()

print(f'ราคาสินค้า 2000 ภาษีเป็นเงิน {2000 * test06.VAT}')



print(f'7 ยกกำลัง 15 มีค่า {math.pow(7, 15)}')

print(f'พื้นที่วงกลม รัสมี 3 มีค่า {math.pi * math.pow(3 , 2)}')




print(f'พื้นที่วงกลม รัสมี 8 มีค่า {calCircleArea(8)}')

print(f'พื้นที่สี่เหลี่ยม กว้าง 10 ยาว 5 มีค่า {calSquareArea(10,5)}')





