
#"Test file"

def file_raeder(file_path):
	with open(file_path,"r") as f:
		a = f.readlines()
		print(a)
