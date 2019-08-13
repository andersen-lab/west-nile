import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../metadata/alignment_statistics.tsv", sep="\t", names=["Name", "Percent coverage", "Depth per nucleotide"])
df["excluded"] = False
df.loc[df.sort_values("Percent coverage").iloc[:14].index, "excluded"] = True

ax = df[~df["excluded"]].plot.scatter(x="Percent coverage", y="Depth per nucleotide", c = "steelblue", label="Included")
df[df["excluded"]].plot.scatter(x="Percent coverage", y="Depth per nucleotide", c = "indianred", label="Excluded", ax = ax)
ax.set_xlabel("Percent coverage of genome at a minimum depth of 10")
plt.tight_layout()
plt.savefig("../plots/alignment_stats.png", dpi=300)
plt.clf()
plt.close()
