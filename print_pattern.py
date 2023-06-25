def print_pattern(num):
    flag = 1
    while flag <= num:
        result =''
        for i in range(1,flag+1):
            result += str(i)
        print(result)
        flag +=1
        
gss = print_pattern(5)
print(gss)