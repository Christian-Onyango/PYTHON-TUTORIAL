def data_type(su):
        
        if type(su) is str:
            return len(su)
        elif su is None:
            return "no value"
        elif type(su) is bool:
        	return su
        
        elif type(su) is int:
            if su > 100:
                return "more than 100"
            elif su < 100:
                return "less than 100"
            else:
                su == 100
                return "equal to 100"
        elif type(su) is list:
            if len(su) > 2:
                return su[2]
        else:
            return "None"