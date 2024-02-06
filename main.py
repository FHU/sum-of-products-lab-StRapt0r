def sum_of_products(list1, list2):
    output=((int(list1[0])*int(list2[0]))+(int(list1[1])*int(list2[1]))+(int(list1[2])*int(list2[2])))
    return(output)


if __name__ == '__main__':
   a=(input())
   b=(input())
   a = a.split()
   b = b.split()
   x= sum_of_products(a,b)
   print(x)
