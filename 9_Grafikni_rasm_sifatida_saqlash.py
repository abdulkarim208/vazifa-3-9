import matplotlib.pyplot as plt

kunlar = [1, 2, 3, 4, 5, 6, 7]
masofa = [2, 3, 2.5, 4, 4.5, 5, 6]

plt.plot(kunlar, masofa, color="green", marker="o")

plt.title("Haftalik sport natijalari")
plt.xlabel("Kunlar")
plt.ylabel("Masofa (km)")

plt.grid()

plt.savefig("natija.png")
plt.show()