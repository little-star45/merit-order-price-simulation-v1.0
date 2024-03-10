
#SOURCE: https://stackoverflow.com/questions/19254852/how-to-set-bar-widths-independent-of-ticks-in-matplotlib
# https://stackoverflow.com/questions/46780367/variable-width-barplot-with-seaborn
# https://www.statology.org/matplotlib-add-text/
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, CheckButtons, TextBox, Button
import tkinter as tk
import numpy as np
import webbrowser


em_coal = "0"
em_solar = "0"
em_nuclear = "0"
em_wind = "0"
em_BrownCoal = "0"
em_gas = "0"
em_hydro = "0"
em_biofuel = "0"

eff_solar = "100"
eff_wind = "100"
eff_hydro = "100"
eff_coal = "46"
eff_gas = "58"
eff_bcoal = "44"
eff_nuclear = "36"
eff_biofuel = "85"

#EMISSION CO2 ---------------------------------------------
#WO - MJ/kg

WO_coal = 21.72
WO_Bcoal = 7.94

    #gaz ziemny - MJ/kg
WO_Ngas = 48

    #gaz ziemny wysokometanowy - MJ/m3
WO_CH4Ngas = 36.65

#WE CO2 - kg/GJ

WE_coal = 93.54
WE_Bcoal = 111.53
WE_gas = 55.48

#Power plant efficiency


def effPower_GJ(eff,power): # [GJ] - ile trzeba mocy biorąc pod uwagę sprawność elektrowni
    #power [MWh]
    #eff [%]
    power = float(power)*3.6 #[GJ]
    eff = float(eff)/100
    if eff > 0:
        return power/eff
    else:
        return 0

#def fuelCons(grossPwr,Wo): # energia z paliwa po uwzgl sprawnosci elektrowni [kg]
    #return  grossPwr/Wo
def C02EmmFromFuel_kg(fuelCons,coeff): # [kg] - ile bedzioe CO2 z takiej ilosci spalonego paliwa
    #fuelCons - GJ
    #coeff - kg/GJ
    return float(coeff)*fuelCons

def CO2All_tonn(eff,power,coeff): # [tonn CO2]
    return float(C02EmmFromFuel_kg(effPower_GJ(eff, power),coeff)/1000)
#--------------------------------------------------------------------------------------------


