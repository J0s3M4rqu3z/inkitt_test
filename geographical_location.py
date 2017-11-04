import nltk

teaser="A MET detective investigates a mysterious party which occurs in a New York North Avenue suburb. His only hope is that he can save the lives (even if they are dead already) of those inside before time runs out"

sent = nltk.tokenize.wordpunct_tokenize(teaser)
words_tagging = nltk.pos_tag(sent)
chunks = nltk.ne_chunk(pos_tag)
Geographical_locations = []
for chunk in chunks:
    if type(chunk) is nltk.tree.Tree:
        if (chunk.label() == 'GPE'):
            Geographical_locations.append(u' '.join([i[0] for i in chunk.leaves()]))
            print(chunk.leaves())
print(Geographical_locations)
