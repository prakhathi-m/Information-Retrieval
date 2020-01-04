import sys
from sys import argv

f = open(sys.argv[1], "r+")
docId=[]
doc_dict = {}
term_dict = {}
posting_list = {}
mydoc = {}
i = 0
num = {}
fo = open(sys.argv[2], "w")
for line in f:
    docId.append(line.split(None, 1)[0])
    tokens = line.split()
    d={}
    for word in tokens:
        doc_dict[docId[i]]=d
        num[docId[i]] = len(tokens)-1 
        if word != docId[i]:
            if word in posting_list.keys():
                posting_list[word].append(docId[i])
            else:
                posting_list[word] = [docId[i]]
            if word in doc_dict[docId[i]].keys():
              d[word]+=1
            else:
              d[word]=1
    doc_dict[docId[i]]=d
    i+=1
    
for word in posting_list:
    posting_list[word] = sorted(set(posting_list[word]))
    term_dict[word] = len(posting_list[word]) 

tfidf_list={}
tf_list={}
total_doc = len(docId)
idf = total_doc / len(term_dict)
for term in posting_list.keys():
  idf = total_doc / len(posting_list[term])
  tf_list={}
  for i in docId:
    if i in posting_list[term]:
        tf = (doc_dict[i][term]/num[i])
    else: 
        tf = 0
    tf_list[i] = tf * idf
  tfidf_list[term] = tf_list


def getTfIdf(tokens, result):
    sum = {}
    for term in tokens:
        for docId in result:
            if docId in sum:
                sum[docId] += tfidf_list[term][docId] 
            else:
                sum[docId] = tfidf_list[term][docId] 
    arr = sorted(sum.items(), key=lambda kv: kv[1], reverse=True)
    res_list = [x[0] for x in arr]
    fo.write('\n')
    fo.write('Results:')
    writeToFile(res_list)


def DaatOr(postings):
    n=0
    union_list, n = union(postings, 0, len(postings)-1, n)
    union_list = sorted(union_list)
    fo.write('Results:')
    writeToFile(union_list)
    fo.write('\n')
    fo.write('Number of documents in results: ')
    fo.write(str(len(union_list)))
    fo.write('\n')
    fo.write('Number of comparisons: ')
    fo.write(str(n))
    return union_list

def union(lists,l,h,count):
    if l==h:
        return lists[l],count
    if h-l == 1:
        return union_of_twoLists(lists[h],lists[l],count)
    
    m = l+h //2
    left_result,count = union(lists,l,m,count)
    right_result,count = union(lists,m+1,h,count)
    return union_of_twoLists(left_result,right_result,count)

def union_of_twoLists(a,b,count):
    result_array = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        count = count+2
        if(a[i] == b[j]):
            result_array.append(a[i])
            count = count-1
            i = i+1
            j = j+1
        elif (a[i] > b[j]):
            result_array.append(b[j])
            j = j+1
        else:
            result_array.append(a[i])
            i = i+1
    
    if i<len(a):
        for k in range(i,len(a)):
            result_array.append(a[i])
            
    if j < len(b):
        for k in range(j,len(b)):
            result_array.append(b[j])
            
    count = count+2
    return result_array,count
    


def findIntersection(lists):
    count = 0
    countArr = []
    intersectArray = []
    indexesArray = []
    for index in range(len(lists)):
        indexesArray.append(index)
    for i in lists:
        countArr.append(0)
    while(True):
        try:
            largestArrayIndex = [0]
            smallestValueIndex = []
            largestValue = lists[0][countArr[0]]
            x = range(1,len(lists))
            for r in x:
                count = count +2
                if lists[r][countArr[r]] == largestValue:
                    count = count-1
                    largestArrayIndex.append(r)
                elif lists[r][countArr[r]] > largestValue:
                    smallestValueIndex.extend(largestArrayIndex)
                    largestArrayIndex = [r]
                    largestValue = lists[r][countArr[r]]
                else:
                    smallestValueIndex.append(r)

            if len(smallestValueIndex) == 0:
                intersectArray.append(largestValue)
                for a in range(len(countArr)):
                    countArr[a] = countArr[a]+1
            else:
                for i in smallestValueIndex:
                    countArr[i] = countArr[i]+1
        except Exception:
            return intersectArray, count
            break

    
def DaatAnd(postings):
    intersection_list, count = findIntersection(postings)
    result = ['empty']
    if len(intersection_list) > 0: 
        result = sorted(intersection_list)
    fo.write('\n')
    fo.write('Results:')
    writeToFile(result)
    fo.write('\n')
    fo.write('Number of documents in results: ')
    fo.write(str(len(intersection_list)))
    fo.write('\n')
    fo.write('Number of comparisons: ')
    fo.write(str(count))
    return intersection_list

def writeToFile(list):
    for item in list:
        fo.write(" ")
        if item == []:
            fo.write(empty)
        else:
            fo.write(item)
        
def getPostings(tokens):
    post = []
    for term in tokens:
      fo.write('GetPostings')
      fo.write('\n')
      fo.write(term)
      fo.write('\n')
      fo.write('Postings list:')
      writeToFile(posting_list[term])
      fo.write('\n')
      post.append(posting_list[term])
    fo.write('DaatAnd')
    fo.write('\n')
    for item in tokens:
        fo.write(item)
        fo.write(' ')
    result = DaatAnd(post)
    fo.write('\n')
    fo.write('TF-IDF')
    if len(result) > 0:
     getTfIdf(tokens, result)
    else: 
      fo.write('\n')
      fo.write('Results: empty')
    fo.write('\n')
    fo.write('DaatOr')
    fo.write('\n')
    for item in tokens:
        fo.write(item)
        fo.write(' ')
    result = DaatOr(sorted(post,key=len, reverse=True))
    fo.write('\n')
    fo.write('TF-IDF')
    if len(result) > 0:
     getTfIdf(tokens, result)
    else: 
      fo.write('\n')
      fo.write('Results: empty')
    fo.write('\n')


input = open(sys.argv[3], 'r')
for line in input:
   tokens = line.split()
   getPostings(tokens)
   fo.write('\n')