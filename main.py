from matplotlib import pyplot as plt


def menu():
    print('✩'*3, 'MAIN MENU', '✩'*3, '\n')
    print('1 : Summary Report - Details of Screw Types\n'
          '2 : Report - Number of Units in each Length Category\n'
          '3 : Report - Screw Details based on Length Category \n'
          '4 : Increase or Decrease Stock Levels\n'
          '5 : Discount Feature - Category with the Highest Stock\n'
          '6 : Bar Chart - Number of Units in each Length Category\n'
          '7 : Exit Program\n')
    while True:
        try:
            choice = int(input('Enter your choice: '))  # asks user to choose an option
            if choice == 1:
                summary_report()
                break
            elif choice == 2:
                print('\n✩✩✩ OPTION 2: Report - Number of Units in each Length Category ✩✩✩\n')
                stock_len_category()
                break
            elif choice == 3:
                print('\n✩✩✩ OPTION 3: Report - Screw Details based on Length Category ✩✩✩\n')
                screw_details_len()
                break
            elif choice == 4:
                print('\n✩✩✩ OPTION 4: Increase or Decrease Stock Levels ✩✩✩\n')
                stock_level()
                break
            elif choice == 5:
                print('\n✩✩✩ OPTION 5: Discount Feature for Category with the Highest Stock ✩✩✩\n')
                discount_feature()
                break
            elif choice == 6:
                bar_chart()
                break
            elif choice == 7:
                print('\n✩✩✩ GOODBYE! ✩✩✩')
                exit()
            else:
                print('PLease choose an option (1 to 7)!\n')
                continue
        except ValueError:
            print('Invalid Input!\n')
            continue


# function to print the headers in a table
def headers_print(headers):
    # prints every element in the list headers
    for header in headers:
        print('¦', header, sep=' ', end=' ')
    print('¦')
    # prints the row of dashes of specific lengths
    for header in headers:
        print('¦', '-' * len(header), end=' ')
    print('¦')


# prints a report with a summary
def summary_report():
    total_stock = total_cost = total_discount_cost = 0
    print('\n', '✩' * 30, 'SUMMARY REPORT', '✩' * 29, '\n')
    headers_print(headers_main)  # prints the main headers
    # print the table and calculates total stock and value
    for item in stock:
        each_stock = int(item[3]) + int(item[4]) * 2 + int(item[5]) * 4  # number of units in each item
        total_stock += each_stock  # adds it to the total number of units
        total_cost += each_stock * float(item[6])  # adds cost of each item to the total cost
        # prints each item details
        print('¦ {:<8} ¦ {:<9} ¦ {:<6} ¦ {:<9} ¦ {:<10} ¦ {:<10} ¦ {:14} ¦ {:<8} ¦'.format(*item))  # (Pedamkar, 2020)
    for item in stock:
        # check if the item is on discount
        if item[7] in 'yes':
            each_stock = int(item[3]) + int(item[4]) * 2 + int(item[5]) * 4  # number of units in each item
            discount_cost = each_stock * float(item[6]) - each_stock * float(item[6]) * 0.1  # discounted cost
            total_discount_cost = total_cost - each_stock * float(item[6]) + discount_cost  # total discounted value
    print('\n✩✩✩ Total Stock Available', ' '*6, ': ', total_stock, ' units', sep='')
    print('✩✩✩ Total Value of Stock', ' '*7, ': £', format(total_cost, '.2f'), sep='')
    print('✩✩✩ Discounted Total Value', ' '*5, ': £', format(total_discount_cost, '.2f'), sep='')
    # ask user if they want to go to the menu or exit
    go_to_options(['Go to Menu', 'Exit Program'])


# total units in each length category
def stock_len_category():
    headers = ['LENGTH', 'NUM OF UNITS']  # headers for the table
    headers_print(headers)
    # prints key and value in the dictionary returned by the function
    for key, value in length_stock_dict().items():
        print('¦ {:<6} ¦ {:<12} ¦'.format(key, value))
    go_to_options(['View Bar Chart', 'Go to Menu', 'Exit Program'])  # print options for user to choose from


