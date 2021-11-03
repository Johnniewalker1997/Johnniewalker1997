
from faker import Faker
import pandas as pd
import csv

fake=Faker()

def create_csv(limit,file_path):
    name,address,email,country,url=[],[],[],[],[]

    for x in range(limit):
        name.append(fake.name()),address.append(fake.address()),email.append(fake.email()),country.append(fake.country()),url.append(fake.url())

    dict={"Name": name, "Address":address,"Email":email,"country":country,"url":url}
    df=pd.DataFrame(dict)
    print(df)
    df.to_csv(file_path)

if __name__=="__main__":
    #PASS SIZE OF CSV AND FILEPATH/NAME
    create_csv(100,"created_csv.csv")



