# 숫자를 문자열로 변환시키는 함수 "{}".format()

format_a = "{}".format(5)

format_b = "{} {}".format(1,2)

format_c = "오늘은 4월 {}일".format(20)

print(format_a)
print(format_b)
print(format_c)

# 숫자 이외의 자료형도 문자열로 변환 가능
format_d = "{} {} {}".format(1, "string", True)

print(format_d)