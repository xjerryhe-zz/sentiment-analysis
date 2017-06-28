import sys
import pandas as pd

reload(sys)
sys.setdefaultencoding("utf-8")


file1 = pd.read_excel("Infomedia_Batch_2.xlsx")
file2 = pd.read_excel("batch_2.xlsx")

a = pd.DataFrame(file1)
b = pd.DataFrame(file2)

df1 =a.set_index(['ArticleId', 'TopicName']).join(b.set_index(['ArticleId', 'TopicName']), how='inner', lsuffix='_left', rsuffix='_right')

df1.to_csv("output.csv")


