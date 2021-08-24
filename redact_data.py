import csv


# Read csv
def read_csv(source):
    data = []
    fieldnames = None
    with open(source, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for row in reader:
            data.append(row)
    return data


# Write to CSV
def write_csv(data, field_names, destination):
    with open(destination, 'w', newline='') as f:
        fieldnames = ['emp_name', 'dept', 'birth_month']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerows(data)


if __name__ == "__main__":
    csv_name_list = ['Employee']
    for csv_name in csv_name_list:
        source = f"data/{csv_name}.csv"
        data = read_csv(source)
