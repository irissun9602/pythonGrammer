n, k = map(int, input().split())
result = 0

# n은 항상 k보다 크다는 조건을 통해 while문 작성
while n >= k:
    # n이 k의 배수가 아닐 경우는 계속 1씩 빼줌
    while n % k != 0 :
        n -= 1
        result += 1
    # n이 k의 배수이면 계속 나눠서 n을 1로 만들 때까지 계속 result를 카운트 하기
    n //= k
    result += 1

# k로 나누고 남은 수에 대하여 1씩 빼기
while n > 1 :
    while n != 0 :
        n -= 1
        result += 1

print(result)