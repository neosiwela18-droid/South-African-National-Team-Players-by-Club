# South-African-National-Team-Players-by-Club

## What the code does

1. **Load data**: `pd.read_csv("players_lookup.csv")` reads the CSV into a DataFrame `df`.
2. **Filter & clean**: Inside `ClassName.__init__`, `df[df["country"] == country]` filters rows to only the given country ("South Africa").
3. **Aggregate**: `.groupby('club_name').size()` counts how many players belong to each club — this is your cleaning/summarizing step, collapsing raw rows into club-level counts.
4. **Reshape for plotting**: `sample_method()` loops through the grouped Series (`self.country.items()`) and splits it into two parallel lists: `x` = club names, `y` = player counts.
5. **Display**: `plt.barh(x, y)` draws a horizontal bar chart, with labels, rotated tick marks, grid, and a title added for readability.

<img width="1920" height="959" alt="234" src="https://github.com/user-attachments/assets/1d5961d3-b1c1-40da-8f1f-312ceff7323b" />
