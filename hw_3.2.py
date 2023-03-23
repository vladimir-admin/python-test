a = input('Введите своё имя:')
b = input('Ведите свою фамилию:')
c = input('Ваш год рождения:')
d = input('Город проживания:')
e = input('Ваш email:')
f = input('Ваш телефон:')


def user_date(first_name, last_name, birthday, city, email, phone):
    print(
        f"Имя - {first_name}, Фамилия - {last_name}, Год рождения - {birthday}, город проживания - {city}, email - {email}, телефон - {phone}")


user_date(first_name=a, last_name=b, birthday=c, city=d, email=e, phone=f)
