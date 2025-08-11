# from 24 file 

# 7143CEM Programming for Data Science
# Live coding -- Week 12 -- Friday

# Reminder to Mark --> RECORD SESSION


# REVISION


#---
# 1. Practice Exam (current format)

# Q3
nobel['Category'].value_counts()
nobel.Category.value_counts()

AAA = nobel.query("IndivOrg=='Individual'")
AAA['Name'].value_counts()

BBB = nobel.query("Name=='Marie Curie'")
BBB[['Year','Category','Motivation']]

CCC = nobel.query("Category=='Peace'")
DDD = CCC.groupby('Continent')
DDD['PrizeAmount'].mean()

# Q4

#---
# 2. GDPR Cheatsheet (Lab 9)

#---
# 3. Any requests

# -- the end --
