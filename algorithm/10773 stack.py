# 백준 10773번

k = int(input())

a = []
for i in range(k):
    n = int(input())

    # 입력받은 숫자가 0이라면 최근 리스트 노드 제거
    if n==0 :
        a.pop()
    
    # 리스트 추가
    else :
        a.append(n)
# 합계 출력
print(sum(a))




