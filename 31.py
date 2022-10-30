#Name:Mahim Ali
#Email:mahim.ali32@myhunter.cuny.edu
#Date:October 30,2022
#This program prints internet users in population percentage

import matplotlib.pyplot as plt
import pandas as pd

internet = pd.read_csv('country_internet.csv')
output = input("Enter outputfile name: ")
internet['Percentage'] = (internet['Internet users']/internet['Population'])*100
internet.plot(x = 'Country', y = 'Percentage')
print("Maximum percentage of all countries: ", internet['Country'].value_counts()[:1],
internet['Percentage'].max(), "%")
fig = plt.gcf()
fig.savefig(output)
