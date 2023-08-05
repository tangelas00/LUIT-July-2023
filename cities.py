
city_1 = "Los Angeles"
city_2 = "Houston"
city_3 = "Dallas"
city_4 = "Chicago"
city_5 = "New Orleans"

empty_list = []   #empty list intoduced with square brackets
top_cities = [ "Los Angeles", "Houston","Dallas","Chicago","New Orleans"]  
print(top_cities)
print(top_cities[0])  # gives access to 1st element
print(top_cities[4])
print (top_cities[-2])
print( top_cities[0:2]) #this slice gives you 2 eleemts 0 and 1
print(top_cities[2:])

del top_cities [2]
print (top_cities)

