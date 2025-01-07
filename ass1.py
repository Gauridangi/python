data = [
    {
        "name":"Sangam",
        "type":[
            {
                "name":"NTC",
                "number":986652
            },
        

        ]
    },
     {
        "name":"Sudan",
        "type":[
            {
                "name":"NTC",
                "number":9844906571
            },
            {
                "name":"Ncell",
                "number":9806245117
            },
             {
                "name":"Smart cell",
                "number":0
            }

              ]
}
]
# list_data = data[0]
# name = list_data['name']
# print(name)

# dict_data = list_data['type']
# for i in dict_data:
#     print(f"{i["name"]} number of {name} is {i["number"]}")


for x in data:
    name = x['name']
    dict_data = x['type']
    for x in dict_data:
         print(f"{x["name"]} number of {name} is {x["number"]}")

