#
def checknumber():
    if num % 2==0:
        print(num, "is an even number.")
    else:
        print(num, "is an odd number.")

num = int(input("enter a number: \n >"))
checknumber()

while True:
    a = input("Do you wan to run it again?(yes/no): \n >").strip().lower()
    if a == "yes":
        num = int(input("enter a number: \n >"))
        checknumber()

    else:
        print("Program Finished")
        break 