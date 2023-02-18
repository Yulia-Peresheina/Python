# Вариант создания файла через open-close, чежим a

# colors = ['red ', 'green ', 'blue ']
# data = open('file.txt', 'a')
# data.writelines(colors)
# data.close()

# ----------------------------------------------------

# Вариант создания через with, режим w
# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')

# print(56)

# ---------------------------------------------------

# Режим чтения

path = 'file.txt'
data = open('file.txt', 'r')
for line in data:
    print(line)
data.close()
