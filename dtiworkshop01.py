# ใช้โปรแกรมคำนวนหาพื้นที่สามเหลี่ยม โดยรับค่าฐาน และสูงทางแป้นพิมพ์แบะแสดงผลพื้นที่ทางหน้าจอ

# มองหา feature การทำงานว่ามีอะไรบ้างเพื่อจะไปสร้าง function
# 1 รับค่า ฐาน สูง
# 2 คำนวนหาพื้นที่สามเหลี่ยมและแสดงผล






def inputBaseHigh():
    base = float (input('ป้อนความยาวของฐาน : '))
    high = float (input('ป้อนความสูง : '))
    return base , high

def calAndShowTriangleArea(base,high):
    area = base * high / 2
    print(f'สามเหลี่ยมฐาน {base:.2f} สูง {high:.2f} มีพื้นที่ {area:.2f}')

print('---------------------------')
print('--* Calculate Triangle Area')
print('---------------------------')
base,high = inputBaseHigh()
print('---------------------------')
calAndShowTriangleArea(base,high)
print('---------------------------')