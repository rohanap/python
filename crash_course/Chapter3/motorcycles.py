motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles.append('bajaj')
print(motorcycles)


mobile_brands = []
print(mobile_brands)
mobile_brands.append('apple')
mobile_brands.append('samsung')
mobile_brands.append('lg')
print(mobile_brands)

mobile_brands.insert(0,'nokia')
print(mobile_brands)

print(motorcycles)
del motorcycles[3]
print(motorcycles)

print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)
print(f"Last motor cycle i brought is {popped_motorcycle}")

first_owned = motorcycles.pop(0)
print(f"The first motorcycle  i owned was a {first_owned.title()}")

motorcycles.remove('yamaha')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\n A {too_expensive.title()} is too expensive for me.")