# 숫자를 입력받습니다. input으로 입력 받은 데이터의 자료형은 string이기 때문에 int로 형변환 필요
raw_input = int(input("inch 단위의 숫자를 입력해주세요: "))


# cm 단위로 변경
cm = raw_input *2.54

# 출력합니다.
print(raw_input, "inch는 cm단위로", cm, "cm입니다.")