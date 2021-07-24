# print("Hello World")

# myage = input("How old are you?")
# print(type(myage))
# print(myage.capitalize())

# print(type(print))
# print(type(678))
# str(678)
# Number: integers, floats(int, float), immutable
# booleans: True, False()bool
# print(4+False)
# Immutable Sequence types
# String(str)
myname = 'Johnn'
# print(len(myname))
# print(myname[2])
# myname[2] = "w"
# newname = myname[:2] + "w" + myname[3:]
# newname = myname.replace("h", "w")
# print(newname)
# print(myname)
# turple
# Local Enclosing Global Builtin
def my_lenght_determiner(password):
    counter = 0
    for item in password:
        # print(item)
        counter = counter + 1

        def something():
            hobby = "cycling"
            return hobby

    return counter
    print("can you see me?")

user_password = input("Please add your password: ")

password_lenght = my_lenght_determiner(user_password)

if password_lenght < 5:
    print("Please insert a longer password")
elif password_lenght < 10:
    print("The password is strong but can be stronger")
else:
    print("Perfet, your password is very strong")

print(myname)
print(__name__)



