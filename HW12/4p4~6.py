def read_rainfall(weather_filename):
    dataset = []
    with open(weather_filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(float(tokens[9]))

    return dataset

def get_rain_event_days(rainfall):

    dataset_rainfall = []
    for r in rainfall: #비가 오면 1, 안 오면 0
        if r > 0:
            dataset_rainfall.append(1)
        else:
            dataset_rainfall.append(0)

    dataset_rain_event = []
    for i in range(len(dataset_rainfall)):
        r = dataset_rainfall[i]
        if r == 0:
            dataset_rain_event.append(0)
        else:
            dataset_rain_event.append(dataset_rain_event[i-1] +1) #(어제까지 연속으로 비 온 횟수 + 오늘 하루 추가)

    return max(dataset_rain_event) #최장연속강우일수

def get_max_rainfall_event(rainfall): #연속으로 내린 비의 총량(최대 강우량)
    dataset = []
    for r in rainfall:
        if r > 0:
            if rainfall_event != None: #비어있지 않음
                rainfall_event.append(r)
            else:
                rainfall_event = [r]

        else:
            if rainfall_event != None:
                dataset.append(rainfall_event)
            rainfall_event = None

def read_tmax(weather_filename):  #가장 더운 날 top3
    dataset = []
    with open(weather_filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(float(tokens[3]))

    return dataset


def get_top3(list_values):
    return sorted(list_values) [-3:] #top3로 정렬하기


def main():
    weather_filename = "weather(146)_2022-2022.csv"
    rainfall = read_rainfall(weather_filename)
    tmax = read_tmax(weather_filename)

    max_rainy_days = get_rain_event_days(rainfall)
    print(f"최장 연속 강우일수 : {max_rainy_days}")

    max_rainfall_event = get_rain_event_days(rainfall)
    print(f"최대 강우량 : {max_rainfall_event}")

    tmax_top3 = get_top3(tmax)
    print(f"가장 더운 날 top3 : {tmax_top3}")


if __name__ == "__main__":
    main()