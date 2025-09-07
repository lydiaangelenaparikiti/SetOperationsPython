# =========================
# Set Operations in Python
# =========================

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


# Sample sets
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}

# Performing operations
print("Set A:", setA)
print("Set B:", setB)


print("Union:", union_sets(setA, setB))
print("Intersection:", intersection_sets(setA, setB))
print("Difference (A - B):", difference_sets(setA, setB))
print("Difference (B - A):", difference_sets(setB, setA))
print("Is A a subset of B?:", is_subset(setA, setB))
print("Is B a subset of A?:", is_subset(setB, setA))
