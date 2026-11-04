import random

print("=" * 40)
print("BIENVENUE AU JEU DU JUSTE PRIX !")
print("=" * 40)
print("Je pense à un nombre entre 1 et 100...")
print("À toi de le deviner en un minimum d'essais !\n")

scores = []

rejouer = "o"

while rejouer == "o":
    # Génération du nombre mystère
    nombre_mystere = random.randint(1, 100)
    essais = 0
    trouve = False

    print("\nNouvelle partie ! J'ai choisi mon nombre...")

    while not trouve:
        try:
            proposition = int(input("Ton choix : "))
            essais += 1

            if proposition < 1 or proposition > 100:
                print("Choisis un nombre entre 1 et 100 !")
                essais -= 1  # On ne compte pas cet essai
            elif proposition < nombre_mystere:
                print("C'est PLUS grand !")
            elif proposition > nombre_mystere:
                print("C'est PLUS petit !")
            else:
                print(f"\nBRAVO ! Trouvé en {essais} essai(s) !")
                trouve = True
                scores.append(essais)

        except ValueError:
            print("Entre un nombre valide !")

    rejouer = input("\nRejouer ? (o/n) : ").lower().strip()

print("\n" + "=" * 40)
print("STATISTIQUES DE TA SESSION")
print("=" * 40)

if scores:
    print(f"Parties jouées : {len(scores)}")
    print(f"Meilleur score : {min(scores)} essai(s)")
    print(f"Pire score : {max(scores)} essai(s)")
    print(f"Moyenne : {sum(scores) / len(scores):.1f} essais")

    print("\nClassement de tes parties :")
    for i, score in enumerate(sorted(scores), 1):
        print(f"   {i}. {score} essais")

print("\nMerci d'avoir joué ! À bientôt !")
