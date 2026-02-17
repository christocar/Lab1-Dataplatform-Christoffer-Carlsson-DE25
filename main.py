import pandas as pd

# Läs in filen korrekt
df = pd.read_csv("products.csv", sep=";")

# Gör kolumnnamnen lowercase och ta bort mellanslag
df.columns = df.columns.str.strip().str.lower()

# Rensa alla textkolumner: strip + lowercase
for col in df.select_dtypes(include="object"):
    df[col] = df[col].str.strip().str.lower()

# Gör price till numeriskt värde
df["price"] = pd.to_numeric(df["price"], errors="coerce")

# Kontrollera resultatet
print(df.head())
print(df.columns)

# Skriv ut saknade värden och statistik
print("\n--- Missing values per column ---")
print(df.isnull().sum())

print("\n--- Basic price statistics ---")
print(df["price"].describe())

print("\n--- Products with negative price ---")
print(df[df["price"] < 0])

# Flagga avvikelser
df["flag"] = ""

df.loc[df["currency"].isnull(), "flag"] += "missing_currency;"
df.loc[df["price"] == 0, "flag"] += "free_products;"
df.loc[df["price"] > 100000, "flag"] += "luxury_products;"

# Räkna saknade priser innan rejection (för labbens krav)
missing_price_count = df["price"].isnull().sum()

# Rejecta produkter med negativa priser, saknat id eller saknat price
rejected_products = df[
    (df["price"] < 0) |
    (df["id"].isnull()) |
    (df["price"].isnull())
]

print("\n--- Rejected products ---")
print(rejected_products[["id", "name", "price", "currency"]])

# Skapa en ny DataFrame med de rensade produkterna
clean_products = df.drop(rejected_products.index)

print("\n--- Clean products count ---")
print(len(clean_products))

# Statistik på clean dataset
average_price = clean_products["price"].mean()
median_price = clean_products["price"].median()
product_count = len(clean_products)

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
