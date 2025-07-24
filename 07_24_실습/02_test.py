food_list = [
    {
        '종류': '한식',
        '이름': '잡채'
    },
    {
        '종류': '채소',
        '이름': '토마토'
    },
    {
        '종류': '중식',
        '이름': '자장면'
    },
]

# 아래에 코드를 작성하시오.

for i in food_list:
    if i['이름'] == '토마토':
        food_list[1]['종류'] = '과일'
        print(f'{i["이름"]}은/는 {i["종류"]}(이)다')
    elif i['이름'] == '자장면':
        print(f'{i["이름"]}은 고춧가루지')
        print(f'{i["이름"]}은/는 {i["종류"]}(이)다')
    else:
        print(f'{i["이름"]}은/는 {i["종류"]}(이)다')

print(food_list)

count = 0
while len(food_list) != count:
    if food_list[count]['이름'] == '토마토':
        food_list[1]['종류'] = '과일_2'
        print(f'{food_list[count]["이름"]}은/는 {food_list[count]["종류"]}(이)다')
    elif food_list[count]['이름'] == '자장면':
        print(f'{food_list[count]["이름"]}은 고춧가루지')
        print(f'{food_list[count]["이름"]}은/는 {food_list[count]["종류"]}(이)다')
    else:
        print(f'{food_list[count]["이름"]}은/는 {food_list[count]["종류"]}(이)다')
    count += 1
print(food_list)
