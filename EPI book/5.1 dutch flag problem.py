#dutch flag problem:
'''
Write a program , that takes an Array , A and in index 'i'
into A an d rearragges the elements such that all the elements less 
than A[i] the 'pivot  appear first , followed by the elemnets equal to pivit and 
then the elemnts greater than pivot .
'''

def dutch_flag_partition(A:[int],pivot_index:int)->None:
   
    pivot = A[pivot_index]# since we are modifying A inplace ,
    # better to store this first

     #first arrange all elemnt less than the pivot 
    small_swap_index =0
    for i in range (len(A)):
        if A[i]< pivot:
            #swap the element
            A[i],A[small_swap_index] =A[small_swap_index],A[i] 
            #incrememt the index
            small_swap_index+=1

    # Arrange the element greater than pivot
    large_swap_index =len(A)-1
    for i in reversed(range (len(A))):
        if A[i]>pivot:
            #swap the element
            A[i],A[large_swap_index] = A[large_swap_index],A[i]
            #deccrememt the index
            large_swap_index-=1
     
#Driver code

A = [0,1,2,0,2,1,1]
pivot_index =3#A[3]=0
dutch_flag_partition(A,pivot_index)
print(A)
# [0, 1, 0, 2, 2, 1, 1]
pivot_index =2 #A[2]=2
dutch_flag_partition(A,pivot_index)
print(A)
#[0, 0, 1, 1, 1, 2, 2]

