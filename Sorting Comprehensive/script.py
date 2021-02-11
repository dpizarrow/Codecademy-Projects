import utils
import sorts

bookshelf = utils.load_books('books_small.csv')

bookshelf_v1 = bookshelf.copy()
bookshelf_v2 = bookshelf.copy()

long_bookshelf = utils.load_books('books_large.csv')

long_bookshelfv2 = long_bookshelf.copy()

def by_title_ascending(book_a, book_b):
  return book_a['title_lower'] > book_b['title_lower']

def by_author_ascending(book_a, book_b):
    return book_a['author_lower'] > book_b['author_lower']

def by_total_length(book_a, book_b):
    return len(book_a['title_lower']) + len(book_a['author_lower']) > len(book_b['title_lower']) + len(book_b['author_lower']) 

# Comment sort_3 when not in use, as it takes a long time to sort the large dataset

sort_1 = sorts.bubble_sort(bookshelf, by_title_ascending)
sort_2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)
sort_3 = sorts.bubble_sort(long_bookshelf, by_total_length)

# Quicksort operates on the input directly, so we simply call quicksort on bookshelf_v2

sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2)-1, by_author_ascending)
sorts.quicksort(long_bookshelfv2, 0, len(long_bookshelfv2)-1, by_total_length)

# Comment these calls to sort the bookshelves one at a time, or else the console will get cluttered

for book in sort_1:
    print(book['title_lower'])

for book in sort_2:
    print(book['author_lower'])

for book in bookshelf_v2:
    print(book['author_lower'])

for book in sort_3:
    print(len(book['author_lower']) + len(book['title_lower']))

for book in long_bookshelfv2:
    print(len(book['author_lower']) + len(book['title_lower']))