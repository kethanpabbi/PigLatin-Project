'''
====================================================
FUNCTION: find_couples(brides, grooms) takes two 
          textfiles and finds matching couples.
AUTHOR: Kethan Pabbi
REGNO: 121102356
DATE CREATED: 20th Febraury 2021
====================================================
'''

# The function finds any matching couples 
# Prints the details according to the required format.

import re
def find_couples(brides, grooms):
    b = open(brides,'r').read()
    g = open(grooms,'r').read()
    # Capture the values using compile and regex multiline
    year = re.compile(r'in\s(\d{4})', re.M)
    area = re.compile(r'Returns\sArea\t([A-Za-z])', re.M)
    quarter = re.compile(r'Quarter\t(\d{1})', re.M)
    volume = re.compile(r'Volume\sNo\t(\d{1,2})', re.M)
    page = re.compile(r'Page\sNo\t(\d{1,4})', re.M)
    name = re.compile(r"of\s([A-Za-z]+(?:\s[A-Za-z]+)*$)", re.M)

    # Zip Nicolas values in a list of lists
    mdata = [*zip(name.findall(b), year.findall(b), area.findall(b),\
        quarter.findall(b), volume.findall(b), page.findall(b))]
    
    # Zip Mary values in a list of lists
    ndata = [*zip(name.findall(g), year.findall(g), area.findall(g),\
        quarter.findall(g), volume.findall(g), page.findall(g))]

    # Run within try for debug
    try:
    # Iterate Nicholas list
        for i in range(len(ndata)):
            # Iterate Mary list
            for j in range(len(mdata)):
                # compare the areas of Nicolas and Mary
                if (ndata[i][2] == mdata[j][2]):
                    # Compare all other values
                    if(ndata[i][1] == mdata[j][1] and ndata[i][3] == mdata[j][3] \
                        and ndata[i][4] == mdata[j][4] and ndata[i][5] == mdata[j][5]):
                        # Print if matches
                        print('Possible match!\n'+mdata[j][0]+' and '+ndata[i][0]+' in '\
                            +ndata[i][2]+' in '+ndata[i][1] +'\nQuater = '+ndata[i][3]+\
                            ', Volume = '+ndata[i][4], ', Page = '+ndata[i][5]+'\n')
    # Return Error
    except: print("Sorry, Error Occured!")
    return ''