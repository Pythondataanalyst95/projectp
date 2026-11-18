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

#Il mese più caro e il mese più economico, con il nome del mese.

max=max(spese)
print("Il massimo è", max)
for i in range(len(spese)):
    if max==spese[i]:
        print("Il mese massimo di spesa è", mesi[i], "con spesa di", spese[i])
        
min=min(spese)
print("Il minimo è", min)
for i in range(len(spese)):
    if min==spese[i]:
        print("Il mese minimo di spesa è", mesi[i], "con spesa di", spese[i])
        
#Quanti mesi sono sopra il budget, con la funzione conta_sopra dell'esercizio "Conta sopra soglia".
g=0
for i in range(len(spese)):
    if spese[i]>budget:
        g=g+1
print("Il numero di mesi sforati è", g)

#Di quanto avete sforato o risparmiato sull'anno, rispetto a 12 volte il budget.
sfor=sum(spese)-12*900
print("Budget sforato di", sfor)
    
#Il budget chiesto all'utente con input , invece che scritto nel codice.
x=int(input("inserisci budget mensile: "))
sfora=sum(spese)-12*x
if sfora>0:
    print("Budget sforato di", sfora)
else:
    sfora=-sfora
    print("Budget positivo di", sfora)
