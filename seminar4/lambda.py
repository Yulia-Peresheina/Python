a = [3, 4, 5, 2, 7, 8]	
b = [7, 9, 2, 4, 5, 1]	
c = [5, 7, 3, 4, 5, 9]

dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]


dict_b = [{"name": "John", "age": 12}, 
          {"name": "Sonia", "age": 10},
          {"name": "Steven", "age": 13}, 
          {"name": "Natasha", "age": 9}]

names = ["Abram", "Arib", "Bob", "Shawn",
	     "Aria", "Cicilia", "John", "Reema",
         "Alice", "Craig", "Aaron", "Simi"]

print(*map(lambda x, y, z: x + y + z, a, b, c))            # * позволяет нам увидеть результат, без нее не будет показываться итог
                                                           # lambda - ей не нужно давать названия, нужно сразу объявлять аргументы и действия 
                                                           # (x, y, z: x + y + z), а потом передавать ресурс (a, b, c)
                                                           # взаимодействовать с результатом нельзя! для дальнейшей работы нужно использовать это:

print(list(map(lambda x, y, z: x + y + z, a, b, c)))       # нужно преобразовать в лист

# print(list(map(lambda x: x['name'], dict_a)))             # бере  т и формирует список только из значений ключей. Можно и работать со значениями
print(list(map(lambda x: x['name'] == "python", dict_a)))   # Задаем условие. выведет [True, False]. Лямбда пробежится по нашим ключам
                                                            #  и значениям и выведет истинно-ложно ли условие
#----------------------------------------------------------------------------------------------------------------------------------------------
#  filter. Собирает или пропускает то, что дает истину в его логических выражениях.

print(list(filter(lambda x: x > 5, c )))                    #Отфильтровали список c. Взяли только те значения, которые больше 5 и сформировали из него новый список.
print(list(filter(lambda x: x % 2 == 0, a)))                # Отфильтровать список a так, чтобы остались только кратные 2 значения.
print(list(filter(lambda x: x['name'] == "python", dict_a))) #Остался список из того множества, которое содержит пару name-python.
                                                            #  Там есть еще одна пара, points-10, она также осталась. 
#-------------------------------------------------------------------------------------------------------------------------------
# sorted

print(sorted(names, key=lambda x: x.endswith('n')))          #сортирует список. Но не по-умолчанию, по номеру символа, а по ключу.
                                                             #  Ключ - лямбда, которая заканчивается на n.
                                                             # отсортированные по ключу ставятся в конец.  
print(sorted(map(lambda x: x['age'], dict_b)))               #с помощью лямбды достали значения по ключу и полученный список отсортировали
print(sorted(dict_b, key=lambda x: x['age'], reverse=True))  # отсортировали в обратном порядке (reverse=True) по значениям ключей "age"
print(*sorted(dict_b, key=lambda x: x['age'], reverse=True), sep='\n') #все аналогично вышенаписанному, но вывод каждого индекса списка будет на новой строке.