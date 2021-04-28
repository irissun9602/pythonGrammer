
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
     contact = Contact(name,phone_number,e_mail, addr)
     return contact

# 연락처 출력
def print_contact(contact_list):
    for contact in contact_list:
        contact.print_info()

# 연락처 삭제
def delete_contact(contact_list, name):
    for i, contact in enumerate(contact_list):
        if contact.name == name:
            del contact_list[i]

# 메인 메뉴 구성
def print_menu():
    print("1. 연락처 입력")
    print("2. 연락처 출력")
    print("3. 연락처 삭제")
    print("4. 종료")
    menu = input("메뉴선택: ")
    return int(menu)

# 연락처 파일로 저장
def store_contact(contact_list):
    f = open("contact_db.txt", "wt")
    for contact in contact_list:
        f.write(contact.name + '\n')
        f.write(contact.phone_number + '\n')
        f.write(contact.e_mail+ '\n')
        f.write(contact.addr+ '\n')
    f.close()

# 연락처 파일 불러들이기
def load_contact(contact_list):
    f = open("contact_db.txt", "rt")
    lines = f.readlines()
    num = len(lines) / 4
    num = int(num)

    for i in range(num):
        name = lines[4*i].rstrip('/n')
        phone = lines[4*i+1].rstrip('/n')
        email = lines[4*i+2].rstrip('/n')
        addr = lines[4*i+3].rstrip('/n')
        contact =Contact(name, phone, email, addr)
        contact_list.append(contact)
    f.close()

# 메뉴 반복 출력
def run():
    contact_list = [] # 주소록 리스트
    load_contact(contact_list)

    while 1:
        menu = print_menu() # 메뉴 선택
        if menu == 1:
            contact = set_contact() # 데이터 입력
            contact_list.append(contact) #주소록 추가
        elif menu == 2:
            print_contact(contact_list) # 주소록 출력
        elif menu == 3:
            name = input("Name: ") # 삭제할 연락처 이름 입력
            delete_contact(contact_list, name) # 해당 연락처 삭제
        elif menu == 4: # 종료 조건
            store_contact(contact_list)
            break



if __name__ == "__main__":
    run()

