# TextDataPreprocessing

## Problem statement:
Four types of text processing has been implemented:
1- split the text of documents into sentences.
2- tokenize the sentences into sequences of words.
3- associate the tokenized words with their POS tags.
4- analyze the text to get some statistics about the dataset.

## Limitations
We considered three types of labels during an article : DOC, TITLE , and TEXT. 
This could be counted as a limitation since this code will not work properly for the articles with more labels, if available.

## How to test:
All the programs are implemented in Python3, so it is crucial to run all the files. There is a necessary sequence in running the files since the output of each code will be used in the next implementation as the input file. First, you should run the “split.py,” and its input is the
“articles.txt”, this will make a file named “articles.splitted” as the output, containing splitted sentences of the dataset.
Then, for tokenizing the sentences, you should run the “Tokenization.py” file. This code receives the “articles.splitted” file as the input, which was the output of the previous code, and returns the “articles.tokenized” as the output file, which contains the tokenized sentences.
By running the “pos-tag.py” code with “articles.tokenized” input file, tagged tokens will be available in the output file named “articles.tagged”.

For statistical analysis, we can use the final output we resulted, “articles.tagged”, so this file will
be the input file for “Data_analysis.py” code and prints below information:
1- The number of documents in the data collection.
2- Min, max, and average of documents’ length by the number of sentences.
3- Min, max, and average of documents’ length by the number of tokens.
4- Average sentence lengths by the number of tokens in the whole article.
5- Average sentence lengths by the number of tokens in each document.
