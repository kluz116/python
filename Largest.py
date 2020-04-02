import string
def secoundLargestNumber(number):
    number.sort()
    n = len(number) - 2
    print(number[n])

'''number = [1,2,4,6,8,32,10,34]
secoundLargestNumber(number)//32'''

def captalise():
    name = 'allan musembya'
   
    print( string.capwords(name))

captalise()