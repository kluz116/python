def getSumOfAdvisors(number):
    list = []
    for i  in range(number ):
        if(i > 0):
            if number % i == 0:
                list.append(i)
    print(list)


getSumOfAdvisors(100)

x =4
y = 5
a = lambda x,y: x+y
print(a)
