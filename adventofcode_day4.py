with open('input4', 'r') as file:
    data = file.read().replace(':', ' ')
    data = data.replace('\n', ' ')
    data = data.split('  ')


# data formatted to an arrays of an array
def formatted(a):
    format_data = []

    for i in range(len(a)):
        format_data.append(a[i].split(' '))

    del format_data[len(a)-1][-1]

    return format_data


# data formatted to dictinarries of an array
def new_dict(b):
    res_dict = {}
    res_arr = []

    for i in range(len(b)):
        it = iter(b[i])
        res_dict = dict(zip(it, it))
        res_arr.append(res_dict)

    return res_arr


# count missing keys
def missing_key(c):
    num = 0
    req_lst = {'byr': '', 'iyr': '', 'eyr': '',
               'hgt': '', 'hcl': '', 'ecl': '', 'pid': ''}
    opt_lst = {'byr': '', 'iyr': '', 'eyr': '',
               'hgt': '', 'hcl': '', 'ecl': '', 'pid': '', 'cid': ''}

    for i in range(len(c)):
        if set(req_lst) <= set(c[i].keys()) <= set(opt_lst):
            num += 1

    return num


# checks every category
def passports_check(d):
    correct_passports = 0

    req_lst = {'byr': '', 'iyr': '', 'eyr': '',
               'hgt': '', 'hcl': '', 'ecl': '', 'pid': ''}
    opt_lst = {'byr': '', 'iyr': '', 'eyr': '',
               'hgt': '', 'hcl': '', 'ecl': '', 'pid': '', 'cid': ''}

    for i in range(len(d)):

        if set(req_lst) <= set(d[i].keys()) <= set(opt_lst):
            valid = True

            for key, value in d[i].items():

                if key == 'byr' and int(value) not in range(1920, 2003):
                    valid = False
                    break

                if key == 'iyr' and int(value) not in range(2010, 2021):
                    valid = False
                    break

                if key == 'eyr' and int(value) not in range(2020, 2031):
                    valid = False
                    break

                if key == 'hgt':
                    if value[-2:] not in ['cm', 'in']:
                        valid = False
                        break

                    if value[-2:] == 'cm' and int(value[:-2]) not in range(150, 194):
                        valid = False
                        break

                    if value[-2:] == 'in' and int(value[:-2]) not in range(59, 77):
                        valid = False
                        break

                if key == 'hcl' and (value[0] != '#' or len(value[1:]) != 6 or not all(char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'] for char in value[1:])):
                    valid = False
                    break

                if key == 'ecl' and value not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                    valid = False
                    break

                if key == 'pid' and not (len(value) == 9):
                    valid = False
                    break

            if valid == True:
                correct_passports += 1

    return correct_passports


a1 = formatted(data)
b1 = new_dict(a1)
c1 = missing_key(b1)
d1 = passports_check(b1)
print('Number of valid passports (Part1): {}'.format(c1))
print('Number of valid passports (Part2): {}'.format(d1))
