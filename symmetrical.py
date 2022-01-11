input_array = input("Please enter like this  1,2,2,1 : ")

flag = False
list = input_array.split(",")
len_list = len(list)      

for i in range(len_list):
    if list[i] == list[len_list - 1]:
        flag = True

    else :
        flag = False
        break

    len_list -= 1

if flag == True:
    print("Symmetrical") 
else:
    print("Not symmetrical")