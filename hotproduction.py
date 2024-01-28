import numpy as np
#Vocabulary
def hotproductionVocabulary(txt):
    #compile a vector with a row for each new word
    words = txt.split(" ")
    veclst = np.array([])
    for i in range(len(words)):
        if words[i] in veclst:
            veclst[veclst.index(words[i])] += 1
        else:
            veclst.append(words[i])
    vector = np.zeros((0, len(veclst)))
    for i in range(len(veclst)):
        vector[0][i].append(veclst[i])
    return veclst

def hotproductionPlace(txt):
    #compiles a vector with a row for each word in the text, unique words(words )
    words = txt.split(" ")
    veclst = np.array([])
    for i in range(len(words)):
        if words[i] in veclst:
            veclst[veclst.index(words[i])] += 1
        else:
            veclst.append(words[i])
        
    vector = np.zeros((0, len(words)))
    for i in range(len(words)):
    vector[0][i] = veclst.index(words[i])
        
    
    
    
            
            
    
    