'''
Find the nearest repeated entries in an Array
Write a program that takes as input array and finds the distance between the closest pair of equal entries.
s = ["All","work","and","no","play","makes","for","no","work","no","fun","and","no","results"]

'''
from typing import List

def find_nearest_repetition(paragraph:List[str])->int:
    word_latest_index_hash_table:dict[str,int]= {}
    nearest_distance_so_far  = float('inf')

    for i,word  in enumerate(paragraph):
        if word in word_latest_index_hash_table:
            previous_word_index  = word_latest_index_hash_table[word]
            nearest_distance_so_far = min(nearest_distance_so_far,i-previous_word_index)
        word_latest_index_hash_table[word] = i

    return nearest_distance_so_far if nearest_distance_so_far !=float('inf') else -1 
        

#driver code
#s = ["All","work","and","no","play","makes","for","no","work","no","fun","and","no","results"]
#The nearest repetition distance is: 2
s = ["All","work","and","no","play","makes","for"]
print(f'The nearest repetition distance is: {find_nearest_repetition(s)}')
#The nearest repetition distance is: -1