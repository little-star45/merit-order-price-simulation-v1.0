#Tabela 1. Elektrownie i elektrociepłownie zawodowe
#KOBIZE
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

eff_solar = 1
eff_wind = 1
eff_hydro = 1
eff_coal = 1
eff_gas = 1
eff_bcoal = 1
eff_nuclear = 1


def effPower_GJ(eff,power): # [GJ] - ile trzeba mocy biorąc pod uwagę sprawność elektrowni
    #power [MWh]
    #eff [%]
    power = power*3.6 #[GJ]
    eff = eff/100
    return power/eff

#def fuelCons(grossPwr,Wo): # energia z paliwa po uwzgl sprawnosci elektrowni [kg]
    #return  grossPwr/Wo
def C02EmmFromFuel_kg(fuelCons,coeff): # [kg] - ile bedzioe CO2 z takiej ilosci spalonego paliwa
    #fuelCons - GJ
    #coeff - kg/GJ
    return coeff*fuelCons

def CO2All_tonn(eff,power,coeff): # [tonn CO2]
    return C02EmmFromFuel_kg(effPower_GJ(eff, power),coeff)/1000

print(CO2All_tonn(100,1,93.64))



