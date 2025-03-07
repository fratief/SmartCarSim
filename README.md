# Studio del Sistema Cruise Control

Il sistema **Cruise Control** (controllo automatico della velocità) è un esempio pratico di sistema retroazionato, progettato per mantenere la velocità costante di un veicolo senza l'intervento diretto del conducente. Questo progetto esplora la modellazione del sistema di Cruise Control utilizzando un modello dinamico del **primo ordine**, che tiene in considerazione la **resistenza viscosa** e la **forza motrice** fornita dal motore, regolata da un controller (ad esempio un controller PID).

## Modello Dinamico

Il comportamento del veicolo è descritto dall'equazione dinamica:

\[
M \frac{dv(t)}{dt} = F_m(t) - b v(t)
\]

Dove:
- M è la massa del veicolo,
- v(t) è la velocità del veicolo,
- F_m(t) è la forza motrice (controllata dal sistema Cruise Control),
- b è il coefficiente della resistenza viscosa, che è proporzionale alla velocità del veicolo.

## Funzione di Trasferimento

La funzione di trasferimento del sistema, che descrive il comportamento dinamico in frequenza, è data da:

\[
G(s) = \frac{V(s)}{F_m(s)} = \frac{1}{Ms + b}
\]

Questa è una funzione di trasferimento di **primo ordine**, il che significa che la risposta del sistema alla forza motrice è caratterizzata da una costante di tempo \tau = \frac{M}{b}.

## Ruolo del Controller

Il **controller** (ad esempio, un controller PID) agisce sulla forza motrice F_m(t) in risposta alla differenza tra la velocità desiderata v_d(t) e la velocità attuale v(t), mantenendo la velocità del veicolo stabile. Il feedback del sistema permette di adattarsi alle variazioni di pendenza, resistenza e altri fattori esterni.

## Obiettivo