import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.dates as mdates
import datetime as dt
import seaborn as sns

data = pd.read_excel(r'C:\Users\48530\Desktop\zap_energ\dem.xlsx',sheet_name='demand')
df = pd.DataFrame(data, columns=['Data', 'Rzeczywiste zapotrzebowanie KSE [GW]', 'dummy','Godz', 'Dni', 'DZIEN_TYG','nazwa_dzien'])

x = df['Data']

y = df['Rzeczywiste zapotrzebowanie KSE [GW]']

dem = df['Rzeczywiste zapotrzebowanie KSE [GW]']

df['Data'] = pd.to_datetime(df['Data'])
df.head()

nazwa_dnia=df['nazwa_dzien']

#kolory = ["#FF0000", "#00FF00", "#0000FF", "#B0E0E6", "#FF00FF", "#00FFFF", "#FFA500",
    # "#800080", "#008080", "#808000", "#FFC0CB", "#800000", "#008000", "#000080",
    # "#FFD700", "#A52A2A", "#808080", "#FF6347", "#ADFF2F", "#F0E68C", "#DDA0DD",
    # "#D2691E", "#8B0000", "#32CD32", "#800000", "#D8BFD8", "#4B0082", "#FF8C00",
    # "#48D1CC", "#7B68EE", "#FF69B4", "#2E8B57", "#B8860B"]

kolory = [
    "#800080",  # Purple
    "#FFA07A",  # Light Salmon
    "#6fa8dc",  # Teal
    "#FF1493",  # Deep Pink
    "#0000FF",  # Maroon
    "#1eb065",  # Gold
    "#800000",  # Dark Olive Green
]

# Plotting both the curves simultaneously
fig,ax = plt.subplots(2,2)
zapotrz = df['Rzeczywiste zapotrzebowanie KSE [GW]']
data = df['Godz']
licz = 0
legenda = []
dni = df['Dni']
dzien_tyg = df['DZIEN_TYG']

#PONIEDZIALKI
# for i in range(0,3676,24): #pon-2
#     if dzien_tyg[i] == 2:
#         plt.plot(data[0+i:24+i], zapotrz[0+i:24+i], color=kolory[licz])
#         licz+=1
#         legenda.append(dni[i].date())
it = 0
it1 = 0
zakr = 0
tydz_wcz = 0
#----CZERWIEC---
for i in range(0,671,24): #pon-2
    ax[it, it1].plot(data[0 + i:24 + i], zapotrz[0 + i:24 + i], color=kolory[licz])
    licz += 1
    legenda.append(nazwa_dnia[i])
    if i+24== (7*24):
        ax[it, it1].set_xticks(np.arange(1, 23, 1))
        ax[it, it1].set_xlim(1, 23)
        ax[it, it1].set_yticks(np.arange(11, 27.5, 1))
        ax[it, it1].set_ylim(11, 27.5)
        ax[it, it1].set_title(f"{dni[tydz_wcz].date()} - {dni[i].date()}")
        ax[it, it1].legend(labels=legenda, loc='upper right', ncol=3, fontsize =8)
        ax[it, it1].grid(color='grey', linestyle='--', linewidth=0.45, alpha=0.5)
        tydz_wcz = i+24
        it = 0
        it1 = 1
        legenda.clear()
        licz = 0
        print("1----")
        continue
    if i+24 == (2*7*24):

        ax[it, it1].set_xticks(np.arange(1, 23, 1))
        ax[it, it1].set_xlim(1, 23)
        ax[it, it1].set_yticks(np.arange(11, 27.5, 1))
        ax[it, it1].set_ylim(11, 27.5)
        ax[it, it1].set_title(f"{dni[tydz_wcz].date()} - {dni[i].date()}")
        ax[it, it1].legend(labels=legenda, loc='upper right', ncol=3, fontsize =8)
        ax[it, it1].grid(color='grey', linestyle='--', linewidth=0.45, alpha=0.5)
        tydz_wcz = i+24
        it = 1
        it1 = 0
        legenda.clear()
        licz = 0
        print("2---")
        continue
    if i+24 == 3*7*24:

        ax[it, it1].set_xticks(np.arange(1, 23, 1))
        ax[it, it1].set_xlim(1, 23)
        ax[it, it1].set_yticks(np.arange(11, 27.5, 1))
        ax[it, it1].set_ylim(11, 27.5)
        ax[it, it1].set_title(f"{dni[tydz_wcz].date()} - {dni[i].date()}")
        ax[it, it1].legend(labels=legenda, loc='upper right', ncol=3, fontsize =8)
        ax[it, it1].grid(color='grey', linestyle='--', linewidth=0.45, alpha=0.5)
        tydz_wcz = i+24
        it = 1
        it1 = 1
        legenda.clear()
        licz = 0
        print("3----")
        continue
    if i+24 == 4*7*24:
        ax[it, it1].set_xticks(np.arange(1, 23, 1))
        ax[it, it1].set_xlim(1, 23)
        ax[it, it1].set_yticks(np.arange(11, 27.5, 1))
        ax[it, it1].set_ylim(11, 27.5)
        ax[it, it1].set_title(f"{dni[tydz_wcz].date()} - {dni[i].date()}")
        ax[it, it1].legend(labels=legenda, loc='upper right', ncol=3, fontsize =8)
        ax[it, it1].grid(color='grey', linestyle='--', linewidth=0.45, alpha=0.5)
        tydz_wcz = i+24
        legenda.clear()
        licz = 0
        print("4-----")
        continue

for ax1 in ax.flat:
    ax1.set(xlabel="Time [hour]", ylabel="Electricity demand [GW]")

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax1 in ax.flat:
    ax1.label_outer()
plt.show()


fig,ax = plt.subplots(2,2)
zapotrz = df['Rzeczywiste zapotrzebowanie KSE [GW]']
data = df['Godz']
licz = 0
legenda = []
dni = df['Dni']
dzien_tyg = df['DZIEN_TYG']

licz=0
it = 0
it1 = 0
zakr = 0
tydz_wcz = 2208
#---CZERWIEC---
for i in range(2208,2880,24): #pon-2
    ax[it, it1].plot(data[0 + i:24 + i], zapotrz[0 + i:24 + i], color=kolory[licz])
    print(data[0 + i:24 + i])
    licz += 1
    legenda.append(nazwa_dnia[i])
    print(dni[i].date())
    if i+24== (2376):
        ax[it, it1].set_xticks(np.arange(1, 23, 1))
        ax[it, it1].set_xlim(1, 23)
        ax[it, it1].set_yticks(np.arange(11, 27.5, 1))
        ax[it, it1].set_ylim(11, 27.5)
        ax[it, it1].set_title(f"{dni[tydz_wcz].date()} - {dni[i].date()}")
        ax[it, it1].legend(labels=legenda, loc='upper right', ncol=3, fontsize =8)
        ax[it, it1].grid(color='grey', linestyle='--', linewidth=0.45, alpha=0.5)
        tydz_wcz = i+24
        it = 0
        it1 = 1
        legenda.clear()
        licz = 0
        print("1----")
        continue
    if i+24 == (2544):

        ax[it, it1].set_xticks(np.arange(1, 23, 1))
        ax[it, it1].set_xlim(1, 23)
        ax[it, it1].set_yticks(np.arange(11, 27.5, 1))
        ax[it, it1].set_ylim(11, 27.5)
        ax[it, it1].set_title(f"{dni[tydz_wcz].date()} - {dni[i].date()}")
        ax[it, it1].legend(labels=legenda, loc='upper right', ncol=3, fontsize =8)
        ax[it, it1].grid(color='grey', linestyle='--', linewidth=0.45, alpha=0.5)
        tydz_wcz = i+24
        it = 1
        it1 = 0
        legenda.clear()
        licz = 0
        print("2---")
        continue
    if i+24 == 2712:

        ax[it, it1].set_xticks(np.arange(1, 23, 1))
        ax[it, it1].set_xlim(1, 23)
        ax[it, it1].set_yticks(np.arange(11, 27.5, 1))
        ax[it, it1].set_ylim(11, 27.5)
        ax[it, it1].set_title(f"{dni[tydz_wcz].date()} - {dni[i].date()}")
        ax[it, it1].legend(labels=legenda, loc='upper right', ncol=3, fontsize =8)
        ax[it, it1].grid(color='grey', linestyle='--', linewidth=0.45, alpha=0.5)
        tydz_wcz = i+24
        it = 1
        it1 = 1
        legenda.clear()
        licz = 0
        print("3----")
        continue
    if i+24 == 2880:
        ax[it, it1].set_xticks(np.arange(1, 23, 1))
        ax[it, it1].set_xlim(1, 23)
        ax[it, it1].set_yticks(np.arange(11, 27.5, 1))
        ax[it, it1].set_ylim(11, 27.5)
        ax[it, it1].set_title(f"{dni[tydz_wcz].date()} - {dni[i].date()}")
        ax[it, it1].legend(labels=legenda, loc='upper right', ncol=3, fontsize =8)
        ax[it, it1].grid(color='grey', linestyle='--', linewidth=0.45, alpha=0.5)
        tydz_wcz = i+24
        legenda.clear()
        licz = 0
        print("4-----")
        continue

