# Sieve 
# 
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
n = len(a)

for i in range(1, int(n**(1/2))+1):
    # if 
    pass

p = [True]*n

# for i in range(len(a)):
#     p[i] = True

p[0] = False

for i in range(2, int(n**(1/2))+1):
    if p[i] == True:
        j = i*i
        while j<n+1:
            p[i*j] = False
            j == i

cp = 
print(p)
