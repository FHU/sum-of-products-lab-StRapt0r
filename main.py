def sum_of_products(list1, list2):
    output=0
    a = [int(i) for i in list1.split(' ')]
    b = [int(i) for i in list2.split(' ')]
    for i in (list1):
        output=output+(list1[i-1]*list2[i-1])
    return(output)


if __name__ == '__main__':
   a=input()
   b=input()
   x= sum_of_products(a,b)
   print(x)
