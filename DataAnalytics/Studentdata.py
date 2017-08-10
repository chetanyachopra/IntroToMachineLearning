import unicodecsv
import typeconvert

# Convert datestring to datetime

enrollments = []
def checkFirstData(filename):
	with open(filename,'rb') as file:
		reader = unicodecsv.DictReader(file)
		enrollments = list(reader)	
		return enrollments[0]


checkFirstData('data/enrollments.csv')
typeconvert.typeConvert('data/enrollments.csv')



