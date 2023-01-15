import pandas as pd
       
def create(my_list_two): 
    data = {'Id': [i["id"] for i in my_list_two], 'Name': [i["name"] for i in my_list_two],
            'Surname': [i["surname"] for i in my_list_two],'Date': [i["date"] for i in my_list_two],
            'Work': [i["work"] for i in my_list_two]
            }
    df = pd.DataFrame.from_dict(data)
    ok = df.to_html()
    with open('index_user.html', 'w') as page:
            page.write(ok)

