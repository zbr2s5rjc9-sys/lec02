def read_weather_col(weather_filename, col_idx, conv_fn):
    dataset = []
    with open(weather_filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(conv_fn(tokens[col_idx]))

    return dataset

def sumifs(rainfall, months, selected_months):
    total_value = 0
    for i in range(len(rainfall)): # 같은 위치에 있는 걸 보겠다는 거임
        r = rainfall[i]
        m = months[i]
        if m in selected_months:
            total_value += r

    return total_value

def sum_annual(rainfall, years): # 이 변수들을 함수 안에서 자유롭게 쓸 수 있다는 것!
    dataset = []
    for y in range(2001, 2023):
        dataset[y] = sumifs(rainfall, years, [y])

    return dataset

def main():
    weather_filename = "weather(146)_2001-2022 (1).csv"
    rainfall = read_weather_col(weather_filename, 9, float)
    years = read_weather_col(weather_filename, 0, int)

    for y in range(2001, 2023):
        rainfall_y = sumifs(rainfall, years, [y])
        print(f"{y}년 강수량 : {rainfall_y:.1f}mm")


if __name__ == "__main__":
    main()