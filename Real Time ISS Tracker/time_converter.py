# Edited from the source : https://www.geeksforgeeks.org/convert-unix-timestamp-to-dd-mm-yyyy-hhmmss-format/

def unixTimeToHumanReadable(seconds):
	
	ans = ""
	daysOfMonth = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]

	(currYear, daysTillNow, extraTime, extraDays, index, date, month, hours, minutes, secondss, flag) = ( 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )

	
	daysTillNow = seconds // (24 * 60 * 60)
	extraTime = seconds % (24 * 60 * 60)
	currYear = 1970

	while (daysTillNow >= 365):
		if currYear % 400 == 0 or currYear % 4 == 0 and currYear % 100 != 0: 
			daysTillNow -= 366
		
		else:
			daysTillNow -= 365
		
		currYear += 1
		
	extraDays = daysTillNow + 1

	if currYear % 400 == 0 or currYear % 4 == 0 and currYear % 100 != 0:
		flag = 1

	month = 0
	index = 0
	
	if flag == 1:
		while True:

			if index == 1:
				if extraDays - 29 < 0:
					break
				
				month += 1
				extraDays -= 29
			
			else:
				if extraDays - daysOfMonth[index] < 0:
					break
				
				month += 1
				extraDays -= daysOfMonth[index]
			
			index += 1
		
	else:
		while True:
			if extraDays - daysOfMonth[index] < 0:
				break
			
			month += 1
			extraDays -= daysOfMonth[index]
			index += 1

	
	if extraDays > 0:
		month += 1
		date = extraDays
	
	else:
		if month == 2 and flag == 1:
			date = 29
		else:
			date = daysOfMonth[month - 1]

	
	hours = extraTime // 3600
	minutes = (extraTime % 3600) // 60
	secondss = (extraTime % 3600) % 60

	ans += str(date)
	ans += "/"
	ans += str(month)
	ans += "/"
	ans += str(currYear)
	ans += " "
	ans += str(hours)
	ans += ":"
	ans += str(minutes)
	ans += ":"
	ans += str(secondss)

	return ans


