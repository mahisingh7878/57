def sum(n):
    return n*(n+1)/2
print(sum(5))


def arrsum(b):
    sum=0
    for i in range(len(b)):
        sum+=b[i]

    print(sum)

b=[4,7,9,6,8,]
arrsum(b)
 