def opcje(event):
    root = tk.Tk()
    root.geometry("1050x800")
    root.title("CO2 emission OPTIONS")

    L0 = tk.Label(root, text="Co2 emission factor from fuel combustion", font=('Helvetica', 12, 'bold'), padx=10, pady=15)
    L0.grid(column=0, row=0, columnspan = 2)

    L9 = tk.Label(root, text="Power Plant Efficiency [%]", font=('Helvetica', 12, 'bold'), padx=10, pady=15)
    L9.grid(column=2, row=0, pady=20, columnspan = 2)

    L8 = tk.Label(root, text="Co2 price [EUR/tonne]")
    L8.grid(column=0, row=9, pady=20)

    L1 = tk.Label(root, text="Solar [kg/GJ]")
    L2 = tk.Label(root, text="Wind [kg/GJ]")
    L3 = tk.Label(root, text="Hydro [kg/GJ]")
    L4 = tk.Label(root, text="Coal [kg/GJ]")
    L5 = tk.Label(root, text="Gas [kg/GJ]")
    L6 = tk.Label(root, text="Brown Coal [kg/GJ]")
    L7 = tk.Label(root, text="Nuclear [kg/GJ]")
    L17 = tk.Label(root, text="Biofuel [kg/GJ]")

    L1.grid(column=0, row=1)
    L2.grid(column=0, row=2)
    L3.grid(column=0, row=3)
    L4.grid(column=0, row=4)
    L5.grid(column=0, row=5)
    L6.grid(column=0, row=6)
    L7.grid(column=0, row=7)
    L17.grid(column=0, row=8)

    L15 = tk.Label(root, text="Solar Efficiency [%]")
    L16 = tk.Label(root, text="Wind Efficiency [%]")
    L10 = tk.Label(root, text="Hydro Efficiency [%]")
    L11 = tk.Label(root, text="Coal Efficiency [%]")
    L12 = tk.Label(root, text="Gas Efficiency [%]")
    L13 = tk.Label(root, text="Brown Coal Efficiency [%]")
    L14 = tk.Label(root, text="Nuclear Efficiency [%]")
    L18 = tk.Label(root, text="Biofuel Efficiency [%]")

    L15.grid(column=2, row=1)
    L16.grid(column=2, row=2)
    L10.grid(column=2, row=3)
    L11.grid(column=2, row=4)
    L12.grid(column=2, row=5)
    L13.grid(column=2, row=6)
    L14.grid(column=2, row=7)
    L18.grid(column=2, row=8)

    global Es
    global Ew
    global Eh
    global Ec
    global Eg
    global Ebc
    global Enc
    global Ebf

    global Effs
    global Effw
    global Effh
    global Effc
    global Effg
    global Effbc
    global Effnc
    global Effbf

    global ECO2

    Es = tk.Entry(root, bd=5)
    Ew = tk.Entry(root, bd=5)
    Eh = tk.Entry(root, bd=5)
    Ec = tk.Entry(root, bd=5)
    Eg = tk.Entry(root, bd=5)
    Ebc = tk.Entry(root, bd=5)
    Enc = tk.Entry(root, bd=5)
    Ebf = tk.Entry(root, bd=5)

    Effs = tk.Entry(root, bd=5)
    Effw = tk.Entry(root, bd=5)
    Effh = tk.Entry(root, bd=5)
    Effc = tk.Entry(root, bd=5)
    Effg = tk.Entry(root, bd=5)
    Effbc = tk.Entry(root, bd=5)
    Effnc = tk.Entry(root, bd=5)
    Effbf = tk.Entry(root, bd=5)

    ECO2 = tk.Entry(root, bd=5)
    ECO2.grid(column=1, row=9)


    Es.grid(column=1, row=1)
    Ew.grid(column=1, row=2)
    Eh.grid(column=1, row=3)
    Ec.grid(column=1, row=4)
    Eg.grid(column=1, row=5)
    Ebc.grid(column=1, row=6)
    Enc.grid(column=1, row=7)
    Ebf.grid(column=1, row=8)

    Effs.grid(column=3, row=1)
    Effw.grid(column=3, row=2)
    Effh.grid(column=3, row=3)
    Effc.grid(column=3, row=4)
    Effg.grid(column=3, row=5)
    Effbc.grid(column=3, row=6)
    Effnc.grid(column=3, row=7)
    Effbf.grid(column=3, row=8)

    global em_coal
    global em_solar
    global em_nuclear
    global em_wind
    global em_BrownCoal
    global em_gas
    global em_hydro
    global em_biofuel

    global co2_price
    ECO2.insert(0, co2_price)

    global eff_solar
    global eff_wind
    global eff_hydro
    global eff_coal
    global eff_gas
    global eff_bcoal
    global eff_nuclear
    global eff_biofuel

    Es.insert(0, em_solar)
    Ew.insert(0, em_wind)
    Eh.insert(0, em_hydro)
    Ec.insert(0, em_coal)
    Eg.insert(0, em_gas)
    Ebc.insert(0, em_BrownCoal)
    Enc.insert(0, em_nuclear)
    Ebf.insert(0, em_biofuel)

    Effs.insert(0, eff_solar)
    Effw.insert(0, eff_wind)
    Effh.insert(0, eff_hydro)
    Effc.insert(0, eff_coal)
    Effg.insert(0, eff_gas)
    Effbc.insert(0, eff_bcoal)
    Effnc.insert(0, eff_nuclear)
    Effbf.insert(0, eff_biofuel)

    exit_button = tk.Button(root, text="EXIT", command=root.destroy, bg='#c9375a', fg='white',font=('Laksaman', 12, 'bold'))
    butt_def_co2 = tk.Button(root, text="DEFAULT", command=butt_co2,bg='#969696',fg='white',font=('Laksaman', 12, 'bold'))
    conf_button = tk.Button(root, text="CONFIRM", command=conf_co2, bg='#79c059',fg='white',font=('Laksaman', 12, 'bold'))
    exit_button.grid(column=3, row=10, columnspan=1, pady=10)
    butt_def_co2.grid(column=1, row=10, columnspan=1, pady=10)
    conf_button.grid(column=0, row=10, columnspan=1, pady=10)
    Ltext = tk.Label(root, text="First press CONFIRM and then EXIT to save and view changes !!!", font=('Minion Pro Med', 14, 'bold'), fg="#c13934", padx=10, pady=15)
    Ltext.grid(column=0, row=11, columnspan=3)
    Ltext2 = tk.Label(root, text="In the graph, the hatched bars symbolize CO2 emission fees",
                     font=('Minion Pro Med', 12, 'bold'), fg="black", padx=10, pady=15)
    Ltext2.grid(column=0, row=12, columnspan=2)

    labelframe = tk.LabelFrame(root, text="DATA SOURCES HYPERLINKS:",font=('Helvetica', 10, 'bold'), padx=10, pady=15)
    #Lsource= tk.Label(root, text="DATA SOURCES HYPERLINKS:", )
    #Lsource.grid(column=0, row=12)
    labelframe.grid(column=1, row=13)

    Llink1 = tk.Label(labelframe, text="CO2 emission factor: (CLICK HERE) ",anchor="w", justify="left", font=('Helvetica', 10, 'bold'), padx=10, pady=5,fg="#3950d5", cursor="hand2")
    Llink1.grid(column=0, row=14)
    Llink1.bind("<Button-1>", lambda e: webbrowser.open_new_tab("https://www.kobize.pl/uploads/materialy/materialy_do_pobrania/monitorowanie_raportowanie_weryfikacja_emisji_w_eu_ets/WO_i_WE_do_monitorowania-ETS-2023.pdf"))

    Llink2 = tk.Label(labelframe, text="Power plants efficiency: (CLICK HERE) ",anchor="w", justify="left",  font=('Helvetica', 10, 'bold'), padx=10, pady=5,
                      fg="#3950d5", cursor="hand2")
    Llink2.grid(column=0, row=15)
    Llink2.bind("<Button-1>", lambda e: webbrowser.open_new_tab(
        "https://bip.mos.gov.pl/fileadmin/user_upload/bip/strategie_plany_programy/Polityka_energetyczna_Polski/zal._2_do_PEP2040_-_Wnioski_z_analiz_prognostycznych_2021-02-02.pdf"))

    Llink3 = tk.Label(labelframe, text="Current market prices of CO2 allowances: (CLICK HERE) ",anchor="w", justify="left",  font=('Helvetica', 10, 'bold'), padx=10,
                      pady=5,fg="#3950d5", cursor="hand2")
    Llink3.grid(column=0, row=16)
    Llink3.bind("<Button-1>", lambda e: webbrowser.open_new_tab(
        "https://www.pse.pl/dane-systemowe/funkcjonowanie-rb/raporty-dobowe-z-funkcjonowania-rb/podstawowe-wskazniki-cenowe-i-kosztowe/rozliczeniowa-cena-uprawnien-do-emisji-co2-rcco2"))

    root.mainloop()

    main_bar(demand, df)

# robimy przycisk do wywoływania funkcji wykresu

def butt_co2():
    global Effs
    global Effw
    global Effh
    global Effc
    global Effg
    global Effbc
    global Effnc
    global Effbf

    Effs.delete(0, 'end')
    Effw.delete(0, 'end')
    Effh.delete(0, 'end')
    Effc.delete(0, 'end')
    Effg.delete(0, 'end')
    Effbc.delete(0, 'end')
    Effnc.delete(0, 'end')
    Effbf.delete(0, 'end')

    Effs.insert(0, "100")
    Effw.insert(0, "100")
    Effh.insert(0, "100")
    Effc.insert(0, "46")
    Effg.insert(0, "58")
    Effbc.insert(0, "44")
    Effnc.insert(0, "36")
    Effbf.insert(0, "85")

    global Es
    global Ew
    global Eh
    global Ec
    global Eg
    global Ebc
    global Enc

    Es.delete(0, 'end')
    Ew.delete(0, 'end')
    Eh.delete(0, 'end')
    Ec.delete(0, 'end')
    Eg.delete(0, 'end')
    Ebc.delete(0, 'end')
    Enc.delete(0, 'end')
    Ebf.delete(0, 'end')

    Es.insert(0, "0")
    Ew.insert(0, "0")
    Eh.insert(0, "0")
    Ec.insert(0, str(WE_coal))
    Eg.insert(0, str(WE_gas))
    Ebc.insert(0, str(WE_Bcoal))
    Enc.insert(0, "0")
    Ebf.insert(0, "0")

    global ECO2
    ECO2.delete(0, 'end')
    ECO2.insert(0, "80.24")


