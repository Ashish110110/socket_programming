import xlrd as xl
def func(frp):
	ct=0
	loc = ("rast.xlsx")
	wb = xl.open_workbook(loc)
	sheet = wb.sheet_by_index(0)
	list = []
	for i in range(sheet.nrows):
		if(sheet.cell_value(i,2)==frp):
			abbr=sheet.cell_value(i,1)
	for i in range(5,15):
		for j in range(1,9):
			test=(sheet.cell_value(i,j)).split('(')
			#print(test)
			if(test[0]!=u''):
				if(((test[1].split(')',1))[0])==abbr):
					list.append((sheet.cell_value(i,0) + " " + (sheet.cell_value(4,j))))
					ct+=1
	list.append(ct)
	return list
					

