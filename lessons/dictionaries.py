"""Demonstration of dictionary capabilities."""


# declaring the type of a dictionary
schools: dict[str, int]

# Initialze to an empty dictionary
schools = dict()

# set a key-value pairing in the dictionary
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NSCU"] = 26150

# Print a dictionary literal representation
print(schools)

# Access a value by its key -- "lookup"
print(f"UNC has {schools['UNC']} students.")

# Remove a key-value pair from a dictionary by its key
schools.pop("Duke")

# Test for the existence of a key
if "Duke" in schools:
    print("Found the key 'Duke' in  schools")
else:
    print("No key 'Duke' in schools")

# Update/ Reassign a key--value pair
schools["UNC"] = 20000
schools["NSCU"] += 200
print(schools)

# Demonstration of dictionary literals

# Empty dictionary literal
schools = {}  # Same as dict()
print(schools)

# Alternatively, intialize key-value pairs
schools = {
    "UNC": 19400, 
    "Duke": 6717, 
    "NCSU": 26150}
print(schools)

# What happpens when a key does not exist?
# print(schools["UNCC"])

# Example looping over the keys of a dict
for key in schools:
    print(f"Key: {key} -> Value: {schools[key]}")
print("space")
for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")