def read_rainfall(weather_filename):
    dataset = []
    with open(weather_filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(float(tokens[9]))

    return dataset

def read_years(weather_filename):
    dataset = []
    with open(weather_filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(float(tokens[0]))

    return dataset

def sumifs(rainfall, years, selected): # 더할 값, 조건 기준, 원하는 조건
    total = 0
    for i in range(len(rainfall)):
        if years[i] in selected: #조건 확인(원하는 조건 안에 있냐는 거지)
            total += rainfall[i] #더해!


    return total


def main():
    weather_filename = "weather(146)_2001-2022 (1).csv"

    rainfall = read_rainfall(weather_filename)
    years = read_years(weather_filename)

    result_2021 = sumifs(rainfall, years, [2021])
    result_2022 = sumifs(rainfall, years, [2022])

    print(f"2021년 총 강수량 : {result_2021}")
    print(f"2022년 총 강수량 : {result_2022}")


if __name__ == "__main__":
    main()