def conf_co2():
    global em_coal
    global em_solar
    global em_nuclear
    global em_wind
    global em_BrownCoal
    global em_gas
    global em_hydro
    global em_biofuel

    global co2_price

    global eff_solar
    global eff_wind
    global eff_hydro
    global eff_coal
    global eff_gas
    global eff_bcoal
    global eff_nuclear
    global eff_biofuel

    em_coal = float(Ec.get())
    em_solar = float(Es.get())
    em_nuclear = float(Enc.get())
    em_wind = float(Ew.get())
    em_BrownCoal = float(Ebc.get())
    em_gas = float(Eg.get())
    em_hydro = float(Eh.get())
    em_biofuel = float(Ebf.get())

    eff_solar = float(Effs.get())
    eff_wind = float(Effw.get())
    eff_hydro = float(Effh.get())
    eff_coal = float(Effc.get())
    eff_gas = float(Effg.get())
    eff_bcoal = float(Effbc.get())
    eff_nuclear = float(Effnc.get())
    eff_biofuel = float(Effbf.get())

    co2_price = float(ECO2.get())
    ECO2.delete(0, 'end')
    
    ECO2.insert(0, co2_price)

    Es.delete(0, 'end')
    Ew.delete(0, 'end')
    Eh.delete(0, 'end')
    Ec.delete(0, 'end')
    Eg.delete(0, 'end')
    Ebc.delete(0, 'end')
    Enc.delete(0, 'end')
    Ebf.delete(0, 'end')

    Es.insert(0, em_solar)
    Ew.insert(0, em_wind)
    Eh.insert(0, em_hydro)
    Ec.insert(0, em_coal)
    Eg.insert(0, em_gas)
    Ebc.insert(0, em_BrownCoal)
    Enc.insert(0, em_nuclear)
    Ebf.insert(0, em_biofuel)

    Effs.delete(0, 'end')
    Effw.delete(0, 'end')
    Effh.delete(0, 'end')
    Effc.delete(0, 'end')
    Effg.delete(0, 'end')
    Effbc.delete(0, 'end')
    Effnc.delete(0, 'end')
    Effbf.delete(0, 'end')

    Effs.insert(0, eff_solar)
    Effw.insert(0, eff_wind)
    Effh.insert(0, eff_hydro)
    Effc.insert(0, eff_coal)
    Effg.insert(0, eff_gas)
    Effbc.insert(0, eff_bcoal)
    Effnc.insert(0, eff_nuclear)
    Effbf.insert(0, eff_biofuel)

print(f"nowy--------------")


# technology = ["Solar", "Wind", "Hydro", "Coal", "Natural Gas", "Biofuel"]
# #gen_capacity = [5,10,15,20,25]
# gen_capacity = [5,10,15,20,25,25,25,25]
# gen_price = [5,10,15,20,25,20,25,35]
# left = [0,0,0,0,0,0,0,0]
# co2_cost = [0,0,0,0,0,0,0,0]
# sum_co2_genP=[0,0,0,0,0,0,0,0]

fig, ax = plt.subplots(figsize = (19,9))
plt.subplots_adjust(bottom=0.1, right=0.95, top=0.95,left = 0.17)
bars_color = color=['#fbc93d', '#10e5aa', '#6cc0e5', '#333e48','#dddddd']

data_raw = {"gen_capacity":[12.1,9.1,2.4,22.4,3.8,8.3,0,1.1],"left":[0,5,10,15,20,25,20,20],"gen_price":[52,50,110,70,88,155,102,76],"bar_width":[12.1,9.1,2.4,22.4,3.8,8.3,0,1.1], "bars_color":['#fbc93d', '#10e5aa', '#6cc0e5', '#333e48','#dddddd','#70441c', '#e1015e', "#d2b4De"], "co2_cost":[0,0,0,0,0,0,0,0], "sum_co2_genP":[0,0,0,0,0,0,0,0]}
df = pd.DataFrame(data_raw)
df.index = ["Solar", "Wind", "Hydro", "Coal", "Natural Gas", "Brown Coal", "Nuclear", "Biofuel"]
#print(df)
demand = 35
index = np.cumsum(df["bar_width"])

####CO2 PRICE [EUR/tonne]
#https://stooq.pl/q/?s=ck.f
##https://tradingeconomics.com/commodity/carbon

co2_price = 80.24
#EMMISION FACTOR
#https://www.researchgate.net/figure/CO2-emission-factors-of-industrial-power-plants-in-Spain_tbl2_282734491
# Carbon Dioxide Emissions Coefficients by Fuel [tonn co2/MWh


#!!!!
#print(np.array(gen_capacity))
#print(np.array(df["bar_width"]))

#bar1 = ax.bar(np.array(gen_capacity) - np.array(df["bar_width"]), gen_price, color=bars_color, width=df["bar_width"])

#ax.hlines(y = 5, color ="green", linestyle =":",xmin=0, xmax=index)
plt.xlabel('Capacity [GWh/h]')
plt.ylabel('Generator Price [EUR/MWh]')

choices = df.index
chceck_state = [True, True, True, True, True, True, True,True]
#for i in range(len(df.index)):
    #chceck_state.append(True)
ax_checkbox = plt.axes([0.03, 0.50, 0.1, 0.25])
ax_checkbox.margins(x=2, y=1)

checkbox = CheckButtons(ax=ax_checkbox, labels=choices, actives=chceck_state)


#for rectang in checkbox.rectangles: # adjust radius here. The default is 0.05
    #rectang.set_height(0.08)
    #rectang.set_width(0.08)
    #rectang.set_joinstyle('round')

[ll.set_color("black") for l in checkbox.lines for ll in l]
[ll.set_linewidth(3) for l in checkbox.lines for ll in l]

