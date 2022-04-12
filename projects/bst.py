import ssl
from urllib.request import urlopen


def caractère(chaine):
    liste1 = ["à", "â", "ä", "A", "B", "ç", "C", "D", "é", "è", "ê", "ë", "E", "î", "ï", "ô", "ö", "ù", "û", "ü", "ÿ",
              "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "œ"]
    liste2 = ["a", "a", "a", "a", "b", "c", "c", "d", "e", "e", "e", "e", "e", "i", "i", "o", "o", "u", "u", "u", "y",
              "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "oe"]
    for a, b in zip(liste1, liste2):
        chaine = chaine.replace(a, b)  # remplace a par b
    return(chaine)


def ABR(res_lignes):
    arbre = []
    arbre.append([res_lignes.pop(0), None, None])

    for i in res_lignes:
        indice_comparaison = 0
        côté = 0
        while indice_comparaison != None:
            save = indice_comparaison
            if caractère(i) > caractère(arbre[indice_comparaison][0]):
                indice_comparaison = arbre[indice_comparaison][2]
                côté = "droite"
            else:
                indice_comparaison = arbre[indice_comparaison][1]
                côté = "gauche"
        if côté == "droite":
            arbre[save][2] = len(arbre)
        else:
            arbre[save][1] = len(arbre)
        arbre.append([i, None, None])
    return (arbre)


def liste(fichier):

    contenu = []

    f = open(fichier, "r", encoding='utf-8')

    res_lignes = []
    contenu = f.readlines()
    for ligne in contenu:
        res_lignes.append(ligne.rstrip('\n'))
    return res_lignes


def ajouterfichier(fichier, arbre=None):
    if arbre == None:
        return (ABR(liste(fichier)))
    else:
        # si l'arbre est déja créé (arbre != None)
        f = open(fichier, "r", encoding='utf-8')
        l = f.readline().rstrip("\n")
        while l != "":  # si on arrive a la fin du fichier
            ajouter(arbre, l)
            l = f.readline().rstrip("\n")
    return (arbre)


# res = ajouterfichier("/tmp/words.txt")
# print(res)
URL = "https://raw.githubusercontent.com/devw/spen/main/projects/words.txt"


def get_words(url=URL):
    response = urlopen(url, context=ssl._create_unverified_context())
    words = response.read().decode('utf-8').split("\n")
    return [word.lower() for word in words if word != '']


def get_label(node):
    return node[0]


def get_tree(words):
    tree = []

    if words == []:
        return tree

    tree.append([words.pop(0), None, None])

    for word in words:
        node_index = 0
        side = None
        while node_index != None:
            last_node_index = node_index
            if word > get_label(tree[node_index]):
                node_index = tree[node_index][2]
                side = "right"
            else:
                node_index = tree[node_index][1]
                side = "left"

        if side == "right":
            tree[last_node_index][2] = len(tree)
        else:
            tree[last_node_index][1] = len(tree)

        tree.append([word, None, None])

    return (tree)


words = get_words()
print(words)
tree = get_tree(words)
print(tree)
