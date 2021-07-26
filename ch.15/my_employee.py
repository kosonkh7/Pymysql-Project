#직원 클래스와 이를 상속 받는 일용직 클래스
import pickle

class Employee:
    count = 0
    #__init__생성자는 객체를 초기화하는 역할
    def __init__(self, name, salary=0):
        self.__name = name
        self.__salary = salary
        Employee.count += 1
    #소멸자. 객체 삭제하면 count 감소
    def __del__(self):
        Employee.count -= 1
    #멤버의 이름 앞에 __을 붙임으로써 이 멤버를 바로 참조하지 못하도록 한다.
    # -> 진짜로 막는 것보다 이름을 복잡하게 하여 의도치 않은 변경을 예방하는 것에 가까움
    def show(self):
        print(self.__name, self.__salary)
    #getter메서드 -> 외부에서 멤버 조작 일어나지 않도록 게터, 세터 메서드 권장
    def get_salary(self):
        return self.__name, self.__salary
    #setter메서드 / 파이썬에선 언어 차원에서 정보 은폐를 지원하지 않지만, 이것만 잘 활용하면 어느 정도 안정성 확보 가능
    def set_salary(self, salary):
        self.__salary = salary
    #특수 메서드 예시 -> 객체를 문자열화 가능 (그냥 def print() 함수 정의와 활용법 다름)
    def __str__(self):
        return f"이름: {self.__name}, 급여: {self.__salary}"
    #클래스 데코레이터
    @classmethod
    def get_count(cls):
        return cls.count
#상속 class 자식(부모):
class DailyWorker(Employee):
    def __init__(self, name, daily_salary, days=1):
        super().__init__(name, daily_salary)
        self.__days = days

    def get_salary(self):
        name, salary = super().get_salary()
        return name, salary * self.__days

    def show(self):
        name, salary = super().get_salary()
        print(name, salary)

#클래스를 요소로 가진 리스트 e_list
e_list = [ Employee('고광하', 350), Employee('정준일', 250), DailyWorker('손흥민', 10, 30) ]

def display_salary():
    for member in e_list:
        member.show()

def change_salary():
    e_list[0].set_salary(385)
    e_list[2].set_salary(22)

def employee_number():
    print(Employee.get_count(),"명입니다.")

def new_employee():
    name = input("이름을 입력하시오 : ")
    salary = int(input("월급을 입력하시오 : "))
    type = input("(Employee/ DailyWorker) : ")

    if type == "Employee":
        e_list.append(Employee(name, salary))
    elif type == "DailyWorker":
        days = input("근무일을 입력하시오 : ")
        e_list.append(DailyWorker(name, salary, days))

# employee.dat read --> e_list (pickle 사용)
# def load():
#     try:
#         with open("employee.dat", "rb") as fr:
#             e_list = pickle.load(fr)
#     except:
#         print("파일이 존재하지 않습니다")
#
# #employee.dat write <-- e_list
# def save():
#     with open("employee.dat", "wb") as fw:
#         pickle.dump(e_list, fw)
# pickle 모듈을 활용해 파일을 불러오는 것도 배웠었다.
new_employee()
change_salary()
display_salary()
employee_number()
