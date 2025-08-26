# Analisi visiva UGC vs DMO – Caso Sicilia

Questo repository contiene il materiale empirico e gli script utilizzati per la tesi di laurea:  
**"Il ruolo degli UGC visivi nella costruzione e diffusione dell’immaginario turistico: una content analysis tra percezione e promozione"**

## Obiettivo della ricerca

Analizzare e confrontare la **destination image** della Sicilia su Instagram, distinguendo tra:

- **Immagine proiettata**: contenuti visivi pubblicati dall’account ufficiale “@visit.sicily”
- **Immagine percepita**: contenuti generati dagli utenti (UGC), con un focus sulla **Generazione Z**

## Metodo

L’analisi si basa su una **content analysis visiva qualitativa**, fondata su una griglia di codifica interpretativa.  
Sono stati analizzati **120 contenuti DMO** e **120 contenuti UGC**, raccolti attraverso due procedure automatizzate in Python.

## Raccolta delle immagini

### Contenuti DMO
- Estratti dall’account Instagram ufficiale **@visit.sicily**
- Periodo considerato: **anno 2024**
- Filtrati per escludere **video** e **reel**, garantendo uniformità visiva

### Contenuti UGC
- Raccolti tramite scraping di Instagram con l’hashtag **#sicily2024**
- Dataset iniziale: **3.514 immagini**
- Scrematura automatica su base semantica:
  - Rimozione di contenuti con **hashtag sponsorizzati** (es. `#ads`)
  - Esclusione di post contenenti **tag/menzioni a profili istituzionali**
- Estrazione casuale di un sottocampione di **300 immagini**
- **Validazione manuale** per escludere immagini non pertinenti:
  - Locandine, eventi, selfie non territoriali, foto generiche
- Selezione finale: **120 immagini UGC autentiche**, per garantire parità numerica con i contenuti DMO

## Contenuti della repository

| File                         | Descrizione |
|-----------------------------|-------------|
| `Excel file TESI 07082025.xlsx` | Dataset completo con codifica delle immagini DMO e UGC |
| `scraper_dmo.py` *(opzionale)* | Script Python per l’estrazione automatica dei post DMO |
| `scraper_ugc.py` *(opzionale)* | Script Python per l’estrazione e pulizia dei post UGC |
| `README.md`                 | Descrizione del progetto, obiettivi, metodo e contenuti |

## Piattaforma

- **Instagram**
- Hashtag utilizzati: `#sicily2024` (e derivati)
- Focus visuale su contenuti fotografici pubblici, coerenti con il contesto turistico

## Target analizzato

La ricerca si concentra sui contenuti UGC attribuibili alla **Generazione Z**, data la prevalenza d’uso di Instagram da parte di questa fascia d’età per documentare esperienze di viaggio.

---

*Tesi presentata presso l’Università Ca’ Foscari Venezia*  
Corso di Laurea: Marketing e Comunicazione
Anno Accademico: 2024/2025  

