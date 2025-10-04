import math
a = float(input("Введите длину первой стороны: "))
b = float(input("Введите длину второй стороны: "))
angle = float(input("Введите угол между сторонами в градусах: "))

# Преобразование угла в радианы и расчет
angle_rad = math.radians(angle)
c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(angle_rad))

print(f"Длина третьей стороны: {c:.2f}")