#https://learndataanalysis.org/how-to-insert-check-buttons-widget-matplotlib-tutorial/

def autolabel(rects, tech):
    # attach some text labels
    for ii,rect in enumerate(rects):
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05, '%s'%(tech[ii]), ha='center', va='bottom', fontweight=650, size=12, fontstretch=700, rotation="vertical")
#autolabel(bar1,df.index)


def set_visible(label): #label - red, green, blue
    #labels.index(label)  -1,2,3, czyli pole o którym numerze zostało uruchomione; to jest index naszej opcji
    #labels = df.index
    #for i in range(len(df.index)):
        #labels[i] = df.index[i]
    #idx = labels.index(label)
    #sliders[idx].set_visible(not sliders[idx].get_visible())
    global df
    if label == "Solar":
        sliders[0].set_visible(not sliders[0].get_visible())
        sliders_prc[0].set_visible(not sliders_prc[0].get_visible())

        if sliders[0].get_visible() == False:
            df.drop(labels = "Solar",axis=0, inplace=True)
        else:
            df.loc["Solar", :] = [0, 0, 0, 0, data_raw["bars_color"][0],0,0]
            slider_solar.set_val(float(0))
            slider_solarP.set_val(float(0))

        for i in range(len(df)):
            if i == 0:
                df.iat[i, 1] = 0
                MCP = df.iat[i, 6]
            else:
                df.iat[i, 1] = df.iat[i - 1, 1] + df.iat[i - 1, 3]
                if df.iat[i, 0] < demand and df.iat[i, 6] > MCP:
                    MCP = df.iat[i, 6]

        #print('solar', df)

        main_bar(demand, df)


    elif label == "Wind":
        sliders[1].set_visible(not sliders[1].get_visible())
        sliders_prc[1].set_visible(not sliders_prc[1].get_visible())

        if sliders[1].get_visible() == False:
            df.drop(labels = "Wind",axis=0, inplace=True)
        else:
            df.loc["Wind", :] = [0, 0, 0, 0, data_raw["bars_color"][1],0,0]
            slider_wind.set_val(float(0))
            slider_windP.set_val(float(0))

        for i in range(len(df)):
            if i == 0:
                df.iat[i, 1] = 0
                MCP = df.iat[i, 6]
            else:
                df.iat[i, 1] = df.iat[i - 1, 1] + df.iat[i - 1, 3]
                if df.iat[i, 0] < demand and df.iat[i, 6] > MCP:
                    MCP = df.iat[i, 6]
        main_bar(demand, df)

    elif label == "Hydro":
        sliders[2].set_visible(not sliders[2].get_visible())
        sliders_prc[2].set_visible(not sliders_prc[2].get_visible())

        if sliders[2].get_visible() == False:
            df.drop(labels = "Hydro",axis=0, inplace=True)
        else:
            df.loc["Hydro", :] = [0, 0, 0, 0, data_raw["bars_color"][2],0,0]
            slider_hydro.set_val(float(0))
            slider_hydroP.set_val(float(0))

        for i in range(len(df)):
            if i == 0:
                df.iat[i, 1] = 0
                MCP = df.iat[i, 6]
            else:
                df.iat[i, 1] = df.iat[i - 1, 1] + df.iat[i - 1, 3]
                if df.iat[i, 0] < demand and df.iat[i, 6] > MCP:
                    MCP = df.iat[i, 6]

        main_bar(demand, df)

    elif label == "Coal":
        sliders[3].set_visible(not sliders[3].get_visible())
        sliders_prc[3].set_visible(not sliders_prc[3].get_visible())

        if sliders[3].get_visible() == False:
            df.drop(labels = "Coal",axis=0, inplace=True)
        else:
            df.loc["Coal", :] = [0, 0, 0, 0, data_raw["bars_color"][3],0,0]
            slider_coal.set_val(float(0))
            slider_coalP.set_val(float(0))

        for i in range(len(df)):
            if i == 0:
                df.iat[i, 1] = 0
                MCP = df.iat[i, 6]
            else:
                df.iat[i, 1] = df.iat[i - 1, 1] + df.iat[i - 1, 3]
                if df.iat[i, 0] < demand and df.iat[i, 6] > MCP:
                    MCP = df.iat[i, 6]

        main_bar(demand, df)

    elif label == "Natural Gas":
        sliders[4].set_visible(not sliders[4].get_visible())
        sliders_prc[4].set_visible(not sliders_prc[4].get_visible())

        if sliders[4].get_visible() == False:
            df.drop(labels = "Natural Gas",axis=0, inplace=True)
        else:
            df.loc["Natural Gas", :] = [0, 0, 0, 0, data_raw["bars_color"][4],0,0]
            slider_gas.set_val(float(0))
            slider_gasP.set_val(float(0))

        for i in range(len(df)):
            if i == 0:
                df.iat[i, 1] = 0
                MCP = df.iat[i, 6]
            else:
                df.iat[i, 1] = df.iat[i - 1, 1] + df.iat[i - 1, 3]
                if df.iat[i, 0] < demand and df.iat[i, 6] > MCP:
                    MCP = df.iat[i, 6]
        main_bar(demand, df)

    elif label == "Brown Coal":
        sliders[5].set_visible(not sliders[5].get_visible())
        sliders_prc[5].set_visible(not sliders_prc[5].get_visible())

        if sliders[5].get_visible() == False:
            df.drop(labels = "Brown Coal",axis=0, inplace=True)
        else:
            df.loc["Brown Coal", :] = [0, 0, 0, 0, data_raw["bars_color"][5],0,0]
            slider_browncoal.set_val(float(0))
            slider_browncoalP.set_val(float(0))

        for i in range(len(df)):
            if i == 0:
                df.iat[i, 1] = 0
                MCP = df.iat[i, 6]
            else:
                df.iat[i, 1] = df.iat[i - 1, 1] + df.iat[i - 1, 3]
                if df.iat[i, 0] < demand and df.iat[i, 6] > MCP:
                    MCP = df.iat[i, 6]
        main_bar(demand, df)
    elif label == "Nuclear":
        sliders[6].set_visible(not sliders[6].get_visible())
        sliders_prc[6].set_visible(not sliders_prc[6].get_visible())

        if sliders[6].get_visible() == False:
            df.drop(labels = "Nuclear",axis=0, inplace=True)
        else:
            df.loc["Nuclear", :] = [0, 0, 0, 0, data_raw["bars_color"][6],0,0]
            slider_nuclear.set_val(float(0))
            slider_nuclearP.set_val(float(0))

        for i in range(len(df)):
            if i == 0:
                df.iat[i, 1] = 0
                MCP = df.iat[i, 6]
            else:
                df.iat[i, 1] = df.iat[i - 1, 1] + df.iat[i - 1, 3]
                if df.iat[i, 0] < demand and df.iat[i, 6] > MCP:
                    MCP = df.iat[i, 6]
        main_bar(demand, df)

    elif label == "Biofuel":
        sliders[7].set_visible(not sliders[7].get_visible())
        sliders_prc[7].set_visible(not sliders_prc[7].get_visible())

        if sliders[7].get_visible() == False:
            df.drop(labels = "Biofuel",axis=0, inplace=True)
        else:
            df.loc["Biofuel", :] = [0, 0, 0, 0, data_raw["bars_color"][7],0,0]
            slider_biofuel.set_val(float(0))
            slider_biofuelP.set_val(float(0))

        for i in range(len(df)):
            if i == 0:
                df.iat[i, 1] = 0
                MCP = df.iat[i, 6]
            else:
                df.iat[i, 1] = df.iat[i - 1, 1] + df.iat[i - 1, 3]
                if df.iat[i, 0] < demand and df.iat[i, 6] > MCP:
                    MCP = df.iat[i, 6]
        main_bar(demand, df)


