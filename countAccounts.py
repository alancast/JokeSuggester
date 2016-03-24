totalAccounts = set()

with open('accountList.txt', 'r') as myfile:
	data=myfile.read()

for handle in data.split():
	totalAccounts.add(handle)


print len(totalAccounts)
