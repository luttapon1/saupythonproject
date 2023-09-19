def inputProduct():
    product = input('ป้อนชื่อสินค้า : ')
    price = int(input('ป้อนราคาสินค้า : '))
    return product, price

def calprice(product , price):
    productprice = price + (price*10/100)
    return productprice

def show(productprice):
    print(f'{product} = {productprice}')


product , price = inputProduct()
productprice = calprice(product , price)
show(productprice)

