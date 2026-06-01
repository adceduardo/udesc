def bubble(arr):
    n = len(arr)

    print(arr)

    for i in range(n-1):

        for j in range(n-1):
            if arr[j] > arr[j+1]:
                aux = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = aux
    print(arr)

def quick(arr):
    n = len(arr)

    if n <=1:
        return arr
    
    left, right, middle = [], [], []
    middle = n//2
    pivot = arr[middle]


    for i in range(n):
        if arr[i] == pivot:
            middle.append(arr[i])
            continue

        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    
    return quick(left) + middle + quick(right)

def selection(arr):
    print(arr)
    n = len(arr)

    for i in range(n):
        minor = i

        for j in range(i+1, n):
            if(arr[j] < arr[minor]):
                minor = j

        aux = arr[i]
        arr[i] = arr[minor]
        arr[minor] = aux

    print(arr)

def insertion(arr):
    print(arr)
    n = len(arr)

    for i in range(1, n):
        j = i-1
        aux = arr[i]

        while j >=0 and arr[j] > aux:
            arr[j+1] = arr[j]
            j-=1

        arr[j+1] = aux   
    
    print(arr)      
            
def merge(arr):
    n = len(arr)

    if n <= 1:
        return arr
    
    middle = n//2

    left = arr[:middle]
    rigth = arr[middle:]

    newL = merge(left)
    newR = merge(rigth)

    output = []

    topL, topR = 0, 0

    while topL < len(newL) and topR < len(newR):
        if newR[topR] < newL[topL]:
            output.append(newR[topR])
            topR += 1

        else:
            output.append(newL[topL])
            topL +=1

    output += newL[topL:] 
    output += newR[topR:]
   
    return output

def shell(arr):
    print(arr)
    n = len(arr)
    gap = n//2

    while gap > 0:
        print('gap', gap)

        for i in range(gap, n):
            aux = arr[i]
            j = i - gap

            print(aux, arr[j])



        gap = gap//2

    


    


arr = [9, 8, 3, 7, 5, 6, 4, 1]

shell(arr)