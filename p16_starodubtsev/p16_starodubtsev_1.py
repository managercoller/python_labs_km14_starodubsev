from functools import reduce

book_pages = input('Enter the number of pages in a book: ')
while book_pages not in [str(a) for a in range(16, 1281, 16)]:
    print('The number isn\'t correct')
    book_pages = input('Enter the number of pages, less than 1280, divisible by 16: ')
book_pages = int(book_pages)

def presentation_fabric(f_type='list', classic=True):
    def wrap(f):
        def wrapper(arg):
            result = (f(arg) if f_type == 'list' else [*f(arg)] if f_type == 'gen' else None)
            if result == None:
                raise ValueError(f'`{f_type}` isn\'t a valid function type, choose `gen` or `list`') # Why not
            if not classic:
                print(result[:-1])
                print(result[-1][0])
            else:
                for line in result:
                    print(*line)
        return wrapper
    return wrap

@presentation_fabric(classic=False)
def list_of_page_numbers(book_pages):
    def numeration(pages):
        lst = []
        for page in range(0, 8, 2):
            lst += [pages - page, (page + 1) + (pages - 16), (page + 2) + (pages - 16), pages - page - 1]
        return lst
    result = []
    pages = [*range(16, book_pages+1, 16)]
    for notebook_pages in pages:
        result.append(numeration(notebook_pages))
    return result + [[f'> book has {book_pages//16} notebooks in it']]

@presentation_fabric('gen')
def num_gen(book_pages):
    for pages in range(16, book_pages+1, 16):
        yield reduce(lambda res, lst: res + lst, [[pages-page, (page+1)+(pages-16), (page+2)+(pages-16), pages-page-1] for page in range(0, 8, 2)])
    yield [f'> book has {book_pages//16} notebooks in it']


print('First type (classic) (list of lists):')
list_of_page_numbers(book_pages)
print(f'{"* "*25}\nSecond type (list) (generator):')
num_gen(book_pages)