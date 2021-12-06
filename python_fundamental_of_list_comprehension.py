print('\nOrdered delete')
book_list = ['atomic habbit', 'who the hell are you', 'outlier', 'The leadership handbook']
del book_list[0]
for i in range(0, len(book_list)):
    print(book_list[i])
print('\nOrdered delete with list comprehensive')
book_list = ['atomic habbit', 'who the hell are you', 'outlier', 'The leadership handbook']
del book_list[:2]
for i in range(0, len(book_list)):
    print(book_list[i])

print('\nOrdered delete with start list comprehensive ')
book_list = ['atomic habbit', 'who the hell are you', 'outlier', 'The leadership handbook']
del book_list[::2]  # start:end
for i in range(0, len(book_list)):
    print(book_list[i])

print('\nMake new list')
book_list = ['atomic habbit', 'who the hell are you', 'outlier', 'The leadership handbook']
book_new_list = book_list[:]
for i in range(0, len(book_list)):
    print(book_list[i])

print('\nMake new list')
del book_list[:]
for i in range(0, len(book_new_list)):
    print(book_new_list[i])

# create new list with comprehension
print('\nCreate new list  with comprehension: odd')
book_list = ['1. atomic habbit', '2. who the hell are you', '3. outlier', '4. The leadership handbook']
book_new_list = book_list[0::2]
for i in range(0, len(book_new_list)):
    print(book_new_list[i])

print('\nCreate new list  with comprehension: even')
book_list = ['1. atomic habbit', '2. who the hell are you', '3. outlier', '4. The leadership handbook']
book_new_list = book_list[1:2]  # start stop and end
for i in range(0, len(book_new_list)):
    print(book_new_list[i])
print('\nCreate new list  with comprehension: throw at the end')
book_list = ['1. atomic habbit', '2. who the hell are you', '3. outlier', '4. The leadership handbook']
book_new_list = book_list[0:-1:2]
for i in range(0, len(book_new_list)):
    print(book_new_list[i])

