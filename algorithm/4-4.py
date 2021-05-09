n,m = map(int, input().split())

d = [[0]* m for _ in range(n)] # 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
#현재 캐릭터의 X좌표, Y좌표, 방향을 입력받기
x, y, direction = map(int, input().split())

#현재좌표 방문 처리
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

#북, 동, 남, 서 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0 ,-1]

#왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction =3 # 북 다음은 서

#시뮬레이션 시작
count = 1
turn_time = 0
while True :
    #왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == 0 and array [nx][ny] ==0: #가보지 않은 칸이 존재하고 육지일때
        d[nx][ny] = 1 # 방문 처리
        #현재 위치 이동
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    #네 방향 모두 갈 수 없는 경우 방향을 유지한 채 뒤로 1칸
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        #바다가 아니라 뒤로 갈 수 있는 경우 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        #뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time=0

print(count)

