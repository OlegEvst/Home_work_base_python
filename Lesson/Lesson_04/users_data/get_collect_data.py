from get_user_data import get_name_and_surname, get_brihtday, get_work

def add_users(number):
    all_users = []
    for i in range(number):
        new_user = {
            "id" : i+1,
            "name" : get_name_and_surname()[0],
            "surname" : get_name_and_surname()[1],
            "date" : str(get_brihtday()),
            "work" : get_work()
        }
        all_users.append(new_user)
    return all_users

        










