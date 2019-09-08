###
# My methodology is to use a brute force method, i.e., keep increasing the number of pita by 1 to see if the remaining
#  profit can be divided by pitta profit without a remainder
###
def main():
    read_data("1.in")
    read_data("2.in")

def read_data(input_file):
    with open (input_file, 'rt', encoding="ISO-8859-1") as myfile:
        for a_line in myfile:
            data = a_line.split()
            month_profit = float(data[0])
            pita_profit = float(data[1])
            pizza_profit = float(data[2])

    count_pita_pizza_combo(month_profit, pita_profit, pizza_profit)

def count_pita_pizza_combo(month_profit, pita_profit, pizza_profit):
    # '//' floor division, the same output in Python 2 and 3
    for pita_counter in range(int(month_profit//pita_profit) + 1):
        profit_remained_for_pizza = (month_profit - (pita_counter * pita_profit)) 

        # Instead of division without remainder i.e. 'if profit_remained_for_pizza % pizza_profit == 0'
        #  test if remainder is less than a tiny amount as below
        # E.g., with 199 pizza 'profit_remained_for_pizza % pizza_profit' produces '1.9539925233402755e-14'
        if profit_remained_for_pizza % pizza_profit < 1e-10:
            print("{0} {1}".format(pita_counter, int(profit_remained_for_pizza // pizza_profit)))

if __name__ == '__main__':
    main()