#REMOVE PASS AND FIX THE FUNCTION
#change to test push and forks
def sum_of_products(list1, list2):
    output=((list1[0]*list2[0])+(list1[1]*list2[1])+(list1[2]*list2[2]))
    return(output)


if __name__ == '__main__':
   #REMOVE PASS AND YOUR CODE GOES HERE
   a=([int(input()),int(input()),int(input())])
   b=([int(input()),int(input()),int(input())])
   x= sum_of_products(a,b)
   print(x)
