# N, M, K를 공백으로 구분하여 입력받기
n,m,k = map(int,input().split())
#N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() #입력받은 수 정렬하기
first = data[n-1]
second = data[n-2]

#반복되는 수열 K+1 묶음으로 전체 반복횟수와 나머지 횟수 구하기
times = m/(k+1) # 큰 묶음 반복 횟수
time = m%(k+1) # 나머지 반복 횟수

result = (first*k+second)*times + first*time
print(result)