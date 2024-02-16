current_users=["nana","yaw","jojo","wallace","jones"]
new_users=["nana","papa","nkay","bab","jeff"]


for user_name in new_users:
    low_username = user_name.lower()
    if low_username in current_users:
        print (f"The user name '{low_username}' has already been used ")
    else:
        print(f"the username '{low_username}' is available.")
