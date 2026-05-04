def read_rainfall(weather_filename):
    dataset = []
    with open(weather_filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(float(tokens[9]))

    return dataset

def read_months(weather_filename):
    dataset = []
    with open(weather_filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(float(tokens[1]))

    return dataset

def sumifs(rainfall, months, selected): # 더할 값, 조건 기준, 원하는 조건
    total = 0
    for i in range(len(rainfall)):
        if months[i] in selected: #조건 확인(원하는 조건 안에 있냐는 거지)
            total += rainfall[i] #더해!

    return total


def main():
    weather_filename = "weather(146)_2022-2022.csv"

    rainfall = read_rainfall(weather_filename)
    months =read_months(weather_filename)

    result = sumifs(rainfall, months, [6,7,8])

    print("6~8월 총 강수량 : ", result)

if __name__ == "__main__":
    main()