import pandas as pd
data={"Post_ID": [1,2,3,4,5,6,7,8,9,10],
    "Category": ["Meme","Product","Meme","Education","Product",
                 "Education","Meme","Education","Product","Meme"],
    "Likes": [120, 340, 560, None, 230, 180, 400, 210, None, 500],
    "Shares": [30, 50, 100, 25, None, 20, 70, 40, 60, None],
    "Comments": [10, 20, None, 15, 12, 18, 25, None, 14, 30]}
df=pd.DataFrame(data)
print("\n===Raw Data===")
print(df)

print("\nMissing Values Summary:")
print(df.isnull().sum())

df['Likes'].fillna(df['Likes'].median(),inplace=True)
df['Shares'].fillna(df['Shares'].median(),inplace=True)
df['Comments'].fillna(df['Comments'].median(),inplace=True)

df['Engagements']=df['Likes']+df['Shares']+df['Comments']
print(df)
import numpy as np
Likes=df['Likes'].to_numpy()
Shares=df['Shares'].to_numpy()
Comments=df['Comments'].to_numpy()
print("\n===Numpy Based Analysis===")
print(f"Total Likes:{np.sum(Likes)}")
print(f"Total Average:{np.median(Likes):.2f}")
print(f"Min and Max Likes:{np.min(Likes)}-{np.max(Likes)}")
print(f"Total Shares:{np.sum(Shares)}")
print(f"Total Average:{np.median(Shares):.2f}")
print(f"Min and Max:{np.min(Shares)}-{np.max(Shares)}")
print(f"Total Comments:{np.sum(Comments)}")
print(f"Total Average:{np.median(Comments):.2f}")
print(f"Min and Max:{np.min(Comments)}-{np.max(Comments)}")


summary=df.groupby("Category")[["Likes","Shares","Comments","Engagements"]].agg(['median','max','min'])
print("\n====Summary Statistic by Category====")
print(summary)
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
categories = df["Category"].unique()
likes_data = [df[df["Category"]==cat]["Likes"] for cat in categories]
plt.boxplot(likes_data, labels=categories, patch_artist=True)
plt.title("Distribution of Likes by Post Category", fontsize=14)
plt.xlabel("Category")
plt.ylabel("Likes")
plt.show()
plt.figure(figsize=(8,5))
avg_engagement=df.groupby('Category')['Engagements'].mean()
avg_engagement.plot(kind='bar',color='skyblue',edgecolor='red')
plt.title('Average Engagements by Post')
plt.xlabel('Category')
plt.ylabel('Engagements')
plt.grid(True)
plt.show()
import matplotlib.pyplot as plt

# 1. Category distribution (counts of posts per category)
category_distribution = df["Category"].value_counts()

# 2. Engagement breakdown (total likes, shares, comments)
engagement_distribution = {
    "Likes": df["Likes"].sum(),
    "Shares": df["Shares"].sum(),
    "Comments": df["Comments"].sum()
}

# Plot side-by-side pie charts
fig, axes = plt.subplots(1, 2, figsize=(12,6))

# Pie chart 1 - Categories
axes[0].pie(category_distribution, labels=category_distribution.index,
            autopct='%1.1f%%', startangle=140, shadow=True)
axes[0].set_title("Distribution of Post Categories")

# Pie chart 2 - Likes, Shares, Comments
axes[1].pie(engagement_distribution.values(), labels=engagement_distribution.keys(),
            autopct='%1.1f%%', startangle=140, shadow=True)
axes[1].set_title("Overall Engagement Breakdown")

plt.tight_layout()
plt.show()
