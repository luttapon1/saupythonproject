# คุณสมบัติ Inheritance สืบทอด คือ การที่คลาสหนึ่ง สืบทอดอีกคลาสหนึ่ง *** (re-use)
# สืบทอด มีแม่ (super class) มีลูก (sub class)

# คุณสมบัติเด่น Polymorphism (พ้องรูป) คือการที่คลาสลูก เอาเมธอดของแม่มาเขียนใหม่

class Sau01 :
    infoA = 10

    def showHi():
        print('Hi..........')


class Sau02(Sau01) :
    infoB = 20

    def showHey():
        print('Hey..........')

    # overiding method : Polymorphism
    def showHi():
        print('Hi Hi Hi..........')



ob1 = Sau01()
ob2 = Sau02()
ob2.showHi()
