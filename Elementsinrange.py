input_usr = input()
input_nums = input_usr.split()

num_list = [int(x) for x in input_nums]

input_bnds = input()
bounds = input_bnds.split()

lower_bound = int(bounds[0])
upper_bound = int(bounds[1])


for i in range(len(num_list)):
    if num_list[i] >= lower_bound and num_list[i] <= upper_bound:
        print(num_list[i], end=" ")