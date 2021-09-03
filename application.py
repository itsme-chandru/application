def check_for_num(string):
    for i in string:
        if i.isdigit() :
            return True
    return False
def check_for_gender(string):
    gender=["m","f","M","F","other","male","female","Other","MALE","FEMALE","Male","Female"]
    if string not in gender:
            return True
    return False
main_list=[]
while True:
    name = input("Enter a name: ")
    if name == "" or check_for_num(name):
        print("Invalid Name")
    else:
        main_list.append(name)
        break

while True:
    try:
        age = int(input("Enter a age: "))
    except Exception as error:
        print("please enter a valid age")
    else:
        main_list.append(age)
        break
while True:
    gender = input("Enter a gender: ")
    if gender == "" or check_for_gender(gender):
        print("Invalid gender")
    else:
        main_list.append(gender)
        break
while True:
    try:
        salary = int(input("Enter a salary: "))
    except Exception as error:
        print("please enter a valid salary")
    else:
        if(salary<=0):
            print("enter a valid salary")
        else:
            main_list.append(salary)
            break
while True:
    state = input("Enter a state: ")
    if state == "" or check_for_num(state):
        print("Invalid state")
    else:
        main_list.append(state)
        break
while True:
    city = input("Enter a city: ")
    if city == "" or check_for_num(city):
        print("Invalid city")
    else:
        main_list.append(name)
        break

print(main_list)
