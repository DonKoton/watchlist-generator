import requests
import gzip
import shutil

url = "https://datasets.imdbws.com/name.basics.tsv.gz"
filename_tsv = url.split("/")[-1][:-3]
filename_gz = filename_tsv + 'gz'

with open(filename_gz, "wb") as f:
    r = requests.get(url)
    f.write(r.content)

with gzip.open(filename_gz, 'rb') as f_in:
    with open(filename_tsv, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
