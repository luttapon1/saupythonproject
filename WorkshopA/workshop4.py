def inputxequation():
    xequation = int(input('ป้อนค่า X : '))
    return xequation

def EquationY(xequation):
    EquationYs = (2*(xequation**2)) + (2*xequation)+1
    return EquationYs

def show(EquationYs):
    print(f'ได้สมการ = {EquationYs}')



xequation = inputxequation()
EquationYs = EquationY(xequation)
show(EquationYs)