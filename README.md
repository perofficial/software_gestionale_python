# 🛒 BioMarket Management System

Sistema gestionale per una bottega BioMarket.

## 📋 Obiettivo del Progetto

BioMarket Management System è un software gestionale testuale progettato per facilitare la gestione di un piccolo negozio. Il sistema permette di:

- **Registrare nuovi prodotti** con nome, quantità, prezzo di acquisto e prezzo di vendita
- **Gestire l'inventario** con aggiornamenti automatici delle quantità
- **Registrare le vendite** effettuate con calcolo automatico dei profitti
- **Visualizzare i profitti** lordi e netti
- **Persistenza dei dati** tra diverse esecuzioni del programma

## 📁 Struttura della Repository

```
biomarket-management/
│
├── main.py                      # Entry point dell'applicazione
├── requirements.txt             # Dipendenze Python (nessuna libreria esterna)
├── README.md                    # Documentazione del progetto
├── .gitignore                   # File da ignorare in git
│
├── src/                         # Codice sorgente principale
│   ├── __init__.py
│   │
│   ├── models/                  # Modelli di dati
│   │   ├── __init__.py
│   │   ├── product.py           # Classe Product
│   │   ├── warehouse.py         # Classe Warehouse
│   │   └── sales.py             # Classe SalesManager
│   │
│   ├── ui/                      # Interfaccia utente
│   │   ├── __init__.py
│   │   └── menu.py              # Gestione menu e interazioni
│   │
│   └── utils/                   # Utility e helpers
│       ├── __init__.py
│       ├── input_validator.py   # Validazione input utente
│       └── logger.py            # Configurazione logging
│
├── logs/                        # File di log (generati automaticamente)
│   └── biomarket_YYYYMMDD.log
│
└── *.csv                        # File dati (generati durante l'uso)
    ├── <nome_magazzino>.csv     # Inventario prodotti
    └── vendite.csv              # Registro vendite
```

## 🚀 Installazione

### Prerequisiti

- Python 3.7 o superiore
- Git (per clonare la repository)

### Passo 1: Clonare la Repository

```bash
# Clona la repository
git clone https://github.com/perofficial/software_gestionale_python.git

# Entra nella directory del progetto
cd software_gestionale_python
```

### Passo 2: Creare un Ambiente Virtuale

#### Su Linux/macOS:

```bash
# Crea l'ambiente virtuale
python3 -m venv venv

# Attiva l'ambiente virtuale
source venv/bin/activate
```

#### Su Windows:

```bash
# Crea l'ambiente virtuale
python -m venv venv

# Attiva l'ambiente virtuale
venv\Scripts\activate
```

### Passo 3: Installare le Dipendenze

```bash
# Installa le dipendenze (nessuna libreria esterna richiesta)
pip install -r requirements.txt
```

### Passo 4: Eseguire il Programma

```bash
# Esegui l'applicazione
python main.py
```

## 📖 Guida all'Uso

### Menu Principale

All'avvio del programma, verrà visualizzato il menu principale con le seguenti opzioni:

```
==================================================
        BIOMARKET - MENU PRINCIPALE
==================================================

1. Aggiungi prodotto
2. Vendita prodotto
3. Profitti
4. Esci

--------------------------------------------------
```

### 1. Aggiungi Prodotto

- Selezionare o creare un magazzino
- Inserire nome del prodotto
- Inserire quantità
- Inserire prezzo di acquisto
- Inserire prezzo di vendita

**Nota:** Se il prodotto esiste già, la quantità verrà aggiunta a quella esistente.

### 2. Vendita Prodotto

- Selezionare il magazzino
- Inserire nome del prodotto da vendere
- Inserire quantità da vendere

Il sistema verificherà:
- Esistenza del prodotto nel magazzino
- Disponibilità della quantità richiesta

### 3. Visualizza Profitti

Mostra i profitti totali:
- **Profitto Lordo**: Totale ricavato dalle vendite
- **Profitto Netto**: Profitto lordo meno i costi di acquisto

### 4. Esci

Termina l'applicazione in modo sicuro.

## 🗂️ Gestione dei Dati

### File CSV Generati

- **Magazzini** (`<nome>.csv`): Contengono l'inventario dei prodotti
- **Vendite** (`vendite.csv`): Registro di tutte le vendite effettuate

### Formato Dati Magazzino

```csv
nome,quantita,prezzo di acquisto,prezzo di vendita
Mele,50,0.80,1.50
Arance,30,0.90,1.80
```

### Formato Dati Vendite

```csv
nome,quantita venduta,profitto,data e ora
Mele,10,7.00,17/11/2025 14:30:45
```

## 🔧 Caratteristiche Tecniche

### Validazione Input

- Controllo di tutti gli input utente
- Gestione errori con messaggi chiari
- Conversione automatica formati numerici (virgola → punto)

### Gestione Errori

- Eccezioni per operazioni su file
- Validazione dati di prodotti
- Controllo disponibilità stock
- Gestione file mancanti

### Logging

- Log automatico delle operazioni
- File di log giornalieri in `/logs`
- Tracciamento errori e operazioni

## 🛠️ Sviluppo

### Codice Pulito

- Nomenclatura in inglese (snake_case per funzioni/variabili)
- Docstrings complete per classi e metodi
- Commenti esplicativi dove necessario

### Architettura

- **Modelli** (models/): Logica di business e gestione dati
- **UI** (ui/): Interfaccia utente e menu
- **Utils** (utils/): Funzioni di utilità

## 📝 Note

- Il sistema utilizza solo la libreria standard di Python
- Non sono necessarie dipendenze esterne
- I dati sono persistenti tra diverse esecuzioni
- Tutti i prezzi sono in Euro (€)

## 🤝 Contributi

Per contribuire al progetto:

1. Fork la repository
2. Crea un branch per la tua feature (`git checkout -b feature/nuova-feature`)
3. Commit le modifiche (`git commit -m 'Aggiunge nuova feature'`)
4. Push sul branch (`git push origin feature/nuova-feature`)
5. Apri una Pull Request

## 📄 Licenza

Questo progetto è sviluppato per fini didattici.

## 📧 Contatti

Per domande o supporto, contattare il team di sviluppo BioMarket.

---

**Versione:** 1.0.0  
**Ultimo Aggiornamento:** Novembre 2025
