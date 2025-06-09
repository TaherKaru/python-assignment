marks={"alice":78,"nick":96,"mick":50,"stefan":67}
name=input("Enter your name: ")
result=(marks.get(name.lower(), "student not found"))
print(result)

