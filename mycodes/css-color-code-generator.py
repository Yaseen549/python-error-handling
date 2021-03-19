# import colorsys

k = '_'
file1 = open("myfile.txt", "w+")
for i in range(1,10+1):
    # L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
    line1 = "._"+'{:06X}'.format(i).upper() +"{\n"
    line2 = "   color: #" +'{:06x}'.format(i).upper() + ";\n"
    line3 = "}"

    L = [line1, line2, line3, "\n"]

    file1.writelines(L)

file1.close()

j = '_'
# loop for all characters
for numbers in line1:
    if numbers.isdigit():
        line1 = line1.replace(numbers, j)

print("The resultant string : " + str(line1))

K = '_'
# loop for all characters
for numm in line1:
    if numm == 0:
        line1 = line1.replace(numm, K)

# printing result
print("The resultant string : " + str(line1))

# for i in range(1,255+1):
#     print('{:06x}'.format(i))

#     print('{:d}'.format(i).zfill(1))
#     print(hex(15))

# Python3 program to illustrate
# hex() function


# original important number for upto ffffff
# print('{:06x}'.format(16777215))

