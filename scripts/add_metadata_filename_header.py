import pandas as pd
import os
import sys
import shutil

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

mt_dir = sys.argv[1]           # First argument is path to metadata
cns_dir = sys.argv[2]           # Second argument is path to directory with consensus sequences that need to be renamed. Consensus sequences need to be named as Wxxx_L*.fa
county_col_name = sys.argv[3]   # Argument for county location. When la,lon available use "computed_location".

# Remove spaces from location names
df = pd.read_csv(mt_dir)
df.columns = df.columns.str.replace(" ","_").str.lower()
# use location computed from lat and lon
df[county_col_name] = df[county_col_name].str.replace("_", "").str.replace(" ", "")
# reformat dates
df["collection_date"] = pd.to_datetime(df["collection_date"], format="%m/%d/%y").dt.strftime("%Y-%m-%d")
df = df.set_index("scripps_id")

for f in os.listdir(cns_dir):
    id = f.split("_")[0]
    _d = df.ix[id]
    _ = [id, _d["collection_date"], _d["country"], _d["state"], _d[county_col_name], str(round(_d["longitude"], 3)), str(round(_d["latitude"], 3))]
    new_f = "_".join(_) + ".fa"
    print(new_f)
    if f == new_f:
        new_f = new_f + ".tmp"
    fin = open(cns_dir+f, mode="r")
    fin.readline()
    fout = open(cns_dir+new_f, mode="w")
    if ".tmp" in new_f:
        fout.write(">"+new_f[:-7]+"\n")
    else:
        fout.write(">"+new_f[:-3]+"\n")
    shutil.copyfileobj(fin, fout)
    fout.flush()
    fin.flush()
    fout.close()
    fin.close()
    os.remove(cns_dir+f)
    if ".tmp" in new_f:
        os.rename(cns_dir+new_f, cns_dir+new_f[:-4])
