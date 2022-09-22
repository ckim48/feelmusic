import pandas

data = {"Name": ["Scott","Jason","Amy","Bob"],
		"GPA" : [3.14,2.9,4.0,2.9],
		"Phone":["123-2312","1234-5678","9872-1234","9888-9999"]
}

print(data)

data = pandas.DataFrame(data)
print(data)
print(data["GPA"])
data["Weighted GPA"] = [4,3,4,3]
print(data["GPA"].mean()) # Average GPA of the students
print(data["GPA"].max())
print(data["GPA"].min())
print(data["GPA"].median())

print(data["Weighted GPA"].mean())

print(data["GPA"] + data["Weighted GPA"])


print(data.info()) 


