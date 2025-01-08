 # given number is odd or even
# a=int(input("enter a number :"))
# if a%2==0:
#      print("the number is even ")
# else:
#      print("the num is odd")

# # largest of three number  
# a=10
# b=50
# c=60                                                                    
# largest=int()
# print(type(largest),' - ',largest)
# def check_largest_number(a,b,c) :
#     if a>=b and a>=c:
#         largest=a
#         return largest
#     elif b>=a and b>=c:
#         largest=b
#         return largest
#     else:
#         largest=c
#         return largest
# print("largest number is: ",check_largest_number(a,b,c))

# REVERSE A STRING
# def reverse_string(input_string):
#     return input_string[::-1]
# result = reverse_string("Skyllx")
# print(result)

# PALINDROME

# def is_palindrome(input_string):
#     return input_string == input_string[::-1]
# input_str = "VISHAL"
# if is_palindrome(input_str):
#     print("The string is a palindrome.")
# else:
#     print("The string is not a palindrome.")

# MERGE DICTIONARY

# def merge_dicts(dict1, dict2):
#     return dict1 | dict2
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'c': 3, 'd': 4}
# merged_dict = merge_dicts(dict1, dict2)
# print(merged_dict)

#FACTORIAL

# num=int(input("Enter number to find the Factorial : "))
# def fact(num):
#     if num==1 or num==0:
#         return 1
#     else:
#         return num * fact(num-1)
# print("Factorial Number of",num,"is :",fact(num))
