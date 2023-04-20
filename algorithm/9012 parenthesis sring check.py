T = int(input())

for i in range(T):
    stack = []
    a = input()

    for j in a:
        if j =='(':
            stack.append(j)
        elif j ==')':
            # 짝이 맞은 괄호는 제거
            if stack :
                stack.pop()
            # 제거할 (가 없으면 잘못된 괄호로 NO 출력
            else:
                print("NO")
                break

    else :
        # break 문 걸리지 않고 stack을 모두 비웠으면 YES
        if not stack :
            print("YES")

        # ( 짝이 안맞아서 남아있는 경우 NO
        else :
            print("NO")


