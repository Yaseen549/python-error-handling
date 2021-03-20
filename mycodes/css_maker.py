def css_class_generator():
    total_num_of_classes = int(input("How many CSS class you need?"))
    myfile = open("mycolors.txt", "w+")

    for i in range(int(total_num_of_classes)):
        print("Class ", int(i+1))
        total_num_of_pv = int(input("How many properties?"))
        myselector = input(str("Selector: "))
        for j in range(int(total_num_of_pv)):
            myproperty = input(str("Property: "))
            myvalue = input(str("Value: "))
            # line1 = "._"+'{:06X}'.format(i).upper() +"{"
            line1 = "." + myselector +"{\n"
            line2 = "    " + myproperty + ": " + myvalue + ";\n"
            line3 = "}"
            l = [line1, line2, line3]
            print(l)
            myfile.writelines(l)
    myfile.close()

# css_class_generator()