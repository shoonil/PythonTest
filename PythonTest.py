import pandas as pd
df=pd.read_csv('C:\\Users\\ACER\\Desktop\\sample_process.csv')
t = df.groupby('parent_page_id')['id'].apply(lambda x: ';'.join(x.astype(str)))
t=pd.DataFrame(t).reset_index()
t.columns=['id','child']
a=pd.concat([df, t])
a.to_csv('S.csv',index=False)