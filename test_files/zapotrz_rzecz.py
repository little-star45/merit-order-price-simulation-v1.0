import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.dates as mdates
import datetime as dt
import seaborn as sns

data = pd.read_excel(r'C:\Users\48530\Desktop\zap_energ\dem_kopia.xlsx',sheet_name='demand')
df = pd.DataFrame(data, columns=['Data', 'Rzeczywiste zapotrzebowanie KSE [GW]', 'dummy','Godz', 'Dni'])
#print(df)
x = df['Data']

y = df['Rzeczywiste zapotrzebowanie KSE [GW]']

fig,ax = plt.subplots()
plt.scatter(x, y, c="hotpink", s=4, alpha=0.65)

plt.grid(color = 'grey', linestyle = '--', linewidth = 0.45, alpha = 0.5)

dem = df['Rzeczywiste zapotrzebowanie KSE [GW]']
ax.axvspan(dt.date(2022, 6, 1), dt.date(2022, 9, 1), facecolor='#FBFE73', alpha=0.2)
ax.axvspan(dt.date(2022, 9, 1), dt.date(2022, 12, 1), facecolor='#E16C4A', alpha=0.2)
ax.axvspan(dt.date(2022, 12, 1), dt.date(2023, 3, 1), facecolor='#4AB5E1', alpha=0.2)
ax.axvspan(dt.date(2023, 3, 1), dt.date(2023, 5, 31), facecolor='#88FE73', alpha=0.2)
min = plt.axhline(y = min(dem), color = 'r', linestyle = ':', linewidth = 1.5, alpha = 0.7, label="min demand")
max = plt.axhline(y = max(dem), color = 'b', linestyle = ':', linewidth = 1.5, alpha = 0.7, label='max demand')



plt.title("Real electricity demand in Poland 01.06.2022-31.05.2023")
plt.xlabel("Time [dd:mm:yy]")
plt.ylabel("Electricity demand [GW]")

ax.xaxis.set_major_locator(mdates.MonthLocator())

ax.set_xlim([dt.date(2022, 6, 1), dt.date(2023, 5, 31)])
plt.yticks(np.arange(11,28, 0.5))

df['Data'] = pd.to_datetime(df['Data'])
df.head()

df['MA12'] = data['Rzeczywiste zapotrzebowanie KSE [GW]'].rolling(window = 24, min_periods=1).mean()

# plot the data and MA
#import plotly.express as px
plt.scatter(df["Data"],df["MA12"],s=4, alpha=0.65, label='mean (roll:24)')
plt.legend()
# To show the plot

plt.show()

sns.distplot(a=df['Rzeczywiste zapotrzebowanie KSE [GW]'], hist=True, bins=30, kde=True)

plt.xticks(np.arange(9.5,29, 0.7))
plt.grid(color = 'grey', linestyle = '--', linewidth = 0.45, alpha = 0.5)

plt.show()

#import random
import datetime
#get_colors = lambda n: ["#%06x" % random.randint(0, 0xFFFFFF) for _ in range(n)]
#line_colors= get_colors(50)

kolory = ["#FF0000", "#00FF00", "#0000FF", "#B0E0E6", "#FF00FF", "#00FFFF", "#FFA500",
    "#800080", "#008080", "#808000", "#FFC0CB", "#800000", "#008000", "#000080",
    "#FFD700", "#A52A2A", "#808080", "#FF6347", "#ADFF2F", "#F0E68C", "#DDA0DD",
    "#D2691E", "#8B0000", "#32CD32", "#800000", "#D8BFD8", "#4B0082", "#FF8C00",
    "#48D1CC", "#7B68EE", "#FF69B4", "#2E8B57", "#B8860B"]

# Plotting both the curves simultaneously
fig,ax = plt.subplots()
zapotrz = df['Rzeczywiste zapotrzebowanie KSE [GW]']
data = df['Godz']
# for i in range(0,350,24):
#     plt.plot(data[0+i:24+i], zapotrz[0+i:24+i], color='r')
# To load the display window
plt.xticks(np.arange(1,23, 1))
ax.set_xlim(1,23)
plt.yticks(np.arange(11,27.5, 0.5))
ax.set_ylim(11,27.5)
plt.grid(color = 'grey', linestyle = '--', linewidth = 0.45, alpha = 0.5)
licz = 0
legenda = []
dni = df['Dni']

for i in range(0,720,24):
    plt.plot(data[0+i:24+i], zapotrz[0+i:24+i], color=kolory[licz])
    licz+=1
    legenda.append(dni[i].date())
