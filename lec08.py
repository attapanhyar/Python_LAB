# Dictionaries

record = {"name":"Shahbaz", "class":"21TC", "dept": "Telecommunication",
            "age":20}
## 1 Printing values from a dictionary in different ways
# print(record)
#print(record['age'])
#print(record.get('name'))
#print(record.items())
#print(record.keys())
#print(record.values())

## 2 Inserting  record in a dictionary
# record['car']="Mercedes"

## 3 Pop-out a value from a dictionary
# print(record.pop('dept'))
# print(record)

## 4 Looping through items in a dictionary
# for field in record:
#     print(field)      # Shall only print keys
    
## 5 for printing only values
# for field in record.values():
#     print(field)      # Shall only print keys

## 6 for printing both
# for key, value in record.items():
#     print(key,' ', value)      # Shall only print keys

