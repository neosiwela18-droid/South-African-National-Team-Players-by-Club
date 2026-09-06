import pandas as pd
import matplotlib.pyplot as plt
x = []
y = []

df = pd.read_csv("players_lookup.csv")
class ClassName:
    def __init__(self, country):
        self.country = df[df["country"] == country].groupby('club_name').size()

    def sample_method(self): 
        for i, m in self.country.items():
            x.append(i)
            y.append(m)
                        
love = ClassName('South Africa')
love.sample_method()

plt.barh(x,y)
plt.yticks(rotation=30)
plt.grid(True, alpha = 0.4)
plt.xlabel("Number of Players", fontweight='bold')
plt.ylabel("Club", fontweight='bold', labelpad=20)
plt.title("South African National Team Players by Club", fontweight='bold')

plt.show()
