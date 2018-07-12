from zipfile import ZipFile


def getInternalName(zipName):
	with ZipFile(zipName, 'r') as f:
		names = f.namelist()
		#print names

	return str(names[0])

def unzip(zipName,passwd):
	with ZipFile(zip_file) as zf:
  		zf.extractall(pwd=bytes(password))

zip_file = 'hackthebox.zip'
password = 'hackthebox'
while True:
	print zip_file + ' | ' + password 
	unzip(zip_file,password)
	zip_file = getInternalName(zip_file)
	password = getInternalName(zip_file)
	password = password.replace('.zip','').replace('\n','')