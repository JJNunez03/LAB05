import builtins

def sum(list):  
    return builtins.sum(list)  

def average(list):
    return sum(list) / len(list) if list else 0


