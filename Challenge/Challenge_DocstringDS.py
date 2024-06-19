#C'est un challenge de niveau débutant qui a été proposer sur le discord de Docstring ! Le discord de mon formateur.
#Les note des élève
notes_brut = """Tao     -> 18, 12, 3, 5, 19
Josette -> 20, 2, 12, 18, 14
Patrick -> 2, 4, 6, 18, 17
Pema    -> 3, 19, 15, 3, 12
Jean    -> 0, 9, 8, 8, 4
Bixente -> 14, 20, 10, 12, 4
Paco    -> 16, 1, 1, 1, 20
Chuluun -> 15, 6, 17, 20, 15
Marie   -> 16, 4, 16, 20, 12
Mohamed -> 16, 19, 17, 6, 20"""
#Transformation des notes brut en dictionnaire
notes = {}
lines = notes_brut.split('\n')
for str in lines:
    name, notes_str = str.split('->')
    name = name.strip()
    scores = list(map(int, notes_str.split(',')))
    notes[name] = scores
#Création de la moyenne et des résultats séparer 
resultats = []
for name, select in notes.items():
    moyenne = sum(select) / len(select)
    moyenne = round(moyenne)
    resultats.append((name, moyenne))
#Tri et affichage des résultats 
resultats =  sorted(resultats, key=lambda x: x[1], reverse=True)
resultats_final = "\n".join([f"{index}. {name} {moyenne}" for index, (name, moyenne) in enumerate(resultats, 1)])

print(resultats_final)
