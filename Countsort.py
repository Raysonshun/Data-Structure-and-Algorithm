def CountSort(arr):

    ma = max(arr)
    mi = min(arr)
    
    counter = [0 for i in range(mi, ma + 1)]
    
    for i in range(len(arr)):
        counter[arr[i]-mi] += 1
    
    sortedIndex = 0
    
    for i in range(mi,ma+1):
        
        while(counter[i-mi]) > 0:
    
            arr[sortedIndex] = i
            sortedIndex += 1
            counter[i-mi] -= 1   # 这里是为了考虑重复元素
            
    return arr
        

arr = [3,5,10,4,6,7,11,9,8,0,100]
print(CountSort(arr))