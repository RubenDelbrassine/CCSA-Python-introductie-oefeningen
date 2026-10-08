# print((10 // 3) * 3 + 10 % 3)

aantalPerKist = 20
aantalPerPallet = 35

input = int(input())

print(input//aantalPerKist//aantalPerPallet)
print(input//aantalPerKist%aantalPerPallet)
print(input % aantalPerKist)
