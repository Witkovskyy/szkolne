n = int(input())
cities = {}
for i in range(n):
    city = input().strip().split()
    # city[0] = {"x":int(city[1]), "y":int(city[2])}
    cords = {"x":city[1], "y":city[2]}
    cities[city[0]] = cords
    
tour = input().strip().split()
for i in range(len(tour)):
    if i+1>len(tour):
        distance = pow((pow((cities[tour[i]]["x"] + cities[tour[0]]["x"]),2)),0.5)
print(cities)