for ax1 in ax.flat:
    ax1.set(xlabel="Time [hour]", ylabel="Electricity demand [GW]")

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax1 in ax.flat:
    ax1.label_outer()
plt.show()

fig,ax = plt.subplots(2,2)
zapotrz = df['Rzeczywiste zapotrzebowanie KSE [GW]']
data = df['Godz']
licz = 0
legenda = []
dni = df['Dni']
dzien_tyg = df['DZIEN_TYG']

licz=0
it = 0
it1 = 0
zakr = 0
tydz_wcz = 4393
#---CZERWIEC---
for i in range(4393,5064,24): #pon-2
    ax[it, it1].plot(data[0 + i:24 + i], zapotrz[0 + i:24 + i], color=kolory[licz])
    print(data[0 + i:24 + i])
    licz += 1
    legenda.append(nazwa_dnia[i])
    print(dni[i].date())
    if i+24== (4393+(7*24)):
        ax[it, it1].set_xticks(np.arange(1, 23, 1))
        ax[it, it1].set_xlim(1, 23)
        ax[it, it1].set_yticks(np.arange(11, 27.5, 1))
        ax[it, it1].set_ylim(11, 27.5)
        ax[it, it1].set_title(f"{dni[tydz_wcz].date()} - {dni[i].date()}")
        ax[it, it1].legend(labels=legenda, loc='lower right', ncol=3, fontsize =8)
        ax[it, it1].grid(color='grey', linestyle='--', linewidth=0.45, alpha=0.5)
        tydz_wcz = i+24
        it = 0
        it1 = 1
        legenda.clear()
        licz = 0
        print("1----")
        continue
    if i+24 == (4393+2*(7*24)):

        ax[it, it1].set_xticks(np.arange(1, 23, 1))
        ax[it, it1].set_xlim(1, 23)
        ax[it, it1].set_yticks(np.arange(11, 27.5, 1))
        ax[it, it1].set_ylim(11, 27.5)
        ax[it, it1].set_title(f"{dni[tydz_wcz].date()} - {dni[i].date()}")
        ax[it, it1].legend(labels=legenda, loc='lower right', ncol=3, fontsize =8)
        ax[it, it1].grid(color='grey', linestyle='--', linewidth=0.45, alpha=0.5)
        tydz_wcz = i+24
        it = 1
        it1 = 0
        legenda.clear()
        licz = 0
        print("2---")
        continue
    if i+24 == (4393+3*(7*24)):

        ax[it, it1].set_xticks(np.arange(1, 23, 1))
        ax[it, it1].set_xlim(1, 23)
        ax[it, it1].set_yticks(np.arange(11, 27.5, 1))
        ax[it, it1].set_ylim(11, 27.5)
        ax[it, it1].set_title(f"{dni[tydz_wcz].date()} - {dni[i].date()}")
        ax[it, it1].legend(labels=legenda, loc='lower right', ncol=3, fontsize =8)
        ax[it, it1].grid(color='grey', linestyle='--', linewidth=0.45, alpha=0.5)
        tydz_wcz = i+24
        it = 1
        it1 = 1
        legenda.clear()
        licz = 0
        print("3----")
        continue
    if i+24 == (4393+4*(7*24)):
        ax[it, it1].set_xticks(np.arange(1, 23, 1))
        ax[it, it1].set_xlim(1, 23)
        ax[it, it1].set_yticks(np.arange(11, 27.5, 1))
        ax[it, it1].set_ylim(11, 27.5)
        ax[it, it1].set_title(f"{dni[tydz_wcz].date()} - {dni[i].date()}")
        ax[it, it1].legend(labels=legenda, loc='lower right', ncol=3, fontsize =8)
        ax[it, it1].grid(color='grey', linestyle='--', linewidth=0.45, alpha=0.5)
        tydz_wcz = i+24
        legenda.clear()
        licz = 0
        print("4-----")
        continue

