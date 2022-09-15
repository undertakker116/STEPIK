words_list = ['махачкала', 'хач', '123', '12234', ')))', "2"]
sorted_list = []
for i in words_list:
    if len(i) <= 3:
        sorted_list.append(i)
print(sorted_list)

