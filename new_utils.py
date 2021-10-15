from lxml import etree

def get_tokens(path_to_doc):
    tree = etree.parse(path_to_doc)
    root = tree.getroot()
    tags = root.findall("xdrs/taggedtokens/tagtoken")
    return tags


def get_token_pos(token_element):
    tags = token_element.findall("tags/tag")
    for tag in tags: 
        if tag.get("type") == "tok":
            tag_token = tag.text
        elif tag.get("type") == "pos":
            tag_pos = tag.text
    return tag_token, tag_pos


def get_doc_text(path_to_doc):
    doc_tree = etree.parse(path_to_doc)
    root = root = doc_tree.getroot()
    tags = root.findall("xdrs/taggedtokens/tagtoken/tags/tag")
    token_list = []
    for tag in tags: 
        if tag.get("type") == "tok":
            tag_token = tag.text
            token_list.append(tag_token)
    token_string = " ".join(token_list)
    return token_string


import glob 
import os 

def sort_documents(path_pmb):
    #unpack the gold folder with glob
    en_set = set()
    it_set = set()
    de_set = set()
    nl_set = set()
    for folder1 in glob.glob(f"{path_pmb}/*"):
        for folder in glob.glob(f"{folder1}/*"):
            for file in glob.glob(f"{folder}/*"):
                f_name = os.path.basename(file)
                name = f_name.split(".")
                if name[0] == "en":
                    folder = folder.replace("\\", "/")
                    en_set.add(folder)
                elif name[0] == "it":
                    folder = folder.replace("\\", "/")
                    it_set.add(folder)
                elif name[0] == "de":
                    folder = folder.replace("\\", "/")
                    de_set.add(folder)
                elif name[0] == "nl":
                    folder = folder.replace("\\", "/")
                    nl_set.add(folder)
        
            
    d = {}
    d["en"] = en_set
    d["it"] = it_set
    d["de"] = de_set
    d["nl"] = nl_set
    
    return d 

def get_pairs(language_list):
    """Given a list, return a list of tuples of all element pairs."""
    pairs = []
    for l1 in language_list:
        for l2 in language_list:
            if l1 != l2:
                if (l1, l2) not in pairs and (l2, l1) not in pairs:
                    pairs.append((l1, l2))
    return pairs


