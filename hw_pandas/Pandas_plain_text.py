import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pandas_profiling as pp

train_df = pd.read_csv("https://raw.githubusercontent.com/Serfentum/bf_course/master/14.pandas/train.csv")

sns.displot(train_df, x="A")
sns.displot(train_df, x="T")
sns.displot(train_df, x="G")
sns.displot(train_df, x="C")


for nucleotide in ['A', 'T', 'G', 'C']:
    train_df[nucleotide].hist(bins=50, alpha=0.5, label=nucleotide)
plt.legend(loc='upper right')
plt.title('Histogram of A, T, G, C')
plt.xlabel('number of contigs with this nucleotide')
plt.ylabel('count')
plt.show()

train_part = train_df.loc[:,
                        ['pos', 'reads_all', 'mismatches', 'insertions']][train_df.mismatches > train_df.mismatches.mean()]
train_part.to_csv('train_part.csv', index=False)

yersinia = pd.read_csv("./Chromosomes_full.tsv", sep='\t')


yersinia = yersinia.iloc[:, 1:]
yersinia.head()

yersinia.describe()

yersinia.info()

yersinia['rec.shape'].unique()
yersinia['rec.type'].unique()
yersinia['species'].unique()

yersinia.columns

f, axes = plt.subplots(figsize=(60, 5), nrows=1, ncols=11)
features = ['rec.length', 'rec.proteins', 'species', 'minGC', 'maxGC',
            'length_replichore1', 'length_replichore2', 'ratio', 'genome_size',
            'disbalance', 'GCcontent']

for feature in range(11):
    axes_number = axes[feature]
    sns.histplot(x=yersinia[features[feature]], ax=axes_number)


f, axes = plt.subplots(figsize=(60, 60), nrows=11, ncols=11)

used_features = []
for feature in range(11):
    for feature2 in range(11):
        axes_number = axes[feature, feature2]
        if feature == feature2:
            sns.histplot(x=yersinia[features[feature]], ax=axes_number)
        else:
            sns.scatterplot(data=yersinia, y=features[feature], x=features[feature2], ax=axes_number)


corr = yersinia.corr(method='pearson')
corr.style.background_gradient(cmap='coolwarm')

pp.ProfileReport(yersinia)
