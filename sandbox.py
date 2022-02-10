# x = int(0)
# y = float(0.00)
# str1 = "Ali"
# record = ['Shahzad','21TCXX',20,1.234]   #mutable
# tup1 =('Jazbati','21TCXX',20,1.234)     #immutable
# Set1 = {'Jazbati','21tcxx','Jazbati',20}
# Set2 = {'Jazbati','21tcxx'}
# record1= {"name":"Shahzad",'class':'21TC','Char':'Good', 'sub':{'ITC':'A+', 'phy':'F'}}

# print(record1.key())
# print(record1.values())
# print(record1.items())

# record1['city']="Sukkur"
# print(record1.get('class'))
# print(record1.pop('class'))

# for key,value in record1.items():
#     print(key, value)

# print(type(x))
# print(type(y))
# print(type(str1))
# print(type(record))
# print(type(tup1))
# print(record)
# print(tup1)
# print(Set1.difference(Set2))

# def print_val(dict1):
#     for key,value in dict1.items():
#         print(key,' ',value)

# my_rec = {'name':'Sheeraz','roll':'21TC31','age':43,3:'Three','addr':'Sukkur'}
# new_dic = {1:'One',2:'Two',3:'three'}
# print_val(my_rec)
# print_val(new_dic)









def record_print(dict):
    for key,value in dict.items():
        print(key,value)




record = {'name_s':'Abdur Rehman','cast':'Gadehee','batch':'21TC'}
record_print(record)











