def solution(code, day, data):
    answer = []
    data_dict = {}

    for d in data:
        data_splits = d.split()
        price = data_splits[0].split('=')[1]
        code = data_splits[1].split('=')[1]
        time = data_splits[2].split('=')[1]
        if data_dict.get(code) is None:
            data_dict[code] = [(time, price)]
        else:
            data_dict[code].append((time, price))

    for k,v in data_dict.items():
        data_dict[k].sort(key=lambda x: x[0])
    print(data_dict)

    for data in data_dict[code]:
        if data[0][:-2] == day:
            answer.append(int(data[1]))

    return answer

print(solution("012345", "20190620",["price=80 code=987654 time=2019062113", "price=90 code=012345 time=2019062014", "price=120 code=987654 time=2019062010", "price=110 code=012345 time=2019062009", "price=95 code=012345 time=2019062111"]))