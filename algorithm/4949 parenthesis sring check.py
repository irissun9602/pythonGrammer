
while True:
    stack = []
    a = input()

    if a == ".":
        break

    for j in a:
        if j =='(' or j == '[':
            stack.append(j)
        elif j ==')':
            # 짝이 맞은 괄호는 제거
            if len(stack) != 0 and stack[-1] == '(' :
                stack.pop()
            # 제거할 (가 없으면 잘못된 괄호로 NO 출력
            else:
                stack.append(')')
                break

        elif j == ']':
            # 짝이 맞은 괄호는 제거
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            # 제거할 (가 없으면 잘못된 괄호로 NO 출력
            else:
                stack.append(']')
                break
    # break 문 걸리지 않고 stack을 모두 비웠으면 YES
    if not stack :
        print("yes")

    # ( 짝이 안맞아서 남아있는 경우 NO
    else :
        print("no")


