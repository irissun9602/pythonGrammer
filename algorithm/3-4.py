
#K로 나누었을 때 나머지만큼 먼저 빼는 연산을 한 후 나누기 연산 작업
n,k = map(int, input().split())
result = 0


remainder = n % k
n = n- remainder #K의 배수로 만들기
result = remainder


while(n > 1):
    n = n//k
    result += 1

print(result)
