import pandas as pd;

def getMostCommonNgram(pd,colName,resultPath,ngcount=3):
    from collections import Counter
    df = pd
    ngramSet = list();
    c = 0
    for index, row in df.iterrows():
        data = row[colName]
        ngram = generate_ngrams(data,ngcount)
        for f in ngram:
            ngramSet.append(f)
        c = c+1;
    Counter = Counter()
    for word in ngramSet:
        word = str(word)
        Counter[word] +=1;

    with open(resultPath, "w", encoding="utf-8") as f:
        for k, v in Counter.most_common():
            f.write("{} {}\n".format(k, v))

def generate_ngrams(text, n):
    words = text.split()
    output = []
    for i in range(len(words)-n+1):
        output.append(words[i:i+n])
    return output

def wordToVec():
    from gensim.models import Word2Vec
    sent = [["rakesh","chaudhari"],["rake","chaudhari","rakesh"],["rakesh","chaudhari"]]
    model = Word2Vec(sent, min_count=1)

    words = list(model.wv.vocab)
    print(words)
    # access vector for one word
    path = 'D:/sqlite/sqliteSpatial/MexicoDataAnalysis/model.bin';
    model.save_word2vec_format(path)
    new_model = Word2Vec.load(path)
    print(new_model)

#df = pd.read_csv("D:/sqlite/sqliteSpatial/MexicoDataAnalysis/MEXICOEMAILLIST_1.csv", usecols=["ID","EMAIL"],delimiter=",")
def getMostEmailCommonDomain(df):
    from collections import Counter
    Counter = Counter()
    for word in df['EMAIL']:
            word1 = word;
            word = str(word).split("@")
            if len(word)>1:
                str1 = word
                str1 = str1[len(str1)-1]
                Counter[str1] += 1;
            else:
                print(word1)
    return Counter
def getCosineSimilarity(fieldListPath,resultPath,colIndex=0,similarity=0.90):
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    import csv
    documents = [];
    pyMap = {}
    index = 0
    with open(fieldListPath) as emfile:
        spamreader = csv.reader(emfile, delimiter=',')
        for data in spamreader:
            documents.append(data[colIndex])
            pyMap[index] = data[colIndex]
            index = index + 1
            #if index == 2000:
            #   break
    try:
        tfidf_vectorizer = TfidfVectorizer(analyzer="char")
        tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
        cs = cosine_similarity(tfidf_matrix, tfidf_matrix)
        fw = open(resultPath, "w")
        for vecArr in cs:
            selfName = "";
            tocompareList = [];
            i = 0;
            for vec in vecArr:
                if vec >= 1 and len(selfName) == 0:
                    selfName = pyMap[i]
                elif vec >= similarity:
                    tocompareList.append(pyMap[i])
                i = i + 1;
            if len(tocompareList) > 0:
                fw.write(str(selfName) + "\t" + str(tocompareList) + "\n")

            tocompareList = []
        print("Result saved to: ",resultPath)
    except Exception as inst:
           print(inst, ", Reduce input list size")
