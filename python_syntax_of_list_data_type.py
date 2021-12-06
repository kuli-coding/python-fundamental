book_list = ['atomic habbit', 'who the hell are you', 'outlier', 'The leadership handbook']
print('show the list variable book')
print(book_list)

print('\nall the procces with for in')
for book in book_list:
    print(book)
print('\ndisplay the contents of a list of books at a certain index')
print(book_list[0])
print(book_list[2])

print('\nShow  with for in range')
for i in range(0, len(book_list)):
    print(book_list[i])

book_list = [1, 'kenji volume 2', -313, 3.14]
print('\nShow  with for in range, where is data type is differences')
for i in range(0, len(book_list)):
    print(book_list[i])

print('\nReturn the first content book list')
book_list = ['atomic habbit', 'who the hell are you', 'outlier', 'The leadership handbook']
print('\nadd new book')
book_list.append('blink')
for i in range(0, len(book_list)):
    print(book_list[i])

print('\nClear list')
book_list.clear()
for i in range(0, len(book_list)):
    print(book_list[i])

print('\nChange first element')
book_list = ['atomic habbit', 'who the hell are you', 'outlier', 'The leadership handbook']
book_list[0] = 'atomic habit human'
for i in range(0, len(book_list)):
    print(book_list[i])

print('\nchoose second element')
book = book_list.pop(1)
print(book)
for i in range(0, len(book_list)):
    print(book_list[i])

print('\n The book was taken')
print(book)

"""
ordered pop
"""
print('\nPop')
book_list.pop()
for i in range(0, len(book_list)):
    print(book_list[i])

print('\nPop -1')
book_list = ['atomic habbit', 'who the hell are you', 'outlier', 'The leadership handbook']
book_list.pop(0)
for i in range(0, len(book_list)):
    print(book_list[i])
