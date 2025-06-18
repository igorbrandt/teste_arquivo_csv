import csv

path_do_arquivo = "data.csv"

def csv_reader(file_to_read: str) -> list[dict]:

    list_of_items = []
    with open(file_to_read, mode="r", encoding="utf-8") as open_file:
        reader = csv.DictReader(open_file)
        for line in reader:
            list_of_items.append(line)

    return list_of_items
    
print(csv_reader(path_do_arquivo))