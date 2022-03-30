def merge(list1 , list2):
    combined_list = []
    # i and j are pointing to indices of list1 and list2
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined_list.append(list1[i])
            i += 1
        else:
            combined_list.append(list2[j])
            j += 1
    # Edge cases to check if any one list is still having elements while other list is
    # already added in the combined_list list
    while i < len(list1):
        combined_list.append(list1[i])
        i += 1
    while j < len(list2):
        combined_list.append(list2[j])
        j += 1

    return combined_list

def merge_sort(mylist):
    # Here we use recursion
    if len(mylist) == 1:
        return mylist
    mid = int(len(mylist) / 2)
    left = mylist[:mid]
    right = mylist[mid:]
    return merge(merge_sort(left) , merge_sort(right))

print(merge_sort([4,3,5,6,2]))