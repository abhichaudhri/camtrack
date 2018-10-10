import pandas as pd
import numpy as np
mydata=pd.read_csv("/home/abhishek/Desktop/Hacka/CamTrack.csv")
df=pd.DataFrame(mydata)
#print(df)
while (True):
	print("Enter Your Search:")
	TS = input("Enter TimeStamp: ")
	manu = input("Enter Manufacturer: ")
	color = input("Enter Color: ")
	numplt = input("Enter Number Plate: ")
	loc = input("Enter Location: ")
	
	
	for index, row in df.iterrows():
		if row["Timestamp"]==TS or row["Manufacturer"]==manu or row["Color"]==color or row["Plate"]==numplt or row["Location"]==loc:
			print(str(row["Timestamp"])+" - "+str(row["Manufacturer"])+" - "+str(row["Color"])+" - "+str(row["Plate"])+" - "+str(row["Location"]))

		