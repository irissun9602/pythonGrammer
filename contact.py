
class Contact:
    # 생성자
    def __init__(self, name, phone_number, e_mail, addr):
        self.name =name
        self.phone_number =phone_number
        self.e_mail = e_mail
        self.addr = addr

    # 객체 정보 출력
    def print_info(self):
        print("Name: ", self.name)
        print("Phone Number: ", self.phone_number)
        print("E-mail: ", self.e_mail)
        print("Address: ", self.addr)

# 사용자로부터 데이터를 입력 받을 때는 input 함수를 사용한다.
def set_contact():
     name = input("Name: ")
     phone_number = input("Phone Number: ")
     e_mail = input("Email: ")
     addr = input("Address: ")

def run():
   set_contact()


if __name__ == "__main__":
    run()

