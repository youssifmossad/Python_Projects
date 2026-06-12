# list=[]
# print('You will add the numbers to shape the f letter to quit use 0 number \n number not accepted')
# n=int(input("Enter the shape layout numbers please: "))       
# x=int(input("enter the number of columns you want in the shape !")) 
# for i in range(x):
#     list.append(n)
#     
# print("Thanks for using my code")


    
list =[]
x=int(input("enter the number of rowsyou want in the shape !"))
for i in range(x):
    n=int(input("Enter the shape layout numbers please: "))
    list.append(n)
for i in list:
    print(i*'x')
print("Thanks for using my code")       