checkbox.on_clicked(set_visible)

#czesc ze sliderem

plt.subplots_adjust(bottom=0.50) #żeby nie nahcodził na plot nasz slider

hFsSl = 0.39
dHSl = 0.045

ax_slider_s = plt.axes([0.1,hFsSl,0.35,0.05], facecolor = 'teal') # liczby - rectangle geometries - [left value,top value,szerokosc, wysokosc]
ax_slider_w = plt.axes([0.1,hFsSl-(dHSl)*1,0.35,0.05], facecolor = 'teal')
ax_slider_h = plt.axes([0.1,hFsSl-(dHSl)*2,0.35,0.05], facecolor = 'teal')
ax_slider_c = plt.axes([0.1,hFsSl-(dHSl)*3,0.35,0.05], facecolor = 'teal')
ax_slider_g = plt.axes([0.1,hFsSl-(dHSl)*4,0.35,0.05], facecolor = 'teal')
ax_slider_bc = plt.axes([0.1,hFsSl-(dHSl)*5,0.35,0.05], facecolor = 'teal')
ax_slider_nc = plt.axes([0.1,hFsSl-(dHSl)*6,0.35,0.05], facecolor = 'teal')
ax_slider_bf = plt.axes([0.1,hFsSl-(dHSl)*7,0.35,0.05], facecolor = 'teal')

ax_slider_ps = plt.axes([0.59,hFsSl,0.35,0.05], facecolor = 'teal') # liczby - rectangle geometries - [left value,top value,szerokosc, wysokosc]
ax_slider_pw = plt.axes([0.59,hFsSl-(dHSl)*1,0.35,0.05], facecolor = 'teal')
ax_slider_ph = plt.axes([0.59,hFsSl-(dHSl)*2,0.35,0.05], facecolor = 'teal')
ax_slider_pc = plt.axes([0.59,hFsSl-(dHSl)*3,0.35,0.05], facecolor = 'teal')
ax_slider_pg = plt.axes([0.59,hFsSl-(dHSl)*4,0.35,0.05], facecolor = 'teal')
ax_slider_pbc = plt.axes([0.59,hFsSl-(dHSl)*5,0.35,0.05], facecolor = 'teal')
ax_slider_pnc = plt.axes([0.59,hFsSl-(dHSl)*6,0.35,0.05], facecolor = 'teal')
ax_slider_pbf = plt.axes([0.59,hFsSl-(dHSl)*7,0.35,0.05], facecolor = 'teal')

ax_slider_dem = plt.axes([0.1,0.025,0.85,0.05], facecolor = '#9d1039')
#funkcja do updatowania obrazka wraz z ustawianiem slidera
sliders = [ax_slider_s,ax_slider_w,ax_slider_h,ax_slider_c,ax_slider_g,ax_slider_bc,ax_slider_nc, ax_slider_bf]
sliders_prc = [ax_slider_ps,ax_slider_pw,ax_slider_ph,ax_slider_pc,ax_slider_pg,ax_slider_pbc,ax_slider_pnc,ax_slider_pbf]

# ax_co2_text = plt.axes([0.10, 0.93, 0.03,0.02], facecolor = 'teal')
#
# plt.gcf().text(0.025, 0.89, 'Co2 emmiss [tonn/MWh]', fontweight = 'bold')
#
# ax_text_s = plt.axes([0.10, 0.86, 0.03,0.02], facecolor = 'teal')
# ax_text_w = plt.axes([0.10, 0.835, 0.03,0.02], facecolor = 'teal')
# ax_text_h = plt.axes([0.10, 0.81, 0.03,0.02], facecolor = 'teal')
# ax_text_c = plt.axes([0.10, 0.785, 0.03,0.02], facecolor = 'teal')
# ax_text_g = plt.axes([0.10, 0.76, 0.03,0.02], facecolor = 'teal')
# ax_text_bc = plt.axes([0.10, 0.735, 0.03,0.02], facecolor = 'teal')
# ax_text_nc = plt.axes([0.10, 0.71, 0.03,0.02], facecolor = 'teal')

ax_butt_def = plt.axes([0.03,0.83,0.1,0.05], facecolor = 'teal')
#ax_butt_check = plt.axes([0.75,0.025,0.1,0.05], facecolor = 'teal')
ax_butt_menu = plt.axes([0.03,0.90,0.1,0.05], facecolor = 'teal')

demand = 0
MCP = 0

social_welf = 0

