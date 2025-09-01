

# str = "Ramesh"

# for ch in str:
#     print(ch)

# str = "Ramesh"

# for i in range (0 , len(str)):
#     if(i%2 ==0):
#         print(str[i] , i)
    
# for i in range(len(str)-1 , -1 , -1):
#     print(str[i])
# for i in range (-1 , -len(str)-1 , -1):
#     print(i , str[i])

# n = 567
# s = str(n)

# sum = 0

# for ch in s :
#     sum += int(ch)
# print(sum)

# str = "Ramesh Upadhyay"
# str = str.lower()
# cunt =0
# for ch in str :
#     if (ch =='a' or ch ==  'e' or ch =='i' or ch == 'o' or ch == 'u' ):
#         print(ch)
#         cunt = cunt+1
# print (cunt)


str ="Abhishek"
for i in range(0, len(str)-2 ):
    print(str[i:i+3])
   

str = "madddddmmmmaaaaamdmamdmadmamdmddmmmaammddmmda"

s1 = ""

for ch in str:
    if (ch in s1) != True:
        s1 = s1+ch
print(s1)