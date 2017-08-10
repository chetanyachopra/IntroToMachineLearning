from datetime import datetime as dt
from Studentdata import enrollments
def parse_date(date):
    if date == '':
        return None
    else:
        return dt.strptime(date, '%Y-%m-%d')

# Convert string to int
def parse_maybe_int(i):
    if i == '':
        return None
    else:
        return int(i)

#print(checkFirstData('data/enrollments.csv'))
def typeConvert(filename):
	if filename == 'data/enrollments.csv':
		for enrollment in enrollments:
			enrollment['join_date'] = parse_date(enrollment['join_date'])
			enrollment['cancel_date'] = parse_date(enrollment['cancel_date'])
			enrollment['is_canceled'] = enrollment['is_canceled'] == True
			enrollment['is_udacity'] =  enrollment['is_udacity'] == True
			enrollment['days_to_cancel'] = parse_date(enrollment['days_to_cancel'])