# creates a dictionary of lengths as keys and total units as values
def length_stock_dict():
    length_stock = {}
    for item in stock:
        length = int(item[2])  # length of each screw
        total = int(item[3]) + int(item[4]) * 2 + int(item[5]) * 4  # total number of units
        # checks if the
        if length not in length_stock:
            # the length is added as a key with the number of units as the value
            length_stock[length] = total
        else:
            # if the key exists, adds the number of units to the total
            length_stock[length] += total
    return length_stock  # returns the dict


# gets the details of screws of a specific length category
def screw_details_len():
    details = []
    length = detail_options('length')  # asks user to choose a length category
    for item in stock:
        # checks if the screw type is of the user specified length
        if length == int(item[2]):
            # append the screw type to the new list
            details += [[item[0], item[1], item[3], item[4], item[5], item[6], item[7]]]
    print('\n', '✩' * 3, ' LENGTH CATEGORY: ', length, 'mm ', '✩' * 3, '\n', sep='')
    # prints headings for the table
    headers = ['MATERIAL', 'HEAD TYPE', 'STOCK(50)', 'STOCK(100)', 'STOCK(200)', 'COST(per unit)', 'DISCOUNT']
    headers_print(headers)
    # prints the table
    for item in details:
        print('¦ {:<8} ¦ {:<9} ¦ {:<9} ¦ {:<10} ¦ {:<10} ¦ {:14} ¦ {:<8} ¦'.format(*item))
    search_again(screw_details_len)  # asks user if they want to search again


# the function creates dictionaries listing out materials, headtype, lengths and box sizes
def type_dicts(dictionary):
    material_dict = {}
    head_type_dict = {}
    length_dict = {}
    box_dict = {1: 50, 2: 100, 3: 200}  # values are sizes of boxes
    material_key = head_type_key = length_key = 1
    for item in stock:
        material = item[0]
        head_type = item[1]
        length = item[2]
        # each material type found in stock is listed in the materials dictionary
        if material not in material_dict.values():
            material_dict[material_key] = material
            material_key += 1
        # each head type found in stock is listed in the materials dictionary
        if head_type not in head_type_dict.values():
            head_type_dict[head_type_key] = head_type
            head_type_key += 1
        # each length type found in stock is listed in the materials dictionary
        if length not in length_dict.values():
            length_dict[length_key] = length
            length_key += 1
    # returns the dictionary based on the argument
    if dictionary == 'material':
        return material_dict
    elif dictionary == 'headtype':
        return head_type_dict
    elif dictionary == 'length':
        return length_dict
    elif dictionary == 'box size':
        return box_dict


# prints the type options based on argument for users to choose from
# argument detail is the name of the dictionary of options
def detail_options(detail):
    while True:
        print('✩✩✩', detail.upper())
        # print options from the dictionary returned based on the argument
        for key, value in type_dicts(detail).items():
            print(key, ':', value)
        try:
            choice = int(input('Enter your choice: '))  # gets user's choice
            # if the argument in box size, the key is returned
            if detail == 'box size':
                detail_choice = choice
            # if the argument is length, the value is stored as an integer
            elif detail == 'length':
                detail_choice = int(type_dicts(detail)[choice])
            else:
                detail_choice = type_dicts(detail)[choice]  # value is stored as a string
            return detail_choice
        except ValueError:
            print('Invalid Input!\n')
            continue
        except KeyError:  # if choice is a key that is not in the dictionary
            print('Invalid Input!\n')
            continue


