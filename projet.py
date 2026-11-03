"""
🎲 JEU DU JUSTE PRIX - Devine le nombre mystère !
Par Thomas GOBERT

Un petit jeu fun qui utilise les notions du Mémento Python :
- Conditions (if/elif/else)
- Boucles (while, for)
- Input/Output
- Module random
- Gestion d'erreurs
- Listes et scores
"""

import random

print("=" * 40)
print("   🎲 BIENVENUE AU JEU DU JUSTE PRIX ! 🎲")
print("=" * 40)
print("Je pense à un nombre entre 1 et 100...")
print("À toi de le deviner en un minimum d'essais !\n")

# Variable pour le score (liste des tentatives)
scores = []

# Boucle principale du jeu
rejouer = "o"

while rejouer == "o":
    # Génération du nombre mystère
    nombre_mystere = random.randint(1, 100)
    essais = 0
    trouve = False

    print("\n🎯 Nouvelle partie ! J'ai choisi mon nombre...")

    # Boucle de devinette
    while not trouve:
        try:
            proposition = int(input("Ton choix : "))
            essais += 1

            if proposition < 1 or proposition > 100:
                print("⚠️  Choisis un nombre entre 1 et 100 !")
                essais -= 1  # On ne compte pas cet essai
            elif proposition < nombre_mystere:
                print("📈 C'est PLUS grand !")
            elif proposition > nombre_mystere:
                print("📉 C'est PLUS petit !")
            else:
                print(f"\n🎉 BRAVO ! Trouvé en {essais} essai(s) !")
                trouve = True
                scores.append(essais)

        except ValueError:
            print("❌ Entre un nombre valide !")

    # Demander si on rejoue
    rejouer = input("\nRejouer ? (o/n) : ").lower().strip()

# Afficher les statistiques finales
print("\n" + "=" * 40)
print("📊 STATISTIQUES DE TA SESSION")
print("=" * 40)

if scores:
    print(f"Parties jouées : {len(scores)}")
    print(f"Meilleur score : {min(scores)} essai(s)")
    print(f"Pire score : {max(scores)} essai(s)")
    print(f"Moyenne : {sum(scores) / len(scores):.1f} essais")

    # Classement des parties
    print("\n🏆 Classement de tes parties :")
    for i, score in enumerate(sorted(scores), 1):
        print(f"   {i}. {score} essais")

print("\n👋 Merci d'avoir joué ! À bientôt !")
