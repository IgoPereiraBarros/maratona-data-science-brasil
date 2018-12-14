list_nums = [100, 200, 400, 500,600, 700, 800, 900]
for itens in range(len(list_nums)): # usando a função Range
    list_nums[itens] += 1000
print(list_nums)

for ind, itens in enumerate(list_nums): # usando a funcao enumerate
    list_nums[ind] += 1000
print(list_nums)