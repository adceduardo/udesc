
def bubble(arr):
    n = len(arr)

    for i in range(0, n-1):
        for j in range(0, n-1):
            if(arr[j] > arr[j+1]):
                aux = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = aux

    return(arr)

def quick(arr):
    n = len(arr)

    if n <= 1:
        return arr

    pivot = n//2
    pivot = arr[pivot]

    left, right = [], []

    for i in arr:

        if i == pivot:
            continue

        if i < pivot:
            left.append(i)

        else:
            right.append(i)

    return(quick(left) + [pivot] +  quick(right))

def insertion(arr):
    n = len(arr)

    for i in range(1, n):        
        aux = arr[i]
        
        j = i-1
        while j >=0 and aux < arr[j]:
            arr[j+1] = arr[j]

            j-=1

        arr[j+1] = aux
    
    return(arr)

arr = [10, 4, 7, 2, 9]

