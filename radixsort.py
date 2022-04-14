def radixsort(arr):
    
    ma = str(max(arr))
    n = len(ma)
    
    for i in range(n):
        
        cur_bit = [[] for i in range(10)] #当前位，0~9，故建立十个桶
        
        for j in range(len(arr)):
            
            cur_bit[(arr[j]//(10**i))%10].append(arr[j])
        
        indx = 0
        
        for k in range(len(cur_bit)):
            
            for l in range(len(cur_bit[k])):
                
                arr[indx] = cur_bit[k][l]
                
                indx += 1
                
    return arr 

a = [4,3,6,5,7,10]
print(radixsort(a))
            
        