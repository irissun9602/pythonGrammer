#현재 나이트의 위치 입력받기
now_location = input()
row = int(now_location[1]) - 1 #인덱스 0부터 시작하는 행
column = int(ord(now_location[0])) - int(ord('a'))   #인덱스 0부터 시작하는 열

print(row, column)
steps = [(-2, -1), (-2, 1), (2, 1), (2, -1), (-1, 2), (-1, -2), (1, 2), (1, -2)]
count = 0

for step in steps:
    x = step[0]+ row
    y = step[1] +column
    if (0<=x<=8) and (0<=y<=8):
        print(step[0], step[1])
        count += 1

print(count)


