numbers_count = 0

value_checker = 0

value_counter = 0

group_value_counter = 0

bruh = 372*372

for i in range(372*372, 809*809 + 1):
    holder = str(i)
    for j in range(0, len(holder)):
        if int(holder[j]) >= value_checker:
            value_checker = int(holder[j])
            value_counter += 1
        else:
            value_checker = 0
            value_counter = 0
            break;

        if value_counter == len(holder):
            value_checker = 0
            value_counter = 0
                
            for h in range(0, len(holder)):
                    try:
                        if holder[h] == holder[h - 1] or holder == holder[h + 1]:
                            group_value_counter += 1

                        if group_value_counter == 2:
                            group_value_counter = 0
                            numbers_count += 1
                    except:
                        continue
        
print("Total numbers that meet criteria: " + str(numbers_count))