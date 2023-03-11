def leftRotate(arr,d,n):
    d = d % n
    g_c_d = gcd(d,n)
    for i in range(g_c_d):
        temp = arr[i]
        j = i
        while 1:
            k = j+d
            if k>=n:
                k = k-n
            if k==i:
                break
            arr[j]=arr[k]
            j=k
        arr[j]=temp
    return arr

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
arr = [1,2,3,4,5,6,7]
n = len(arr)
d =2
print(leftRotate(arr,d,n))