#Allan Musembya
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
             if(arr[j] > arr[j+1]):
                 temp = arr[j]
                 arr[j] = arr[j +1]
                 arr[j + 1] = temp

    str = "The Sorted List Is : {}"
    print(str.format(arr))

bubbleSort([20,10,1,30,20,25])#The Sorted List Is : [1, 10, 20, 20, 25, 30]
