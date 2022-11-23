#Circumference of a Circle Formula:
# π = 3.14
# r = int(input("Enter Radius: "))
# c = 2*π*r
# print("Circumference of a Circle is: ", c)

# c = 2 * π * r
r = float(input("What is the radius of your circle? :"))
π = 3.14
def circumference(r):
    c = 2 * π * r
    print(f"Circumference = {c}")

circumference(r)