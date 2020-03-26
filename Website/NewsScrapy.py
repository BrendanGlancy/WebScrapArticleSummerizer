#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Description, This program reads important new articles for me


# In[1]:


# Imports the libaries, cause I'm too lazy to reinvent the wheel
import nltk
from newspaper import Article


# In[2]:


# Grabs the urls
url1 = 'https://www.washingtonpost.com/technology/2019/07/17/you-downloaded-faceapp-heres-what-youve-just-done-your-privacy/'
url2 = 'https://www.marketwatch.com/story/stock-markets-historic-bounce-may-signal-near-term-bottom-but-a-retest-of-the-low-like-1987-and-2008-is-still-a-possibility-2020-03-25?mod=home-page'
article1 = Article(url1)
article2 = Article(url2)


# In[5]:


# NLP, Natural language processesing 
article1.download()
article2.download()
article1.parse()
article2.parse()
nltk.download('punkt')
article1.nlp()
article2.nlp()


# In[6]:


# Authors
article1.authors
article2.authors


# In[8]:


# publish date
article1.publish_date
article2.publish_date


# In[9]:


# Top image
article1.top_image
article2.top_image


# In[16]:


# Get a summary of the article
print(article1.summary)
print("\n" + article2.summary)


# In[ ]:




