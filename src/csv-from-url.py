import requests
import csv


def read_csv_from_internet(url):
    response = requests.get(url)
    lines = response.text.splitlines()
    reader = csv.reader(lines)

    for row in reader:
        print(row)  # You can process the rows as per your requirements


# Example usage
# Replace with the actual CSV file URL
csv_url = "https://docs.google.com/spreadsheets/d/18cGZ-6-2aWKnVUY-pBYU_BluGP2MeptOqKOszG43L6M/edit#gid=0"
read_csv_from_internet(csv_url)
