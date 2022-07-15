'''
======================================================================================================
FUNCTION: The function pig_latin(s)takes a string as input from the user and converts it to pig latin.
AUTHOR: Kethan Pabbi
REGNO: 121102356
DATE CREATED: 18th November 2021
======================================================================================================
'''

# The function converts the input string to pig latin
# Returns the converted string in pig latin
# Returns error message if the function fails to convert due to exceptions

def pig_latin(s):

    punctuations = ['?', '!', '.', ',', '[', ']', '@', '#', '%', '*', '<', '>',
                    '~', '\\', '|', ':', ';', '"', "'", '=', '-', '_', '+', '`']
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    # result from individual lines
    result_combined = ''
    # final result of all result lines
    final = ''
    lines = s.splitlines()

    # checks if the code is error free 
    try:
        for line in lines:
            words = line.split()

            # result of each line 
            result_of_line = ''

            for word in words:
                flag = 0

                # returns true and sets flag to 1 if the word has a capital letter
                if not word.isupper() and not word.islower():
                    flag = 1

                punct = ''
                for i in range(len(word)):

                    # if the word has punctuations then save the punctuations in punct
                    if word[i] in punctuations:
                        punct = word[i:]

                        # if the word does have punctuation 
                        # save the word without the puctuation
                        if i != 0:
                            word = word[0:i]
                        break

                # if true then word has no punctuations and set punct empty
                if word == punct:
                    punct = ''

                # if the first letter in word is a vowel then add 'way' to it
                if word[0] in vowels:
                    word = word + "way" + punct 

                    # if true then the word has capital letter and 
                    # the converted word must also follow same
                    if flag == 1:
                        result_of_line = result_of_line + word.capitalize() + " "
                    else:
                        result_of_line = result_of_line + word + " "

                # if word has no vowels
                elif word not in vowels and word.isalpha():
                    converted = ''
                    for i in range(len(word)):

                        # shift the letters of the word to after vowel
                        if word[i] not in vowels:
                            converted = converted + word[i]
                        else:
                            word = word[i:]
                            break
                    
                    # if true then the converted word is same as
                    #  word and set converted as empty
                    if word == converted:
                        converted = ''
                    
                    # add 'ay' and punctuations after converting the word
                    word = word + converted + "ay" + punct
                    
                    # if the word has capital letter then 
                    # the converted string must also have the same
                    if flag == 1:
                        result_of_line = result_of_line + word.capitalize() + " "
                    else:
                        result_of_line = result_of_line + word + " "
                
                # if the word is not alphanumeric 
                else:
                    liresult_of_linene_result = result_of_line + word + punct + " "

            # has the result of each line as list        
            result_combined = result_combined + result_of_line + '\n'
 
        for line in result_combined.splitlines():

            # if the line is not empty print the 
            # lines of result else print empty line
            if len(line.strip()) != 0:
                final = final +line[0].upper() + line[1:] + '\n'
            else:
                final = final + '\n'
    
    # error generated due to exceptions
    except:
        return print("Error Message: Sorry Invalid Input!")

    # always executes nonetheless
    finally:
        p = "PIG LATIN:"
        print(p)
        print ("=" * len(p))
        # print the converted string
        print(final)
        return '' 