def inputproductAndPrice():
    product = input('ชื่อสินค้า : ')
    price = int(input('ราคาสินค้า : '))
    return price,product

def Producttax(price):
    Producttaxs = ((price * 7)/100)

def show(product,price,Producttaxs):
     Producttaxs = ((price * 7)/100)
     print(f'สินค้าชื่อ {product} ราคา {price} คิดภาษี {Producttaxs}')

price,product = inputproductAndPrice()
show(product,price,Producttax)

 