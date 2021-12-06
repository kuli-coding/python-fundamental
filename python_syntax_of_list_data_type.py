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
