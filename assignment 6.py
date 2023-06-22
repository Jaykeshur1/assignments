def ds(roll_no, name):
    # Create the data structures
    my_list = [roll_no, name]
    my_tuple = (roll_no, name)
    my_set = {roll_no, name}
    my_dict = {'roll_no': roll_no, 'name': name}

    # Print the initial data structures
    print("Initial data structures:")
    print("List:", my_list)
    print("Tuple:", my_tuple)
    print("Set:", my_set)
    print("Dictionary:", my_dict)

    # Change values during runtime
    my_list[0] = 10
    my_tuple = (20, "John")
    my_set.remove(roll_no)
    my_dict['name'] = "Alice"

    # Print the modified data structures
    print("Modified data structures:")
    print("List:", my_list)
    print("Tuple:", my_tuple)
    print("Set:", my_set)
    print("Dictionary:", my_dict)

    # Delete the data structures
    del my_list
    del my_tuple
    del my_set
    del my_dict

    print("Modified data structures:")
    print("List:", my_list)
    print("Tuple:", my_tuple)
    print("Set:", my_set)
    print("Dictionary:", my_dict)

