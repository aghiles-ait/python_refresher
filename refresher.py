from imports.grade_average_service import compute_grade
import imports.drink_selector as drink_selector

def string_assignement():
    print("================ String assignement ====================")
    
    name="Aghiles"
    greeting1 = "Hi " + name
    print(greeting1)

    greeting2 = f"Hi {name}"
    print(greeting2)

    greeting3 = "Hi {}"
    print(greeting3.format(name)) 

def list_manipulation():
    print("================ List manipulation ====================")
    
    # create
    my_list = ["Hi", 24, "yes"]
    print(f"Create: {my_list}")
    
    # read
    print(f"Read part: {my_list[0:2]}")

    # update (modify)
    my_list[0] = "Hello"
    print(f"Update (modify): {my_list}")

    # update (add last)
    my_list.append("last")
    print(f"Update (add last): {my_list}")

    # update (add middle)
    my_list.insert(2, "middle")
    print(f"Update (add middle): {my_list}")
    
    # remove (value)
    my_list.remove("middle")
    print(f"Remove (value): {my_list}") 

    # remove (index)
    my_list.pop(1)
    print(f"Remove (index): {my_list}") 

def set_manipulation():
    print("================ Set manipulation ====================")
    
    my_set = {1,2,3,4,5}
    print(f"Create: {my_set}")

    # update (add one single)
    my_set.add(6)
    print(f"Update (add single): {my_set}")

    # update (add multiple)
    my_set.update([7,8,9])
    print(f"Update (add multiple): {my_set}")

    # remove (value)
    my_set.discard(3)
    print(f"Remove (value): {my_set}")

def tuple_manipulation():
    print("================ Tuple manipulation ====================")
    
    my_tuple = (1,2,3,4,5)
    print(f"Create: {my_tuple}")

    # read
    print(f"Read part: {my_tuple[0:2]}")

def dictionnary_manipulation():
    print("================ Tuple manipulation ====================")

    my_dic = {
        "username": "aghia",
        "name": "aghiles",
        "age": 28
    }
    
    # create
    print(f"Create: {my_dic}")

    # read (key)
    print(f"Read part: {my_dic.get("username")}")

    # update (add or modify)
    my_dic["married"]= True
    print(f"Update: {my_dic}")
    
    # delete key-value
    my_dic.pop("age")
    print(f"Delete (key-value): {my_dic}")

    #looping key
    for key in my_dic:
        print(f"loop keys: {key}")
    
    #looping key-value
    for key, value in my_dic.items():
        print(f"loop key-values: {key} : {value}")

    # delete all entries
    my_dic.clear()
    print(f"Delete all: {my_dic}")


if __name__ == "__main__":
    #string_assignement()
    #list_manipulation()
    #set_manipulation()
    #tuple_manipulation()
    #dictionnary_manipulation()

    # use first import
    homeworks = {
        'homework1': 15,
        'homework2': 17,
        'homework3': 14
    }
    print(compute_grade(homeworks))

    # use second import
    print(drink_selector.choose_drink(["Water", "Coffee", "Soda"]))
