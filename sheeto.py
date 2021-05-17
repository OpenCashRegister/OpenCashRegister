import ezsheets
id = ""
while not id:
  pass
ss=ezsheets.Spreadsheet(id)
Itemsheet=ss["Items"]
orders=ss["Purchases"]
IDlist=list(filter(lambda x: x != "", Itemsheet.getColumn(5)))
del IDlist[0]
ids={}
for l in range(len(IDlist)):
  ids[IDlist[l]]=l+2