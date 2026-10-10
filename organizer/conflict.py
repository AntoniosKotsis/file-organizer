from pathlib import Path

max_attempts = 50

def take_choice():
    # The user decides for the file
    value_res_con = input("Do you want to skip, rename or replace the file?")
    while (value_res_con.lower() != "skip" 
           and value_res_con.lower() != "rename" 
           and value_res_con.lower() != "replace"):
        value_res_con = input("Do you want to skip, rename or replace the file?")

    return value_res_con.lower() 

def take_confirmation():
    # We protect the user so as to be sure for overwriting file
    sure_replace = input("Are you sure (Y/N)?")
    while (sure_replace.upper() != "Y" 
        and sure_replace.upper() != "N"):
        sure_replace = input("Are you sure (Y/N)?")

    return sure_replace.upper() 
    

def resolve_conflict(initial_path: Path, final_path: Path, value_conflict: str):
    list_conflict = []

    # If we call resolve_conflict recursively then we display appropriate messages
    if value_conflict == "rename":
        print(f"You try to move and rename {str(initial_path)} in {str(final_path)}")    
    else:
        print(f"You try to move {str(initial_path)} in {str(final_path)}")
    
    print(f"There is the {str(final_path)}")

    for attempt in range(max_attempts):
        choice = take_choice()

        if choice == "skip":
            list_conflict.append("skip")
            return list_conflict

        elif choice == "rename":
            new_namefile = input("Type a namefile:")
            # We change only the name from final path. We keep the other path and file extension.
            new_final_path = final_path.with_stem(new_namefile)

            # If the file exists after renaming
            if new_final_path.exists():
                list_conflict = resolve_conflict(initial_path,new_final_path,"rename")
                return list_conflict

            # The renaming becomes successfully
            else: 
                list_conflict.append("rename")
                list_conflict.append(new_final_path)
                return list_conflict

        elif choice == "replace":
            answer = take_confirmation()

            if answer == "Y":
                list_conflict.append("replace")
                list_conflict.append(final_path)
                return list_conflict

    print(f"No decision after {max_attempts} attempts")
    print(f"The file skipped. It remains at {initial_path}")

    list_conflict.append("skip")
    return list_conflict