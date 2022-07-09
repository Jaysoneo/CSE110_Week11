with open('books.txt') as book_data:
    for data in book_data:
        data=data.strip()
        print(data)