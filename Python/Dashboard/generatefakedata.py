import csv
import random
from datetime import datetime, timedelta

# Function to generate fake data
def generate_fake_data(num_entries=1000):
    data = []
    start_date = datetime(2020, 1, 1)
    
    for i in range(num_entries):
        # Simulating a date range
        date = start_date + timedelta(days=i)
        
        # Simulating random values for different types of sales
        cash_sale = random.randint(100, 1000)  # Cash sale between 100 and 1000
        installment_sale = random.randint(200, 2000)  # Installment sale between 200 and 2000
        received = random.randint(100, 500)  # Amount received (could be part of installment)
        
        # Calculating other values
        entry = cash_sale + received  # Entry is the sum of cash sale and received money
        debit = installment_sale - received  # Debit is the remaining installment payment
        credit = random.uniform(0.1, 0.5) * installment_sale  # Credit granted (portion of installment sale)
        
        data.append([
            date.strftime('%Y-%m-%d'),
            cash_sale,
            installment_sale,
            received,
            entry,
            round(debit, 2),
            round(credit, 2)
        ])

    return data

# Function to write the data into a CSV file
def write_to_csv(filename='fake_sales_data.csv'):
    data = generate_fake_data()
    
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Writing headers
        writer.writerow(['Date', 'Cash Sale', 'Installment Sale', 'Received', 'Entry', 'Debit', 'Credit'])
        # Writing the data
        writer.writerows(data)

    print(f"CSV file '{filename}' generated successfully.")

# Call the function to generate the CSV file
write_to_csv()
