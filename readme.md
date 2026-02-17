# Lab1 – Dataplattform

## Introduktion
Den här laborationen handlar om att bygga en enkel data pipeline med produktdata.  
Målet är att läsa in en produktfil, rensa datan, hantera datakvalitet och skapa en analysfil.

Pipeline-flödet följer:

**Extract → Transform → Load**

---

## Vad som gjordes

Labben löstes genom att arbeta i flera steg:

| Steg | Del | Beskrivning |
|------|-----|------------|
| Extract | Inläsning | CSV-filen lästes in med Pandas (`read_csv`) |
| Transform | Rensning | Text rensades med `strip()` och `lower()` |
| Transform | Datatyper | Pris gjordes numeriskt med `to_numeric()` |
| Flagging | Misstänkta värden | Missing currency, gratis produkter och luxury-priser markerades |
| Rejecting | Omöjliga värden | Negativa priser och saknat id avvisades |
| Load | Output | `analytics_summary.csv` skapades med statistik |

---

## Datakvalitet

Två typer av problem hanterades:

- **Flagging**: värden som kan vara okej men bör kontrolleras  
  (t.ex. saknad valuta eller extremt höga priser)

- **Rejecting**: värden som inte är möjliga och därför tas bort  
  (t.ex. negativt pris eller saknat produkt-id)

---

## Analytics Summary

När datan var rensad skapades filen:

### `analytics_summary.csv`

Den innehåller:

- snittpris  
- medianpris  
- antal produkter  
- antal produkter med saknat pris  

Resultatet visade att snittpriset blev högt eftersom vissa produkter hade extremt stora priser.

---

## Slutsats

Laborationen gav en introduktion till hur en enkel data pipeline kan byggas med Pandas, inklusive ingestion, transformering, datakvalitet och export av analysdata.


---

## Källhänvisning

DataFrame Pandas  
https://www.geeksforgeeks.org/pandas/python-pandas-dataframe/

Pandas – Kom igång  
https://pandas.pydata.org/docs/getting_started/index.html

10 Minutes to Pandas  
https://pandas.pydata.org/docs/getting_started/10min.html

Pandas API Reference  
https://pandas.pydata.org/docs/reference/index.html

Indexing (loc och iloc)  
https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html

read_csv()  
https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html

Missing values (isnull)  
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isnull.html

Statistik (describe)  
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html

to_csv()  
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html

---

## LLM Usage

Have used for handling error codes when stuck and for explaining parts from documentation when relations felt hard to understand.