def max_price(df): #ustalanie market clearing price
    global MCP
    global social_welf
    social_welf = 0

    for i in range(len(df)):

        #print(i)
        if i == 0:
            MCP = df.iat[i, 6]
            social_welf = 0
            #print("tutaj")

        else:
            if df.iat[i, 1] < demand and df.iat[i, 6] > MCP:
                MCP = df.iat[i, 6]
                #print('nowy',i)
                #print('df.iat[i, 2]', df.iat[i, 2])
                #print("bar width", df.iat[i, 3])
    for a in range(i):
        if MCP>= df.iat[a, 6]:
            social_welf = social_welf + (MCP - df.iat[a, 6])*df.iat[a, 3]*1000
            #print("social_welf czesc = (", MCP, "-", df.iat[a, 2],")*",df.iat[a, 3],"=",(MCP - df.iat[a, 2])*df.iat[a, 3])
            #print(social_welf)
    return MCP

def main_bar(demand, df):
    ax.clear()

    global em_coal
    global em_solar
    global em_nuclear
    global em_wind
    global em_BrownCoal
    global em_gas
    global em_hydro
    global em_biofuel

    global co2_price

    global eff_solar
    global eff_wind
    global eff_hydro
    global eff_coal
    global eff_gas
    global eff_bcoal
    global eff_nuclear
    global eff_biofuel

    df.at['Solar', 'co2_cost'] = CO2All_tonn(eff_solar, 1, em_solar) * co2_price
    df.at['Wind', 'co2_cost'] = CO2All_tonn(eff_wind, 1, em_wind) * co2_price
    df.at['Hydro', 'co2_cost'] = CO2All_tonn(eff_hydro, 1, em_hydro) * co2_price
    df.at["Coal", 'co2_cost'] = CO2All_tonn(eff_coal, 1, em_coal) * co2_price
    df.at['Natural Gas', 'co2_cost'] = CO2All_tonn(eff_gas, 1, em_gas) * co2_price
    df.at["Brown Coal", 'co2_cost'] = CO2All_tonn(eff_bcoal, 1, em_BrownCoal) * co2_price
    df.at['Nuclear', 'co2_cost'] = CO2All_tonn(eff_nuclear, 1, em_nuclear) * co2_price
    df.at['Biofuel', 'co2_cost'] = CO2All_tonn(eff_biofuel, 1, em_biofuel) * co2_price

    df.at['Solar', 'sum_co2_genP'] = df.at['Solar', 'gen_price'] + df.at['Solar', 'co2_cost']
    df.at['Wind', 'sum_co2_genP'] = df.at['Wind', 'gen_price'] + df.at['Wind', 'co2_cost']
    df.at['Hydro', 'sum_co2_genP'] = df.at['Hydro', 'gen_price'] + df.at['Hydro', 'co2_cost']
    df.at["Coal", 'sum_co2_genP'] = df.at["Coal", 'gen_price'] + df.at["Coal", 'co2_cost']
    df.at['Natural Gas', 'sum_co2_genP'] = df.at['Natural Gas', 'gen_price'] + df.at['Natural Gas', 'co2_cost']
    df.at["Brown Coal", 'sum_co2_genP'] = df.at["Brown Coal", 'gen_price'] + df.at["Brown Coal", 'co2_cost']
    df.at['Nuclear', 'sum_co2_genP'] = df.at['Nuclear', 'gen_price'] + df.at['Nuclear', 'co2_cost']
    df.at['Biofuel', 'sum_co2_genP'] = df.at['Biofuel', 'gen_price'] + df.at['Biofuel', 'co2_cost']


    #print('main', df)
    df.dropna(inplace=True)
    MCP = max_price(df)

    sorting()

    ax.set_title(f'Demand = {demand} [GWh/h]   Market Clearing Price = {round(MCP,2)} [EUR/MWh]    Social Welfare = {round(social_welf,2):,} [EUR]')


    bar1 = ax.bar('left', 'gen_price', data=df, color=df["bars_color"], width=df["bar_width"], alpha=0.6, align='edge',
                  edgecolor='k', linewidth=2)  # replot the plot
    bar1 = ax.bar('left', 'co2_cost', data=df, hatch="////", color=df["bars_color"],bottom = df['gen_price'], width=df["bar_width"], alpha=0.5, align='edge',
                  edgecolor='k', linewidth=2)

    all_dem = ax.vlines(x=demand, color="red", linestyle=":", ymin=0, ymax=max(df['sum_co2_genP']) + 10, linewidth=3)
    wyk_MCP = ax.hlines(y=MCP, color="blue", linestyle=":", xmin=0, xmax=df["left"][len(df)-1] + df["bar_width"][len(df)-1],
                        linewidth=3)
    box = {'facecolor': '#fef2f0',
           'edgecolor': '#fa8072',
           'boxstyle': 'round'
           }
    box1 = {'facecolor': '#c1d9e8',
            'edgecolor': '#293f69',
            'boxstyle': 'round'
            }
    ax.text(demand - 0.6, max(df["gen_price"]) + 10, 'DEM', rotation=360, color='black', weight='bold', bbox=box)
    ax.text(df["left"][len(df)-1] + df["bar_width"][len(df)-1], MCP+1, 'MCP', rotation=360, color='#000051', weight='bold', bbox=box1)
    ax.vlines(x=demand, color="red", linestyle=":", ymin=0, ymax=max(df["gen_price"]) + 10, linewidth=3)
    ax.set_xlim(left=0)
    ax.set_xlim(right=df["left"][len(df)-1] + df["bar_width"][len(df)-1])
    ax.set_xlabel('Capacity [GWh/h]', fontsize=13)
    ax.set_ylabel('Generator Price [EUR/MWh]', fontsize=13)
    autolabel(bar1, df.index)
    ax.grid(linestyle='--', alpha=0.5)

    plt.draw()
