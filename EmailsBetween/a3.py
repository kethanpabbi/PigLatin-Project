'''
====================================================
FUNCTION: emails_between(suspects) takes dictionary 
          as input and returns email object if match
          found between the suspects.
AUTHOR: Kethan Pabbi
REGNO: 121102356
DATE CREATED: 15th March 2021
====================================================
'''

# The function finds red flags from email_corpus
# Returns the email object if there is a match.

from email.parser import Parser
import os
import regex as re

def emails_between(suspects):
    # Store the values in list
    dictlist = []; email_obj = []
    # Iterate dictionary, get list of lists
    for key, value in suspects.items():
        temp = [key,value]
        dictlist.append(temp)

    # Iterate through the 'enron_email_corpus' directory
    for subd, dir, file in os.walk('enron_email_corpus'):
        # Iterate the files
        for f in file:
            # Get file name
            fname = os.path.join(subd, f)
            # Try, except to catch errors
            try:
                # Open file and parse with Parser
                p = Parser()
                fopen = open(fname)
                msg = p.parse(fopen, True)
                r =[]; s=[]
                # Get relevent information
                sender = msg.get('From')
                receiver = msg.get('To')   
                origin = msg.get('X-Origin')
                reg = receiver.split()
                
                # Remove commas
                for i in reg:
                    new = re.sub(r',','',i)
                    r.append(new)
                
                # If directory origin is match
                if origin.lower() in suspects.keys():
                    rec_val = []; origin_val=[]

                    # Iterate list of lists and get values
                    for sublist in dictlist:
                        # If sender and origin is a match
                        if sublist[0] == origin.lower():
                            origin_val = sublist[1]
                        # Append rest to check receiver 
                        else:
                            rec_val.append(sublist[1])
                for i in r:
                    # Check if receiver match in suspect
                    res1 = any(i in sublist for sublist in rec_val)
                    # Check if sender and origin match
                    res2 = sender in origin_val
                    # If sender from origin directory and reciever match 
                    if res1 and res2 == True:
                        email_obj.append(msg)
            except Exception: pass 
    return email_obj