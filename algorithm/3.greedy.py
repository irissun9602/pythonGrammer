# N*M 행렬 입력값 입력 받기
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 가장 작은 수 찾기
    min_value = min(data)
    # 최종적으로 가장 높은 숫자가 쓰인 카드를 뽑을 수 있도록 max로 최댓값 찾기
    result = max(result, min_value)

print(result)