file1 = open("styles.css", "w+")
for i in range(1,4095+1):
    # for i in range(1, 4095 + 1):
    # L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
    line1 = "._"+'{:03X}'.format(i).upper() +"{\n"
    line2 = "   color: #" +'{:03x}'.format(i).upper() + ";\n"
    line3 = "}"
    L = [line1, line2, line3, "\n"]
    file1.writelines(L)
file1.close()