def update_line(val):
    ax.clear()  # czyscimy osie
    """ax.clear()#czyscimy osie
    bar_width[0]=slider_solar.val
    bar_width[1]=slider_wind.val
    bar_width[2]=slider_hydro.val
    bar_width[3]=slider_coal.val
    bar_width[4]=slider_gas.val"""

    df.at['Solar',"bar_width"] = slider_solar.val
    df.at['Wind',"bar_width"] = slider_wind.val
    df.at['Hydro',"bar_width"] = slider_hydro.val
    df.at["Coal","bar_width"] = slider_coal.val
    df.at['Natural Gas',"bar_width"] = slider_gas.val
    df.at["Brown Coal", "bar_width"] = slider_browncoal.val
    df.at['Nuclear', "bar_width"] = slider_nuclear.val
    df.at['Biofuel', "bar_width"] = slider_biofuel.val

    for i in range(len(df)):
        if i == 0:
            df.iat[i,1] = 0
            MCP = df.iat[i, 6]
        else:
            df.iat[i,1]=df.iat[i-1,1] + df.iat[i-1,3]
            if df.iat[i,0]< demand and df.iat[i, 6]>MCP:
                MCP = df.iat[i, 6]

    #slider_dem = Slider(ax_slider_dem, "Demand [GW]", valmin=0, valmax=df["left"][4] + df["bar_width"][4], valinit=0, valstep=1)

    main_bar(demand, df)

def update_dem(val):
    ax.clear()
    global demand
    demand = val

    main_bar(demand, df)

def update_prc(val):
    ax.clear()  # czyscimy osie
    df.dropna(inplace=True)

    df.at['Solar','gen_price'] = slider_solarP.val
    df.at['Wind','gen_price'] = slider_windP.val
    df.at['Hydro','gen_price'] = slider_hydroP.val
    df.at["Coal",'gen_price'] = slider_coalP.val
    df.at['Natural Gas','gen_price'] = slider_gasP.val
    df.at["Brown Coal", 'gen_price'] = slider_browncoalP.val
    df.at['Nuclear', 'gen_price'] = slider_nuclearP.val
    df.at['Biofuel', 'gen_price'] = slider_biofuelP.val

    df.at['Solar', 'sum_co2_genP'] = df.at['Solar','gen_price'] + df.at['Solar','co2_cost']
    df.at['Wind', 'sum_co2_genP'] = df.at['Wind','gen_price'] + df.at['Wind','co2_cost']
    df.at['Hydro', 'sum_co2_genP'] = df.at['Hydro','gen_price'] + df.at['Hydro','co2_cost']
    df.at["Coal", 'sum_co2_genP'] = df.at["Coal",'gen_price'] + df.at["Coal", 'co2_cost']
    df.at['Natural Gas', 'sum_co2_genP'] = df.at['Natural Gas','gen_price']+df.at['Natural Gas', 'co2_cost']
    df.at["Brown Coal", 'sum_co2_genP'] = df.at["Brown Coal", 'gen_price']+df.at["Brown Coal", 'co2_cost']
    df.at['Nuclear', 'sum_co2_genP'] = df.at['Nuclear', 'gen_price']+df.at['Nuclear', 'co2_cost']
    df.at['Biofuel', 'sum_co2_genP'] = df.at['Biofuel', 'gen_price'] + df.at['Biofuel', 'co2_cost']

    sorting()

    #print(max_price(df))

    main_bar(demand, df)

def sorting():
    global df_sorted
    df.dropna(inplace=True)
    df_sorted = df.sort_values('sum_co2_genP')

    for i in range(len(df)):  # check left
        if i == 0:
            df_sorted.iat[i, 1] = 0
            MCP = df_sorted.iat[i, 6]
        else:
            df_sorted.iat[i, 1] = df_sorted.iat[i - 1, 1] + df_sorted.iat[i - 1, 3]
            if df_sorted.iat[i, 0] < demand and df_sorted.iat[i, 6] > MCP:
                MCP = df_sorted.iat[i, 6]

    index = df_sorted.index

    df.index = index

    df['gen_capacity'] = df_sorted['gen_capacity'].values.tolist()
    df['left'] = df_sorted['left'].values.tolist()
    df['gen_price'] = df_sorted['gen_price'].values.tolist()
    df['bar_width'] = df_sorted['bar_width'].values.tolist()
    df['bars_color'] = df_sorted['bars_color'].values.tolist()
    df['co2_cost'] = df_sorted['co2_cost'].values.tolist()
    df['sum_co2_genP'] = df_sorted['sum_co2_genP'].values.tolist()

def data_start(event):
    global df
    dem = 175.2*1000/365/24

    status_box = checkbox.get_status()
    for _ in range(len(status_box)):
        if status_box[_] == False:
            checkbox.set_active(_)

    df.at['Solar', 'gen_capacity'] = 13.9
    df.at['Wind', 'gen_capacity'] = 8.3
    df.at['Hydro', 'gen_capacity'] = 2.3
    df.at["Coal", 'gen_capacity'] = 21.5
    df.at['Natural Gas', 'gen_capacity'] = 4
    df.at["Brown Coal", 'gen_capacity'] = 8.9
    df.at['Nuclear', 'gen_capacity'] = 0
    df.at['Biofuel', 'gen_capacity'] = 1.3

    slider_solar.set_val(float(df.at['Solar', 'gen_capacity']))
    slider_wind.set_val(float(df.at['Wind','gen_capacity']))
    slider_hydro.set_val(float(df.at['Hydro','gen_capacity']))
    slider_coal.set_val(float(df.at['Coal','gen_capacity']))
    slider_gas.set_val(float(df.at['Natural Gas','gen_capacity']))
    slider_browncoal.set_val(float(df.at['Brown Coal','gen_capacity']))
    slider_nuclear.set_val(float(df.at['Nuclear','gen_capacity']))
    slider_biofuel.set_val(float(df.at['Biofuel','gen_capacity']))

    df.at['Solar', 'gen_price'] = 52
    df.at['Wind', 'gen_price'] = 50
    df.at['Hydro', 'gen_price'] = 110
    df.at["Coal", 'gen_price'] = 70
    df.at['Natural Gas', 'gen_price'] = 88
    df.at["Brown Coal", 'gen_price'] = 155
    df.at['Nuclear', 'gen_price'] = 102
    df.at['Biofuel', 'gen_price'] = 76

    slider_windP.set_val(float(df.at['Wind', 'gen_price']))
    slider_solarP.set_val(float(52))
    slider_hydroP.set_val(float(110))
    slider_coalP.set_val(float(70))
    slider_gasP.set_val(float(88))
    slider_browncoalP.set_val(float(155))
    slider_nuclearP.set_val(float(102))
    slider_biofuelP.set_val(float(76))

    slider_dem.set_val(float(20.5))

    #set_visible("Nuclear")

    print("checkbox.set_active(6)",checkbox.set_active(6))
    print("checkbox.get", checkbox.get_status())


    print(df)

    main_bar(dem,df)
    print(df)

