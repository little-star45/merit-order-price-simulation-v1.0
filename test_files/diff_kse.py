import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.dates as mdates
import datetime as dt

data = pd.read_excel(r'C:\Users\48530\Desktop\cena_enrg\cen_enrg_rok.xlsx',sheet_name='Sheet1')
df = pd.DataFrame(data, columns=['dat_razem','cena[PLN]','cena_EUR'])
# data = pd.read_excel(r'C:\Users\48530\Desktop\zap_energ\dem_kopia.xlsx',sheet_name='demand')
# df = pd.DataFrame(data, columns=['Data','Rzeczywiste zapotrzebowanie KSE [GW]', 'dummy','Godz', 'Dni','Diff',])
#print(df)
x = df['dat_razem']
cena=df['cena[PLN]']
cena_EUR = df['cena_EUR']

fig,ax = plt.subplots()

ax.axvspan(dt.date(2022, 6, 1), dt.date(2022, 9, 1), facecolor='#FBFE73', alpha=0.2)
ax.axvspan(dt.date(2022, 9, 1), dt.date(2022, 12, 1), facecolor='#E16C4A', alpha=0.2)
ax.axvspan(dt.date(2022, 12, 1), dt.date(2023, 3, 1), facecolor='#4AB5E1', alpha=0.2)
ax.axvspan(dt.date(2023, 3, 1), dt.date(2023, 5, 31), facecolor='#88FE73', alpha=0.2)
plt.grid(color = 'grey', linestyle = '--', linewidth = 0.45, alpha = 0.5)

#plt.plot(x,cena,color='red')
lns1=ax.plot(x,cena_EUR, label = 'Market price of electricity in Poland')

plt.title("Market price of electricity in Poland 01.06.2022-31.05.2023")
plt.xlabel("Time [dd:mm:yy]")
plt.ylabel("Energy price [EUR/MWh]")

data = pd.read_excel(r'C:\Users\48530\Desktop\cena_enrg\cen_enrg_rok.xlsx',sheet_name='Arkusz1')
df_ceny_gaz = pd.DataFrame(data, columns=['obs_date','price_EUR'])
x_c = df_ceny_gaz['obs_date']
cena_eur=df_ceny_gaz['price_EUR']

ax2 = ax.twinx()
lns2 = ax2.plot(x_c,cena_eur, c='red', label = 'Global price of Natural gas, EU (PNGASEUUSDM)')
ax2.set_ylim(0, 80)
ax2.set_ylabel("Natural Gas price [EUR/MWh]")

ax.xaxis.set_major_locator(mdates.MonthLocator())

ax.set_xlim([dt.date(2022, 6, 1), dt.date(2023, 5, 31)])
ax.set_yticks(np.arange(0,800,20))
ax.set_ylim(0,800)

#https://samchaaa.medium.com/how-to-plot-two-different-scales-on-one-plot-in-matplotlib-with-legend-46554ba5915a
leg = lns1 + lns2
labs = [l.get_label() for l in leg]
ax.legend(leg, labs, loc=0)

print(type(lns1))
print(type(lns2))
plt.show()
