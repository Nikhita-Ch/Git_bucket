def union(set1, set2):
    return set1.union(set2)

def intersection(set1, set2):
    return set1.intersection(set2)

def difference(set1, set2):
    return set1.difference(set2)

def symmetric_difference(set1, set2):
    return set1.symmetric_difference(set2)

def is_subset(set1, set2):
    return set1.issubset(set2)

def is_superset(set1, set2):
    return set1.issuperset(set2)

def disjoint(set1, set2):
    return set1.isdisjoint(set2)

def add_element(set1, element):
    set1.add(element)
    return set1

def remove_element(set1, element):
    set1.discard(element)
    return set1

def clear_set(set1):
    set1.clear()
    return set1

def copy_set(set1):
    return set1.copy()

def set_size(set1):
    return len(set1)

def set_max(set1):
    return max(set1)

def set_min(set1):
    return min(set1)

# Example usage
set_A = {1, 2, 'apple'}
set_B = {'apple', 'banana', 'cherry'}

print("Union:", union(set_A, set_B))
print("Intersection:", intersection(set_A, set_B))
print("Difference (A - B):", difference(set_A, set_B))

print("Difference (B - A):", difference(set_B, set_A))
print("Symmetric Difference:", symmetric_difference(set_A, set_B))
print("Is A a subset of B?", is_subset(set_A, set_B))

print("Is A a superset of B?", is_superset(set_A, set_B))
print("Are A and B disjoint?", disjoint(set_A, set_B))
print("Add 6 to A:", add_element(set_A, 6))
print("Remove 'apple' from B:", remove_element(set_B, 'apple'))

print("Clear set A:", clear_set(set_A))
print("Copy set B:", copy_set(set_B))
print("Size of set B:", set_size(set_B))
print("Max element in set B:", set_max(set_B))
print("Min element in set B:", set_min(set_B))