# function to change stock levels
def stock_level():
    # prints the material options and returns the material chosen
    material = detail_options('material')
    print()
    head_type = detail_options('headtype')  # head type options
    print()
    length = detail_options('length')  # length options
    while True:
        count = found = 0  # count gets the index of the matched item
        for item in stock:
            # checking if the item matches the details entered by user
            if material == item[0] and head_type == item[1] and length == int(item[2]):
                print('\n✩✩✩ Current stock level:\n')  # printing the matched item details
                headers_print(headers_main)
                print('¦ {:<8} ¦ {:<9} ¦ {:<6} ¦ {:<9} ¦ {:<10} ¦ {:<10} ¦ {:14} ¦ {:<8} ¦'.format(*item))
                # user can now choose to edit the matched item
                while True:
                    print('\n1 : Increase stock level\n'
                          '2 : Decrease stock level\n'
                          '3 : Search another category\n'
                          '4 : Go back to menu\n')
                    try:
                        choice = int(input('Enter your choice: '))
                        if choice == 1:
                            print('\n', '✩'*3, ' INCREASING STOCK LEVEL ', '✩'*3, '\n', sep='')
                            # increase stock and print updated item details
                            increase_stock(count, box_index())
                            continue
                        elif choice == 2:
                            print('\n', '✩'*3, ' DECREASING STOCK LEVEL ', '✩'*3, '\n', sep='')
                            # decrease stock and print updated item details
                            decrease_stock(count, box_index())
                            continue
                        elif choice == 3:
                            print()
                            stock_level()  # asks users to enter details of their new search
                        elif choice == 4:
                            print()
                            menu()  # goes back to the menu
                        else:
                            print('Please choose an option!')
                            continue
                    except ValueError:  # if the 'choice' is not an integer
                        print('Invalid Input!')
                        continue
                found = 1  # the item is found
            if found == 0:  # if the item is not found while searching in the loop
                count += 1
        if found == 0:  # if item is not found
            print('\nThe description does not match with the stock available.')
            search_again(stock_level)


# gets the index of the box type user has entered
def box_index():
    while True:
        # prints the box options and gets the user's choice
        box = detail_options('box size')
        # if user chose box of 50 screws
        if box == 1:
            item_index = 3  # element is on index 3
        elif box == 2:  # box of 100 screws
            item_index = 4  # element is on index 4
        elif box == 3:  # box of 200 screws
            item_index = 5  # element is on index 5
        else:
            print('Invalid Input!\n')
            continue
        return item_index


# function to increase the stock levels
# 'count' is the index of item match and 'box' is the index of the box size
def increase_stock(count, box):
    while True:
        try:
            # gets number of units to increase
            increase = int(input('\nEnter units of stock you would like to increase: '))
            # changes the element 'box' in the item in index 'count' in list 'stock'
            stock[count][box] = str(int(stock[count][box]) + increase)  # adds 'increase' to existing num of units
            print_update(count)  # prints the updated item table
            return False
        except ValueError:
            print('\nInvalid Input!')
            continue


# function to decrease the stock levels
# 'count' is the index of item match and 'box' is the index of the box size
def decrease_stock(count, box):
    try:
        decrease = int(input('\nEnter number of units sold: '))  # gets number of units to decrease
        # checks if number of units available is less than the units sold
        if int(stock[count][box]) < decrease:
            print('\nInsufficient Stock!\n'
                  'There are', stock[count][box], 'unit(s) of stock available.\n')
            # checks if they want to continue with the sale partially
            print('Would you like to continue with a partial order?\n1 : Yes\n2 : No')
            while True:
                try:
                    choice = int(input('Enter your choice: '))
                    if choice == 1:  # continues partial sale
                        # num of units sold is equal to the current number of units available
                        decrease = int(stock[count][box])
                        stock[count][box] = '0'  # updates current number of units to 0
                        cost(box, decrease, count)  # gets the cost of the sale
                        print_update(count)  # prints the updated item table
                        break
                    elif choice == 2:
                        break  # breaks from this function
                    else:
                        print('Invalid Input!\n')
                        continue
                except ValueError:
                    print('Invalid Input!\n')
                    continue
        # if the units sold is not more than the number of units in stock
        else:
            stock[count][box] = str(int(stock[count][box]) - decrease)
            cost(box, decrease, count)
            print_update(count)
    except ValueError:
        print('\nInvalid Input!\n')
        decrease_stock(count, box)  # starts the function all over again


