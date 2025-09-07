def union_sets(set1, set2):
    """Return the union of two sets"""
    return set1.union(set2)

def intersection_sets(set1, set2):
    """Return the intersection of two sets"""
    return set1.intersection(set2)

def difference_sets(set1, set2):
    """Return the difference of set1 - set2"""
    return set1.difference(set2)

def is_subset(set1, set2):
    """Check if set1 is a subset of set2"""
    return set1.issubset(set2)

# Function to read a set from user input
def read_set(name):
    elements = input("Enter elements of " + name + " separated by space: ").split()
    return set(elements)

setA = read_set("Set A")
setB = read_set("Set B")

print("\nSet A:", setA)
print("Set B:", setB)

print("1️⃣ Union:", union_sets(setA, setB))
print("2️⃣ Intersection:", intersection_sets(setA, setB))
print("3️⃣ Difference (A - B):", difference_sets(setA, setB))
print("4️⃣ Difference (B - A):", difference_sets(setB, setA))
print("5️⃣ Is A a subset of B?:", is_subset(setA, setB))
print("6️⃣ Is B a subset of A?:", is_subset(setB, setA))

