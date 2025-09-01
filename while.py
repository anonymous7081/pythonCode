# i = 1
# max = 0
# while(i<=5):
    
#     a = int(input())
#     if(a>max):
#         max = a
#     i = i+1
    
# print(max)


# n = 7068

# for i in range (n):
#     last = n%10
#     print(last)
#     n = n//10
#     if n==0:
#         break

n = 7065

rev =0
while(n!=0):
    digit = n%10
    rev = rev*10 + digit
    n = n//10
print (rev)