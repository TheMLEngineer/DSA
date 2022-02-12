'''
# O(n)
def print_items(n):
    for i in range(n):
        print(i)

print_items(5)
print('*' * 50)


# O(2n) == O(n)
def print_items(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)


print_items(5)
print('*' * 50)
'''

# O(n * n) / O(N squared) / O(n2)
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i , j)

print_items(5)
print('*' * 50)
