def iterator(s):
    try:
        print(next(s))
    except TypeError:
        print("It was a type error")

s = 'AronShrestha'
 
print("wihout making string iterable to iterator as string is iterable bt not iterator by default")
iterator(s)
i =  iter(s)
print("After making iterator")
iterator(i)


#Same goes for list,tuples as for string

#Generator

def test(j):
    l =[]
    for i in range(j):
        l.append(i**3)
        print(l)
    yield(l)

print(test(5))

for i in test(5):
    print(i)



