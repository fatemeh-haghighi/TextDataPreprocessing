'''
This code gets the tokenized senteses of the article and tagges each token.
each token and its tag will be written in the output file
input: articles.tokenized
output: articles.tagged
'''
import nltk
nltk.download('averaged_perceptron_tagger')
from nltk import pos_tag

# to add tag to each token
def tag(infile, outfile):
    previous_word = ""
    lines = infile.readlines()
    for line in lines:
        tokens = line.split()
        tagged = pos_tag(tokens)
        paired = []
        for (word, tag) in tagged:
            # to skip to labels and document numbers
            if word == "$DOC" or word == "$TITLE" or word == "$TEXT":
                paired.append(word)
                if word == "$DOC":
                    previous_word = "$DOC"
                else:
                    previous_word = ""
                
            else:
                if previous_word == "$DOC":
                    paired.append(word)
                    previous_word = ""
                else:
                    # store each token and its tag
                    paired.append(word + '/' + tag)
        outfile.write(' '.join(paired) + '\n')

#input = open('samples.tokenized2', 'r')
#output = open('samples.tagged2', 'w')

input = open('articles.tokenized', 'r')
output = open('articles.tagged', 'w')
tag(input, output)
input.close()
output.close()
