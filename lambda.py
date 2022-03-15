x=(lambda x:x*2)(12)
print(x)
x=lambda a,b:a+b
print(x(10,15))
double=lambda x:x*2
print(double(5))


def myfunc(n):
    return lambda a:a*n
x=myfunc(2)
print(x(5))

L1=[1,2,3,4,5,6,7,8,9]
print(map(lambda x:pow(x,3),L1))
print(list(map(lambda x:pow(x,3),L1)))

