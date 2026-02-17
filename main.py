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

# Flagga avvikelser
df["flag"] = ""

# Flagga saknat värde i "currency"
df.loc[df["currency"].isnull(), "flag"] += "missing_currency;"
# Flagga produkter med värde 0
df.loc[df["price"] == 0, "flag"] += "free_products;"
# Flagga produkter med pris över 100000
df.loc[df["price"] > 100000, "flag"] += "luxury_products;"

# Ta bort produkter med negativt pris eller saknat id
rejected_products = df[(df["price"] < 0) | (df["id"].isnull())]

print("\n--- Rejected products ---")
# Visa endast relevanta kolumner för de avvisade produkterna
print(rejected_products[["id", "name", "price", "currency"]])

# Skapa en ny DataFrame med de rensade produkterna
clean_products = df.drop(rejected_products.index)

print("\n--- Clean products count ---")
# Visa antalet rensade produkter
print(len(clean_products))

# Skriv ut statistik för de rensade produkterna
average_price = clean_products["price"].mean()
median_price = clean_products["price"].median()
product_count = len(clean_products)
missing_price_count = clean_products["price"].isnull().sum()

# Skapa sammanfattningen i en DataFrame
summary = pd.DataFrame({
    "average_price": [average_price],
    "median_price": [median_price],
    "product_count": [product_count],
    "missing_price_count": [missing_price_count]
})

# Spara sammanfattningen till en CSV-fil
summary.to_csv("analytics_summary.csv", index=False)
print("\n--- analytics_summary.csv created ---")
print(summary)
