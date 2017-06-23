import sys

cifra = sys.argv[1]
matriz = [ ['0','0'],['1','1'],['2','2'],['3','3'],['4','4'],['5','5'],['6','6'],['7','7'],['8','8'],['9','9'],['_','_'],['?','?'],[':',':'],['/','/'],[' ',' '],['.','.'],[',',','],['J' , 'a'],['H' ,'b'],['N' , 'c'], ['C' , 'd'],['D','e'],['A','f'],['M','g'],['O','h'],['B','i'],['P','j'],['Q','k'],['E','l'],['Z','m'],['L','n'],['S','o'],['T','p'],['R','q'],['I','r'],['V','s'],['F','t'],['W','u'],['K','v'],['Y','w'],['U','x'],['G','y'],['X','z']]
decipher = ""
alphabet = ""

for x in range(len(matriz)):
	alphabet = alphabet+matriz[x][0]

for i in range(len(cifra)):
	for x in range(len(matriz)):
		if cifra[i] == matriz[x][0]:
			decipher = decipher + matriz[x][1]

#print("\n"+alphabet)
#print("\n"+decipher)
print("\n"+decipher.upper())

