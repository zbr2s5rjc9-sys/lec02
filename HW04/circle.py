import math

R = float(input("반지름을 입력해라 : "))

area =  math.pi * (R ** 2)
circumference = 2 * math.pi * R

print(f"원의 면적 : {area:.2f}")
print(f"원의 둘레 : {circumference:.1f}")