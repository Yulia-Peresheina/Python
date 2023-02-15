	# Хакер Василий получил доступ к классному	
	# # журналу и хочет заменить все свои минимальные	
	# # оценки на максимальные. Напишите программу,	
	# # которая заменяет оценки Василия,	
	# # но наоборот: все максимальные – на минимальные.		
	# # 8	# 5 4 2 2 4 2 2 5


#Вариант 1 через цикл:
#  
# def change_estim(list):
# 	maximum = max(list)
# 	minimum = min(list)
# 	for i in range(len(list)):                                 #можно заменить return [minimum if i == maximum else i for i in list]
# 		if list[i] == maximum:                            
# 			list[i] = minimum                                
# 	return list

# list_1 = [5, 4, 2, 2, 4, 2, 2, 5]

# print(change_estim(list_1))
# ------------------------------------------------------------------


# Вариант 2 через генератор списков
list_1 = input().split()
list_1 = [ int(list_1[i]) for i in range(len(list_1))]
list_2 = [min(list_1) if list_1[i] == max(list_1) else list_1[i]  for i in range(len(list_1))]
print(list_2)
