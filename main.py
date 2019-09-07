###
# - Think a peak or valley as synmetrical slopes on either side with the data point list considered as a top or bottom
# - My methodology loop through data points from left to right starting from a top or bottom for peak or valley respectively
# - For Example, where n = 2 for peak my loop starts at list[1], NOT list[0]. Then look to the value on the right
#   to see if that value is lower than that of the peak i.e., list[2] < list[1].
# - Turn to the left and do the same, i.e., check if list[0] < list[1]
# - When both conditions are met, increment peak_counter or valley_counter by 1.
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
#     peak_counter = 0
#     valley_counter = 0
#     stop_pos = 0

#     # Peak
#     stop_pos = total_idx_count - (peak_count - 1) + 1
#     for idx in range(peak_count - 1, stop_pos):
#         if is_continous_up_or_down(data_points, idx, peak_count, True, False) and \
#             is_continous_up_or_down(data_points, idx, peak_count, False, False):
#             peak_counter += 1

#     # Valley
#     stop_pos = total_idx_count - (valley_count - 1) + 1
#     for idx in range(valley_count - 1, stop_pos):
#         if is_continous_up_or_down(data_points, idx, valley_count, True, True) and \
#             is_continous_up_or_down(data_points, idx, valley_count, False, True):
#             valley_counter += 1

#     print("peak = {0}, valley = {1}".format(peak_counter, valley_counter))            

# def is_continous_up_or_down(data_points, current_idx, data_point_count, idx_count_to_right = True, up_from_idx_pos = True):   
#     stop_idx = current_idx + data_point_count - 1 if idx_count_to_right else current_idx - data_point_count + 1

#     for idx in range(current_idx, stop_idx, 1 if idx_count_to_right else - 1): 
#         # If condition is NOT met, get out this function immediately with 'return False'
#         if idx_count_to_right and up_from_idx_pos:
#             if not(data_points[idx] < data_points[idx + 1]): return False
#         elif (not idx_count_to_right) and up_from_idx_pos:
#             if not(data_points[idx - 1] > data_points[idx]): return False
#         elif idx_count_to_right and (not up_from_idx_pos):
#             if not(data_points[idx] > data_points[idx + 1]): return False
#         elif (not idx_count_to_right) and (not up_from_idx_pos):
#             if not(data_points[idx - 1] < data_points[idx]): return False

#     return True

if __name__ == '__main__':
    main()