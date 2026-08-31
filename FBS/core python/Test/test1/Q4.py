area = float(input("Enter area of one wall: "))
interior_cost = float(input("Enter cost of interior wall: "))
exterior_cost = float(input("Enter cost of exterior wall: "))

interior_total = area * interior_cost
exterior_total = area * 7 * exterior_cost

total_cost = interior_total + exterior_total

print("Interior painting cost =", interior_total)
print("Exterior painting cost =", exterior_total)
print("Total painting cost =", total_cost)