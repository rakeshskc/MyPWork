import pandas as pd;
from  Util import  getMostCommonNgram;
from Util import  getMostEmailCommonDomain;
from Util import  getCosineSimilarity;
def testNgramForCompanyNames():
    df = pd.read_csv("D:\sqlite\sqliteSpatial\MexicoDataAnalysis\Company_Name\distinct_company_name_10Oct.tab", usecols=["Company_Name"],
                     delimiter='\t', encoding="utf-8")
    resultPath = "D:/sqlite\sqliteSpatial/MexicoDataAnalysis/Company_Name/Company_Name-mostcommonwordsNGRAM.txt";
    getMostCommonNgram(df,"Company_Name",resultPath)

def testMostEmailCommon():
    df = pd.read_csv("D:/sqlite/sqliteSpatial/MexicoDataAnalysis/Email/mexicoemailList_12Oct.csv", usecols=["ID", "EMAIL"],
                     delimiter=",");
    resultPath = "D:/sqlite/sqliteSpatial/MexicoDataAnalysis/Email/MostCommonDomainNameInEmail.csv";
    Counter = getMostEmailCommonDomain(df)
    with open(resultPath, "w", encoding="utf-8") as f:
        f.write("\"DomainName\",\"Count\"\n")
        for k, v in Counter.most_common():
            f.write("\"{}\",\"{}\"".format(k,v) +"\n")
    return Counter;



def testCosineSimilarity():
    resultPath = "D:/sqlite/sqliteSpatial/MexicoDataAnalysis/Email/Emails_Similarity_Output.txt";
    getCosineSimilarity("D:/sqlite/sqliteSpatial/MexicoDataAnalysis/Email/EmailListForCosineSimilarity.csv",resultPath,colIndex=0,similarity=0.95)


#testMostEmailCommon()
testCosineSimilarity();