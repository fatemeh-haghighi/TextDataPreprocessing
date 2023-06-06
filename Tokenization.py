'''
This file gets the splitted senteces of the article and tokenize each sentece 
input: articles.splitted
output: articles.tokenized
'''
import ply.lex as lex
from ply.yacc import yacc
from decimal import *
 
# List of token names, always needed
tokens = (
   'LABEL',
   'HYPHENATED',
   'APOSTROPHIZED',
   'WORD',
   'NUMBER',
   # 'DELIMITERS',
   'PUNCTUATION',
   'ERROR'
)

# Regular expresion --> RE
# RE for label tokens [$DOC, $TEXT, $TITLE]
def t_LABEL(t): r'[($)]DOC' '|' r'[($)]TITLE' '|' r'[($)]TEXT'; return t

# RE for hyphenated tokens
def t_HYPHENATED(t): r'(\- [a-zA-Z_0-9])+ (\- [a-zA-Z_0-9]+)+'; return t

# RE for apostrophized tokens
def t_APOSTROPHIZED(t): r'[a-zA-Z_]+\'[a-zA-Z_\']*';  return t

# RE for words: letters and digits, first letters then digits
def t_WORD(t): r'[0-9]*[a-zA-Z_]+[a-zA-Z_0-9]*'; return t

# RE for signed integer or decimal number
def t_NUMBER(t): r'\-?\d+(\.\d+)?';  return t

# RE for whitespaces
t_ignore  = ' [\t]+[\n]*'
# t_DELIMITERS = '\s+'

# RE for other characters as puctuation
t_PUNCTUATION = r'.'

# Error handling
def t_error(t):
    print("Shouldn't get here")


# Build the lexer
lexer = lex.lex()

# to extract a sunstring based on a delimiter 
# uses in the cases we want to split tokens in further parts
def split_with_delimiter(str_input, delimiter):
   str_output = ""
   for i in range(len(str_input)):
      if str_input[i] != delimiter:
         str_output += str_input[i]
      else:
         str_output += ' ' + str_input[i]
         if i != len(str_input) - 1:
            str_output += ' '
   return str_output


# to calculate the number of chars between two delimiters in a string
def count_char_between_delimiters(str_input, start_del, end_del):
   flag = False
   char_counter = 0
   for i in range(len(str_input)):
      if flag == False and str_input[i] != start_del:
         continue
      elif flag == False and str_input[i] == start_del:
         flag = True
      elif flag == True and str_input[i] != end_del:
         char_counter += 1
      elif flag == True and str_input[i] == end_del:
         break
   return char_counter



# for analysing hyphenated tokens and spliting if needed
def hyphenated_handler(str_token):
   # three-part hyphenated tokens
   if str_token.count('-') == 2:
      char_counter = count_char_between_delimiters(str_token, "-", "-")

      if char_counter < 2 or char_counter > 3:
         return split_with_delimiter(str_token, "-")
      else: 
         return str_token
   
   # hyphenated tokens with more than 3 parts
   if str_token.count('-') > 2:
      return split_with_delimiter(str_token, "-")
   
   else:
      return str_token

# for analysing apostrophized tokens and spliting if needed
def apostrophized_handler(str_token):
   # two-parts apostrophized tokens
   if str_token.count("'") == 1:
      index = str_token.find("'")

      if (len(str_token[:index]) == 1 and len(str_token[index + 1:]) > 2) or (str_token[index + 1:] == "s") or (str_token[index + 1:] == "S"):
         return str_token
     
      else:
         if len(str_token[index + 1:]) < 3 and len(str_token[index + 1:]) > 0:
            first_tok = str_token[:index]
            second_tok = str_token[index:]
            return first_tok + " " + second_tok
         else:
            return split_with_delimiter(str_token, "'")

   # three-parts apostrophized tokens   
   elif str_token.count("'") == 2:
      len_first_tok = 0
      for i in range(len(str_token)):
         if str_token[i] != "'":
            len_first_tok += 1
         else:
            break
      second_index = 0
      flag = False
      for i in range(len(str_token)):
         if str_token[i] == "'" and flag== False:
            flag = True
         elif str_token[i] == "'" and flag == True:
            second_index = i
            break
        
      
      if len_first_tok == 1 and (str_token[second_index + 1:] == "s" or str_token[second_index + 1:] == "S"):
         return str_token
      else:
         return split_with_delimiter(str_token, "'")
   else:
      return split_with_delimiter(str_token, "'")


      


      
   

def scan(data):
   tokens = ""
   lexer.input(data)
   while True:
      tok = lexer.token()
      if not tok:
         break
      # print(tok)
      print(tok.type, tok.value, tok.lineno, tok.lexpos)
      if(tok.type == 'HYPHENATED'):
         # print(len(data))
         tokens += hyphenated_handler(tok.value)
         if tok.lexpos + len(tok.value) != len(data) - 1:
            # print(tok.type, tok.value, tok.lineno, tok.lexpos + len(tok.value))
            tokens += " "
      elif(tok.type == 'APOSTROPHIZED'):
         tokens += apostrophized_handler(tok.value)
         if tok.lexpos + len(tok.value) != len(data) - 1:
            tokens += " "
      else:
         tokens += tok.value
         if tok.lexpos + len(tok.value) != len(data) - 1:
            tokens += " "
   
   return tokens

# open the input and output files
#input = open('samples.splitted2', 'r')
#output = open('samples.tokenized2', 'w')

# input = open('articles.splitted', 'r')
# output = open('articles.tokenized', 'w')

# lines = input.readlines()
# for line in lines:
#    line_tokens = ""
#    line_tokens = scan(line)
#    output.write(line_tokens + '\n')


# input.close()
# output.close()

temp = scan("John's  O'Reily's  you're  a''s")
print(temp)

