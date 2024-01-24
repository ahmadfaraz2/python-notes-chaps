state_capitals = {"Arkansas": "Little Rock", "Colorado": "Denver",
                "California": "Sacramento", "Georgia": "Atlanta"}

# To get a value, refer to it by its key
ca_capital = state_capitals["California"]
print(ca_capital)

# You can also get all the keys in a dictionary and then iterate over them:
for k in state_capitals.keys():
    print("{} is the capital of {}".format(state_capitals[k],k))
 
# Little Rock is the capital of Arkansas
# Denver is the capital of Colorado
# Sacramento is the capital of California
# Atlanta is the capital of Georgia

# Now we will only iterate keys
keys = state_capitals.keys()
for k in keys:
    print(k)
 
# Arkansas
# Colorado
# California
# Georgia

values = state_capitals.values()
for v in values:
    print(v)

# Little Rock
# Denver
# Sacramento
# Atlanta

for k, v in state_capitals.items():
    print(k, v)

# Arkansas Little Rock
# Colorado Denver
# California Sacramento
# Georgia Atlanta