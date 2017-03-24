import math

month =0

def pay_off_dept():

    if month <= 12:
        bal = float(raw_input('Enter the Outstanding bal: '))
        annual = float(raw_input('Enter annual credit card rate: '))

            
        mon_int_rate = math.ceil((annual/100/12.0)*bal)
        min_mon_pay = math.ceil(bal/12 + mon_int_rate)
        no_of_month = math.ceil(bal/min_mon_pay)
        bal = bal - min_mon_pay*no_of_month

        print 'RESULT'
        print 'Monthly payment to pay off dept in 1 year is: ', min_mon_pay
        print 'Month needed to pay off dept is: ', no_of_month
        print 'Balance: ', bal
        

pay_off_dept()
    

