import pandas as pd

# Läs in filen korrekt
df = pd.read_csv("products.csv", sep=";")

# Gör kolumnnamnen lowercase och ta bort mellanslag
df.columns = df.columns.str.strip().str.lower()

# Rensa alla textkolumner: strip + lowercase
for col in df.select_dtypes(include="object"):
    df[col] = df[col].str.strip().str.lower()

# Kontrollera resultatet
print(df.head())
print(df.columns)
