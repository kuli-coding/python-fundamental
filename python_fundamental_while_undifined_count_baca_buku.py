"""
The program looping read the book  while until understood
"""
number_of_book = 10
print('Mom said, "read all your book')
number_of_books_read_and_understood = 0
print(f'number of books read and understood {number_of_books_read_and_understood}')
total_number_of_reads = 0
while total_number_of_reads < number_of_book * 2:
    total_number_of_reads = total_number_of_reads + 1
    if number_of_books_read_and_understood == 9:
        print(f"book to {number_of_books_read_and_understood + 1 } not understood yet")
    else:
        number_of_books_read_and_understood = number_of_books_read_and_understood + 1
    print(f"book to {number_of_books_read_and_understood} has read and understood")

print(f'number of books read {number_of_books_read_and_understood}')
if number_of_books_read_and_understood == number_of_book:
        print('"mom, all the book  has  read and understood')
else:
        print(f'"Mom, do not all book  can understood. budi only can understood {number_of_books_read_and_understood} book')




