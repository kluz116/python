import math
def linearsearch(list,targetValue):
    for i in list:
        if i == targetValue:
            print("The Value Was Found In The List");
        

def binarySearch(list,targetValue):
    firstIndex = 0
    lastIndex = len(list) -1
    
    while firstIndex <= lastIndex:
        middleIndex = math.floor((firstIndex + lastIndex)/2)
        if list[middleIndex] == targetValue:
            print(list[middleIndex])
            print("Target Value ", list[middleIndex], " Found At Index " ,list.index(targetValue))
            break;
        if targetValue > list[middleIndex] :
            firstIndex = middleIndex + 1
            
        if targetValue < list[middleIndex] :
            lastIndex = middleIndex - 1

def bubbleSort(list):
    n = len(list)
    for i in range(n -1):
        for j in range(n-i-1):
            if(list[j] > list[j+1]):
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    print(list)



            

list = [14,12,13,18,16,17]
#targetValue = 12
#linearsearch(list,targetValue)
#binarySearch(list,targetValue)
bubbleSort(list)
