team={}
for i in range(11):
    name=input("Enter The Name: ")
    ht=float(input("Enter The Height: "))
    team[name]=ht
print(team)
cap=max(team,key=team.get)
print(cap,"Is Your Captain.")
