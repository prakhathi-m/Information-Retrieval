# Information-Retrieval
### Goal:
* To build an inverted index using the information extracted from the given data.
* To implement a Document-at-a-time (DAAT) strategy to return Boolean query results.
* To calculate a TF_IDF score to rank and sort the query results.

### Challenges:
*	Retrieving the postings lists for each of the given query terms.
*	Implementing multi-term boolean AND, OR query on the index using document-at-a-time (DAAT) strategy.
*  Performing TF-IDF scoring of the retrieved results.

Formulas to calculate TF-IDF:

TF(t) = (Number of times term t appears in a document) / (Total number of terms in the document).

IDF(t) = (Total number of documents / Number of documents with term t in it).

TF-IDF(t)  = TF(t) * IDF(t)
