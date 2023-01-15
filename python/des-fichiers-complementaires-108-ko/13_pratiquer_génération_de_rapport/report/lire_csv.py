import csv

def lire_csv(ficname):
    data = []

    with open(ficname) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            data.append(row)
    return data

if __name__ == "__main__":
    data = lire_csv("data.csv")
    print(data)
