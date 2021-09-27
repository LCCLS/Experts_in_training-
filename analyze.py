import nltk
import glob
import os
from utils import get_paths
from utils import get_basic_stats

var1 = get_paths(input_folder="../Data/books")
book2stats = {}

for i in var1: 
    
    basename = os.path.basename(i)
    book = basename.strip('.txt')
    info = get_basic_stats(i)
    book2stats.update({book:info})
    
print(book2stats)