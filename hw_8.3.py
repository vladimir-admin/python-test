class OnlyNumbersError(Exception):
    pass


def fill_num_list():
    num_list = []

    while True:
        try:
            user_input = input("Введите число: ")
            if user_input == "stop":
                break
            elif not user_input.isdigit():
                raise OnlyNumbersError("Можно вводить только числа")
            else:
                num_list.append(int(user_input))
        except OnlyNumbersError as err:
            print(err)

    return num_list


try:
    num_list = fill_num_list()
    print(f"Список с числами: {num_list}")
except KeyboardInterrupt:
    print("\nПрограмма была остановлена пользователем")