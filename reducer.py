import sys

current_month = None
total_sales = 0

for line in sys.stdin:
    try:
        month, sales = line.strip().split("\t")
        sales = float(sales)

        if current_month == month:
            total_sales += sales
        else:
            if current_month:
                # Emit the previous month's total sales
                print("{}\t{}".format(current_month, total_sales))
            current_month = month
            total_sales = sales
    except ValueError:
        # Skip lines with errors
        continue

# Emit the last month's total sales
if current_month:
    print("{}\t{}".format(current_month, total_sales))



