from new_utils import sort_documents, get_tokens, get_pairs, get_doc_text

my_path = "/Users/elena/OneDrive/Desktop/python-for-text-analysis-master/python-for-text-analysis-master/Data/"
path_pmb = f"{my_path}PMB/pmb-2.1.0/data/gold"
language_doc_dict = sort_documents(path_pmb)

languages = ["en", "it", "de", "nl"]

for language in languages:
    n_docs = len(language_doc_dict[language])
    docs = language_doc_dict[language]
    num_tokens = []
    for doc in docs:
        path_to_doc = f"{doc}/{language}.drs.xml"
        tokens = get_tokens(path_to_doc) 
        for tok in tokens:
            num_tokens.append(tok)
            n_tokens = len(num_tokens)
            #for tag in tok.findall("tags/tag"):
                #if tag.get("type") == "tok":
                    #num_tokens.append(tag)
                    #n_tokens = len(num_tokens)
    print(f"{language}: num docs: {n_docs}, num tokens: {n_tokens}")
        
language_list = ["en", "it", "de", "nl"]
pairs = get_pairs(language_list)

import os
for lang1, lang2 in pairs: 
    docs_lang1 = language_doc_dict[lang1]
    docs_lang2 = language_doc_dict[lang2]
    set_docs1 = set()
    set_docs2 = set()
    for doc1 in docs_lang1:
        set_docs1.add(doc1)
    for doc2 in docs_lang2:
        set_docs2.add(doc2)
    set_docs = set_docs1.intersection(set_docs2)
    n_documents = len(set_docs)

    #print(f"Coverage for parallel data in {lang1} and {lang2}: {n_documents}")

from lxml import etree
import glob 

input_lang1 = input("Choose one language between en, it, de, nl: ")
input_lang2 = input("Choose a seconde language between en, it, de, nl: ")

setl1 = set()
setl2 = set()
my_lang = []

for lang1, lang2 in pairs:
    my_lang.append(lang1)
    my_lang.append(lang2)
    if lang1 == input_lang1:
        docsl1 = language_doc_dict[lang1]
        for d1 in docsl1:
            setl1.add(d1)
    if lang2 == input_lang2:
        docsl2 = language_doc_dict[lang2]
        for d2 in docsl2:
            setl2.add(d2)
    set_docs_l = setl1.intersection(setl2)
for lang in my_lang:
    for d in set_docs_l:
        doc_files = glob.glob(f"{d}/{lang}.drs.xml")
        for d1 in doc_files:
            doc_text = get_doc_text(d1) 
            print(doc_text)
            input_continue = input("Do you want to continue? yes/no ")
        if input_continue == "yes":
            continue 
        else: 
            break 
    else: 
        continue 
    break  
            
                
     
    
        