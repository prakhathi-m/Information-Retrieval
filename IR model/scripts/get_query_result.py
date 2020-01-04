import json
import urllib.request 
corenames = ['BM25', 'language_model', 'DFR']
# corenames = ['DFR']

fp = open("test_queries.txt", "r",encoding="utf-8")
i = 1
for line in fp: 
    queryId=line.strip().split(None,1)[0]
    text= line.partition(' ')[2].strip()
    text=text.replace(":","\:")
    text=urllib.parse.quote(text)
    for model in corenames:
        inurl = 'http://18.191.209.23:8984/solr/'+model+'/select?defType=edismax&q='+text+'&fl=id%2Cscore&wt=json&indent=true&rows=20'
        outfn = str(i)+'.txt'

        qid = queryId
        IRModel=model
        outf = open(outfn, 'w')
        outfile = open(model+'-mod.txt', 'a+')
        data = urllib.request.urlopen(inurl)

        docs = json.load(data)['response']['docs']
        # the ranking should start from 1 and increase
        rank = 1
        for doc in docs:
            outf.write(qid + ' ' + 'Q0' + ' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(doc['score']) + ' ' + IRModel + '\n')
            outfile.write(qid + ' ' + 'Q0' + ' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(doc['score']) + ' ' + IRModel + '\n')
            rank += 1
        i+=1
        outf.close()
        outfile.close()
