def pay_off_credit_card_bal_dept():
    
    bal = float(raw_input('Enter the outstanding balance: '))
    mmpr = float(raw_input('Enter the minimum monthly payment rate: '))
    Annual_interest_rate = float(raw_input('Enter the Annual interest rate: '))
    month = 1
    total = 0
    total_amount_paid = 0

    while month <= 12:

        mmp = round(mmpr/100*bal)
        interest_paid = Annual_interest_rate/100/12*bal
        principal_paid = round(mmp-interest_paid)
        bal = round(bal-principal_paid)

        print 'Month', month
        print 'Minimum monthly payment: ', mmp
        print 'Principal paid: ', principal_paid
        print 'Remaining balance: ', bal

        month+=1
        total_amount_paid+=mmp
        total+=bal

    print 'RESULT'
    print 'Total amount paid: ', total_amount_paid
    print 'Total amount remaining: ', bal
   
pay_off_credit_card_bal_dept()

