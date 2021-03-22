#! usr/bin/usr python3

import locale as lc
result = lc.setlocale(lc.LC_ALL, "")
if result[0] == "C":
    lc.etlocale(lc.LC_ALL)


def title():
    print("Interest Calculator")
    print()


def loan():
    while True:
        try:
            loan_amount = float(input("Enter loan amount:   "))
            # format loan amount here before returning to the main
            round(loan_amount, 2)
            return loan_amount
        except ValueError:
            print("Must be an decimal or integer value")


def interest():
    while True:
        try:
            interest_rate = float(input("Enter interest rate: "))
            print()
            return interest_rate
        except ValueError:
            print("Must be a decimal or integer value.")


def interest_amount_calculation(interest_rate, loan_amount):
    interest_amount = (interest_rate / 100) * loan_amount
    round(interest_amount, 3)
    return interest_amount


def main():
    title()
    again = "y"

    while again.lower() != "n":
        loan_amount = loan()
        interest_rate = interest()
        interest_amount = interest_amount_calculation(interest_rate, loan_amount)

# This portion of code lc.currency will append all relevant currency marks such as commas and decimals
# It was not usable from my experience with percentage sign which is appended at end of variable.

        loan_amount = lc.currency(loan_amount, grouping=True)
        interest_amount = lc.currency(interest_amount, grouping=True)

# loan_amount = "{:,.2f}".format(loan_amount)
        print("{:16}{:>16}".format("Loan Amount: ", loan_amount))
        print("{:16}{:>15}{:1}".format("Interest rate: ", interest_rate, "%"))
        print("{:16}{:>15}".format("Interest Amount: ", interest_amount))

        print()
        again = str(input("Continue? (y/n): "))
        print()

# print("{:15} {:>5}".format("Order Total: ", round(order_total, 2)))
# print("{:.2f}".format(number))

    if again.lower() == "n":
        print("Bye!")


if __name__ == '__main__':
    main()


# reference
# https://www.w3schools.com/python/ref_string_format.asp
# https://intellipaat.com/community/2447/how-to-print-number-with-commas-as-thousands-separators
