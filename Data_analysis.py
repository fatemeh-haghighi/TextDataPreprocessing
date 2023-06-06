'''
\This code reads the article.tagged file and answers the following  questions:
1- the number of documents in the data collection?
2- min, avg, and max document length by the number of sentences?
3- min, avg, and max document length by the number of tokens?
4- avg sentence lengths by the number of tokens in the whole article?
5- avg sentence lengths by the number of tokens in each document?

input file: articles.tagged
'''



# 1-to calculate the number of documents in the article
def doc_counter(article_lines):
    counter = 0
    for line in article_lines:
        # print(line, '\n\n')
        words = line.split()
        if "$DOC" in words:
            counter += 1
    return counter


# 2-to calculate the number of sentences in each document and return a list of numbers,
# in the output each number indicates the sentence counts of the document associated with that index
def doc_sent_counter(article_lines, doc_counter):
    doc_sent_numbers = []
    flag = False
    sent_counter = 0
    for line in article_lines:
        words = line.split()
        if "$TEXT" in words or "$TITLE" in words:
            continue
        elif "$DOC" in words:
            if flag == False:
                flag = True
            elif flag == True:
                doc_sent_numbers.append(sent_counter)
                sent_counter = 0
        else:
            sent_counter += 1
    doc_sent_numbers.append(sent_counter)
    return doc_sent_numbers


# 3-to calculate the overall number of tokens in each document
# and return a list of numbers, each indicates the count of tokens in a document
def doc_token_counter(article_lines):
    doc_token_numbers = []
    flag = False
    token_counter = 0
    for line in article_lines:
        words = line.split()
        if "$TEXT" in words or "$TITLE" in words:
            continue
        elif "$DOC" in words:
            if flag == False:
                flag = True
            elif flag == True:
                doc_token_numbers.append(token_counter)
                token_counter = 0
        else:
            token_counter += len(line.split())
    doc_token_numbers.append(token_counter)
    return doc_token_numbers


#4-1- make an array contaning the token numbers of each sentence in the article
def sent_token_counter(article_lines):
    sents_token_counts = []
    for line in article_lines:
        words = line.split()
        if "$DOC" in words or "$TITLE" in words or "$TEXT" in words:
            continue
        else:
            sents_token_counts.append(len(words))
    return sents_token_counts


# to calculate the avg number of tokens in each document of the article
def sent_token_counter_per_doc(article_lines):
    avg_sent_tokens = []
    document_label = ""
    flag = False
    sent_counter = 0
    sent_tokens = []
    for line in article_lines:
        words = line.split()
        if "$TEXT" in words or "$TITLE" in words:
            continue
        if "$DOC" in words:
            if flag == False:
                document_label = words[0] + " " + words[1]
                flag = True 
            elif flag == True:
                avg_sent_tokens.append((document_label, sum(sent_tokens) / len(sent_tokens)))
                sent_tokens.clear()
                document_label = words[0] + " " + words[1]
        else:
            sent_tokens.append(len(line.split()))
    avg_sent_tokens.append((document_label, sum(sent_tokens) / len(sent_tokens)))
    return avg_sent_tokens






#input = open('samples.tagged2', 'r')

input = open('articles.tagged', 'r')
article_lines = input.readlines()

document_numbers = doc_counter(article_lines)
print("The number of documents in this article is : ", document_numbers, "\n")

document_lengthes = doc_sent_counter(article_lines, document_numbers)
print("The length of documents based on the number of sentences is: ", document_lengthes)
print("Minimum lenght of document by the number of sentences is : ", min(document_lengthes))
print("Maximum lenght of document by the number of sentences is : ", max(document_lengthes))
print("Average lenght of document by the number of sentences is : ", sum(document_lengthes) / len(document_lengthes), "\n")

documents_token_length = doc_token_counter(article_lines)
print("The length of documents based on the number of tokens is: ", documents_token_length)
print("Minimum lenght of document by the number of tokens is : ", min(documents_token_length))
print("Maximum lenght of document by the number of tokens is : ", max(documents_token_length))
print("Average lenght of document by the number of tokens is : ", sum(documents_token_length) / len(documents_token_length), "\n")

article_sents_token_counts = sent_token_counter(article_lines)
print("Average lenght of sentences by the number of tokens in the whole article is : ", sum(article_sents_token_counts) / len(article_sents_token_counts), "\n")

avg_sent_tok_doc = sent_token_counter_per_doc(article_lines)
for (label, num) in avg_sent_tok_doc:
    print("Average length of sentences by the number of the tokens in ", label, " is : ", num)

input.close()
