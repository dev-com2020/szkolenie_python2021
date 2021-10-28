def multi(a, b):
    try:
        return int(a) * int(b)
    except (TypeError, ValueError):
        return 0


def _check_age(users, age):
    count = 0
    for i, user in enumerate(users):
        if int(user['age']) < age:
            count += 1
        return count


def check_age(users, age):
    try:
        return _check_age(users, age)
    except (KeyError, ValueError):
        print("Niepoprawne dane")
        return 0


invalid_data = [{'name': 'Bartek', 'age': 'sto'},
                {'name': 'Dawid', 'age': '25'},
                {'name': 'Marcin', 'age': '23'}]

valid_data = [{'name': 'Jan', 'age': '10'},
              {'name': 'Dawid', 'age': '25'},
              {'name': 'Marcin', 'age': '23'}]

print(check_age(invalid_data, 11))
