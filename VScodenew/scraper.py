from bs4 import BeautifulSoup
import requests
import pandas as pd

url='https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
# url='https://www.google.com/search?sca_esv=007750bc5aee6945&q=dog&udm=2&fbs=AEQNm0CFDpRHaDHkXm_YXueHTfHtrgIXUKlluACpCix4T5ZoUSz6e3GWv4zN_09JkP2cR-DwqD-ER1CSuTjXzdXNKT0Wma9mNyum3oWLzhs1xt8u5N_8f3uUgStDs9UpKFAFlFGSOMoqQM9HMiNsP9mioHh2RXyquw6CV17dtB6pod7Wqwuaoj8KLwF-5ybcxBC-9vVePghwqzsfsWfHCa5dRS4yxLs8KA&sa=X&ved=2ahUKEwiczd6wirGJAxUrSGwGHTzrLxIQtKgLegQIERAB&biw=767&bih=730&dpr=1.25'
page=requests.get(url)
soup=BeautifulSoup(page.text,features="html.parser")
all_table=(soup.find_all('table')) #all the available tables
table=all_table[0] #our table
heads=table.find_all('th') # our table's heading
heads_names=[_.text.strip() for _ in heads] #filtering the data
rows=table.find_all('tr') #our table's data


df=pd.DataFrame(columns= heads_names)#creating data frame
# print(df)
for _ in rows[1:]:#filling in data for the dataframe
    ind_row=_.find_all('td')
    data_row=[_1.text.strip() for _1 in ind_row]
    length=len(df)
    df.loc[length]=data_row
# print(df)
file_path=input("path to save csv:")
file_path=fr"{file_path}"
df.to_csv(file_path,index=False)
