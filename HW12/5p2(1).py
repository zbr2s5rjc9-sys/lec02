def read_rainfall(weather_filename):
    dataset = []
    with open(weather_filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(float(tokens[9]))

    return dataset

def read_2021_rainfall(weather_filename):
    dataset = []
    with open(weather_filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")

            if tokens[0] == "2021":
                dataset.append(float(tokens[9]))

    return dataset

def read_2022_rainfall(weather_filename):
    dataset = []
    with open(weather_filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")

            if tokens[0] == "2022":
                dataset.append(float(tokens[9]))

    return dataset


def main():
    weather_filename = "weather(146)_2001-2022 (1).csv"

    _2021_rainfall = read_2021_rainfall(weather_filename)
    print(f"2021년 총 강수량 : {(sum(_2021_rainfall))}")

    _2022_rainfall = read_2022_rainfall(weather_filename)
    print(f"2022년 총 강수량 : {(sum(_2022_rainfall))}")

if __name__ == "__main__":
    main()