import pandas as pd
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("-i", default="input.list")
parser.add_argument("-f", default="0.2", type=float)
parser.add_argument("-o", default="output.txt")
args = parser.parse_args()

inputdir = "./files_folder"

datadf = pd.DataFrame({
    'chr':[],
    'pos':[]
})

with open(args.i) as f:
    for i in f:
        filename = os.path.join(inputdir, i.strip())
        df = pd.read_csv(filename, sep="\t", low_memory=False, header=None,
                         names=["chr", "pos", i.strip()])
        datadf = pd.merge(left=datadf,
                          right=df,
                          on=["chr","pos"],
                          how='outer')


mask = datadf.iloc[:, 2:].isna().sum(axis=1) / (datadf.shape[1] - 2) < args.f
datadf = datadf[mask]

#print(datadf.head()) #print results

datadf.to_csv(args.o,
              sep="\t",
              na_rep="NA",
              index=None)