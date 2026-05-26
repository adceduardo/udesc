def bubbleSort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                aux = array[j]
                array[j] = array[j+1]
                array[j+1] = aux

    return array

def quickSort(array):
    if len(array) <= 1:
        return array
    
    else:
        pivot = len(array) // 2
        pivot = array[pivot]

        rigth, left = [], []
        
        for element in array:
            if element == pivot:
                continue
            
            if element < pivot:
                left.append(element)
            else:
                rigth.append(element)

        return quickSort(left) + [pivot] + quickSort(rigth)

def insertionSort(array):
    n = len(array)
    
    for i in range(1, n):
        aux = array[i]
        j = i-1

        while j >= 0 and aux < array[j]:       
            array[j+1] = array[j]
            j-=1

        array[j+1] = aux

    return(array)

def selectionSort(array):
    n = len(array)

    for i in range(n-1):
        pos = i

        for j in range(i+1, n):
            if array[j] < arr[pos]:
                pos = j
        
        aux = array[i]
        array[i] = array[pos]
        array[pos] = aux

    return array

def mergeSort(arr):
    n = len(arr)

    if n == 1:
        return arr
    
    half = n//2
    left, right = [], []

    for i in range(n):
        if i < half:
            left.append(arr[i])
        else:
            right.append(arr[i])

  
    returnLeft = mergeSort(left)
    returnRigth = mergeSort(right)

    output = []
    topR, topL = 0, 0

    while topL < len(returnLeft) and topR < len(returnRigth):
        if(returnLeft[topL] < returnRigth[topR]):
            output.append(returnLeft[topL])
            topL += 1
        
        else:
            output.append(returnRigth[topR])
            topR += 1

    if topL < len(returnLeft):
        output += returnLeft[topL:]

    
    if topR < len(returnRigth):
        output += returnRigth[topR:]

    return output

arr = [6, 4, 2, 8, 11]
print(mergeSort(arr))
