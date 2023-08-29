moneyInut = input("Insert the amoount of money: ")
amountOfPeople = input("Inser rhe amount of people: ")
productValue = int(moneyInut)/float(amountOfPeople)
productValeText = format(productValue, ".2f")
print("By average you would get", productValeText, "Baht per Person.")
print("By average you would get " + productValeText + "Baht per Person.")
print(f"By average you would get {productValeText} Baht per Person.")

