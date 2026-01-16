todo_list = ["banana","Apple"]


while True:
    print("---------TO_DO_LIST---------")

    for x in todo_list:
        print(todo_list.index(x)+1,x)

    print("----------------------------")
    quitt = input("Enter New Task(Press Q to Exit):")
    if quitt.capitalize() == 'Q':
        break
    else:
        todo_list.append(quitt)


