# Analisi visiva UGC vs DMO – Caso Sicilia

Questo repository contiene il materiale empirico e gli script Python utilizzati per la tesi di laurea:  
**"Il ruolo degli UGC visivi nella costruzione e diffusione dell’immaginario turistico: una content analysis tra percezione e promozione"**

## Obiettivo della ricerca

Analizzare e confrontare la **tourist destination image** della Sicilia su Instagram, distinguendo tra:

- **Immagine proiettata**: contenuti visivi pubblicati dall’account ufficiale “@visit.sicily”
- **Immagine percepita**: contenuti generati dagli utenti (UGC), con un focus sulla **Generazione Z**

## Metodo

L’analisi si basa su una **content analysis visiva qualitativa**, fondata su una griglia di codifica interpretativa.  
Sono stati analizzati **120 contenuti DMO** e **120 contenuti UGC**, raccolti tramite scraping automatizzato di Instagram.

## Raccolta delle immagini

### Contenuti DMO
- Raccolti dall’account ufficiale **@visit.sicily**
- Periodo: **anno 2024**
- Esclusi video e reel tramite filtro automatico

### Contenuti UGC
- Raccolti con scraping basato sull’hashtag **#sicily2024**
- Dataset iniziale: **3.514 immagini**
- Scrematura automatica:
  - Rimozione post sponsorizzati o istituzionali (`#ads`, tag/mencioni DMO)
- Selezione casuale di **300 immagini**
- Validazione manuale → **120 immagini finali**

## Contenuti della repository

| File                           | Descrizione |
|--------------------------------|-------------|
| `Excel file TESI 07082025.xlsx` | Dataset codificato di immagini UGC e DMO contenente le tabelle e l'analisi |
| `collect_sicily_links.py`      | Script per raccogliere link da Instagram tramite hashtag (#sicily2024) |
| `filter_and_download_sicily.py`| Script per filtrare e scaricare immagini UGC valide |
| `count_and_save_2024_images.py`| Script per conteggiare e salvare immagini DMO |
| `README.md`                    | Descrizione progetto e guida alla repository |

## Tecnologie usate

- Excel e Python3

## Piattaforma

- Instagram (pubblico)
- Hashtag principali: `#sicily2024`, `#sicily`, `#visitsicily`

## Target analizzato

La ricerca si concentra sulla **Generazione Z**, maggiormente attiva su Instagram per la condivisione di esperienze turistiche.

---

*Tesi presentata presso l’Università Ca’ Foscari Venezia*  
Corso di Laurea: Marketing e Comunicazione
Anno Accademico: 2024/2025  
