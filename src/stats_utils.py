import statistics


def calculer_etendue(liste_nombres):
    """Retourne l'étendue d'une liste de nombres (valeur max - valeur min)."""
    return max(liste_nombres) - min(liste_nombres)


def analyser_ventes(transactions):
    """Analyse une liste de montants de ventes (en euros).

    Les montants négatifs ou nuls sont ignorés (erreurs de saisie).
    Retourne un dictionnaire d'indicateurs statistiques, ou un
    dictionnaire d'erreur si aucune vente n'est valide.
    """
    # Nettoyage : on garde uniquement les montants strictement positifs
    ventes_valides = []
    for montant in transactions:
        if montant > 0:
            ventes_valides.append(montant)

    # Cas limite : sans vente valide, mean(), min() et max() planteraient
    if not ventes_valides:
        return {"Erreur": "Aucune transaction valide"}

    nombre = len(ventes_valides)
    somme = sum(ventes_valides)
    moyenne = statistics.mean(ventes_valides)
    mediane = statistics.median(ventes_valides)

    # pstdev = écart-type de la POPULATION (division par n).
    # Pour un écart-type d'échantillon (division par n-1), utiliser stdev.
    ecart_type = statistics.pstdev(ventes_valides)

    # Anomalies : montants supérieurs à 2 fois la moyenne
    seuil = moyenne * 2
    anomalies = []
    for montant in ventes_valides:
        if montant > seuil:
            anomalies.append(montant)

    resultat = {
        "Nombre total de transactions valides": nombre,
        "Somme totale des ventes": somme,
        "Moyenne": moyenne,
        "Médiane": mediane,
        "Écart-type": ecart_type,
        "Minimum": min(ventes_valides),
        "Maximum": max(ventes_valides),
        "Étendue": calculer_etendue(ventes_valides),
        "Seuil d'anomalie": seuil,
        "Anomalies": anomalies,
    }
    return resultat


def afficher_rapport(rapport):
    """Affiche le rapport de façon lisible (colonnes alignées, 2 décimales)."""
    print("=== RAPPORT D'ANALYSE DES VENTES ===")
    for nom, valeur in rapport.items():
        if isinstance(valeur, float):
            valeur = round(valeur, 2)
        print(f"{nom:<40} : {valeur}")


if __name__ == "__main__":
    # Jeu de test avec erreurs (-5, 0) et une valeur extrême (300)
    ventes_test = [10, 20, -5, 0, 30, 40, 300]
    afficher_rapport(analyser_ventes(ventes_test))

    # Cas limite : aucune vente valide
    print()
    afficher_rapport(analyser_ventes([-5, 0]))