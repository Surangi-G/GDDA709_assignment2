import sys

for line in sys.stdin:
    try:
        # Skip the header row
        if line.startswith("InvoiceNo"):
            continue

        # Split the line into columns
        fields = line.strip().split(",")
        invoice_date = fields[4]  # InvoiceDate
        quantity = int(fields[3])  # Quantity
        unit_price = float(fields[5])  # UnitPrice

        # Calculate sales revenue
        sales = quantity * unit_price

        # Extract the month (YYYY-MM) from InvoiceDate
        month = invoice_date[:7]

        # Output the month and sales revenue
        print("{}\t{}".format(month, sales))
    except (IndexError, ValueError):
        # Handle missing or invalid data
        continue



