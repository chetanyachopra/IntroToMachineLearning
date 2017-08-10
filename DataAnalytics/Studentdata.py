import unicodecsv 


def checkFirstData(filename):
	with open(filename,'rb') as file:
		reader = unicodecsv.DictReader(file)
		enrollments = list(reader)	
		return enrollments[0]

print(checkFirstData('data/enrollments.csv'))