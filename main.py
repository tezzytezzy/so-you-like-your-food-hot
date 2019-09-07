###
# 
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
    pass


if __name__ == '__main__':
    main()