
# for ind, value in enumerate(zip(n, x,z)):
#     print(ind, value)
    


# new_dic = {val: number for val, 
#           number in zip(val, number)}
# print(new_dic)

    


# n1 = [21,33,32,5]
# n2 = [1, 1,1, 1, 1]
# kv = list(map(lambda x, y: x + y, n1, n2))
# print(kv)
# a = 5
# b = 7
# c = 4
# rev_upper = lambda x: x.upper() [::-1]
# print(rev_upper(st))

# maximum = lambda x, y, z: max(x,y,z)
# print(maximum(a,b,c))

# x = "greeting from CheckiO Planet"
# print(x.split()[0])

word = 'dimidrol'
guess = 'i'
word_comp = len(word) * '_'

word_list = list(word_comp)
cut_word = [i for i in range(len(word)) if word[i] == guess]
for index in cut_word:
    word_list[index] = guess

print(word_comp := ''.join(word_list))




