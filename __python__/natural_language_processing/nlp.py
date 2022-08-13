from nltk.parse.stanford import StanfordParser

sentence = "The quick brown fox jumps over the lazy dog"

# create parser object
scp = StanfordParser(path_to_jar="E:/stanford/stanford-parser-full-2015-04-20/stanford-parser.jar",
                     path_to_models_jar="E:/stanford/stanford-parser-full-2015-04-20/stanford-parser-3.5.2-models.jar")

# get parse tree
result = list(scp.raw_parse(sentence))
tree = result[0]
# print parse tree
print(tree)
