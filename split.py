'''
this code splites the senteces of input article.
as the output, in a text file all the senteces(end with ".", "!", "?") will be in a line.
also labels and their contex will be in a seperate line
input: articles.txt
output: articles.splitted
'''
import nltk
nltk.download('punkt')
from nltk import sent_tokenize
import re


# this function returns a substring of a sentence
# based that is between two specified strings
def substing(start_string, end_string, str_in):
    if start_string == "":
        end_str_index = str_in.find(end_string)
        return str_in[:end_str_index]

    elif end_string == "":
        start_str_index = str_in.find(start_string) +len(start_string)
        return str_in[start_str_index : ]
    
    else:
        start_str_index = str_in.find(start_string) +len(start_string)
        end_str_index = str_in.find(end_string)
        return str_in[start_str_index : end_str_index]
 

# main function for split the senteces
def split(infile, outfile):
    lines = infile.readlines()
    buffer = ' '.join(line[:-1] for line in lines)
    sents = sent_tokenize(buffer)
    title_found = False
    text_found = False
    for sent in sents:
        
        # writing regular senteces without any label in output file
        if "$DOC" not in sent and "$TITLE" not in sent and "$TEXT" not in sent:
            if title_found == True:
                outfile.write(sent)
            else:
                outfile.write(sent + '\n')

        
        # writing senteces with at leat a label on output file
        else:
            words = sent.split()
        
            if "$DOC" in words:
                # in cases that some sentences without ending are before $DOC label
                if words[0] != "$DOC":
                    end0 = sent.find(" $DOC")
                    if(sent[:end0] != ""):
                        outfile.write(sent[:end0] + '\n')
                                
                # in normal cases that the original sentece start with $DOC
                sub_sent = substing("$DOC ", " $TITLE", sent)
                outfile.write( "$DOC " + sub_sent + '\n')
                        
            
            if "$TITLE" in words:
                title_found = True
                # in cases that the title sentece ends with "." or "!" or "?"
                if "$TEXT" not in words:
                    outfile.write("$TITLE" + '\n')
                    sub_sent = substing("$TITLE ", "", sent)
                    outfile.write(sub_sent)
                
                # in cases the title sentece endes with whitespace and the $TEXT comes after it
                else:
                    text_found = True
                    # print("&&&&&&&&&&&&&&&&&& ", sent)
                    title_found = False
                    outfile.write("$TITLE" + '\n')
                    sub_sent = substing("$TITLE ", " $TEXT", sent)
                    outfile.write(sub_sent)



            if "$TEXT" in words:
                if words[0] != "$TEXT" and text_found == False:
                    # print("@@@@@@@@@@@@@@@ ", sent)
                    title_found = False
                    sub_sent = substing("", " $TEXT", sent)
                    # print("here")
                    outfile.write(sub_sent + '\n')

                else:
                    outfile.write('\n')
            
                outfile.write("$TEXT" + '\n')
                sub_sent = substing("$TEXT ", "", sent)
                outfile.write( sub_sent + '\n')
                # print("after text : ", sub_sent)
                title_found = False
                text_found = False
                
# $DOC LA010190-0087
# $TITLE
# O.C. POP MUSIC REVIEW;
# ORIGINAL T.S.O.L. BAND'S REUNION SHOW PACKS NOSTALGIA, LACKS FOCUS
# $TEXT


            


# open the input and output files
# input = open('samples.txt', 'r')
# output = open('samples.splitted2', 'w')

input = open('articles.txt', 'r')
output = open('articles.splitted', 'w')

# the main function that splites the senteces
split(input, output)

# close the input and output files
input.close()
output.close()
