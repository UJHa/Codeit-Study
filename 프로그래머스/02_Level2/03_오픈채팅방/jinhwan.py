# 오픈채팅방(성공)
# 정확성: 100.0
# 합계: 100.0 / 100.0
def solution(record):
    answer = []
    log_dict = {}

    index = 0
    for r in record:
        data_list = r.split()
        command, user_id = data_list[0], data_list[1]
        if command == 'Enter':
            # 최초 enter 시 log_dict[key]의 value 초기화
            if log_dict.get(user_id) is None:
                log_dict[user_id] = {'log_list': [], 'current_nickname': ''}
            # 과거 이력의 닉네임들 현재 진입 시 닉네임으로 변경
            else:
                for i in log_dict[user_id]['log_list']:
                    answer[i] = answer[i].replace(log_dict[user_id]['current_nickname'], data_list[2])
            log_dict[user_id]['current_nickname'] = data_list[2]

            # 채팅에 추가된 index를 log_list에 저장
            answer.append(f"{data_list[2]}님이 들어왔습니다.")
            log_dict[user_id]['log_list'].append(index)
            index += 1
        elif command == 'Leave':
            # 채팅에 추가된 index를 log_list에 저장
            answer.append(f"{log_dict[user_id]['current_nickname']}님이 나갔습니다.")
            log_dict[user_id]['log_list'].append(index)
            index += 1
        elif command == 'Change':
            for i in log_dict[user_id]['log_list']:
                answer[i] = answer[i].replace(log_dict[user_id]['current_nickname'], data_list[2])
            log_dict[user_id]['current_nickname'] = data_list[2]

    return answer


s = solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])\
    == ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
print(s)
