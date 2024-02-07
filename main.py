def sum_of_products(list1, list2):
    output=0
    for i in (list1):
        output=output+(list1[i-1]*list2[i-1])
    return(output)


if __name__ == '__main__':
   a=(input())
   b=(input())
   a = a.split()
   b = b.split()
   a = [eval(i) for i in a]
   b = [eval(i) for i in b]
   x= sum_of_products(a,b)
   print(x)
