print("types of print statements")
print("lets upgrade")
name="Kaushal"
print(name)
age=2
country="India"
print(name,age,country)
marks=28.1
print('my name is :',name ,'aged :',age ,'lives in :',country ,'i got :',marks)
print("my name is : %s and im on %s old and i stay in : %s and i got :%s"%\
     (name,age,country,marks))
print("my name is : {} and im on {} old and i stay in : {} and i got : {}".format(name,age,country,marks))
print("my name is : {0} and im on {1} old and i stay in : {2} and i got : {3}".format(name,age,country,marks))
#f string
print(f"my name is : {name} and im on {age} old and i stay in : {country} and i got :{marks}")
print(f"{3+9}")
print("data types")
print('list')
min([1,2,3,4,7,9,])
max([9,7,5,4])
total_items=['lets upgrade',"Kaushal",2]
total_items.append(28.1)
for i in total_items:
    print(i,total_items.index(i))
#tuple
tuple_a = (1,2,3,4,5,6,7)
print(tuple_a)
max(tuple_a)
sum(tuple_a)
#dictionary
dict_e={'name':'lets upgrade','user':"Kaushal",'aged' :2}
print(dict_e)