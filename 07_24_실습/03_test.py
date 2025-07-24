matrix = [
        ['0, 1', '0, 2', '0, 3'], 
        ['1, 0', '1, 1', '1, 2', '1, 3'], 
        ['2, 0', '2, 1', '2, 2', '2, 3', '2, 4'], 
        ['3, 0', '3, 1'], 
        ['4, 0', '4, 1', '4, 2'], 
        ['5, 0']
    ]
# 아래애 코드를 작성하시오.

# matrix의 총 길이
for i in matrix:
    matrix_len = 0
    for j in i:
        matrix_len += 1
    print(f'{i}리스트는 총 {matrix_len}개 만큼 요소를 가지고 있습니다.')

# matrix의 각 요소 길이
matrix_len_2 = 0
number = 0
for i in matrix: # 배열 가져오기
    
    for j in i: #리스트 내 리스트 가져오기
        print(f'matirx의{matrix_len_2, number}번째 요소의 값은 {j}입니다.')
        number += 1
    number = 0
    matrix_len_2 += 1

# range와 len을 사용한 순회문

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f'{i, j}번째 요소의 값은 {matrix[i][j]}입니다.')
