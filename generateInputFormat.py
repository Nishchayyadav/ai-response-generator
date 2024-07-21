def create_demo_input_file(filename, num_entries):
    with open(filename, 'w') as file:
        for i in range(1, num_entries + 1):
            if i == num_entries :
                file.write(f"demo prompt : {i}")
                continue
            entry = f"demo prompt : {i}\n\n----\n\n"
            
            file.write(entry)

    print(f"Demo input file '{filename}' created with {num_entries} entries.")

filename = 'input.txt'
num_entries = 5

create_demo_input_file(filename, num_entries)