# Studio del Sistema Cruise Control

Il **Cruise Control** è un sistema che permette di mantenere la velocità di un veicolo costante senza l'intervento del conducente. Questo progetto studia il funzionamento di un sistema di **Cruise Control** usando un modello dinamico di **primo ordine**, che tiene conto della **resistenza viscosa** e della **forza motrice**.

## Descrizione del Sistema

Il sistema di Cruise Control regola la velocità di un veicolo in base alla differenza tra la velocità desiderata e quella effettiva. La **forza motrice** generata dal motore è utilizzata per mantenere stabile la velocità del veicolo, compensando le variazioni dovute a fattori come la pendenza della strada e la resistenza al movimento (ad esempio, la resistenza viscosa).

Il sistema è modellato come un sistema dinamico di primo ordine, dove la velocità del veicolo dipende dalla forza motrice e dalla resistenza viscosa. L'analisi di questo sistema aiuta a capire come il controller (ad esempio un controller PID) possa intervenire per mantenere la velocità desiderata.

## Obiettivi del Progetto

1. Studiare come il sistema di Cruise Control mantiene stabile la velocità del veicolo.
2. Analizzare il comportamento dinamico del sistema in risposta alla forza motrice e alla resistenza.
3. Implementare un controller per regolare la velocità del veicolo e mantenerla costante.

## Conclusioni

Lo studio del sistema di Cruise Control come sistema retroazionato di **primo ordine** consente di comprendere le dinamiche che governano il controllo della velocità di un veicolo. Questo progetto fornisce una base per progettare sistemi di controllo avanzati in scenari reali.