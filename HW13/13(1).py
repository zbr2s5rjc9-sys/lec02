def read_weather_col(weather_filename, col_idx, conv_fn):
    dataset = []
    with open(weather_filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(conv_fn(tokens[col_idx]))

    return dataset

def sumifs(rainfall, months, selected_month):
    total_value = 0
    for i in range(len(rainfall)):
        r = rainfall[i]
        m = months[i]
        if m in selected_month: # [6, 7, 8]
            total_value += r

    return total_value


def main():
    weather_filename = "weather(146)_2022-2022.csv"

    rainfall = read_weather_col(weather_filename, 9, float)
    months = read_weather_col(weather_filename, 1, int)

    summer_rainfall = sumifs(rainfall, months, [6,7,8])

    print(f"2022년 총 강수량 : {sum(rainfall)}mm")
    print(f"2022년 여름철 강수량 : {summer_rainfall:.1f}mm")

if __name__ == "__main__":
    main()