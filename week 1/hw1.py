Mt_age, Vs_age = map(int, input("Enter Mitya's and Vasya's ages: ").split())
if Mt_age < Vs_age:
    print("Vasya is older than Mitya")
elif Mt_age > Vs_age:
    print("Mitya is older than Vasya")
else:
    print("Mitya and Vasya are the same age")
