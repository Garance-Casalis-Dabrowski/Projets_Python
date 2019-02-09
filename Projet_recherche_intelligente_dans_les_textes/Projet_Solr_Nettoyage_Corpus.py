
import pandas as pd
data = pd.read_csv("NYPD_Complaint_Data_Current_YTD.csv")
data.head(3)

table=data[["CMPLNT_NUM","CMPLNT_FR_DT","CMPLNT_FR_TM","CMPLNT_TO_DT","CMPLNT_TO_TM", "OFNS_DESC","LAW_CAT_CD","CRM_ATPT_CPTD_CD","JURIS_DESC","BORO_NM","PREM_TYP_DESC"]]

table.to_csv('Table.csv')

table.head(3)

table.columns = ["ID","Start_Date","Start_Time","End_Date","End_Time","Crime","Type_of_Crime","State","Jurisdiction","Borough","Exact_Place"]
table.to_csv('Table.csv', index = False)


table.head(3)

