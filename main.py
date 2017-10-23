from collections import Counter
from nltk.tokenize import word_tokenize

# text1 = "It's true that the chicken was the best bamboozler in the known multiverse."
# tokens = word_tokenize(text1)
# print(tokens)

def wordScores(articles, refCompany, refParaWeight=2, precParaWeight=1, sucParaWeight=1, otherParaWeight=0.5):
    # Envelop string in a list 
    if isinstance(articles, str):
        articles = [articles]
    # Raise exception if 'articles' is not a list or tuple
    elif type(articles) not in [list,tuple]:
        print("'articles' not string, list or tuple")
        return
    # Raise exception if an article in 'articles' is not a string 
    elif type(articles) in [list,tuple]:
        for article in articles:
            if not isinstance(article, str):
                print("article in 'articles' is not a string")
                return
    # Raise exception if 'refCompany' is not a string 
    if not isinstance(refCompany, str):
        print("'refCompany' is not a string")
        return

    for article in articles:
        # split article into paragraphs
        paragraphs = article.split("\n")
        for paragraph in paragraphs:
            # tokenise paragraph and keep the punctuation
            tokens = word_tokenize(paragraph)
            tokensCount = Counter(tokens)
            print(tokens)
            


wordScores("hello, there\nmy name is anas ayubi", "TRG")

