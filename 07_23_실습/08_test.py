number_of_book = 100
number_of_people = 0
many_user = []
info = {}

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


def increase_user():
    global number_of_people
    number_of_people += 1

def create_user(name, age, address):
    
    increase_user()
    user_info = {
        'name': name,
        'age': age,
        'address': address
    }
    print(f'{name}님 환영합니다.')
    return many_user.append(user_info)

def rental_book(kwargs):
    number, name = kwargs['age'] // 10, kwargs['name']
    decrease_book(number)
    return print(f'{name}님이 {number}권의 책을 대여하였습니다.')

def decrease_book(number):
    global number_of_book

    number_of_book = number_of_book - number
    return print(f'남은 책의 수: {number_of_book}')

list(map(create_user, name, age, address))
print(many_user)
info = list(map(lambda user: {'name': user['name'], 'age': user['age']}, many_user))
print(info)
list(map(rental_book, info))
