import csv, os # import statements

# read csv with ip addresses 
with open('ips.csv') as csvfile: 
	reader = csv.reader(csvfile,delimiter=',')
	# convert it to a list
	new_list = list(reader)
	# remove the first element in the list
	# new_list.pop(0)
	output = ''
	# loop through csv list 
	for row in new_list:
		ip_addr = row[0]
		# ping each server 
		resp = os.system(f"ping -c 2 {ip_addr}")
		if resp == 0:
			output += f"{ip_addr} , is up!\n"
		else:
			output += f"{ip_addr} , is down!\n"

print(output)




