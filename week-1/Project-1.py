print("Welcome, This is a simple interest calculator")
p,r,t = input("Enter the principal amount, rate of interest and time period in years: ").split()
p = float(p)
r = float(r)
t = int(t)
si = (p*r*t)/100
if p <= 0 or r <= 0 or t <= 0:
    print("Please enter a valid input")
else:
    print("The simple interest is: ",si)


#Compound Interest
print("Welcome, This is a compound interest calculator")
p,r,t, = input("Enter the principal amount, rate of interest, time period in years: ").split()
p = float(p)
r = float(r)
t = int(t)
n = 100
a = p*(1+(r/n))**(n*t)
ci = a-p
if p <= 0 or r <= 0 or t <= 0:
    print("Please enter a valid input")
else: 
    print("The compound interest is: ",ci)


# Annuity plan
print("Welcome, This is an Annuity plan calculator!")
pmt = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest: "))
n = int(input("Enter the number of times the interest is compounded in a year: "))
a = pmt*{((1+r/n)**(n*t))-1}/(r/n)
print("Your Annuity plan is: ",a)