# gets the cost of the units sold based on box size
# 'box' is the index of box size, 'decrease' is amount of units sold,
# 'count' is the index of matched item
def cost(box, decrease, count):
    sale_cost = 0
    if box == 3:  # box of 50 screws
        sale_cost = decrease * float(stock[count][6])
    elif box == 4:  # box of 100 screws
        total_cost = decrease * float(stock[count][6]) * 2
        discount = total_cost * 0.1  # 10% discount
        sale_cost = total_cost - discount  # total sale cost
    elif box == 5:  # box of 200 screws
        total_cost = decrease * float(stock[count][6]) * 4
        discount = total_cost * 0.15  # 15% discount
        sale_cost = total_cost - discount
    # check if the item matched has an additional 10% discount
    if stock[count][7] == 'yes':
        discount = sale_cost * 0.1
        sale_cost = sale_cost - discount  # adds the 10% discount to sale cost
        print('\n✩✩✩ Total Cost (after discount): £', format(sale_cost, '.2f'), sep='')
    else:
        print('\n✩✩✩ Total Cost: £', format(sale_cost, '.2f'), sep='')


# prints the updated screw details of the matched item
def print_update(count):
    print('\n✩✩✩ Stock level successfully updated!\n')
    headers_print(headers_main)
    print('¦ {:<8} ¦ {:<9} ¦ {:<6} ¦ {:<9} ¦ {:<10} ¦ {:<10} ¦ {:14} ¦ {:<8} ¦'.format(*stock[count]))


# checks the item with the highest stock and return the index
def highest_stock():
    highest = highest_index = 0
    for item in stock:
        total = int(item[3]) + int(item[4]) * 2 + int(item[5]) * 4  # adds total number of units for each item
        # compare the highest value to the current total
        if highest < total:
            # if true, changes the highest value to the current total
            highest = total
            highest_index = stock.index(item)  # gets the index of the item with the highest stock
    return highest_index


# to edit the discounted screw based on number of units
def discount_feature():
    print('Category currently on discount:\n')
    while True:
        for item in stock:
            # if the discount column says 'yes'
            if item[7] == 'yes':
                headers_print(headers_main)
                print('¦ {:<8} ¦ {:<9} ¦ {:<6} ¦ {:<9} ¦ {:<10} ¦ {:<10} ¦ {:14} ¦ {:<8} ¦'.format(*item))
            else:
                continue
            highest_index = highest_stock()  # gets the index of the item with the highest stock
            # checks if the item has the highest stock
            if highest_index != stock.index(item):
                # print the item details with the highest stock
                print_highest(highest_index)
                print('\nWould you like to place a 10% discount on this screw type?\n1 : Yes\n2 : No')
                while True:
                    try:
                        choice = int(input('Enter your choice: '))
                        if choice == 1:
                            edit_discount(highest_index)  # edits the discounted column
                            # asks if the user wants to go to the mnu or exit the program
                            go_to_options(['Go to Menu', 'Exit Program'])
                        elif choice == 2:
                            go_to_options(['Go to Menu', 'Exit Program'])
                        else:
                            print('Invalid Input\n')
                            continue
                    except ValueError:
                        print('Invalid Input\n')
                        continue
            else:  # if item with the highest stock is already discounted
                print('\n✩✩✩ The category on discount has the highest stock.')
                go_to_options(['Go to Menu', 'Exit Program'])


# prints the screw details of the item with the highest stock
def print_highest(highest_index):
    print('\nCategory with the highest stock:\n')
    headers_print(headers_main)  # prints the headings
    for item in stock:
        if highest_index == stock.index(item):  # checks if the item has the highest stock
            print('¦ {:<8} ¦ {:<9} ¦ {:<6} ¦ {:<9} ¦ {:<10} ¦ {:<10} ¦ {:14} ¦ {:<8} ¦'.format(*item))


