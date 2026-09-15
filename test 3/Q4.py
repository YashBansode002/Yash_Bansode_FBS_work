basic = float(input("Enter basic salary: "))

if basic < 10000:
    da = basic * 10 / 100
    ta = basic * 12 / 100
    hra = basic * 20 / 100

    total = basic + da + ta + hra

    print("Basic Salary =", basic)
    print("DA =", da)
    print("TA =", ta)
    print("HRA =", hra)
    print("Total Salary =", total)
else:
    print("Basic salary is not below 10000")