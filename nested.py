# sample_api_response = {
#     "status": "success",
#     "data": {
#         "users": [
#             {
#                 "id": 12345,
#                 "name": "Gauri Dangi",
#                 "email": "gauri.dangi@example.com",
#                 "password": "MyPassword123",
#                 "profile": {
#                     "age": 30,
#                     "gender": "male",
#                     "location": "New York"
#                 },
#                 "subscription": {
#                     "status": "active",
#                     "plan": "premium",
#                     "expires": "2025-12-31"
#                 }
#             },
#             {
#                 "id": 12346,
#                 "name": "Sita Rai",
#                 "email": "sita.rai@example.com",
#                 "password": "SecurePass456",
#                 "profile": {
#                     "age": 28,
#                     "gender": "female",
#                     "location": "Kathmandu"
#                 },
#                 "subscription": {
#                     "status": "active",
#                     "plan": "standard",
#                     "expires": "2025-11-30"
#                 }
#             },
#             {
#                 "id": 12347,
#                 "name": "Rajesh Shrestha",
#                 "email": "rajesh.shrestha@example.com",
#                 "password": "Rajesh123!",
#                 "profile": {
#                     "age": 35,
#                     "gender": "male",
#                     "location": "Pokhara"
#                 },
#                 "subscription": {
#                     "status": "inactive",
#                     "plan": "basic",
#                     "expires": "2025-01-15"
#                 }
#             }
#         ]
#     }
# }



sample_api_response = {
    "status": "success",
    "data": {
        "users": [
            {
                "id": 12345,
                "name": "Gauri Dangi",
                "email": "gauri.dangi@example.com",
                "password": "MyPassword123"
            },
            {
                "id": 12346,
                "name": "Sita Rai",
                "email": "sita.rai@example.com",
                "password": "SecurePass456"
            },
            {
                "id": 12347,
                "name": "Rajesh Shrestha",
                "email": "rajesh.shrestha@example.com",
                "password": "Rajesh123!"
            }
        ]
    }
}

# email = input("Enter your email")
# password = input("Enter your password")
# users = sample_api_response["data"]["users"]

# for user in users:
    
#     if(email == user["email"] and password == user["password"]):
#         print(f"Hello {user["name"]}!")
#         break;


id = int(input("Enter your id"))
users = sample_api_response["data"]["users"]
for user in users:
    if(id == user["id"]):
        print(f"Your name is {user["name"]}")
        