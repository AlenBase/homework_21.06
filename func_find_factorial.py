def find_factorial(number):
    
    if number == 0:
        pass
    
    else:
        
        result = 1
        while number > 0:
            
            result *= number
            number -= 1
        
        return result
