# Week 7 – Python Exercises
# VAN LOADING

parcels = [50, 90, 120, 110, 40, 30, 85, 85, 110, 100, 100, 100, 100, 120, 90, 50, 85, 120, 40, 0]
capacity = 750
numberOfVans = 0
heaviestVan = 0
parcelWeight = 0
vanDispached = 0

# Get first parcelWeight
while parcels[0]:

# Get first parcelWeight
    payload = 0
    while (payload + parcelWeight <= capacity) and (parcels[0]):

# Load a single van
        payload += parcelWeight
        parcelWeight = parcels[0]
        parcels = parcels[1:]
    vanDispached += 1
    print(f'\n - Van no. {vanDispached} has been dispatched. \n'
          f'Its payload has been {payload}.')
    numberOfVans += 1
# Check whether this is the heaviest van
    if payload > heaviestVan:
        heaviestVan = payload
print(f'\n{vanDispached} vans has been dispatched today\n'
      f'The heaviest payload was: {heaviestVan}')