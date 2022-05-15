import numpy as np

def check_sequnce(sequence: str) -> bool:
    # 4 2 2 3 2 1 4 2 2 2 2 - True
    # 4 4 3 1 2 - False
    sequence = sequence.strip()
    sequence = list(map(int, sequence.split(' ')))
    
    a = sequence

    while True:
        a.sort(reverse=True)
       
        only_zeros = True
        for element in a:
            if not element == 0:
                only_zeros = False

        if only_zeros:
            return True 
        
        if a[0] < 0 or a[0] > len(a):
            return False
        
        for element in a:
            if element < 0:
                return False

        for i in range(1, a[0] + 1):
            a[i] = a[i] - 1
        a[0] = 0
