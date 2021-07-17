import copy

a = {"Nora": ["055-452-322", "Washington Ave."], "Gino": ["006-545", "5th Avenue"]}
#b = a.copy()
b = copy.deepcopy(a)
#b["Nora"] = ["055-452-311", "WDC."]
b["Nora"][0] = "56"

print(a)
print(b)