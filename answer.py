import os, sys
os.environ['CLASSPATH'] = '/home/Aaditya/assignments/Project/stanford-parser-full-2015-12-09/'

from nltk.parse.stanford import StanfordParser
parser = StanfordParser()


question = sys.argv[1].strip('?').lower()
tree = list(parser.parse(question.split()))[0]

person = ' '.join(list(tree.subtrees(filter = lambda x: x.label() =='NP'))[0].leaves()).lower()

l = list(tree.subtrees(filter = lambda x: x.label() =='VP'))
if len(l) == 0 and 'who' in question:
    what = 'who'
else:
    what = ' '.join(l[0].leaves()).lower()

print(person) 
print(what)

from get_results import query

if 'star' in what or 'appear' in what:
    sparql = open('./films.sparql').read()
    sparql = sparql.replace('[[name]]',person)
    query(sparql)
elif what == 'who' or 'tell' in what:
    sparql = open('./about.sparql').read()
    sparql = sparql.replace('[[name]]',person)
    query(sparql)
elif what == 'born' or 'birth' in what:
    sparql = open('./birth.sparql').read()
    sparql = sparql.replace('[[name]]',person)
    query(sparql)
