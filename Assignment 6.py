#Question 1

def perfect_number(n):
    s=0
    for i in range(1,n):
        if(n%i==0):
            s+=i
    if(s==n):
        return True
    else:
        return False
N=int(input("Enter a number: "))
if(perfect_number(N)==True):
    print(N," is a perfect number")
else:
    print(N," is not a perfect number")
print()

#Question 2
def palindrome(S):
    S1=S[::-1]
    if S==S1:
        print(S,"is a palindrome")
    else:
        print(S,"is not a palindrome")

s=str(input("Enter a String: "))
palindrome(s)
print()

#Question 3
from math import factorial


def pascal(n):
    for i in range(n):
        for j in range(n - i + 1):
            print(end=" ")
        for j in range(i + 1):
            print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")
        print()

N = int(input("Enter a number: "))
pascal(N)
print()

#Question 4
def ispangram(str):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    for char in alphabet:
        if char not in str.lower():
            return False

    return True


s = input("Enter a String: ")
if (ispangram(s) == True):
    print(f"Yes '{s}' is a panagram")
else:
    print(f"No '{s}' is not a panagram")
print()

#Question 5
S=str(input("Enter a hyphen separated sentence: "))

S1=S.split("-")
S1.sort()

print("-".join(S1))
print()

#Question 6
def student_data(student_name , student_branch, student_id):
    print("student name: ",student_name)
    print("student branch: ",student_branch)
    print("student id: ",student_id)

student_data("Manish","Civil",21102048)
print()

#Question 7
class Student:
    pass
class Marks:
    pass
student1 = Student()
marks1 = Marks()
print(isinstance(student1, Student))
print(isinstance(marks1, Student))
print(isinstance(marks1, Marks))
print(isinstance(student1, Marks))
print("\nCheck whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(Student, object))
print(issubclass(Marks, object))
print()

#Question 8
def findTriplets(arr, n):
    found = False
    for i in range(0, n - 2):

        for j in range(i + 1, n - 1):

            for k in range(j + 1, n):

                if (arr[i] + arr[j] + arr[k] == 0):
                    print(arr[i], arr[j], arr[k])
                    found = True

    if (found == False):
        print("No triplets exist")

lst = []
n = int(input("Enter number of elements : "))

for i in range(0, n):
    ele = int(input())
    lst.append(ele)
print(findTriplets(lst, n))
print()

#Question 9
class parantheses:
    def find(str):
        a= ['()', '{}', '[]']
        while any(i in str for i in a):
            for j in a:
                str = str.replace(j, '')
        return not str

s = input("Enter the sequence of parantheses : ")
if parantheses.find(s):
    print(s,"-","is balanced")
else:
    print(s,"-","is unbalanced")
