one_set = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'} # множество не является упорядоченным объектом.
one_list = list(one_set) # Переводим множество в список
print(one_list) # проверка результата
two_list = sorted(one_list) # Сортировка списка по алфавиту
print(two_list) # проверка результата
three_list = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
print(three_list)
# w = [5, 3, 3, 5, 4] # пробный список средних арифм.
w =[]
for l in three_list:w.append(sum(l)/len(l))
d = {}
for i in range(len(two_list)):d[two_list[i]]=w[i]
print(d)
