def book_reader(book_name):
    book = {}
    dish_list = []
    with open(book_name, 'rt', encoding= 'utf8') as file:
      for l in file:     
          dish_name = l.strip()   
          ingredients_list = []
          dish = {dish_name: ingredients_list}      
          dish_count = file.readline() 
          for i in range(int(dish_count)):           
            dsh = file.readline().strip().split(' | ') 
            ingredients_list.append({'ingredient_name': dsh[0],
                            'quantity': int(dsh[1]),
                            'measure': dsh[2]})
            dish_list.append(dish)                
          blank_line = file.readline()
          book.update(dish)
    file.close()
    return book

def get_shop_list_by_dishes(cook_book, dishes, person):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for loc in cook_book[dish]:
                person_q = int(loc['quantity']) * person
                dict_list = {loc['ingredient_name']: {'measure': loc['measure'], 'quantity': person_q}}
                shop_list.update(dict_list)
    return shop_list

from pprint import pprint

#Задача 1
print(f'\n Задача 1\n')
cook_book_name = 'cook/cookbook.txt'
cook_book = book_reader(cook_book_name)
print(cook_book)

#Задача 2
print(f'\n Задача 2\n')
dishes = ['Запеченный картофель', 'Фахитос']
person = 5
shop_list = get_shop_list_by_dishes(cook_book, dishes, person)
pprint(shop_list)

#Задача 3
print(f'\n Задача 3\n')
import os

def reader_x_files(dir_files, file_name):
    with open(os.path.join(dir_files, file_name), encoding='utf8') as f:  
        text = f.readlines()
        head_1 = file_name
        head_2 = len(text)
        f.close()
    return head_1, head_2, text

dir_files = 'files'
total_file = 'xxxxx.txt'
head_e = {}
head_x = {}

for file_name in os.listdir(dir_files):
    head_1, head_2, text = reader_x_files(dir_files, file_name)
    head_x[head_1] = head_2
    for x in sorted(head_x, key=head_x.get):
        head_e[x] = head_x[x]
        
# total_lines = sum(head_e.values())
# print(total_lines)   
        
print(head_e)

for x in head_e.keys():
    s = str(head_e[x])
    h1, h2, t = reader_x_files(dir_files, x)
    with open(total_file, 'at') as xxx:
        xxx.write(x + '\n' + s + '\n')
        for lines in t:
            xxx.write(lines)
        xxx.write('\n\n')
    xxx.close()

print('объединенный файл xxxxx.txt создан в корневой директории')