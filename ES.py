import pandas as pd
import numpy as np
mydata=pd.read_csv("/home/abhishek/Desktop/Hacka/Automobiles deatils.csv")
df=pd.DataFrame(mydata)
#print(df)
while (True):
	print("Enter Your Search:")
	manu = input("Enter Manufacturer: ")
	color = input("Enter Color: ")
	numplt = input("Enter Number Plate: ")
	
	for index, row in df.iterrows():
		if row["Manufacturer"]==manu or row["Color"]==color or row["Plate"]==numplt:
			print(row["Manufacturer"]+" - "+row["Color"]+" - "+row["Plate"])

		