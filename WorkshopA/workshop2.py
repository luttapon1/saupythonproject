def inputtestscore():
    name = input('ชื่อ : ')
    number = input('รหัสประจำตัว : ')
    return name , number

def test():
    testscoreone = int(input('คะแนนสอบครั่งที่1 : '))
    testsceretwo = int(input('คะแนนสอบครั่งที่2 : '))
    testscerethree = int(input('คะแนนสอบครั่งที่3 : '))
    return testscoreone, testsceretwo, testscerethree 

def averragetestscroe(testscoreone, testsceretwo, testscerethree ,name , number):
    averragetestscroe = (testscoreone+testsceretwo+testscerethree) / 3
    print(f'ชือ่ {name} รหัส {number} ได้คะแนนเฉลี่ย {averragetestscroe}')


name , number = inputtestscore()
testscoreone, testsceretwo, testscerethree = test()
averragetestscroe(testscoreone, testsceretwo, testscerethree ,name , number)

