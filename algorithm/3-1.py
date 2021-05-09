'''
거스름돈 동전의 최소 개수 구하기
'''
n = 1260
count = 0

#큰 단위의 화폐부터 차례대로 확인
coin_types= [500,100,50,10]

for coin in coin_types:
    count += n // coin # 몫 연산
    n %= coin # 나머지 연산

print(count)