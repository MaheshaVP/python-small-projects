#json 

import json

new_data = {'name':"mahesh",'age':21,"skills":["python",'mysql']}

with open('data.json','w') as file:
    json.dump(new_data,file,indent=4)

# with open('data.json','r') as file:
#     data = json.load(file)

# print(data)