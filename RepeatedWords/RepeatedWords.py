'''
====================================================
FUNCTION: find_repeats(fname) takes a textfile
          and checks for repeated words in file.
AUTHOR: Kethan Pabbi
REGNO: 121102356
DATE CREATED: 27th November 2021
====================================================
'''

# The function finds any repeated word
# Prints the repeated word and line number

def find_repeats(fname):

    # stores first word of each line
    dict1 = {} 
    # stores last word of each line
    dict2 = {}
    # stores repeated word in line
    dict3 = {}
    num_lines = 0
    words = [] 
    
    file = open(fname, "r")
    punct = """'.','!', '@', '#', '$', '%', '^', '&', '*', '(', 
            ')', '-', '=', ',', '/', '?', ';', ':', "'",'"', '[', 
            ']', '{', '}', '\\', '|', '>', '<', '~', '_', '+'"""
    try:
        for line in file:
            if line == "\n":
                num_lines += 1
                continue
            num_lines += 1
            for p in line:
                if p in punct:
                    line = line.replace(p, " ")
            words = ((line.strip(punct)).lower()).split()
                        
            if len(words)>1:
                for i in range(1,len(words)):
                    count = 1
                    if words[i-1] == words[i]:
                        count+=1
                        dict3[words[i]] = count
                for key, value in dict3.items():
                    if value >= 2:
                        print("Line Number:",num_lines,
                        "\nRepeated Word:",key)
            else: print("Enter two or more words!")
            
            dict1[num_lines] = words[0]
            dict2[num_lines] = words[-1]
       # print(dict3)
        for key, value in dict1.items():
            if value in list(dict2.values()):
                print("Line Number:",key,
                "\nRepeated Word:",value)       
    except:
        return "Sorry Error Occurred!"
    return ''