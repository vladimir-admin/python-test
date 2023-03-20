my_str = input('Введите строку из нескольких слов разделенных пробелами: ')
words_list = my_str.split(' ')
index = 0
while index < len(words_list):
    print(f'{index + 1} {words_list[index][:10]}')
    index += 1

# my_str = '1234567890 sdfasdfasdfasdf dfsd sdfsdf'
# words_list = ['1234567890', 'sdfasdfasdfasdf', 'dfsd', 'sdfsdf']
# index = 0
# 0 < 4