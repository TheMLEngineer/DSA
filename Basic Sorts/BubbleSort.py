def bubble_sort(my_list):
    for i in range(len(my_list) - 1, 0 , -1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                my_list[j] , my_list[j+1] = my_list[j+1] , my_list[j]
    return my_list

print(bubble_sort([9,7,5,3]))