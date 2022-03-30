from email import message_from_binary_file


def selection_sort(mylist):
    for i in range(len(mylist) - 1):
        min_index = i
        for j in range(i+1 , len(mylist)):
            if mylist[j] < mylist[min_index]:
                min_index = j
        if i != min_index:
            mylist[i] , mylist[min_index] = mylist[min_index] , mylist[i]
    return mylist



print(selection_sort([6,3,8,23,5]))