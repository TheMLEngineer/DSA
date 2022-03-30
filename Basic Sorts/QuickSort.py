def swap(mylist , index1 , index2):
    mylist[index1] , mylist[index2] = mylist[index2] , mylist[index1]

def pivot(mylist , pivot_index , end_index):
    swap_index = pivot_index

    for i in range(pivot_index + 1 , end_index + 1):
        if mylist[i] < mylist[pivot_index]:
            swap_index += 1
            swap(mylist , swap_index , i)
    swap(mylist , pivot_index , swap_index)
    return swap_index

l = [9,3,2,5,7,3,55]
print(pivot(l , 0 , 6))

# After running pivot checking list
print(l)