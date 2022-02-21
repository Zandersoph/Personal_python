def binary_search(list,t):
    #Assuming a sorted list
    f = 0
    l = len(list) - 1

    while f <= l:
        mid = (f+l)//2
        if list[mid] == t:
            return mid
        elif list[mid] < t:
            f = mid + 1
        else:
            l = mid - 1
    return None

def Verify(index):
    if index is not None:
        print("Target is found at index: ", index)
    else:
        print("Target not found in list.")

n = [5,10,18,17,16,19,21]

r = binary_search(n, 19)
Verify(r)