for ax1 in ax.flat:
    ax1.set(xlabel="Time [hour]", ylabel="Electricity demand [GW]")

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax1 in ax.flat:
    ax1.label_outer()
plt.show()
#-----MARZEC 2023
fig,ax = plt.subplots(2,2)
zapotrz = df['Rzeczywiste zapotrzebowanie KSE [GW]']
data = df['Godz']
licz = 0
legenda = []
dni = df['Dni']
dzien_tyg = df['DZIEN_TYG']

licz=0
it = 0
it1 = 0
zakr = 0
tydz_wcz = 6553
#---CZERWIEC---
for i in range(6553,7224,24): #pon-2
    ax[it, it1].plot(data[0 + i:24 + i], zapotrz[0 + i:24 + i], color=kolory[licz])
    print(data[0 + i:24 + i])
    licz += 1
    legenda.append(nazwa_dnia[i])
    print(dni[i].date())
    if i+24== (6553+(7*24)):
        ax[it, it1].set_xticks(np.arange(1, 23, 1))
        ax[it, it1].set_xlim(1, 23)
        ax[it, it1].set_yticks(np.arange(11, 27.5, 1))
        ax[it, it1].set_ylim(11, 27.5)
        ax[it, it1].set_title(f"{dni[tydz_wcz].date()} - {dni[i].date()}")
        ax[it, it1].legend(labels=legenda, loc='lower right', ncol=3, fontsize =8)
        ax[it, it1].grid(color='grey', linestyle='--', linewidth=0.45, alpha=0.5)
        tydz_wcz = i+24
        it = 0
        it1 = 1
        legenda.clear()
        licz = 0
        print("1----")
        continue
    if i+24 == (6553+2*(7*24)):

        ax[it, it1].set_xticks(np.arange(1, 23, 1))
        ax[it, it1].set_xlim(1, 23)
        ax[it, it1].set_yticks(np.arange(11, 27.5, 1))
        ax[it, it1].set_ylim(11, 27.5)
        ax[it, it1].set_title(f"{dni[tydz_wcz].date()} - {dni[i].date()}")
        ax[it, it1].legend(labels=legenda, loc='lower right', ncol=3, fontsize =8)
        ax[it, it1].grid(color='grey', linestyle='--', linewidth=0.45, alpha=0.5)
        tydz_wcz = i+24
        it = 1
        it1 = 0
        legenda.clear()
        licz = 0
        print("2---")
        continue
    if i+24 == (6553+3*(7*24)):

        ax[it, it1].set_xticks(np.arange(1, 23, 1))
        ax[it, it1].set_xlim(1, 23)
        ax[it, it1].set_yticks(np.arange(11, 27.5, 1))
        ax[it, it1].set_ylim(11, 27.5)
        ax[it, it1].set_title(f"{dni[tydz_wcz].date()} - {dni[i].date()}")
        ax[it, it1].legend(labels=legenda, loc='lower right', ncol=3, fontsize =8)
        ax[it, it1].grid(color='grey', linestyle='--', linewidth=0.45, alpha=0.5)
        tydz_wcz = i+24
        it = 1
        it1 = 1
        legenda.clear()
        licz = 0
        print("3----")
        continue
    if i+24 == (6553+4*(7*24)):
        ax[it, it1].set_xticks(np.arange(1, 23, 1))
        ax[it, it1].set_xlim(1, 23)
        ax[it, it1].set_yticks(np.arange(11, 27.5, 1))
        ax[it, it1].set_ylim(11, 27.5)
        ax[it, it1].set_title(f"{dni[tydz_wcz].date()} - {dni[i].date()}")
        ax[it, it1].legend(labels=legenda, loc='lower right', ncol=3, fontsize =8)
        ax[it, it1].grid(color='grey', linestyle='--', linewidth=0.45, alpha=0.5)
        tydz_wcz = i+24
        legenda.clear()
        licz = 0
        print("4-----")
        continue

for ax1 in ax.flat:
    ax1.set(xlabel="Time [hour]", ylabel="Electricity demand [GW]")

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax1 in ax.flat:
    ax1.label_outer()
plt.show()