#dodajemy klasę slider a do niej axes object
slider_solar = Slider(ax_slider_s, "Cap-Solar [GWh/h]", valmin=0, valmax=50, valinit=0, valstep=0.1, color=df.at['Solar', 'bars_color'], alpha=0.7) #dane slidera, label
slider_wind = Slider(ax_slider_w, "Cap-Wind [GWh/h]", valmin=0, valmax=50, valinit=0, valstep=0.1, color=df.at['Wind', 'bars_color'], alpha=0.7)
slider_hydro = Slider(ax_slider_h, "Cap-Hydro [GWh/h]", valmin=0, valmax=50, valinit=0, valstep=0.1, color=df.at['Hydro', 'bars_color'], alpha=0.7) #dane slidera, label
slider_coal = Slider(ax_slider_c, "Cap-Coal [GWh/h]", valmin=0, valmax=50, valinit=0, valstep=0.1, color=df.at['Coal', 'bars_color'], alpha=0.7)
slider_gas = Slider(ax_slider_g, "Cap-Gas [GWh/h]", valmin=0, valmax=50, valinit=0, valstep=0.1, color=df.at['Natural Gas', 'bars_color'], alpha=1)
slider_browncoal = Slider(ax_slider_bc, "Cap-Brown Coal [GWh/h]", valmin=0, valmax=50, valinit=0, valstep=0.1, color=df.at['Brown Coal', 'bars_color'], alpha=0.7)
slider_nuclear = Slider(ax_slider_nc, "Cap-Nuclear [GWh/h]", valmin=0, valmax=50, valinit=0, valstep=0.1, color=df.at['Nuclear', 'bars_color'], alpha=0.7)
slider_biofuel = Slider(ax_slider_bf, "Cap-Biofuel [GWh/h]", valmin=0, valmax=50, valinit=0, valstep=0.1, color=df.at['Biofuel', 'bars_color'], alpha=0.7)

slider_solarP = Slider(ax_slider_ps, "Price-Solar [EUR/MWh]", valmin=0, valmax=200, valinit=0, valstep=0.5,color=df.at['Solar', 'bars_color'], alpha=0.7) #dane slidera, label
slider_windP = Slider(ax_slider_pw, "Price-Wind [EUR/MWh]", valmin=0, valmax=200, valinit=0, valstep=0.5,color=df.at['Wind', 'bars_color'], alpha=0.7)
slider_hydroP = Slider(ax_slider_ph, "Price-Hydro [EUR/MWh]", valmin=0, valmax=200, valinit=0, valstep=0.5,color=df.at['Hydro', 'bars_color'], alpha=0.7) #dane slidera, label
slider_coalP = Slider(ax_slider_pc, "Price-Coal [EUR/MWh]", valmin=0, valmax=200, valinit=0, valstep=0.5,color=df.at['Coal', 'bars_color'], alpha=0.7)
slider_gasP = Slider(ax_slider_pg, "Price-Gas [EUR/MWh]", valmin=0, valmax=200, valinit=0, valstep=0.5,color=df.at['Natural Gas', 'bars_color'], alpha=1)
slider_browncoalP = Slider(ax_slider_pbc, "Price-Brown Coal [EUR/MWh]", valmin=0, valmax=200, valinit=0, valstep=0.5,color=df.at['Brown Coal', 'bars_color'], alpha=0.7)
slider_nuclearP = Slider(ax_slider_pnc, "Price-Nuclear [EUR/MWh]", valmin=0, valmax=200, valinit=0, valstep=0.5,color=df.at['Nuclear', 'bars_color'], alpha=0.7)
slider_biofuelP = Slider(ax_slider_pbf, "Price-Biofuel [EUR/MWh]", valmin=0, valmax=200, valinit=0, valstep=0.5,color=df.at['Biofuel', 'bars_color'], alpha=0.7)

slider_dem = Slider(ax_slider_dem, "Demand [GWh/h]", valmin=0, valmax=250, valinit=0, valstep=0.1)

# textbox_co2P = TextBox(ax_co2_text, 'Co2 price [EUR/tonn] ', initial = co2_price)
#
# textbox_co2P_s = TextBox(ax_text_s, 'Solar [tonn/MWh] ', initial = em_solar)
# textbox_co2P_w = TextBox(ax_text_w, 'Wind [tonn/MWh] ', initial = em_gas)
# textbox_co2P_h = TextBox(ax_text_h, 'Hydro [tonn/MWh] ', initial = em_hydro)
# textbox_co2P_c= TextBox(ax_text_c, 'Coal [tonn/MWh] ', initial = em_coal)
# textbox_co2P_g= TextBox(ax_text_g, 'Gas [tonn/MWh] ', initial = em_gas)
# textbox_co2P_bc= TextBox(ax_text_bc, 'BrownCoal [tonn/MWh] ', initial = em_BrownCoal)
# textbox_co2P_nc= TextBox(ax_text_nc, 'Nuclear [tonn/MWh] ', initial = em_nuclear)
butt_def = Button(ax_butt_def,'DEFAULT')
butt_men = Button(ax_butt_menu,'CO2 FACTOR MENU')
#butt_chek = Button(ax_butt_check,'CHECK')

#supply the update line function to the unchanged signal
slider_solar.on_changed(update_line)
slider_wind.on_changed(update_line)
slider_hydro.on_changed(update_line)
slider_coal.on_changed(update_line)
slider_gas.on_changed(update_line)
slider_browncoal.on_changed(update_line)
slider_nuclear.on_changed(update_line)
slider_biofuel.on_changed(update_line)

slider_dem.on_changed(update_dem)

slider_solarP.on_changed(update_prc)
slider_windP.on_changed(update_prc)
slider_hydroP.on_changed(update_prc)
slider_coalP.on_changed(update_prc)
slider_gasP.on_changed(update_prc)
slider_browncoalP.on_changed(update_prc)
slider_nuclearP.on_changed(update_prc)
slider_biofuelP.on_changed(update_prc)

butt_men.on_clicked(opcje)
butt_def.on_clicked(data_start)

main_bar(demand, df)
max_price(df)
#mpld3.show()
plt.show()
