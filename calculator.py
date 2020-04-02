class Calculator():

    def sum(self, a,b):
        if isinstance(a,int) and isinstance(b, int):
            return a + b
        else :
            return "ERROR"
    def check_sum_greater(self,n):
        sum = 0
        for  i in range(n):
            if i > 0:
                if n%i == 0:
                    sum = sum + i
        if sum > 10:
            return True
        else:
            return False

    def subtract(self,a,b):
        if isinstance(a, int) and isinstance(b, int):
            return a - b
        else :
            return "ERROR"