from whoosh.index import create_in
from whoosh.fields import *
from whoosh.qparser import QueryParser
from whoosh.index import open_dir
import csv


# schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT(stored=True))
# ix = create_in("index/", schema)
# writer = ix.writer()

f = open('test.csv', 'rb')
o = open('outputFile.txt','w')

reader = csv.reader(f)
jokenum = 0
for row in reader:
    joke = unicode(row[1].decode('utf-8').strip())
    # joke2 = row[1].rstrip('\n')
    joke2 = str(row[1]).replace('\n',' ')
    joke2 = joke2.replace('"',"'")
    print jokenum
    jokenum+=1
    joketitle = unicode("joke" + str(jokenum))

    o.write('[sharedIndex indexObject:@"'+joke2+'"];'+'\n')
    # writer.add_document(title=joketitle, path=u"/a", content=joke)
f.close()

o.close()

# writer.add_document(title=u"First document", path=u"/a", content=u"This is the first document we've added!")
# writer.add_document(title=u"Second document", path=u"/b", content=u"The second one is even more interesting!")
# writer.commit()

# ix = open_dir("index")


# print 
# print 
# print
# with ix.searcher() as searcher:
#     query = QueryParser("content", ix.schema).parse("abortion")
#     results = searcher.search(query)
#     for hit in results:
#     	print hit["content"]
#     	# print hit.docnum
#     	print "------------------------"
#     	f.write('hi there\n')



