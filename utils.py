import nltk


def get_paths(input_folder):
    """returns a list of file paths 
    
    Args: 
        a path to a folder in which the files are stores 
        
    Returns: 
        a list of file paths to the files inside the folder
    """
    
    import glob
    list_1 = []
    
    for i in glob.glob(f'{input_folder}/*.txt'):
        list_1.append(i)
        
    return list_1



def get_basic_stats(txt_path):
    
    """returns text information of each book in a dictioanry
    Args: 
        a text path to a file 
    Returns:
        a ditionary with book as keys and variables such as token_count, sentence_count, the size of the dictionary, number of chapters, and the 30 most frequently used words, as values  
    """
    
    import nltk
    import operator 
    
    Nouns = 'Chapter', 'CHAPTER' , 'ACT'
    list_2 = []
    counts = dict()
    counts_list = []
    
    with open(txt_path, 'r') as infile:
        infile = open(txt_path, 'r')
        text = infile.read()
    
    sent = nltk.sent_tokenize(text)
    tokens = nltk.word_tokenize(text)
    uniques = set(tokens)
    
    for token in tokens: 
        if token in Nouns:
            list_2.append(token)
            
    for token in tokens: 
        if token in counts:
            counts[token] += 1
        else: 
            counts[token] = 1

    for token, freq in sorted(counts.items(), 
                          key=operator.itemgetter(1),
                          reverse=True):
        counts_list.append(token)
        commons = counts_list[:30]
    
    dict_val = [len(sent), len(tokens), len(uniques), len(list_2), commons]
    dict_key = ['num_sents', 'num_tokens', 'vocab_size', 'num_chapters_or_acts','top_30_tokens']
        
    final_dict = {dict_key[i]: dict_val[i] for i in range(len(dict_key))}
    return final_dict
