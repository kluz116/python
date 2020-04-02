def check_sum_greater(n):
    sum = 0
    for  i in range(n):
        if i > 0:
            if n%i == 0:
                sum = sum + i
    if sum > 10:
        return True
    else:
        return False
        

print(check_sum_greater(20))



