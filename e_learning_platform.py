# -*- coding: utf-8 -*-
"""E -LEARNING PLATFORM -(Gajanan Purud)

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wyf5gAxRf6DjjbtVjDhEshUymF1ZwqUg

## Import necessary libraries
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# importing the dependencies
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import numpy as np
import warnings
warnings.filterwarnings("ignore")

"""## Load the dataset"""

dataset_path = '/content/Online_Courses (1).csv'
data = pd.read_csv(dataset_path)

"""## Displaying the first few rows of the dataset"""

print("First 5 rows of the dataset:")
print(data.head())

"""## data type information and missing values"""

print("\nData type information:")
print(data.info())

# Display summary statistics for numerical columns
print("\nSummary statistics:")
print(data.describe())

for col in data.columns:
  print(col)

"""## Exploratory Data Analysis (EDA)"""

data

"""## Analyzing Popular Courses"""

# Scatter plot of course ratings vs. number of views
plt.figure(figsize=(8, 6))
sns.scatterplot( data=data)
plt.title("Course Ratings vs. Number of Views")
plt.xlabel("Rating")
plt.ylabel("Number of Views")
plt.show()

"""## Segmenting Data by Language"""

# Bar plot showing course categories by language
plt.figure(figsize=(12, 6))
sns.countplot( data=data)
plt.title("Course Categories by Language")
plt.xlabel("Category")
plt.ylabel("Count")
plt.legend(title='Language')
plt.show()

# Analyze further based on the data
print()
print(data)

# Distribution of course ratings
plt.figure(figsize=(8, 6))
sns.histplot(data, kde=True)
plt.title("Distribution of Course Ratings")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.show()

"""## Analyzing Course Categories"""

# Count plot of course categories
plt.figure(figsize=(18, 12))
sns.countplot( data=data)
plt.title("Count of Course Categories")
plt.xlabel("Category")
plt.ylabel("Count")
plt.show()

"""## Short Course Introduction"""

# Display the first few rows of short course introductions
print("Short Course Introductions:")
print(data[[]].head(5))

"""## Popular Skills"""

# Split 'skills' by comma and create a count plot of the most common skills


plt.figure(figsize=(12, 6))
sns.histplot(data, kde=True)
plt.title("Top 10 Skills in Courses")
plt.xlabel("Count")
plt.ylabel("Skill")
plt.show()

# If there's a 'date_added' or similar field, analyze trends over time
if 'date_added' in data.columns:
    data['date_added'] = pd.to_datetime(data['date_added'])
    data['year'] = data['date_added'].dt.year
    plt.figure(figsize=(12, 6))
    sns.countplot(x='year', data=data)
    plt.title("Courses Added Over Time")
    plt.xlabel("Year")
    plt.ylabel("Number of Courses")
    plt.show()

# If multiple sites host courses, analyze them by site
if 'site' in data.columns:
    plt.figure(figsize=(12, 6))
    sns.countplot(x='site', data=data)
    plt.title("Course Distribution by Site")
    plt.xlabel("Site")
    plt.ylabel("Count")
    plt.show()

"""# Conclusion of E-Learning Platform

Conclusion of E-Learning Platform Based on Market Segmentation and Analysis

Market segmentation and analysis are crucial in understanding the dynamics of the e-learning platform market. Here is a conclusion derived from a comprehensive study that considers several segmentation factors and market trends:

E-learning platforms offer vast opportunities in a rapidly growing market. Effective market segmentation and analysis provide a pathway to success by addressing the unique needs of different user groups. Platforms that combine tailored content, technology innovation, and strong partnerships are well-positioned to thrive in this competitive landscape. By continuously adapting to market trends and user feedback, e-learning platforms can create lasting value and impact in the education sector

Strategic Focus

To succeed in this dynamic environment, e-learning platforms should focus on:

- Tailored Content:
  Create content that meets the specific needs of each segment, including industry-specific courses, professional development, and academic programs.

- Localized Content:
  Invest in localization to reach global audiences, ensuring content is accessible and relevant across different regions.

- Technology-Driven Solutions:
  Embrace technology to enhance user experiences, utilizing AI, VR/AR, and data analytics to create personalized and engaging learning pathways.

- Collaborative Partnerships:
  Build relationships with educational institutions, industry leaders, and corporate clients to expand the platform's reach and credibility.

- Strong Compliance and Security:
  Maintain strict compliance with regulations and ensure data security to foster user trust.

By embracing these strategic focus areas, e-learning platforms can achieve sustainable growth and make a significant impact on the education landscape. As the market continues to evolve, platforms that remain adaptable and innovative will be best positioned for long-term success.
"""

