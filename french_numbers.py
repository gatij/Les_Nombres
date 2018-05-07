#create the dictionary

def createDictionary():
    '''Returns a tiny french dictionary'''
    french = dict()
    french['0'] = 'zéro'
    french['1'] = 'un'
    french['2'] = 'deux'
    french['3'] = 'deux'
    french['4'] = 'quatre'
    french['5'] = 'cinq'
    french['6'] = 'six'
    french['7'] = 'sept'
    french['8'] = 'huit'
    french['9'] = 'neuf'
    french['10'] = 'dix'
    french['11'] = 'onze'
    french['12'] = 'douze'
    french['13'] = 'treize'
    french['14'] = 'quatorze'
    french['15'] = 'quinze'
    french['16'] = 'seize'
    french['20'] = 'vingt'
    french['30'] = 'trente'
    french['40'] = 'quarante'
    french['50'] = 'cinquante'
    french['60'] = 'soixante'
    french['80'] = 'quatre-vingts'
    french['100'] = 'cent'
    french['1000'] = 'mille'
    return french

french_dictionary=createDictionary()

def GiveFrenchNumber(n): 
    key=str(n)
	if key in french_dictionary:
	    result=french_dictionary[key]
    else:	
			if(n>=17 and n<=69):
				o=n%10
				t=(n%100)-o
				if o==1: 
					symbol=" et "
				else:     
				    symbol="-"	
				result=GiveFrenchNumber(t)+symbol+GiveFrenchNumber(o)
				french_dictionary[key]=result

			elif(n>=70 and n<=79): 
				o=n%10
				o=o+10
				t=60
				if o==11: 
					symbol=" et "
				else:     
				    symbol="-"	
				result=GiveFrenchNumber(t)+symbol+GiveFrenchNumber(o)
				french_dictionary[key]=result

			elif(n>=81 and n<=99):
			    o=n%10
				o=o+10
				t=80
				symbol="-"	
				result=GiveFrenchNumber(t)+symbol+GiveFrenchNumber(o)
				french_dictionary[key]=result

			elif(n>100 and n<=999):
	            t=n%100
                h=n/100
	            result=GiveFrenchNumber(h)+GiveFrenchNumber(100)+GiveFrenchNumber(t)

	        else: 
	            result="try a number between 1 and 1000"    

	return result
			    		

