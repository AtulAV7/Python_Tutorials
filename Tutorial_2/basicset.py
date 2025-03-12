print("Enter elements for set A (one by one, type 'done' when finished):")
set_a = set()
while True:
    element = input("Enter element or 'done': ")
    if element.lower() == 'done':
        break
    set_a.add(element)

print("Enter elements for set B (one by one, type 'done' when finished):")
set_b = set()
while True:
    element = input("Enter element or 'done': ")
    if element.lower() == 'done':
        break
    set_b.add(element)

print("\nSet A:", set_a)
print("Set B:", set_b)
print("\nSet Operations:")
print("Union:", set_a.union(set_b))
print("Intersection:", set_a.intersection(set_b))
print("A - B:", set_a.difference(set_b))
print("B - A:", set_b.difference(set_a))
print("Symmetric difference:", set_a.symmetric_difference(set_b))