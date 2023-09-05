#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


# In[7]:


ipl.drop(["team1","team2"],axis=1)


# In[2]:


ipl=pd.read_csv(r'C:\Users\Welcome\Desktop\matches.csv')


# In[3]:


ipl


# In[78]:


# Top 5 player of match
plt.figure(figsize=(10,5))
plt.bar(list(ipl["player_of_match"].value_counts().keys())[0:5],list(ipl["player_of_match"].value_counts())[0:5],color=["red","green","blue","pink","yellow"],width=0.2)
plt.title("Top 5 player of match")
plt.xlabel("Players")
plt.ylabel("No. of player of match awards")
plt.plot()


# In[5]:


ipl.info()


# In[80]:


ipl.isnull().sum()


# In[84]:


ipl=ipl.fillna("Unknown")


# In[85]:


ipl.isnull().sum()


# In[92]:


a=list(ipl["result"].value_counts())


# In[93]:


b=list(ipl["result"].value_counts().keys())


# In[97]:


plt.bar(b,a,width=0.1)
plt.show()


# In[98]:


ipl


# In[129]:


batting_first=ipl[ipl["win_by_runs"]!=0]


# In[132]:


batting_first.shape


# In[143]:


sns.displot(x=batting_first["win_by_runs"],hue="winner",data=batting_first,palette="Set1",kde=True)
plt.xlabel("Runs")
plt.show()


# In[150]:


batting_first["winner"].value_counts()


# In[162]:


plt.figure(figsize=(10,6))
plt.bar(list(batting_first["winner"].value_counts().keys())[0:3],list(batting_first["winner"].value_counts())[0:3])
plt.show()


# In[180]:


plt.pie(list(batting_first["winner"].value_counts())[0:3],labels=list(batting_first["winner"].value_counts().keys())[0:3],explode=[0.1,0,0],autopct="%.2f%%",shadow=True)
plt.show()


# In[174]:


#getting details of team that won batting second


# In[182]:


batting_second=ipl[ipl["win_by_wickets"]!=0]


# In[183]:


batting_second


# In[185]:


batting_second["win_by_wickets"]


# In[213]:


sns.barplot(x=list(batting_second["win_by_wickets"].value_counts().keys()),y=list(batting_second["win_by_wickets"].value_counts()))
plt.plot()


# In[217]:


sns.displot(batting_second["win_by_wickets"])
plt.plot()


# In[223]:


plt.figure(figsize=(50,5))
sns.barplot(x=list(batting_first["win_by_runs"].value_counts().keys()),y=list(batting_first["win_by_runs"].value_counts()))
plt.plot()


# In[229]:


sns.displot(x=batting_first["win_by_runs"],hue="winner",data=batting_first,palette="Set1")
plt.plot()


# In[ ]:


#top 3 teams win batting second


# In[245]:


list(batting_second["winner"].value_counts()[0:3])


# In[244]:


list(batting_second["winner"].value_counts().keys()[0:3])


# In[250]:


plt.bar(list(batting_second["winner"].value_counts().keys()[0:3]),list(batting_second["winner"].value_counts()[0:3]),color=["purple","blue","red"])
plt.plot()


# In[267]:


plt.pie(list(batting_second["winner"].value_counts()),labels=list(batting_second["winner"].value_counts().keys()),radius=3.5,startangle=0,autopct="%.2f%%")
plt.plot()


# In[270]:


#matches played each season
ipl["season"].value_counts()


# In[272]:


ipl["city"].value_counts()


# In[283]:


np.sum(ipl["toss_winner"]==ipl["winner"])


# In[285]:


np.sum(ipl["winner"].value_counts())


# In[287]:


a=393/752


# In[ ]:





# In[293]:


deliveries=pd.read_csv(r'C:\Users\Welcome\Desktop\deliveries.csv')


# In[300]:


deliveries


# In[318]:


matches
=ipl[ipl["season"]==2017]


# In[319]:


matches_2017["city"].value_counts()


# In[311]:


matches_2017


# In[313]:


ipl


# In[320]:


deliveries


# In[331]:


inning_1=deliveries[deliveries["match_id"]==1]


# In[333]:


srh=inning_1[inning_1["batting_team"]=="Sunrisers Hyderabad"]


# In[335]:


srh["batsman_runs"].value_counts()


# In[337]:


srh["dismissal_kind"].value_counts()


# In[338]:


ipl


# In[339]:


pk


# In[343]:


np.sum(ipl["winner"]=="Mumbai Indians")


# In[344]:


ipl


# In[348]:


np.sum(ipl["winner"]=="Mumbai Indians")

