#Square Footage Formula:
# w= int(input("Enter Width: "))
# l = int(input("Enter Length: "))
# a = l * w 
# print("Square Footage is: ", a)

# a = l * w
l = float(input("What is the lenth of your shape? :"))
w = float(input("What is the width of your shape? :"))
def square_foot(l, w): 
    a = l * w
    print(f"Area = {a}")

square_foot(l, w)
