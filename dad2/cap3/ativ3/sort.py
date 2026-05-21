array = [25, 57, 48, 37, 12]

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

        print(left, pivot, rigth)
        return quickSort(left) + [pivot] + quickSort(rigth)



print(quickSort(array))