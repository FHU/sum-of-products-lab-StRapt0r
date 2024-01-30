def sum_of_products(list1, list2):
    output=((list1[0]*list2[0])+(list1[1]*list2[1])+(list1[2]*list2[2]))
    return(output)


if __name__ == '__main__':
   a=([int(input("Input an interger here:")),int(input("Input an interger here:")),int(input("Input an interger here:"))])
   b=([int(input("Input an interger here:")),int(input("Input an interger here:")),int(input("Input an interger here:"))])
   x= sum_of_products(a,b)
   print("The answer is:", x)
