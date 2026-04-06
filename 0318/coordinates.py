
x1 = float(input("x1의 좌표를 입력하세세요 : "))
y1 = float(input("y1의 좌표를 입력하세요 : "))

if x1 > 0 and y1 > 0:print(f"입력한 좌표 ({x1},{y1})는 1사분면 위의 좌표입니다.")
elif x1 < 0 and y1 > 0:print(f"입력한 좌표 ({x1},{y1})는 2사분면 위의 좌표입니다.")
elif x1 < 0 and y1 < 0:print(f"입력한 좌표 ({x1},{y1})는 3사분면 위의 좌표입니다.")
elif x1 > 0 and y1 < 0:print(f"입력한 좌표 ({x1},{y1})는 4사분면 위의 좌표입니다.")
