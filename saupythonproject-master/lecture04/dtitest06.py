product = (input("กรอกชื่อสินค้า"))
price = float(input("กรอกราคาสินค้า(ต้นทุน)"))
total = (price)+(price*10)/100
print(f"สินค้า {product} ที่มีราคาต้นทุน {price} บาท จะขายสินค้าได้ในราคา {total} บาท")