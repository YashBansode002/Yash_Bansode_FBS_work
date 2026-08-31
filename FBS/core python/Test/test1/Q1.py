

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
radius = float(input("Enter radius: "))

area_rectangle = length * breadth
area_semicircle = (3.14 * radius * radius) / 2

area = area_rectangle + area_semicircle

perimeter = (2 * length) + breadth + (3.14* radius)

print("Area =", area)
print("Perimeter =", perimeter)