weather_data = [
    {
        "city": "Kathmandu",
        "temperature": 15,
        "humidity": 60,
        "description": "Partly Cloudy"
    },
    {
      "city": "Pokhara",
      "temperature": 18,
      "humidity": 65,
      "description": "Sunny"
    },
    {
      "city": "Biratnagar",
      "temperature": 20,
      "humidity": 70,
      "description": "Cloudy"
    },
    {
      "city": "Birgunj",
      "temperature": 22,
      "humidity": 75,
      "description": "Clear"
    },
    {
      "city": "Dharan",
      "temperature": 19,
      "humidity": 68,
      "description": "Rain"
    },
    {
      "city": "Butwal",
      "temperature": 21,
      "humidity": 72,
      "description": "Drizzle"
    },
    {
      "city": "Hetauda",
      "temperature": 23,
      "humidity": 65,
      "description": "Sunny"
    },
    {
      "city": "Nepalgunj",
      "temperature": 25,
      "humidity": 60,
      "description": "Clear"
    },
    {
      "city": "Dhangadhi",
      "temperature": 24,
      "humidity": 70,
      "description": "Windy"
    },
    {
      "city": "Ghorahi",
      "temperature": 17,
      "humidity": 55,
      "description": "Partly Cloudy"
    },
    {
      "city": "Tulsipur",
      "temperature": 16,
      "humidity": 58,
      "description": "Sunny"
    },
    {
      "city": "Lamahi",
      "temperature": 18,
      "humidity": 60,
      "description": "Clear"
    },
    {
      "city": "Ilam",
      "temperature": 14,
      "humidity": 80,
      "description": "Rain"
    },
    {
      "city": "Janakpur",
      "temperature": 20,
      "humidity": 65,
      "description": "Sunny"
    },
    {
      "city": "Bhairahawa",
      "temperature": 22,
      "humidity": 68,
      "description": "Cloudy"
    },
    {
      "city": "Mahendranagar",
      "temperature": 23,
      "humidity": 70,
      "description": "Clear"
    },
    {
      "city": "Chitwan",
      "temperature": 19,
      "humidity": 75,
      "description": "Drizzle"
    },
    {
      "city": "Lalitpur",
      "temperature": 15,
      "humidity": 60,
      "description": "Sunny"
    },
    {
      "city": "Bhaktapur",
      "temperature": 16,
      "humidity": 62,
      "description": "Partly Cloudy"
    },
    {
      "city": "Khandbari",
      "temperature": 18,
      "humidity": 78,
      "description": "Rain"
    }
  ]

# # Ask the user to enter city name.
# # Print the current temperature, humidity and description of that city.
# # If city not found, print "City not Found"
cityfound = False
city = input("Enter you city name")
for x  in weather_data:
    if city == x["city"]:
      print(x["temperature"])
      print(x["humidity"])
      print(x["description"])
      cityfound = True
      break;
    if cityfound == False:
       print("city not found")  
       break;
  
     
      



# sample_api_response = {
#     "status": "success",
#     "data": {
#         "users": [
#             {
#                 "id": 12345,
#                 "email": "gauri.dangi@example.com",
#                 "password": "MyPassword123",
#                 "subscription": {
#                     "plan": "premium"
#                 }
#             },
#             {
#                 "id": 12346,
#                 "email": "sita.rai@example.com",
#                 "password": "SecurePass456",
#                 "subscription": {
#                     "plan": "standard"
#                 }
#             },
#             {
#                 "id": 12347,
#                 "email": "rajesh.shrestha@example.com",
#                 "password": "Rajesh123!",
#                 "subscription": {
#                     "plan": "basic"
#                 }
#             }
#         ]
#     }
# }

# id = int(input("Enter your id"))
# email = input("Enter your email")
# password = input("Enter your password")
# users = sample_api_response["data"]["users"]

# for user in users:
#     if (id == user["id"] and email == user["email"] and password == user["password"]):
#         print(user["subscription"]["plan"])