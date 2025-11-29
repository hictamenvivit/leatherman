# coding: utf-8

def make_blank(word):
    return "_" * len(word)
    
lyrics = """Un grand soleil noir tourne sur la vallée
Cheminées muettes, portails verrouillés
Wagons immobiles, tours abandonnées
Plus de flamme orange dans le ciel mouillé
On dirait la nuit de vieux châteaux forts
Bouffés par les ronces le gel et la mort
Un grand vent glacial fait grincer les dents
Monstre de métal qui va dérivant
Refrain :
J'voudrais travailler encore, travailler encore
Forger l'acier rouge avec mes mains d'or
Travailler encore, travailler encore
Acier rouge et mains d'or
J'ai passé ma vie là, dans ce laminoir
Mes poumons mon sang et mes colères noires
Horizons barrés là, les soleils très rares
Comme une tranchée rouge saignée sur l'espoir
On dirait le soir des navires de guerre
Battus par les vagues rongés par la mer
Tombés sur le flan giflés des marées
Vaincus par l'argent les monstres d'acier
Refrain
J'peux plus exister là, j'peux plus habiter là
Je sers plus à rien moi, y'a plus rien à faire
Quand je fais plus rien moi, je coûte moins cher
Que quand je travaillais moi, d'après les experts
J'me tuais à produire pour gagner des clous
C'est moi qui délire ou qui devient fou
J'peux plus exister là, j'peux plus habiter là
Je sers plus à rien moi, y'a plus rien à faire"""
lines = lyrics.split("\n")
from shuffle import choixe
from shuffle import choice
from random import choice
def modified_line(line):
    indexes = [choice(range(len(line))) for _ in range(3)]
    return " ".join([make_blank(x) if i in indexes else x for (i, x) in enumerate(line.split(" "))])
    
modified_line(lines[0])
def modified_line(line):
    indexes = [choice(range(len(line))) for _ in range(3)]
    print(indexes)
    return " ".join([make_blank(x) if i in indexes else x for (i, x) in enumerate(line.split(" "))])
    
modified_line(lines[0])
def modified_line(line):
    indexes = [choice(range(len(line.split(" ")))) for _ in range(3)]
    print(indexes)
    return " ".join([make_blank(x) if i in indexes else x for (i, x) in enumerate(line.split(" "))])
    
modified_line(lines[0])
modified_line(lines[0])
de
def choose_indexes(line, n=3):
    return sample([i for (i, e) in enumerate(line.split(" ")) if len(e) > 3])
    
    
from random import sample
def choose_indexes(sline, n=3):
    return sample([i for (i, e) in enumerate(sline) if len(e) > 3])
    
lines[0]
sline = lines[0].split(" ")
choose_indexes(sline)
def choose_indexes(sline, n=3):
    return sample([i for (i, e) in enumerate(sline) if len(e) > 3], n)
    
choose_indexes(sline)
lines
def modified_line(line):
    sline = line.split(" ")
    indexes = choose_indexes(sline)
    return " ".join([make_blank(x) if i in indexes else x for (i, x) in enumerate(sline)])
    
modified_line(lines[0])
print("\n".join([modified_line(x) for x in lines]))
def choose_indexes(sline, n=3):
    try:
        return sample([i for (i, e) in enumerate(sline) if len(e) > 3], n)
    except ValueError:
        return choose_indexes(sline, n-1)
        
def modified_line(line):
    sline = line.split(" ")
    indexes = choose_indexes(sline)
    return " ".join([make_blank(x) if i in indexes else x for (i, x) in enumerate(sline)])
    
print("\n".join([modified_line(x) for x in lines]))
import pyperclip
song_holes = "\n".join([modified_line(x) for x in lines])
pyperclip.copy(song_holes)
get_ipython().run_line_magic('pwd', '')
get_ipython().run_line_magic('cd', '')
get_ipython().run_line_magic('cd', 'PycharmProjects/perso/utils/leatherman/leatherman/teach_french/')
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('save', 'blank_text.py 0-100')
get_ipython().run_line_magic('save', 'blank_textEE.py 0-100')