# edits the discounted item
def edit_discount(highest_index):
    for item in stock:
        if item[7] == 'yes':
            item[7] = 'no'  # changes the discount column from 'yes to 'no'
        if highest_index == stock.index(item):
            item[7] = 'yes'  # edits the discount column of item with the highest stock
    print('\n✩✩✩ Discount placed successfully! ✩✩✩')


# prints the bar chart of the screw lengths and respective number of units in stock
def bar_chart():
    # get the dictionary with lengths as keys and number of units as values
    length_stock = length_stock_dict()
    length = []
    # get the number of units and convert it into a list
    units = list(length_stock.values())
    for i in length_stock.keys():
        length.append(str(i))  # gets the lengths and converts it into a list
    plt.grid(zorder=0, axis='y', linestyle='--')  # grid for the bar chart
    plt.bar(length, units, color='cadetBlue', edgecolor='black', zorder=3)  # bar chart
    plt.xlabel('Length (in mm)')
    plt.ylabel('Units')
    plt.title('Units in Stock in each Length Category')
    plt.show()
    go_to_options(['View Bar Chart', 'Go to Menu', 'Exit Program'])  # prints options


# function to search again with the task as the argument
def search_again(task):
    print('\n1 : Search Again\n2 : Go to Menu')
    while True:
        try:
            choice = int(input('Enter your choice: '))
            if choice == 1:
                print()
                task()  # if user wants to search again it goes back to task
            elif choice == 2:
                print()
                menu()  # goes back to the menu
            else:
                print('Invalid Input!\n')
                continue
        except ValueError:
            print('Invalid Input!\n')
            continue


# function to display options based on task requirements
def go_to_options(options):
    num = 1
    options_dict = {}
    print()
    for option in options:
        print(num, ':', option)  # prints the options
        options_dict[num] = option  # stores the num as key and option as the value
        num += 1
    while True:
        try:
            choice = int(input('Enter your choice: '))
            option_chosen = ''
            for key, value in options_dict.items():
                if choice == key:  # checks if the option chosen is a key in the dictionary
                    option_chosen = value  # gets the corresponding value
            if option_chosen == 'Go to Menu':
                print()
                menu()  # goes to the menu
            elif option_chosen == 'Exit Program':
                sure_exit()  # asks user if they are sure if they wnt to exit
            elif option_chosen == 'View Bar Chart':
                print()
                bar_chart()  # displays the bar chart
        except ValueError:
            print('Invalid Input!\n')
            continue


# asks user if they are sure they want to exit
def sure_exit():
    print('\nAre you sure you want to EXIT?\n1 : Yes\n2 : Go to Menu')
    while True:
        try:
            choice = int(input('Enter your choice: '))
            if choice == 1:
                print('\n✩✩✩ GOODBYE! ✩✩✩')
                exit()
            elif choice == 2:
                print()
                menu()  # goes back to the menu
            else:
                print('Invalid Input!\n')
                continue
        except ValueError:
            print('Invalid Input!\n')
            continue


file = open('stock.txt', 'r')  # opens the text file and reads it
stock = []
for line in file:
    if not line.startswith('#'):
        line = line.rstrip('\n').split(',')  # splitting each line and each element separated by commas
        stock.append(line)  # appends each line to the list
file.close()
index = highest_stock()  # gets the index of the stock with the highest stock
for line in stock:
    if stock.index(line) == index:  # finds the item with the highest stock
        line.append('yes')  # appends 'yes' to the discount column
    else:
        line.append('no')  # appends 'no' to the discount column
headers_main = ['MATERIAL', 'HEAD TYPE', 'LENGTH', 'STOCK(50)', 'STOCK(100)', 'STOCK(200)', 'COST(per unit)',
                'DISCOUNT']  # list of main headings
print('✩✩✩ SIMPLY SCREWS INVENTORY ✩✩✩\n')
menu()

# References: # Pedamkar, P. (2020) Python Print Table. Available from: https://www.educba.com/python-print-table/
# [Accessed: 24 November 2022].
