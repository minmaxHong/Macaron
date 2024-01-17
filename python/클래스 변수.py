class Family:
    lastname = "김"

a = Family()
b = Family()

print(a.lastname, b.lastname)

Family.lastname = "최"
print(a.lastname, b.lastname)
