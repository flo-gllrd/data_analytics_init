import statistics
def analyser_ventes(transactions):
    ventes_valides = []
    for montant in transactions:
        if montant > 0:
            ventes_valides.append(montant)
    nombre = len(ventes_valides)
    somme = sum(ventes_valides)
    moyenne = statistics.mean(ventes_valides)
    mediane = statistics.median(ventes_valides)
    ecart_type = statistics.pstdev(ventes_valides)
    anomalies = []
    for montant in ventes_valides:
        if montant >  moyenne * 2:
            anomalies.append(montant)    
    resultat = {
        "Nombre total de transactions valides": nombre,
        "Somme totale des ventes": somme,
        "Moyenne": moyenne,
        "Médiane": mediane,
        "Ecart-type": ecart_type,
        "minimum": min(ventes_valides),
        "Maximum": max(ventes_valides),
        "Anomalies": anomalies
    }
    return resultat


ventes_test = [10, 20, -5, 0, 30, 40]
rapport = analyser_ventes(ventes_test)
for nom, valeurs in rapport.items():
    print(nom, ":", valeurs)
