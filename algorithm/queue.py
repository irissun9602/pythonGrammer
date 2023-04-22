
# 데스트 개수 입력
test_cases = int(input())

for _ in range(test_cases):
    n, m = list(map(int, input().split()))
    imp = list(map(int, input().split()))
    idx = list(range(len(imp)))
    idx[m] = 'target'

    # 순서
    order = 0

    while True:
        # imp의 첫번째 값의 우선순위가 제일 높을 때
        if imp[0] == max(imp):
            order += 1

            # 찾고 있는 문서일 경우 결과값 print
            if idx[0] == 'target':
                print(order)
                break
            # 들러리 문서일 경우 제거만
            else:
                imp.pop(0)
                idx.pop(0)
        # 우선순위가 밀릴 때 맨 마지막으로 보내기
        else:
            imp.append(imp.pop(0))
            idx.append(idx.pop(0))