plt.title('06-2022')
#plt.legend(legenda)
plt.legend(labels=legenda,loc='upper right', ncol=1, bbox_to_anchor=(1.13, 1.04))
plt.show()

fig2,ax2 = plt.subplots()
plt.xticks(np.arange(1,23, 1))
ax2.set_xlim(1,23)
plt.yticks(np.arange(11,27.5, 0.5))
ax2.set_ylim(11,27.5)
plt.grid(color = 'grey', linestyle = '--', linewidth = 0.45, alpha = 0.5)
legenda = []
licz=0
for i in range(720,1464,24):
    plt.plot(data[0+i:0+24+i], zapotrz[0+i:0+24+i], color=kolory[licz])
    licz+=1
    legenda.append(dni[i].date())

plt.title('07-2022')
#plt.legend(legenda)
plt.legend(labels=legenda,loc='upper right', ncol=1, bbox_to_anchor=(1.13, 1.04))

plt.show()

fig3,ax3 = plt.subplots()
plt.xticks(np.arange(1,23, 1))
ax3.set_xlim(1,23)
plt.yticks(np.arange(11,27.5, 0.5))
ax3.set_ylim(11,27.5)
plt.grid(color = 'grey', linestyle = '--', linewidth = 0.45, alpha = 0.5)
legenda = []
licz=0
for i in range(1464,2185,24):
    plt.plot(data[0+i:0+24+i], zapotrz[0+i:0+24+i], color=kolory[licz])
    licz+=1
    legenda.append(dni[i].date())

#print(f"data[1464:  {data[1464]},zapotrz[1464:  {zapotrz[1464]},zapotrz[2209]:  {zapotrz[2209]} ")

plt.title('08-2022')
#plt.legend(legenda)
plt.legend(labels=legenda,loc='upper right', ncol=1, bbox_to_anchor=(1.13, 1.04))

plt.show()

fig4,ax4 = plt.subplots()
plt.xticks(np.arange(1,23, 1))
ax4.set_xlim(1,23)
plt.yticks(np.arange(11,27.5, 0.5))
ax4.set_ylim(11,27.5)
plt.grid(color = 'grey', linestyle = '--', linewidth = 0.45, alpha = 0.5)
legenda = []
licz=0
for i in range(2184,2927,24):
    plt.plot(data[0+i:0+24+i], zapotrz[0+i:0+24+i], color=kolory[licz])
    licz+=1
    legenda.append(dni[i].date())

plt.title('09-2022')
#plt.legend(legenda)
plt.legend(labels=legenda,loc='upper right', ncol=1, bbox_to_anchor=(1.13, 1.04))
plt.show()

fig5,ax5 = plt.subplots()
plt.xticks(np.arange(1,23, 1))
ax5.set_xlim(1,23)
plt.yticks(np.arange(11,27.5, 0.5))
ax5.set_ylim(11,27.5)
plt.grid(color = 'grey', linestyle = '--', linewidth = 0.45, alpha = 0.5)
legenda = []
licz=0
for i in range(2928,3650,24):
    plt.plot(data[0+i:0+24+i], zapotrz[0+i:0+24+i], color=kolory[licz])
    licz+=1
    legenda.append(dni[i].date())
plt.title('10-2022')
#plt.legend(legenda)
plt.legend(labels=legenda,loc='upper right', ncol=1, bbox_to_anchor=(1.13, 1.04))

plt.show()

fig6,ax6 = plt.subplots()
plt.xticks(np.arange(1,23, 1))
ax6.set_xlim(1,23)
plt.yticks(np.arange(11,27.5, 0.5))
ax6.set_ylim(11,27.5)
plt.grid(color = 'grey', linestyle = '--', linewidth = 0.45, alpha = 0.5)
legenda = []
licz=0
for i in range(3673,4393,24):
    plt.plot(data[0+i:0+24+i], zapotrz[0+i:0+24+i], color=kolory[licz])
    licz+=1
    legenda.append(dni[i].date())

plt.title('11-2022')
#plt.legend(legenda)
plt.legend(labels=legenda,loc='upper right', ncol=1, bbox_to_anchor=(1.13, 1.04))

plt.show()

fig7,ax7 = plt.subplots()
plt.xticks(np.arange(1,23, 1))
ax7.set_xlim(1,23)
plt.yticks(np.arange(11,27.5, 0.5))
ax7.set_ylim(11,27.5)
plt.grid(color = 'grey', linestyle = '--', linewidth = 0.45, alpha = 0.5)
legenda = []
licz=0
for i in range(4393,5137,24):
    plt.plot(data[0+i:0+24+i], zapotrz[0+i:0+24+i], color=kolory[licz])
    licz+=1
    legenda.append(dni[i].date())

