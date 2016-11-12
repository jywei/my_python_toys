from decimal import *

def amortization(principal, rate, term):
    pmt = payment(principal, rate, term)
    begBal = float(principal)
    print('Pmt no.'.rjust(6), '', 'Beg. bal.'.ljust(10), '', 'Payment'.ljust(9), 'Principal'.ljust(9), '', 'Interest'.ljust(9), '', 'End . bal.'.ljust(13))
    print(''.rjust(7, '-'), '', ''.ljust(9, '-'), ' ', ''.rjust(8, '-'), ' '.ljust(10, '-'), '', ''.rjust(9, '-'), '', ''.ljust(12, '-'))

    for num in range(1, term + 1):
        interest = float(round(begBal * (rate / (12 * 100.0)), 2))
        applied = float(round(pmt - interest, 2))
        endBal = round(begBal - applied, 2)

        print(str(num).center(6), '', '{0:,.2f}'.format(begBal).rjust(10), '', '{0:,.2f}'.format(pmt).rjust(9), '{0:,.2f}'.format(applied).rjust(9), '', '{0:,.2f}'.format(interest).rjust(9), '', '{0:,.2f}'.format(endBal).rjust(13))
        begBal = endBal

def payment(principal, rate, term):
    rate_per_twelve = rate / (12 * 100.0)
    result = principal * (rate_per_twelve / (1 - (1 + rate_per_twelve) ** (-term)))
    result = float(result)
    result = round(result, 2)
    return result

amortization(100000, 5, 10)
