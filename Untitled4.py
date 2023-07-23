#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
pd.read_csv("C:/Users/yunji/data/pp_2000_2020_1.csv",encoding="cp949")


# In[2]:


import pandas as pd
df_kosis=pd.read_csv("C:/Users/yunji/data/babypopulation_2000_2020.csv",encoding="cp949")
df_kosis.shape


# In[96]:


pd.options.display.max_columns=65
df_kosis.head(1)


# In[ ]:


df_kosis.drop("출산순위별",axis=1,inplace=True)
df_kosis.head()


# In[6]:


df_kosis.head()


# In[18]:


df=df_kosis.melt(id_vars="시군구별")
df.head()


# In[19]:


df["시군구별"].unique()


# In[20]:


print(df.shape)
df=df[df["시군구별"]!="시군구별"].copy()
df.shape


# In[21]:


df.head()


# In[26]:


df["연도"]=df["variable"].str.split(".",expand=True)[0]
df["성별"]=df["variable"].str.split(".",expand=True)[1]
df.head()


# In[25]:


df.tail()


# In[27]:


df["성별"].unique()


# In[28]:


df["성별"].nunique()


# In[30]:


df["성별"]=df["성별"].fillna("전체")
df["성별"].unique()


# In[32]:


df["성별"]=df["성별"].replace("1","남자").replace("2","여자")
df["성별"].unique()


# In[33]:


df["성별"].value_counts()


# In[34]:


df.head()


# In[36]:


df=df.rename(columns={"variable":"기간","value":"출생아수"})
df.head()


# In[38]:


df.info()


# In[51]:


import numpy as np
df["출생아수"]=df["출생아수"].replace("=",np.nan)
df["출생아수"]=df["출생아수"].astype(float)
df["출생아수"].describe()


# In[97]:


df_all=df[(df["시군구별"]=="전국") & (df["성별"]=="전체")]
df_all.head()


# In[59]:


df_all=df_all[["연도","출생아수"]].copy()
df_all.head()


# In[64]:


import matplotlib.pyplot as plt
plt.rc("font",family="GULIM")

df_all.set_index(["연도"]).plot(figsize=(15,4))


# In[67]:


df_all.set_index(["연도"]).plot.bar(figsize=(15,4))


# In[74]:


import seaborn as sns
plt.figure(figsize=(15,4))
sns.lineplot(data=df_all,x="연도",y="출생아수",ci=None)
plt.figure(figsize=(15,4))
sns.barplot(data=df_all,x="연도",y="출생아수",ci=None)


# In[77]:


df_local=df[df["시군구별"]!="전국"].copy()
df_local


# In[80]:


plt.figure(figsize=(15,4))
sns.pointplot(data=df_local,x="연도",y="출생아수",hue="성별")


# In[83]:


df_local_all=df_local[df_local["성별"]=="전체"]
df_local_all


# In[89]:


plt.figure(figsize=(15,4))
sns.pointplot(data=df_local,x="연도",y="출생아수",hue="시군구별",ci=None)
plt.legend(loc='center right',bbox_to_anchor=(1.17,0.5),ncol=1)


# In[91]:


df_local_2=df_local_all[df_local_all["시군구별"].isin(["서울특별시","경기도","세종특별자치시"])]
plt.figure(figsize=(15,4))
sns.pointplot(data=df_local_2,x="연도",y="출생아수",hue="시군구별")


# In[95]:


df_sj=df[df["시군구별"]=="세종특별자치시"].dropna(how="any")
df_sj
sns.pointplot(data=df_sj,x="연도",y="출생아수",ci=None)


# In[ ]:




