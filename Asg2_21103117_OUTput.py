
# QUESTION 1
string1="Python is a case sensitive language" #String1
print("<A>THE LENGTH OF STRING IS",len(string1)) #Function to Find LENGTH OF STRING
print("<B>THE REVERSED STRING IS ",string1[-1::-1])
string2=string1[10:26] #STORED a case sensitive IN A NEW STRING
string2.replace("a case sensitive","object oriented") #REPLACED "a case sensitive" WITH "object oriented"
print("<E>THE INDEX OF SUBSTRING a is ",string1.find('a'))
print("<F>THE ORIGINAL STRING AFTER REMOVING WHITESPACES IS",string1.replace(" ",""))
print("\n")


#QUESTION 2
NAME=input("ENTER YOUR NAME")
SID=int(input("ENTER YOUR SID"))
DEPARTMENT=input("ENTER YOUR DEPARTMENT")
CGPA=float(input("ENTER YOUR CGPA"))
print("Hey %s,"%NAME,"Here!")
print("My SID is %d" %SID)
print("I am from %s"%DEPARTMENT,"and my CGPA is %f"%CGPA)
print("\n")

#QUESTION 3
a=56
b=10
print("a. ",a&b)
print("b. ",a|b)
print("c. ",a^b)
print("Left shift both a and b with 2 bits respectively are :",a<<2 ,b<<2)
print("Right shift a with 2 bits and b with 4 bits respectively are : ",a>>2,b>>4)
print("\n")


#QUESTION 4
numb1 = int(input("Enter first number: "))
numb2 = int(input("Enter second number: "))
numb3 = int(input("Enter third number: "))

if (numb1 > numb2) and (numb1 > numb3):
   largest = numb1
elif (numb2 > numb1) and (numb2 > numb3):
   largest = numb2
else:
   largest = numb3

print("THE LARGEST NUMBER IS ",largest)
print("\n")


#QUESTION 5
i=input("ENTER A STRING")
if 'name' in i:
    print ("Yes")
else:
    print ("No")
print("\n")

#QUESTION 6
p=int(input("ENTER FIRST SIDE OF TRIANGLE"))
q=int(input("ENTER SECOND SIDE OF TRIANGLE"))
r=int(input("ENTER THIRD SIDE OF TRIANGLE"))
if((p+q)>r and (q+r)>p and (r+p)>q and p>0 and q>0 and r>0): #All sides should be positive and sum of two sides should be greater than third side
    print("Yes")
else:
    print("No") 
 36  Asg2_21103050_output.py 
@@ -0,0 +1,36 @@
<A>THE LENGTH OF STRING IS 35
<B>THE REVERSED STRING IS  egaugnal evitisnes esac a si nohtyP
<E>THE INDEX OF SUBSTRING a is  10
<F>THE ORIGINAL STRING AFTER REMOVING WHITESPACES IS Pythonisacasesensitivelanguage


ENTER YOUR NAMEsushantbhatia
ENTER YOUR SID21103117
ENTER YOUR DEPARTMENTcse
ENTER YOUR CGPA9.7
Hey ankitbhalla, Here!
My SID is 21103117
I am from cse and my CGPA is 9.700000


a.  8
b.  58
c.  50
Left shift both a and b with 2 bits respectively are : 224 40
Right shift a with 2 bits and b with 4 bits respectively are :  14 0


Enter first number: 55
Enter second number: 54
Enter third number: 60
THE LARGEST NUMBER IS  60


ENTER A STRINGname
Yes


ENTER FIRST SIDE OF TRIANGLE5
ENTER SECOND SIDE OF TRIANGLE6
ENTER THIRD SIDE OF TRIANGLE8
Yes
