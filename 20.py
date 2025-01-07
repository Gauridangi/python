students = [
    {
        "name": "Gauri",
        "subjects": [
            {"subject": "Math", "score": 78},
            {"subject": "Science", "score": 85},
            {"subject": "English", "score": 88},
            {"subject": "History", "score": 90},
            {"subject": "Geography", "score": 82},
            {"subject": "Computer", "score": 95}
        ]
    },
    {
        "name": "Sangita",
        "subjects": [
            {"subject": "Math", "score": 80},
            {"subject": "Science", "score": 87},
            {"subject": "English", "score": 90},
            {"subject": "History", "score": 88},
            {"subject": "Geography", "score": 85},
            {"subject": "Computer", "score": 92}
        ]
    }
]

students[0]["subjects"].append({"subject": "eco", "score":91})
students[1]["subjects"].append({"subject": "eco", "score":89})
print(students)






# mydict = [
#     {
#         "name" : "Gauri",
#         "age" : 22,
#         "address" :{
#             "city" : "Ghorahi",
#             "State" :"Lumbani",
#             "country" : "Nepal"
#         }
#     }
     
# ]
# mydict[0]["address"]["height"] = 5.4
# print(mydict)