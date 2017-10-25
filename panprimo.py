def panprimo(n):
	numstr = str(n)
	cero,uno,dos,tres,cuatro,cinco,seis,siete,ocho,nueve = 0,0,0,0,0,0,0,0,0,0
	primo = int(numstr[-3:])
	for i in numstr:
		if i == "0":
			cero = 1
		if i == "1":
			uno = 1
		if i == "2":
			dos = 1
		if i == "3":
			tres = 1
		if i == "4":
			cuatro = 1
		if i == "5":
			cinco = 1
		if i == "6":
			seis = 1
		if i == "7":
			siete = 1
		if i == "8":
			ocho = 1
		if i == "9":
			nueve = 1
	if cero == 1 and uno == 1 and dos == 1 and tres == 1 and cuatro == 1 and cinco == 1 and seis == 1 and siete == 1 and ocho == 1 and nueve == 1 and primo%2 != 0:
		return True
	else:
		return False
