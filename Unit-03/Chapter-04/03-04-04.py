user_str = input()
num_spaces_found = 0
current_space_count = 0
str_length = len(user_str)

for char in user_str:
    if char == ' ':
        num_spaces_found += 1
        

for index in range(str_length):
    char_at_index = user_str[index]
    if char_at_index[length] == ' ':
        current_space_count += 1
        
        if current_space_counter == num_spaces_found:
            print(index)
        else:
            print(f'{index}, ', end='')
            
if num_spaces_found == 0:
    print('no spaces found')
    