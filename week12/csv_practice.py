




import csv
from datetime import datetime

SALES_PATH = "data/sales.csv"
CLEANED_PATH = "data/cleaned.csv"
LOG_PATH = "data/run_log.txt"

# ---------- Exercise 2: Read and print raw rows ----------
print("Exercise 2: raw rows")
with open(SALES_PATH, newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)  # every value is a string, including price and quantity

# ---------- Exercise 3: Skip the header ----------
print("Exercise 3: skip the header")
with open(SALES_PATH, newline="") as f:
    reader = csv.reader(f)
    header = next(reader)
    print("Header:", header)
    for row in reader:
        print(row)

# ---------- Exercise 4: Compute totals ----------
print("Exercise 4: totals")
total_revenue = 0.0
with open(SALES_PATH, newline="") as f:
    reader = csv.reader(f)
    next(reader)
    for product, price, quantity in reader:
        price = float(price)
        quantity = int(quantity)
        line_total = price * quantity
        total_revenue += line_total
        print(f"{product}: {quantity} units × ${price:.2f} = ${line_total:.2f}")
print(f"Total revenue: ${total_revenue:.2f}")

# ---------- Exercise 5: Filter and write ----------
print("Exercise 5: filter and write")
original_count = 0
written_count = 0
with open(SALES_PATH, newline="") as infile, \
        open(CLEANED_PATH, "w", newline="") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    next(reader)
    writer.writerow(["Product", "Price", "Qty", "Total"])
    for product, price, quantity in reader:
        original_count += 1
        price = float(price)
        quantity = int(quantity)
        total = price * quantity
        if total > 100:
            writer.writerow([product, f"{price:.2f}", quantity, f"{total:.2f}"])
            written_count += 1
print(f"Wrote {written_count} rows out of {original_count} in the original.")

# ---------- Exercise 6: csv.DictReader ----------
print("Exercise 6: DictReader")
dict_total = 0.0
with open(SALES_PATH, newline="") as f:
    for row in csv.DictReader(f):
        price = float(row["price"])
        quantity = int(row["quantity"])
        line_total = price * quantity
        dict_total += line_total
        print(f"{row['product']}: {quantity} units × ${price:.2f} = ${line_total:.2f}")
print(f"Total revenue: ${dict_total:.2f}")
print("Matches Exercise 4:", round(dict_total, 2) == round(total_revenue, 2))
# reader is faster to write for small, fixed-layout files, but relies on column positions.
# DictReader is better when columns may be reordered or the file is wide, since names self-document.

# ---------- Exercise 7: Sales summary by product ----------
print("Exercise 7: summary by product")
summary = {}
with open(SALES_PATH, newline="") as f:
    for row in csv.DictReader(f):
        revenue = float(row["price"]) * int(row["quantity"])
        summary[row["product"]] = summary.get(row["product"], 0) + revenue
for product in sorted(summary):
    print(f"{product}: ${summary[product]:.2f}")

# ---------- Exercise 8: Append mode log ----------
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open(LOG_PATH, "a") as log:  # "a" appends, so earlier runs are kept
    log.write(f"{timestamp} - total revenue: ${total_revenue:.2f}\n")
print(f"\nLogged run to {LOG_PATH}")