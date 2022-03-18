import enum


class HashTable:
    # Size is 7 coz we have 6  adrees space blocks (For example)
    def __init__(self , size = 7) -> None:
        self.data_map = [None] * size

    # Custom Hash Function
    def __hash(self , key) -> int:
        my_hash = 0
        for letter in key:
            # ord fn returns ascii value of letter
            # 23 is prime number , we multiply by it to reduce collisions
            # we use % to return a value less than length of data map. Why ?
            # Example here default length is 7 , When you modulo any number by 7 the result will be 0 to 6
            # Exact address spaces that we are trying to store key
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)

        return my_hash

    def print_table(self):
        for i , val in enumerate(self.data_map):
            print(i , ' : ' , val)

        
my_hash_table = HashTable()
my_hash_table.print_table()
        