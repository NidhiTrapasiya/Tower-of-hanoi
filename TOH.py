def TowerOfHanoi(n , start, dest, aux): 
    if n == 1: 
        print ("Move disk 1 from rod",start,"to rod",dest) 
        return
    TowerOfHanoi(n-1, start, aux, dest) 
    print ("Move disk",n,"from rod",start,"to rod",dest) 
    TowerOfHanoi(n-1, aux, dest, start) 
          
# Driver code 
n = 3
TowerOfHanoi(n, 'A', 'C', 'B')  
# A, C, B are the name of rods 
