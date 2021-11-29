
arr = (1 ,2 , 3, 3, 4) 

def repeats(arr):
    unicos = set()
    
    for single in arr:
        if single in unicos:
            unicos.remove(single)
        else:
            unicos.add(single) 

    return sum(unicos)  