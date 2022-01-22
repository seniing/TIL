def is_id_valid(user_data):
    pass
    # 여기에 코드를 작성합니다.
    
    # 0~9 사이의 숫자를 정수형으로 변환해 넣을 list
    num_list = [] 
    for i in range(0,10):
        num_list.append(str(i)) 

    # 'id'의 마지막 값이 num_list에 있다면 True 아니면 False
    if user_data['id'][-1] in num_list:
        return 'True'
    else:
        return 'False'


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    user_data1 = {
        'id': 'jungssafy5',
        'password': '1q2w3e4r',
    }
    print(is_id_valid(user_data1)) 
    # True
    
    user_data2 = {
        'id': 'kimssafy!',
        'password': '1q2w3e4r',
    }
    print(is_id_valid(user_data2)) 
    # False