plt.title('12-2022')
#plt.legend(legenda)
plt.legend(labels=legenda,loc='upper right', ncol=1, bbox_to_anchor=(1.13, 1.04))

plt.show()

fig8,ax8 = plt.subplots()
plt.xticks(np.arange(1,23, 1))
ax8.set_xlim(1,23)
plt.yticks(np.arange(11,27.5, 0.5))
ax8.set_ylim(11,27.5)
plt.grid(color = 'grey', linestyle = '--', linewidth = 0.45, alpha = 0.5)
legenda = []
licz=0
for i in range(5137,5881,24):
    plt.plot(data[0+i:0+24+i], zapotrz[0+i:0+24+i], color=kolory[licz])
    licz+=1
    legenda.append(dni[i].date())


plt.title('01-2023')
#plt.legend(legenda)
plt.legend(labels=legenda,loc='upper right', ncol=1, bbox_to_anchor=(1.13, 1.04))

plt.show()

fig9,ax9 = plt.subplots()
plt.xticks(np.arange(1,23, 1))
ax9.set_xlim(1,23)
plt.yticks(np.arange(11,27.5, 0.5))
ax9.set_ylim(11,27.5)
plt.grid(color = 'grey', linestyle = '--', linewidth = 0.45, alpha = 0.5)
legenda = []
licz=0
for i in range(5881,6552,24):
    plt.plot(data[0+i:0+24+i], zapotrz[0+i:0+24+i], color=kolory[licz])
    licz+=1
    legenda.append(dni[i].date())

plt.title('02-2023')
#plt.legend(legenda)
plt.legend(labels=legenda,loc='upper right', ncol=1, bbox_to_anchor=(1.13, 1.04))

plt.show()



fig11,ax11 = plt.subplots()
plt.xticks(np.arange(1,23, 1))
ax11.set_xlim(1,23)
plt.yticks(np.arange(11,27.5, 0.5))
ax11.set_ylim(11,27.5)
plt.grid(color = 'grey', linestyle = '--', linewidth = 0.45, alpha = 0.5)
legenda = []
licz=0
for i in range(7296,8016,24):
    plt.plot(data[0+i:0+24+i], zapotrz[0+i:0+24+i], color=kolory[licz])
    licz+=1
    legenda.append(dni[i].date())

plt.title('04-2023')
#plt.legend(legenda)
plt.legend(labels=legenda,loc='upper right', ncol=1, bbox_to_anchor=(1.13, 1.04))

plt.show()

fig12,ax12 = plt.subplots()
plt.xticks(np.arange(1,23, 1))
ax12.set_xlim(1,23)
plt.yticks(np.arange(11,27.5, 0.5))
ax12.set_ylim(11,27.5)
plt.grid(color = 'grey', linestyle = '--', linewidth = 0.45, alpha = 0.5)
legenda = []
licz=0
for i in range(8016,8759,24):
    plt.plot(data[0+i:0+24+i], zapotrz[0+i:0+24+i], color=kolory[licz])
    licz+=1
    legenda.append(dni[i].date())

plt.title('05-2023')
#plt.legend(legenda)
plt.legend(labels=legenda,loc='upper right', ncol=1, bbox_to_anchor=(1.13, 1.04))

plt.show()
#
data = pd.read_excel(r'C:\Users\48530\Desktop\zap_energ\ZAP_KSE_20230301to20230331_20230331230553.xlsx',sheet_name='demand')
df = pd.DataFrame(data, columns=['Rzeczywiste zapotrzebowanie KSE [GW]', 'dummy','Godz', 'Dni'])
dni = df['Dni']
data = df['Godz']
zapotrz = df['Rzeczywiste zapotrzebowanie KSE [GW]']
fig15,ax15 = plt.subplots()
plt.xticks(np.arange(1,23, 1))
ax15.set_xlim(1,23)
plt.yticks(np.arange(11,27.5, 0.5))
ax15.set_ylim(11,27.5)
plt.grid(color = 'grey', linestyle = '--', linewidth = 0.45, alpha = 0.5)
legenda = []
licz=0

for i in range(0,744,24):
    plt.plot(data[i:24+i], zapotrz[i:24+i], color=kolory[licz])
    licz+=1
    legenda.append(dni[i].date())
    print(data[0+i:0+24+i],zapotrz[0 + i:0 + 24 + i])

plt.title('03-2023')
#plt.legend(legenda)
plt.legend(labels=legenda,loc='upper right', ncol=1, bbox_to_anchor=(1.13, 1.04))

plt.show()