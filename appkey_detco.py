import pandas as pd
import openpyxl
path = "C:/Users/Diaz.R155/Documents/Proyectos Python/eui/Copia de EUI_DETCO1_15062023.xlsx"
file = pd.read_excel(path, sheet_name='Provision 150 Nodos PAE')
sk = open("script_key.sh","w+")

#print(file)



# loop through the rows using iterrows()
for index, row in file.iterrows():
    #print(row['Serial BGH TP'], row['EUI'])
    #t = """curl -X POST --header 'Content-Type: application/json' --header 'Grpc-Metadata-Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcGlfa2V5X2lkIjoiZmY4NGRlNmItZjAxYi00ZGJhLTk4NDEtNGI1NzY3NDg5MWYyIiwiYXVkIjoiYXMiLCJpc3MiOiJhcyIsIm5iZiI6MTY4NjgzNzQ2MCwic3ViIjoiYXBpX2tleSJ9.uV1GaOQ5eb-mO6x0clzkCvX7aCoXpLBOm2Ti4YVwd2E' --header 'Accept: application/json' -d '{"device": {"applicationID":"5", "description": """+str(row['EUI'])+""", "devEUI": """+str(row['EUI'])+""", "deviceProfileID":"58728722-a0d8-4cc1-add9-d6919e2f5c73", "isDisabled": false, "name": """+str(row['EUI'])+"-"+str(row["Serial BGH TP"])+""", "referenceAltitude": 0, "skipFCntCheck": true, "tags": {}, "variables": {}}}' 'http://18.204.151.39:8080/api/devices'"""
    sk.write("""curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{"deviceKeys": {"devEUI": """+'"'+str(row['EUI'])+'"'+""", "nwkKey": "11111111111111111111111111111112"}}' 'http://18.204.151.39:8080/api/devices/"""+str(row['EUI'])+"""/keys' --header 'Grpc-Metadata-Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcGlfa2V5X2lkIjoiZjczMDkxMjMtYzEyNy00ZjJjLWE1MDYtYjAyMGU4ZjYyYzc0IiwiYXVkIjoiYXMiLCJpc3MiOiJhcyIsIm5iZiI6MTY4NjgzNDYwNCwic3ViIjoiYXBpX2tleSJ9.by5sLnpcQXLT_kPvJGEkFsyo8dwzhE2A4vfx9OMCnnc'\n""")
sk.close()