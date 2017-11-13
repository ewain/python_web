import fractions
import datetime
import fileinput
print('Hello World!')

''' 
# determina se i numeri di seq sono pari o dispari
seq = [1, 2, 3, 4, 5]
for n in seq:
    
    print('Il numero', n, 'è', end=' ')
	
	#end=' '
    if n%2 == 0:
        print('pari')
    else:
        print('dispari')
		
print([x for x in range(len(seq))])
print({c for c in 'aAbCCCCccccBcCdDeE' if c.isupper()})#set
a=[c+n for c in 'ABC' for n in '123']#lista
print(type(a))
print(a, '\n---------')


# definisco una funzione che ritorna il quadrato di un numero
def square(n):
    return n**2
squares = map(square, range(10))
print(squares)  # map ritorna un oggetto iterabile
lista = list(squares)  # convertendolo in lista si possono vedere gli elementi
print('lista: ',lista)
# la seguente listcomp è equivalente a usare list(map(func, seq))
print([square(x) for x in range(10)])

print('prova func')

def is_even(n):
    """definisco una funzione che ritorna True se il numero è pari"""
    if n%2 == 0:
        return True
    else:
        return False

even = filter(is_even, range(10))
print(even)  # filter ritorna un oggetto iterabile

print(list(even))  # convertendolo in lista si possono vedere gli elementi

# la seguente listcomp è equivalente a usare list(filter(func, seq))
print([x for x in range(10) if is_even(x)])

print('esempio di funzioni con argomenti passati per nome')
def greet(greeting, *, name):
    print('{} {}!'.format(greeting, name))
#* indica che gli argomenti dopo devono essere passati per nome
#chiamata errata
#greet('Hello', 'Python')

#chiamata corretta
greet('Hello', name='Python')

#produce un errore
#greet(greeting='Hello', name='Python')

print('-----prova argomenti multipli-----')
def make_tag(element, **attrs):
    attrs = ' '.join(['{}="{}"'.format(k, v) for k, v in attrs.items()])
    return '<{} {}>'.format(element, attrs)

print('*',make_tag('div', id='header'))

print('*',make_tag('a', href='https://www.python.org/', title='Visit Python.org'))

print('*',make_tag('img', src='logo.png', alt='Python logo'))
'''
 

print('---operazioni su file---')
f = open('test.txt', 'r+')
print('PRIMA:\n',f.read())

f.seek(0,0)
riga='\nriga del file\n'
print('riga: ', f.tell())
#f.writelines(riga)
f.writelines('zzz')
f.seek(0,0)
print('DOPO:\n',f.read())
f.close()


'''
#print('---REPLACE su file---')
#for line in fileinput.input(['test2.txt'], inplace=True):
#    print(line.replace('bbb\n', 'zzz\n'),end='')#old = myfile.read()
'''

'''
print('---SCRIVO contenut di un file modificandolo in visualizzazione---')
with fileinput.input(files=('test2.txt')) as f2:
	for line in f2:
		print(line.replace('bbb\n', 'zzz\n'),end='')#old = myfile.read()
'''	










