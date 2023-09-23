from moy_mat import *
import json

def somme_coef(modules, module):
    somme = 0
    for mat in modules[module]:
        somme += modules[module][mat]
    return somme

def moyenne_semester(resultat):
    moy = 0
    for module in resultat:
        moy += resultat[module]["moyenne_panier"] / len(resultat)
    return moy

def print_results(results):
    for module in results:
        print("Module: ",module)
        for elm in results[module]:
            print(elm, " : ", results[module][elm])

def fetch_note(file, module, matiere):
    with open(file, "r") as read_file:
        data = json.load(read_file)
        return moy_mat(data[module][matiere]["ds"], data[module][matiere]["exam"])


modules = {
    "scf1": {
        "math": 2,
        "syslog": 2
    },
    "reseau-sys": {
        "reseau": 2,
        "linux": 2
    },
    "algo-prog": {
        "algo": 2,
        "progC": 2
    },
    "sys-info": {
        "htmlcss": 1,
        "bd": 2,
        "cloud": 2
    },
    "langues": {
        "tech-com": 1,
        "eng": 1
    }
}
resultat = {}

def calcul_semester():
    for module in modules:
        resultat[module] = {}
        moyenne = 0
        
        resultat[module]["moyenne_panier"] = 0
        for mat in modules[module]:
        
            # ds, exam = saisir()
            # moy_matiere = moy_mat(ds, exam)
            moy_matiere = fetch_note("adel.json", module, mat)
            resultat[module][mat] = moy_matiere
            moyenne += moy_matiere
            resultat[module]["moyenne_panier"] += moy_matiere * modules[module][mat] / somme_coef(modules, module)
        
calcul_semester()
print("-------------------------------")
print("Moyenne semester:", moyenne_semester(resultat))
print_results(resultat)


