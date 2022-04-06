def caractère(chaine):
    liste1 = ["à", "â", "ä", "A", "B", "ç", "C", "D", "é", "è", "ê", "ë", "E", "î", "ï", "ô", "ö", "ù", "û", "ü", "ÿ", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","œ"]
    liste2 = ["a", "a", "a", "a", "b", "c", "c", "d", "e", "e", "e", "e", "e", "i", "i", "o", "o", "u", "u", "u", "y", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","oe"]
    for a,b in zip(liste1,liste2):
        chaine=chaine.replace(a,b) #remplace a par b
    return(chaine)



def ABR(res_lignes):
    arbre=[]
    arbre.append([res_lignes.pop(0),None,None])
      
    for i in res_lignes:
        indice_comparaison = 0
        côté = 0
        while indice_comparaison != None:
            save = indice_comparaison
            if caractère(i)>caractère(arbre[indice_comparaison][0]): 
                indice_comparaison = arbre[indice_comparaison][2] 
                côté = "droite"
            else:
                indice_comparaison = arbre[indice_comparaison][1]
                côté = "gauche"
        if côté == "droite":
            arbre[save][2] = len(arbre)
        else:
            arbre[save][1] = len(arbre)
        arbre.append([i, None,None])
    return (arbre)

def liste(fichier):
    
    contenu = []
    
    f = open(fichier,"r",encoding='utf-8')
    
    res_lignes = []
    contenu = f.readlines()
    for ligne in contenu:
        res_lignes.append(ligne.rstrip('\n'))
    return res_lignes

def ajouterfichier(fichier,arbre = None):
    if arbre == None:
        return (ABR(liste(fichier)))
    else:
        f = open(fichier,"r",encoding='utf-8')#si l'arbre est déja créé (arbre != None)
        l = f.readline().rstrip("\n")
        while l != "":# si on arrive a la fin du fichier
            ajouter(arbre,l)
            l = f.readline().rstrip("\n")
    return (arbre)
        
res = ajouterfichier("/tmp/words.txt")
print(res)

def get_data(fName):
    f = open(fName,"r", encoding='utf-8')
    return f.readlines()

def get_words(data):
    words = []
    for word in data:
        words.append(word.rstrip())
    return words

def get_tree(words):
    arbre=[]
    arbre.append([words.pop(0),None,None])
      
    for i in words:
        indice_comparaison = 0
        côté = 0
        while indice_comparaison != None:
            save = indice_comparaison
            if caractère(i)>caractère(arbre[indice_comparaison][0]): 
                indice_comparaison = arbre[indice_comparaison][2] 
                côté = "droite"
            else:
                indice_comparaison = arbre[indice_comparaison][1]
                côté = "gauche"
        if côté == "droite":
            arbre[save][2] = len(arbre)
        else:
            arbre[save][1] = len(arbre)
        arbre.append([i, None,None])
    return (arbre)

def main():
    fName = '/tmp/words.txt' 
    data = get_data(fName)
    words = get_words(data)
    tree = get_tree(words)
    return tree

res = main()
print(res)
