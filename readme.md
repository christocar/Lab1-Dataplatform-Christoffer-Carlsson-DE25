# Lab1 – Data Pipeline med Pandas

## Introduktion

Den här laborationen handlar om att bygga en enkel data pipeline med produktdata.  
Målet är att läsa in en CSV-fil, rensa datan, hantera datakvalitet och skapa en analysfil.

Pipeline-flödet följer modellen:

**Extract → Transform → Load**

---

## Pipeline-struktur

Laborationen löstes genom att arbeta i följande steg:

| Steg | Del | Beskrivning |
|------|-----|------------|
| Extract | Inläsning | Produktdata läses in från CSV med `read_csv()` |
| Transform | Rensning | Kolumnnamn och textdata normaliseras med `strip()` och `lower()` |
| Transform | Datatyper | Pris görs numeriskt med `to_numeric()` |
| Kontroll | Dataöversikt | Saknade värden och prisstatistik skrivs ut |
| Flagging | Datakvalitet | Produkter markeras med flaggor för möjliga avvikelser |
| Rejecting | Omöjliga värden | Produkter med negativa priser, saknat id eller saknat pris avvisas |
| Load | Output | En analysfil (`analytics_summary.csv`) skapas med statistik |

---

## Data Cleaning

För att göra datan konsekvent utfördes följande rensning:

- Kolumnnamn gjordes lowercase och mellanslag togs bort
- Alla textkolumner rensades med:
  - `strip()` (tar bort extra mellanslag)
  - `lower()` (gör texten konsekvent)

Pris-kolumnen konverterades till numeriskt format med:

- `pd.to_numeric(..., errors="coerce")`

Detta gör att ogiltiga prisvärden automatiskt blir `NaN`.

---

## Data Quality Checks

Efter inläsning kontrollerades datakvalitet genom att skriva ut:

- Antal saknade värden per kolumn (`isnull().sum()`)
- Grundläggande prisstatistik (`describe()`)
- Produkter med negativa priser

Detta ger en översikt innan flagging och rejection sker.

---

## Flagging (Avvikelsemarkering)

En kolumn `flag` skapades för att markera produkter med möjliga problem:

- Saknad valuta (`missing_currency`)
- Gratis produkter (`free_products`)
- Extremt höga priser (`luxury_products`)

Flagging innebär att produkterna fortfarande finns kvar i datan, men markeras för granskning.

---

## Rejecting (Avvisning av omöjliga värden)

Produkter som inte är rimliga avvisades helt och hamnade i `rejected_products`.

Följande villkor användes:

- Negativt pris
- Saknat produkt-id
- Saknat pris

De avvisade produkterna separerades och ett clean dataset skapades:

- `clean_products`

Detta dataset används för analys och export.

---

## Analytics Summary

När datan var rensad skapades filen:

### `analytics_summary.csv`

Den innehåller:

- **average_price** (snittpris)
- **median_price** (medianpris)
- **product_count** (antal giltiga produkter)
- **missing_price_count** (antal produkter med saknat pris)

Statistiken baseras endast på `clean_products`.

---

## Output

Filen som genereras av programmet:

- `analytics_summary.csv`

Den används som sammanfattning av produktdatasetet efter datarensning och kvalitetskontroller.

---

## Slutsats

Laborationen gav en praktisk introduktion till hur en data pipeline kan byggas med Pandas.  
Arbetet inkluderade ingestion av data, transformering, datakvalitet, flagging, rejecting och export av analysresultat.

---

## Dokumentation

- Pandas – Kom igång  
  https://pandas.pydata.org/docs/getting_started/index.html  

- 10 Minutes to Pandas  
  https://pandas.pydata.org/docs/getting_started/10min.html  

- Pandas API Reference  
  https://pandas.pydata.org/docs/reference/index.html  

- Indexing (`loc` och `iloc`)  
  https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html  

- `read_csv()`  
  https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html  

- Missing values (`isnull`)  
  https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isnull.html  

- Statistik (`describe`)  
  https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html  

- `to_csv()`  
  https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html  

- `pd.DataFrame()`  
  https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html  

- Python builtin `len()`  
  https://docs.python.org/3/library/functions.html#len  

---

## LLM Usage

An AI assistant was used for:

- Explaining Pandas methods (`loc`, `isnull`, `describe`)
- Clarifying pipeline concepts (flagging vs rejecting)
- Structuring the README documentation and workflow explanation
