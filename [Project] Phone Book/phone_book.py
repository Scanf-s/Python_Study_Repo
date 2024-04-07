import os, platform, time

# 연락처 추가 함수
def add_contact() -> dict:
    print("연락처 추가 기능")
    print("추가하고자 하는 사람의 정보를 입력하세요.")
    name = input("이름 : ")
    phone_number = input("전화번호 (숫자만 입력하세요) : ")
    email = input("이메일 주소 : ")

    return {
        "name": name.strip(),
        "phone_number": phone_number.strip(),
        "email": email.strip()
    }
    

# 연락처 목록 보기 함수
def view_contacts(database):
    if not database:
        print("연락처 목록이 비어 있습니다.")
    else:
        for i, contact in enumerate(database, start=1):
            name = contact.get("name")
            phone_number = contact.get("phone_number")
            email = contact.get("email")
            print(f'{i}. 이름: {name} / 전화번호: {phone_number} / 이메일: {email}')
    
    input("엔터를 누르면 초기 화면으로 돌아갑니다.")
    clear_terminal()
    return
    
# 연락처 검색 함수
def search_contacts(database):
    if not database:
        print("연락처 목록이 비어 있습니다.")
    else:
        print("이름, 전화번호, 이메일중 한가지 입력 : ")
        target_string = input()
        
        for contact in database:
            name = contact.get("name")
            phone_number = contact.get("phone_number")
            email = contact.get("email")
            if target_string == name or target_string == phone_number or target_string == email:
                print(f'검색 결과 : {name} / {phone_number} / {email}')
                input("엔터를 누르면 초기 화면으로 돌아갑니다.")
                clear_terminal()
                return

    print("사용자를 찾지 못했습니다.")
    time.sleep(1)
    clear_terminal()
    return


# 연락처 삭제 함수
def delete_contact(database):
    print("삭제하고자 하는 이름을 입력해주세요 : ")
    target_name = input()

    initial_len = len(database)
    database[:] = [contact for contact in database if contact.get("name") != target_name]

    if len(database) < initial_len:
        print("성공적으로 삭제되었습니다.")
        time.sleep(1)
        clear_terminal()
        return
    else:
        print("해당하는 사용자가 존재하지 않습니다.")
        time.sleep(1)
        clear_terminal()
        return


# 화면 초기화 함수
def clear_terminal():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


# 메인 프로그램 루프
def main():
    database = []

    while True:
        print("주소록 관리 시스템")
        print("원하는 메뉴를 입력하세요.")
        print("1. 연락처 추가\n2. 연락처 목록\n3. 연락처 검색\n4. 연락처 삭제\n5. 프로그램 종료")
        menu_number = input()
        if menu_number == "1":
            clear_terminal()
            userdata = add_contact()
            if userdata in database:
                print("이미 추가된 사용자 입니다")
                time.sleep(1)
                clear_terminal()
            else:
                database.append(userdata)
                print("정상적으로 추가되었습니다.")
                time.sleep(1)
                clear_terminal()

        elif menu_number == "2":
            clear_terminal()
            view_contacts(database)

        elif menu_number == "3":
            clear_terminal()
            search_contacts(database)

        elif menu_number == "4":
            clear_terminal()
            delete_contact(database)

        elif menu_number == "5":
            clear_terminal()
            print("프로그램을 종료합니다.")
            time.sleep(1)
            return
        else:
            print("올바른 메뉴를 선택해주세요")
            clear_terminal()

if __name__ == "__main__":
    clear_terminal()
    main()