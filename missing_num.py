def find_missing(list1,list2):
	missing = 0
	if len(list1) > len(list2):
		long_list = list1
		short_list = list2
	else:
		long_list = list2
		short_list = list1

	for num in long_list:
		if num not in short_list:
			missing = num

	return missing
