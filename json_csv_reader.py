import json
import csv

result_list = []
with open('users.json', "r") as f:
    users = json.load(f)
    number_of_users = len(users)
for user in users:
    result_list.append({'name': user['name'],
                        'gender': user['gender'],
                        'address': user['address'],
                        'age': user['age'],
                        'books':[]
                        })

books = []
with open('books.csv', newline='') as f:
    reader = csv.reader(f)
    header = next(reader)
    i=0
    for row in reader:
        book = dict(zip(header, row))
        book.pop('Publisher')
        result_list[i % number_of_users]['books'].append(book)
        i+=1


with open('result.json','w') as file_result:
    file_result.write(json.dumps(result_list, indent=4))


