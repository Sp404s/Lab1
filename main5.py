str = ''
word =''
n = int(input('Введити число слов'))
var = range(n)
for i in var:
    word = input('')
    str += word
    if i+1 !=n:
        str += ','
    else:
        str += '.'
print(str)