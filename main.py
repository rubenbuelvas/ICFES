import requests
import os.path
import pandas as pd
from sklearn.svm import SVR

# Constants
DATASET_NAME = 'ICFES_dataset.csv'
PROCESSED_DATASET_NAME = 'data.csv'
TEST_SIZE = 0.3


def download_file(filename, url):
    """
    Download an URL to a file
    """
    with open(filename, 'wb') as fout:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        # Write response data to file
        for block in response.iter_content(4096):
            fout.write(block)


def download_if_not_exists(filename, url):
    """
    Download a URL to a file if the file
    does not exist already.
    Returns
    -------
    True if the file was downloaded,
    False if it already existed
    """
    if not os.path.exists(filename):
        download_file(filename, url)
        return True
    return False


if __name__ == '__main__':
    download_if_not_exists(DATASET_NAME, 'https://www.datos.gov.co/api/views/ynam-yc42/rows.csv?accessType=DOWNLOAD')
    data = pd.read_csv(DATASET_NAME)
    y = data['PUNT_GLOBAL']
    data.
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=TEST_SIZE, random_state=0)