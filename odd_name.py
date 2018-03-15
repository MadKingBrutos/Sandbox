""" Kieran "MadKingBrutos" Bruton """
UserName = input("Please enter your name.")
output = ""
while UserName == "":
    UserName = input("Invalid name, please try again.")
for i in range(len(UserName)):
    if i % 2 == 0:
        output += UserName[i]
print(output)