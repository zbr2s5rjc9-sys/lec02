def average(nums):
    total = 0
    for n in nums:
        total += n
    return total / len(nums)


def main():
    input_text = "12 19 27 34 90"
    tokens = input_text.split() #['12, 19, 27, 34, 90']
    nums = []
    for token in tokens:
            nums.append(int(token))

    print(average(nums))

if __name__ == "__main__":
    main()

