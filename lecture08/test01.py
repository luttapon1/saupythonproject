# List 
my_list = [ 10, 20 , 10, 'hi' , True , [20, 'HEllo']]
print(my_list)
print(len(my_list))

# Tuple
my_Tuple = ( 10, 20 , 10, 'hi' , True , (20, 'HEllo'))
print(my_Tuple)
print(len(my_Tuple))


# set ไม่มีลำดับ
my_set = {10 ,20 ,10 ,'Hi' ,True}
print(my_set)
print(len(my_set))


for data in my_set : 
    print(data , end='/')

print('----------------')

list_fr_set = list( my_set)
print(list_fr_set)
list_fr_set[0] = 'DTI'
my_set = set(list_fr_set)
print(my_set)

my_set.clear()
print(len(my_set))

my_set1 = {10, 20, 30, 'HI'}
my_set2 = {10, 'Hello', 'HI', True}

my_set1.add(999)
print(my_set1)
my_set1.remove('HI')
print(my_set1)

print(my_set1.intersection(my_set2))
print(my_set1.union(my_set2))


#len จำนวนของข้อมูล min น้อยสุด   max มากสุด
# print(min(my_set2)) error
