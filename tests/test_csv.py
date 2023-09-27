import csv
import os
from .conftest import resources_path


# TODO оформить в тест, добавить ассерты и использовать универсальный путь
def test_csv():
    with open(os.path.join(resources_path, 'users.csv'), 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(['Anna', 'Pavel', 'Peter'])
        csvwriter.writerow(['Alex', 'Serj', 'Yana'])
    assert os.path.exists(os.path.join(resources_path, 'users.csv'))

    with open(os.path.join(resources_path, 'users.csv')) as csvfile:
        csvreader = csv.reader(csvfile)
        count_rows = 0
        for row in csvreader:
            if len(row) > 0:
                count_rows += 1
        assert count_rows == 2
