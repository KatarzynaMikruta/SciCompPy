import pandas as pd
from Bio import SeqIO
from prettytable import PrettyTable

def parse_genbank(file):
    records = SeqIO.parse(file, 'genbank')
    data = []
    for record in records:
        for feature in record.features:
            if feature.type == 'CDS':
                locus_tag = feature.qualifiers.get('locus_tag', [''])[0]
                product = feature.qualifiers.get('product', [''])[0]
                protein_id = feature.qualifiers.get('protein_id', [''])[0]
                data.append({'Locus Tag': locus_tag, 'Product': product, 'Protein ID': protein_id})
    df = pd.DataFrame(data)
    return df

def list_entries(df):
    table = PrettyTable()
    table.field_names = df.columns
    for index, row in df.iterrows():
        table.add_row(row)
    print(table)

def insert_entry(df, locus_tag, product, protein_id, filename):
    new_row = {'Locus Tag': locus_tag, 'Product': product, 'Protein ID': protein_id}
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    save_to_csv(df, filename)
    print(f"Added {locus_tag} to the database.")
    return df

def remove_entry(df, locus_tag, filename):
    if locus_tag in df['Locus Tag'].values:
        df = df[df['Locus Tag'] != locus_tag]
        save_to_csv(df, filename)
        print(f"Removed {locus_tag} from the database.")
    else:
        print(f"Locus Tag {locus_tag} not found in the database.")
    return df

def search_entries(df, keyword):
    result = df[df.apply(lambda row: row.astype(str).str.contains(keyword, case=False).any(), axis=1)]
    if len(result) == 0:
        print(f"No entries found containing '{keyword}' in any column.")
    else:
        table = PrettyTable()
        table.field_names = result.columns
        for index, row in result.iterrows():
            table.add_row(row)
        print(table)

def save_to_csv(df, filename):
    df.to_csv(filename, index=False)
    print(f"Database saved to {filename}.")

def main():
    genbank_file = input("Enter GenBank file path: ")
    df = parse_genbank(genbank_file)
    if df.empty:
        print("No data parsed from the GenBank file.")
        return

    filename = input("Enter filename to save database (e.g., database.csv): ")
    save_to_csv(df, filename)

    while True:
        print("\n1. List database")
        print("2. Insert new entry")
        print("3. Remove entry")
        print("4. Search entry")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            list_entries(df)
        elif choice == '2':
            locus_tag = input("Enter Locus Tag: ")
            product = input("Enter Product: ")
            protein_id = input("Enter Protein ID: ")
            df = insert_entry(df, locus_tag, product, protein_id, filename)
        elif choice == '3':
            locus_tag = input("Enter Locus Tag of entry to remove: ")
            df = remove_entry(df, locus_tag, filename)
        elif choice == '4':
            keyword = input("Enter keyword to search: ")
            search_entries(df, keyword)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
