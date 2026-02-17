import pandas as pd

# Läs in filen korrekt
df = pd.read_csv("products.csv", sep=";")

# Gör kolumnnamnen lowercase och ta bort mellanslag
df.columns = df.columns.str.strip().str.lower()

# Rensa alla textkolumner: strip + lowercase
for col in df.select_dtypes(include="object"):
    df[col] = df[col].str.strip().str.lower()
df["price"] = pd.to_numeric(df["price"], errors="coerce")


# Kontrollera resultatet
print(df.head())
print(df.columns)

# Skriv ut saknade värden och statistik
print("\n--- Missing values per column ---")
print(df.isnull().sum())
# Skriv ut grundläggande statistik för priset
print("\n--- Basic price statistics ---")
print(df["price"].describe())
# Identifiera produkter med negativt pris
print("\n--- Products with negative price ---")
print(df[df["price"] < 0])
