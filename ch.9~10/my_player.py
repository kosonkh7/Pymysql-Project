name_list = [('신수', '추'), ('광현', '김'), ('에릭센', '크리스티안'), ('니퍼트', '더스틴')]

def welcome_msg(name_list):
    for player in name_list:
        f_name, l_name = player
        print(f'{l_name}{f_name} 선수 환영합니다.')

def register_player(name_list):
    name = input("이름 성 : ")
    name = name.split()
    name_list.append(tuple(name))

welcome_msg(name_list)
register_player(name_list)
welcome_msg(name_list)