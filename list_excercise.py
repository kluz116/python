def print_full_name(a, b):
    welcome = "Hello {} {}! You just delved into python.."
    print(welcome.format(a,b))

def getSum(a,b):
    sum = 'The sum of {} and {} is {}' 
    print(sum.format(a,b,(a+b)))


a = 3
b= 4
print_full_name(a,b)
getSum(a,b)

