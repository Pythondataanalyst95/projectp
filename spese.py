#Riscrivete il programma dell'inizio, da zero, senza guardarlo. Questi sono i dati:

mesi = ["gen", "feb", "mar", "apr", "mag", "giu", "lug", "ago", "set", "ott", "nov", "dic"]
spese = [820, 760, 910, 700, 680, 1250, 890, 1420, 730, 770, 800, 1100]
budget = 900
#Il programma deve stampare i mesi sopra il budget, il totale dell'anno e la media mensile con due decimali.

a=0
for a in range(len(spese)):
        print(mesi[a], spese[a])
        a=a+1

for i in range(len(spese)):
    if spese[i]>budget:
        print("mesi budget sforato", mesi[i], spese[i])


mean=sum(spese)/12
round(mean,)

print("Il totale è", sum(spese))
print("La media è", mean )
