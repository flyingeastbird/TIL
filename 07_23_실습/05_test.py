number_of_people = 0

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
    print(f'현재 가입된 유저 수: {number_of_people}')
    print(f'{name}님 환영합니다.')
    return print(user_info)
    
create_user('홍길동', 30, '서울')