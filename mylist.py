import math
mylist = ['Allan Musembya','Jones Williams','Mark Kelly','Cathy Kim','Sarah wells']

def binarySearch(arr, targetValue):

    startIndex = 0
    endIndex = len(arr) -1
    swapped = False

    while startIndex <= endIndex:
        
        middleIndex = math.floor((startIndex + endIndex)/2)
        if swapped == False :
            if targetValue == arr[middleIndex] :
                str = "The Target User : {} Found At Index : {}"
                print(str.format(targetValue,arr.index(targetValue)))
                swapped = True
            
            if targetValue > arr[middleIndex]:
                startIndex = middleIndex + 1

            if targetValue < arr[middleIndex]:
                endIndex = middleIndex - 1

binarySearch(mylist,'Allan Musembya')#The Target Value : Allan Musembya Found At Index : 0