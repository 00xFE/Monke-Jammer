# Monke Traffic Generator

Questo script Python consente di generare traffico testuale verso un insieme di indirizzi IP all'interno di un determinato CIDR. Il traffico testuale è generato casualmente da una pool di curiosità sulle scimmie.

## Requisiti

* Python 3.x
* Librerie standard: `random`, `socket`, `sys`

## Utilizzo

1. Esegui lo script `monke-jammer.py` utilizzando Python.
2. Segui le istruzioni visualizzate a schermo.

All'avvio dello script, verrà richiesto di inserire il CIDR di destinazione nel formato "x.x.x.x/x". Successivamente, verrà richiesto di specificare le porte dei servizi separandole con una virgola, infine sarà richiesto il numero di squadre partecipanti.

Il programma genererà quindi traffico testuale alle porte specificate verso tutti gli indirizzi IP all'interno del CIDR. Verrà utilizzato il terzo ottetto dell'indirizzo IP come variabile, andando da 1 al numero di squadre in gioco.

## Personalizzazione

Puoi modificare la pool di curiosità sulle scimmie aggiungendo o rimuovendo elementi dalla lista `monkey_curiosities` all'interno dello script. Per aumentare l'efficacia del monke jammer aggiungere dei pattern di attacco ai servizi verosimili per depistare gli avversari. Assicurati che le curiosità siano racchiuse tra virgolette e separate da virgole.

```
monkey_curiosities = [
    "Le scimmie sono intelligenti e possono imparare a utilizzare strumenti.",
    "Ci sono oltre 260 specie di scimmie nel mondo.",
    "Le scimmie sono molto sociali e vivono in gruppi chiamati bande.",
    ...
]
```

## Attenzione

Assicurati di utilizzare questo script solo per scopi legittimi e all'interno dei limiti consentiti dalla legge. Non utilizzare questo script per generare traffico non autorizzato o dannoso verso indirizzi IP o porte che non ti appartengono.

L'autore di questo script non è responsabile dell'uso improprio o illecito dello stesso.
