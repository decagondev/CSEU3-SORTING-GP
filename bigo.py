it = [2,3,5,6,7]
# O(1)

def constant_time(items):
    result = items[0] * items[4] #O(1)
    print(result) # O(1)
    # O(4) Constant time operation O(1)

constant_time(it)

# O(n)

def linear_time(items):
    for item in items: # O(n) * O(1)
        print(item) # O(1)
    for item in items: # O(n) * O(1)
        print(item) # O(1)

linear_time(it)

# O(n^2)
def quadratic_time(items):
    for item in items: # O(n) * O(n) = O(n^2)
        for item2 in items: # O(n) * O(1)
            print(item, ' ', item2) # O(1)



