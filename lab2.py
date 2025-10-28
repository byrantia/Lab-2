def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67,32)")

def get_user_input():
    x = input()
    list = x.split(",")
    num_list = []

    for value in list:
        num_list.append(float(value))
    print(num_list)
    return num_list

def calc_average(num_list):
    total = 0
    total_val = 0
    for value in num_list:
        total = value + total
        total_val = total_val + 1
    avg_total = total/total_val
    print(avg_total)
    return avg_total

def find_min_max(num_list):
    max_number = round(max(num_list))
    min_number = round(min(num_list))

    print(max_number)
    print(min_number)    

    return [min_number,max_number]


def sort_temperature(num_list):
      return sorted(num_list)

def calc_median_temperature(num_list):
     num_list = sorted(num_list)

     if len(num_list)%2 == 1:
         #odd
        odd_median = num_list[int(len(num_list)/2)]
        return odd_median
     else:
        #even
     
        even_median = (num_list[int(len(num_list)/2)] + num_list[int(len(num_list)/2)-1])/2
        return even_median


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    calc_average(num_list)
    y = find_min_max(num_list)
    print(y)
    sort_value = sort_temperature(num_list)
    print(sort_value)
    x=calc_median_temperature(num_list)
    print(x)

if __name__ == "__main__":
    main()