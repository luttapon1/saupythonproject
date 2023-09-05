#คำนวนเงินที่จะแชร์กัน ป้อนเงิน ป้อนคนแล้วคำนวนและแสดงเงินที่จะแชร์กันทางหน้าจอ
#โดยให้เขียนเป็นฟังก์ชัน อย่างน้อย 2 ฟังก์ชัน

#รับค่า
def inputMoneyPerson():
    money = float( input('ป้อนเงิน :') )
    person = int(input('ป้อนคน :'))
    return money, person
#คำนวน
def calAndShareMoneyShare(money, person):
    formoney = format(float(money),'.2f')
    foravg = round(money/person)
    # เงิน ขอทศนิยม 2 ตำแหน่ง แชร์กันขอเป็นเลขจำนวนเต็มปัดขึ้น
    print(f'จำนวนเงิน {formoney} บาท คน {person} คน แชร์กันคนละ {foravg} บาท')
    print('จำนวนเงิน', formoney ,'บาท', 'คน',person,'คน แชร์กันคนละ', foravg , 'บาท' )
    print('จำนวนเงิน'+' '+formoney+' '+'บาท'+' '+'คน'+' '+str(person)+' '+'คน แชร์กันคนละ'+' '+str(foravg)+' '+'บาท')
    print('จำนวนเงิน {} บาท คน {} คน แชร์กันคนละ {} บาท' .format(formoney,person,foravg) )
    print('จำนวนเงิน %f บาท คน %s คน แชร์กันคนละ %i บาท' % (formoney,person,foravg))

money, person = inputMoneyPerson()
calAndShareMoneyShare(money, person)