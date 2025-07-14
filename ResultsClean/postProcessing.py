import pandas as pd
import math
import os
import sys
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib.pyplot import cm
import matplotlib as mpl
import matplotlib.colors as mcolors
import numpy as np

rc('text', usetex=True)
plt.rc('text', usetex=True)

parallelisms = list(range(8, 33, 2))

#QiskitTest
QiskitTime = pd.read_csv("floating_point/Time_qiskit_state_vector.csv")
QASMTime = pd.read_csv("floating_point/Time_qiskit_qasm_simulator.csv")

#floating point test
EmulatorTime = pd.read_csv("floating_point/Time.csv")
KLD = pd.read_csv("floating_point/kld.csv")
HF = pd.read_csv("floating_point/HF.csv")
MCD = pd.read_csv("floating_point/MCD.csv")
ACD = pd.read_csv("floating_point/ACD.csv")

#fixed nearest
EmulatorTime_n = pd.read_csv("fixed_point_nearest/Time_nearest.csv")
KLD_n = pd.read_csv("fixed_point_nearest/kld_nearest.csv")
HF_n = pd.read_csv("fixed_point_nearest/HF_nearest.csv")
MCD_n = pd.read_csv("fixed_point_nearest/MCD_nearest.csv")
ACD_n = pd.read_csv("fixed_point_nearest/ACD_nearest.csv")

#fixed nearest
EmulatorTime_ne = pd.read_csv("fixed_point_nearest_even/Time_nearest_even.csv")
KLD_ne = pd.read_csv("fixed_point_nearest_even/kld_nearest_even.csv")
HF_ne = pd.read_csv("fixed_point_nearest_even/HF_nearest_even.csv")
MCD_ne = pd.read_csv("fixed_point_nearest_even/MCD_nearest_even.csv")
ACD_ne = pd.read_csv("fixed_point_nearest_even/ACD_nearest_even.csv")

#fixed truncation
EmulatorTime_t = pd.read_csv("fixed_point_truncation/Time_truncation.csv")
KLD_t = pd.read_csv("fixed_point_truncation/kld_truncation.csv")
HF_t = pd.read_csv("fixed_point_truncation/HF_truncation.csv")
MCD_t = pd.read_csv("fixed_point_truncation/MCD_truncation.csv")
ACD_t = pd.read_csv("fixed_point_truncation/ACD_truncation.csv")

try:
    f_qiskit = open("files/qiskit_res/teleport.txt", "r")
except:
    print("It is not possible to open the files/qiskit_res/teleport.txt file\n")
statevectorQiskit = []
probabilityDensityQiskit = []

lines = f_qiskit.readlines()

for line in lines:
    z = complex(line[:-1])
    statevectorQiskit.append(z)
    probability = z.real**2 + z.imag**2  
    probabilityDensityQiskit.append(probability)
    
f_qiskit.close()

#verify the results floating
try:
    f_emulator = open("files/simulated/teleport.txt", "r")
except:
    print("It is not possible to open the files/simulated/teleport.txt file\n")
    sys.exit(1)
    
statevectorfloat = []
probabilityDensityfloat = []

lines = f_emulator.readlines()

for line in lines:
     val = line[:-1].split(" ")
     if len(val) == 2:
        real = float(val[0])
        img = float(val[1][:-1])
        z = complex(real, img)
        statevectorfloat.append(z)
        probability = real**2 + img**2  
        probabilityDensityfloat.append(probability)
        
f_emulator.close()


#verify the results fixed nearest
try:
    f_emulator = open("files/simulated_n_8/teleport.txt", "r")
except:
    print("It is not possible to open the files/simulated/teleport.txt file\n")
    sys.exit(1)
    
statevector_n = []
probabilityDensity_n = []

lines = f_emulator.readlines()

for line in lines:
     val = line[:-1].split(" ")
     if len(val) == 2:
        real = float(val[0])/2**(6)
        img = float(val[1][:-1])/2**(6)
        z = complex(real, img)
        statevector_n.append(z)
        probability = real**2 + img**2  
        probabilityDensity_n.append(probability)
        
f_emulator.close()


#verify the results fixed nearest even
try:
    f_emulator = open("files/simulated_ne_8/teleport.txt", "r")
except:
    print("It is not possible to open the files/simulated_ne_18/teleport.txt file\n")
    sys.exit(1)
    
statevector_ne = []
probabilityDensity_ne = []

lines = f_emulator.readlines()

for line in lines:
     val = line[:-1].split(" ")
     if len(val) == 2:
        real = float(val[0])/2**(6)
        img = float(val[1][:-1])/2**(6)
        z = complex(real, img)
        statevector_ne.append(z)
        probability = real**2 + img**2  
        probabilityDensity_ne.append(probability)
        
f_emulator.close()


#verify the results fixed nearest
try:
    f_emulator = open("files/simulated_t_8/teleport.txt", "r")
except:
    print("It is not possible to open the files/simulated_t_18/teleport.txt file\n")
    sys.exit(1)
    
statevector_t = []
probabilityDensity_t = []

lines = f_emulator.readlines()

for line in lines:
     val = line[:-1].split(" ")
     if len(val) == 2:
        real = float(val[0])/2**(6)
        img = float(val[1][:-1])/2**(6)
        z = complex(real, img)
        statevector_t.append(z)
        probability = real**2 + img**2  
        probabilityDensity_t.append(probability)
        
f_emulator.close()

label = []
for i in range(len(probabilityDensityfloat)):
    label.append(format(i, 'b').zfill(int(math.log2(len(probabilityDensityfloat)))))
                    

barWidth = 0.2
br1 = np.arange(len(probabilityDensityfloat))
br2 = [x + barWidth for x in br1]
br3 = [x + 2*barWidth for x in br1]
br4 = [x + 3*barWidth for x in br1]
br5 = [x + 4*barWidth for x in br1]
plt.bar(br1, probabilityDensityQiskit, color ='r', width = barWidth, label =r'\textit{State Vector Simulator}')
plt.bar(br2, probabilityDensityfloat, color ='darkorange', width = barWidth,  label =r'\textit{Emulator}')
plt.bar(br3, probabilityDensity_ne, color ='gold', width = barWidth,  label =r'\textit{8 bits nearest even}')
plt.bar(br4, probabilityDensity_n, color ='forestgreen', width = barWidth,  label =r'\textit{8 bits nearest}')
plt.bar(br5, probabilityDensity_t, color ='royalblue', width = barWidth,  label =r'\textit{8 bits truncation}')

plt.xticks([r + barWidth for r in range(len(probabilityDensityfloat))],label)
plt.xlabel(r'\textbf{Basis State}', fontsize=20)
plt.ylabel(r'\textbf{Probability}', fontsize=20)
leg = plt.legend(loc='upper left', frameon=True, fontsize=15)
leg.get_frame().set_facecolor('white')
plt.savefig("TeleportBarPlotComparisons.eps", format='eps')
plt.savefig("TeleportBarPlotComparisons.png", format='png')
plt.savefig("TeleportBarPlotComparisons.pdf", format='pdf')
plt.close() 
                        

plt.plot(EmulatorTime['Unnamed: 0'], EmulatorTime['0'], color='tab:green', linewidth=2,label=r'\textit{Emulator}')
plt.plot(list(QiskitTime['Unnamed: 0']),list(QiskitTime['0']), color='tab:blue', linewidth=2,label=r'\textit{State Vector Simulator}')
plt.plot(list(QASMTime['Unnamed: 0']),list(QASMTime['0']), color='tab:orange', linewidth=2,label=r'\textit{QASM Simulator}')
plt.title(r'\textbf{Emulation Time}',fontsize=20)
plt.xlabel(r'\textbf{File lenght}', fontsize=20)
plt.ylabel(r'\textbf{Time [s]}', fontsize=20)
leg = plt.legend(loc='upper left', frameon=True, fontsize=15)
leg.get_frame().set_facecolor('white')
plt.savefig("ComparisonTime.eps", format='eps', bbox_inches='tight')
plt.savefig("ComparisonTime.png", format='png', bbox_inches='tight')
plt.savefig("ComparisonTime.pdf", format='pdf', bbox_inches='tight')
plt.close()


plt.plot(EmulatorTime['Unnamed: 0'], EmulatorTime['0'], color='tab:green', linewidth=2,label=r'\textit{Emulator}')
plt.plot(list(QiskitTime['Unnamed: 0']),list(QiskitTime['0']), color='tab:blue', linewidth=2,label=r'\textit{State Vector Simulator}')
plt.plot(list(QASMTime['Unnamed: 0']),list(QASMTime['0']), color='tab:orange', linewidth=2,label=r'\textit{QASM Simulator}')
plt.yscale("log")
plt.title(r'\textbf{Emulation Time}',fontsize=20)
plt.xlabel(r'\textbf{File lenght}', fontsize=20)
plt.ylabel(r'\textbf{Time [s]}', fontsize=20)
leg = plt.legend(loc='lower right', frameon=True, fontsize=15)
leg.get_frame().set_facecolor('white')
plt.savefig("ComparisonTime_log.eps", format='eps', bbox_inches='tight')
plt.savefig("ComparisonTime_log.png", format='png', bbox_inches='tight')
plt.savefig("ComparisonTime_log.pdf", format='pdf', bbox_inches='tight')
plt.close()

listaCol = [ "firebrick", "coral", "gold", "yellowgreen", "lightgreen", "forestgreen", "turquoise", "deepskyblue", "royalblue", "slateblue", "purple", "orchid", "hotpink"]

i = 0 
plt.plot(EmulatorTime['Unnamed: 0'], EmulatorTime['0'], color='red', linewidth=2,label=r'\textit{Emulator}')
for parallelism in parallelisms:
    plt.plot(EmulatorTime_n['Unnamed: 0'], EmulatorTime_n[format(parallelism)], color=listaCol[i], linewidth=2,label=r'\textit{'+format(parallelism)+  'bits}') 
    i +=1
plt.title(r'\textbf{Emulation Time}',fontsize=20)
plt.xlabel(r'\textbf{File lenght}', fontsize=20)
plt.ylabel(r'\textbf{Time [s]}', fontsize=20)
plt.yscale("log")
leg = plt.legend(loc='upper right', frameon=True, fontsize=15)
leg.get_frame().set_facecolor('white')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("EmulatorTime_nearest.eps", format='eps',bbox_inches='tight')
plt.savefig("EmulatorTime_nearest.png", format='png', bbox_inches='tight')
plt.savefig("EmulatorTime_nearest.pdf", format='pdf', bbox_inches='tight')
plt.close() 

i = 0 
plt.plot(HF['Unnamed: 0'], HF['0'], color='red', linewidth=2,label=r'\textit{Emulator}')
for parallelism in parallelisms:
    plt.plot(HF_n['Unnamed: 0'], HF_n[format(parallelism)], color=listaCol[i], linewidth=2,label=r'\textit{'+format(parallelism)+  'bits}') 
    i += 1
plt.axhline(y = 0.95, color = 'r', linewidth=4,  linestyle = '--')     
plt.fill_between(HF_n['Unnamed: 0'], 0, 0.95, alpha=0.2, color='r')  
plt.ylim([0, 1.01]) 
plt.xlim([10, 187112]) 
plt.xscale("log")  
plt.title(r'\textbf{Fidelity}',fontsize=20)
plt.xlabel(r'\textbf{File lenght}', fontsize=20)
plt.ylabel(r'\textbf{Fidelity}', fontsize=20)
leg = plt.legend(loc='upper right', frameon=True, fontsize=15)
leg.get_frame().set_facecolor('white')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("HF_nearest.eps", format='eps', bbox_inches='tight')
plt.savefig("HF_nearest.png", format='png', bbox_inches='tight')
plt.savefig("HF_nearest.pdf", format='pdf', bbox_inches='tight')
plt.close()    

i = 0 
plt.plot(HF['Unnamed: 0'], HF['0'], color='red', linewidth=2,label=r'\textit{Emulator}')
for parallelism in range(18, 33, 2):
    plt.plot(HF_n['Unnamed: 0'], HF_n[format(parallelism)], color=listaCol[i], linewidth=2,label=r'\textit{'+format(parallelism)+  'bits}') 
    i += 1
plt.axhline(y = 0.95, color = 'r', linewidth=4,  linestyle = '--')     
plt.fill_between(HF_n['Unnamed: 0'], 0, 0.95, alpha=0.2, color='r')  
plt.ylim([0, 1.01])   
plt.xlim([10, 187112]) 
plt.xscale("log")   
plt.title(r'\textbf{Fidelity}',fontsize=20)
plt.xlabel(r'\textbf{File lenght}', fontsize=20)
plt.ylabel(r'\textbf{Fidelity}', fontsize=20)
leg = plt.legend(loc='upper right', frameon=True, fontsize=15)
leg.get_frame().set_facecolor('white')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("HF_nearest_less.eps", format='eps', bbox_inches='tight')
plt.savefig("HF_nearest_less.png", format='png', bbox_inches='tight')
plt.savefig("HF_nearest_less.pdf", format='pdf', bbox_inches='tight')
plt.close()  

i = 0 
plt.plot(KLD['Unnamed: 0'], KLD['0'], color='red', linewidth=2,label=r'\textit{Emulator}')
for parallelism in parallelisms:
    plt.plot(KLD_n['Unnamed: 0'], KLD_n[format(parallelism)], color=listaCol[i], linewidth=2,label=r'\textit{'+format(parallelism)+  'bits}')   
    i += 1
plt.axhline(y = 0.05, color = 'r', linewidth=4,  linestyle = '--')   
plt.fill_between(KLD_n['Unnamed: 0'],0.05, 1, alpha=0.2, color='r') 
plt.ylim([-0.05, 1])   
plt.xlim([10, 187112]) 
plt.xscale("log")    
plt.title(r'\textbf{kld}',fontsize=20)
plt.xlabel(r'\textbf{File lenght}', fontsize=20)
plt.ylabel(r'\textbf{kld}', fontsize=20)
leg = plt.legend(loc='upper right', frameon=True, fontsize=15)
leg.get_frame().set_facecolor('white')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("Kld_nearest.eps", format='eps', bbox_inches='tight')
plt.savefig("Kld_nearest.png", format='png', bbox_inches='tight')
plt.savefig("Kld_nearest.pdf", format='pdf', bbox_inches='tight')
plt.close() 


i = 0 
plt.plot(KLD['Unnamed: 0'], KLD['0'], color='red', linewidth=2,label=r'\textit{Emulator}')
for parallelism in  range(18, 33, 2):
    plt.plot(KLD_n['Unnamed: 0'], KLD_n[format(parallelism)], color=listaCol[i], linewidth=2,label=r'\textit{'+format(parallelism)+  'bits}')   
    i += 1
plt.axhline(y = 0.05, color = 'r', linewidth=4,  linestyle = '--')   
plt.fill_between(KLD_n['Unnamed: 0'],0.05, 1, alpha=0.2, color='r') 
plt.ylim([-0.05, 1])    
plt.xlim([10, 187112]) 
plt.xscale("log")   
plt.title(r'\textbf{kld}',fontsize=20)
plt.xlabel(r'\textbf{File lenght}', fontsize=20)
plt.ylabel(r'\textbf{kld}', fontsize=20)
leg = plt.legend(loc='upper right', frameon=True, fontsize=15)
leg.get_frame().set_facecolor('white')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("Kld_nearest_less.eps", format='eps', bbox_inches='tight')
plt.savefig("Kld_nearest_less.png", format='png', bbox_inches='tight')
plt.savefig("Kld_nearest_less.pdf", format='pdf', bbox_inches='tight')
plt.close() 

i = 0 
plt.plot(MCD['Unnamed: 0'], MCD['0'], color='red', linewidth=2,label=r'\textit{Emulator}')
for parallelism in parallelisms:
    plt.plot(MCD_n['Unnamed: 0'], MCD_n[format(parallelism)], color=listaCol[i], linewidth=2,label=r'\textit{'+format(parallelism)+  'bits}')    
    i += 1
plt.axhline(y = 0.05, color = 'r', linewidth=4,  linestyle = '--')   
plt.fill_between(MCD_n['Unnamed: 0'],0.05, 1, alpha=0.2, color='r')     
plt.ylim([-0.05, 1])   
plt.xlim([10, 187112]) 
plt.xscale("log")    
plt.title(r'\textbf{Maximum complex distance}',fontsize=20)
plt.xlabel(r'\textbf{File lenght}', fontsize=20)
plt.ylabel(r'\textbf{Maximum complex distance}', fontsize=20)
leg = plt.legend(loc='upper right', frameon=True, fontsize=15)
leg.get_frame().set_facecolor('white')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("MCD_nearest.eps", format='eps', bbox_inches='tight')
plt.savefig("MCD_nearest.png", format='png', bbox_inches='tight')
plt.savefig("MCD_nearest.pdf", format='pdf', bbox_inches='tight')
plt.close()  

i = 0 
plt.plot(MCD['Unnamed: 0'], MCD['0'], color='red', linewidth=2,label=r'\textit{Emulator}')
for parallelism in range(18, 33, 2):
    plt.plot(MCD_n['Unnamed: 0'], MCD_n[format(parallelism)], color=listaCol[i], linewidth=2,label=r'\textit{'+format(parallelism)+  'bits}')    
    i += 1
plt.axhline(y = 0.05, color = 'r', linewidth=4,  linestyle = '--')   
plt.fill_between(MCD_n['Unnamed: 0'],0.05, 1, alpha=0.2, color='r')     
plt.ylim([-0.05, 1])     
plt.xlim([10, 187112]) 
plt.xscale("log")  
plt.title(r'\textbf{Maximum complex distance}',fontsize=20)
plt.xlabel(r'\textbf{File lenght}', fontsize=20)
plt.ylabel(r'\textbf{Maximum complex distance}', fontsize=20)
leg = plt.legend(loc='upper right', frameon=True, fontsize=15)
leg.get_frame().set_facecolor('white')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("MCD_nearest_less.eps", format='eps', bbox_inches='tight')
plt.savefig("MCD_nearest_less.png", format='png', bbox_inches='tight')
plt.savefig("MCD_nearest_less.pdf", format='pdf', bbox_inches='tight')
plt.close()  

i = 0 
plt.plot(ACD['Unnamed: 0'], ACD['0'], color='red', linewidth=2,label=r'\textit{Emulator}')
for parallelism in parallelisms:
    plt.plot(ACD_n['Unnamed: 0'], ACD_n[format(parallelism)], color=listaCol[i], linewidth=2,label=r'\textit{'+format(parallelism)+  'bits}') 
    i += 1
plt.axhline(y = 0.05, color = 'r', linewidth=4,  linestyle = '--')   
plt.fill_between(ACD_n['Unnamed: 0'],0.05, 1, alpha=0.2, color='r')     
plt.ylim([-0.05, 1])    
plt.xlim([10, 187112]) 
plt.xscale("log")    
plt.title(r'\textbf{Average complex distance}',fontsize=20)
plt.xlabel(r'\textbf{File lenght}', fontsize=20)
plt.ylabel(r'\textbf{Average complex distance}', fontsize=20)
leg = plt.legend(loc='upper right', frameon=True, fontsize=15)
leg.get_frame().set_facecolor('white')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("ACD_nearest.eps", format='eps', bbox_inches='tight')
plt.savefig("ACD_nearest.png", format='png', bbox_inches='tight')
plt.savefig("ACD_nearest.pdf", format='pdf', bbox_inches='tight')
plt.close()

i = 0 
plt.plot(ACD['Unnamed: 0'], ACD['0'], color='red', linewidth=2,label=r'\textit{Emulator}')
for parallelism in range(18, 33, 2):
    plt.plot(ACD_n['Unnamed: 0'], ACD_n[format(parallelism)], color=listaCol[i], linewidth=2,label=r'\textit{'+format(parallelism)+  'bits}') 
    i += 1
plt.axhline(y = 0.05, color = 'r', linewidth=4,  linestyle = '--')   
plt.fill_between(ACD_n['Unnamed: 0'],0.05, 1, alpha=0.2, color='r')     
plt.ylim([-0.05, 1])   
plt.xlim([10, 187112]) 
plt.xscale("log")     
plt.title(r'\textbf{Average complex distance}',fontsize=20)
plt.xlabel(r'\textbf{File lenght}', fontsize=20)
plt.ylabel(r'\textbf{Average complex distance}', fontsize=20)
leg = plt.legend(loc='upper right', frameon=True, fontsize=15)
leg.get_frame().set_facecolor('white')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("ACD_nearest_less.eps", format='eps', bbox_inches='tight')
plt.savefig("ACD_nearest_less.png", format='png', bbox_inches='tight')
plt.savefig("ACD_nearest_less.pdf", format='pdf', bbox_inches='tight')
plt.close()  












i = 0 
plt.plot(EmulatorTime['Unnamed: 0'], EmulatorTime['0'], color='red', linewidth=2,label=r'\textit{Emulator}')
for parallelism in parallelisms:
    plt.plot(EmulatorTime_t['Unnamed: 0'], EmulatorTime_t[format(parallelism)], color=listaCol[i], linewidth=2,label=r'\textit{'+format(parallelism)+  'bits}') 
    i +=1
plt.title(r'\textbf{Emulation Time}',fontsize=20)
plt.xlabel(r'\textbf{File lenght}', fontsize=20)
plt.ylabel(r'\textbf{Time [s]}', fontsize=20)
plt.yscale("log")
plt.xlim([10, 187112]) 
plt.xscale("log")  
leg = plt.legend(loc='upper right', frameon=True, fontsize=15)
leg.get_frame().set_facecolor('white')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("EmulatorTime_truncation.eps", format='eps',bbox_inches='tight')
plt.savefig("EmulatorTime_truncation.png", format='png', bbox_inches='tight')
plt.savefig("EmulatorTime_truncation.pdf", format='pdf', bbox_inches='tight')
plt.close() 

i = 0 
plt.plot(HF['Unnamed: 0'], HF['0'], color='red', linewidth=2,label=r'\textit{Emulator}')
for parallelism in parallelisms:
    plt.plot(HF_t['Unnamed: 0'], HF_t[format(parallelism)], color=listaCol[i], linewidth=2,label=r'\textit{'+format(parallelism)+  'bits}') 
    i += 1
plt.axhline(y = 0.95, color = 'r', linewidth=4,  linestyle = '--')     
plt.fill_between(HF_t['Unnamed: 0'], 0, 0.95, alpha=0.2, color='r')  
plt.ylim([0, 1.01])
plt.xlim([10, 187112]) 
plt.xscale("log")      
plt.title(r'\textbf{Fidelity}',fontsize=20)
plt.xlabel(r'\textbf{File lenght}', fontsize=20)
plt.ylabel(r'\textbf{Fidelity}', fontsize=20)
leg = plt.legend(loc='upper right', frameon=True, fontsize=15)
leg.get_frame().set_facecolor('white')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("HF_truncation.eps", format='eps', bbox_inches='tight')
plt.savefig("HF_truncation.png", format='png', bbox_inches='tight')
plt.savefig("HF_truncation.pdf", format='pdf', bbox_inches='tight')
plt.close()    

i = 0 
plt.plot(HF['Unnamed: 0'], HF['0'], color='red', linewidth=2,label=r'\textit{Emulator}')
for parallelism in range(18, 33, 2):
    plt.plot(HF_t['Unnamed: 0'], HF_t[format(parallelism)], color=listaCol[i], linewidth=2,label=r'\textit{'+format(parallelism)+  'bits}') 
    i += 1
plt.axhline(y = 0.95, color = 'r', linewidth=4,  linestyle = '--')     
plt.fill_between(HF_t['Unnamed: 0'], 0, 0.95, alpha=0.2, color='r')  
plt.ylim([0, 1.01]) 
plt.xlim([10, 187112]) 
plt.xscale("log")     
plt.title(r'\textbf{Fidelity}',fontsize=20)
plt.xlabel(r'\textbf{File lenght}', fontsize=20)
plt.ylabel(r'\textbf{Fidelity}', fontsize=20)
leg = plt.legend(loc='upper right', frameon=True, fontsize=15)
leg.get_frame().set_facecolor('white')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("HF_truncation_less.eps", format='eps', bbox_inches='tight')
plt.savefig("HF_truncation_less.png", format='png', bbox_inches='tight')
plt.savefig("HF_truncation_less.pdf", format='pdf', bbox_inches='tight')
plt.close()  

i = 0 
plt.plot(KLD['Unnamed: 0'], KLD['0'], color='red', linewidth=2,label=r'\textit{Emulator}')
for parallelism in parallelisms:
    plt.plot(KLD_t['Unnamed: 0'], KLD_t[format(parallelism)], color=listaCol[i], linewidth=2,label=r'\textit{'+format(parallelism)+  'bits}')   
    i += 1
plt.axhline(y = 0.05, color = 'r', linewidth=4,  linestyle = '--')   
plt.fill_between(KLD_t['Unnamed: 0'],0.05, 1, alpha=0.2, color='r') 
plt.ylim([-0.05, 1])  
plt.xlim([10, 187112]) 
plt.xscale("log")     
plt.title(r'\textbf{kld}',fontsize=20)
plt.xlabel(r'\textbf{File lenght}', fontsize=20)
plt.ylabel(r'\textbf{kld}', fontsize=20)
leg = plt.legend(loc='upper right', frameon=True, fontsize=15)
leg.get_frame().set_facecolor('white')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("Kld_truncation.eps", format='eps', bbox_inches='tight')
plt.savefig("Kld_truncation.png", format='png', bbox_inches='tight')
plt.savefig("Kld_truncation.pdf", format='pdf', bbox_inches='tight')
plt.close() 


i = 0 
plt.plot(KLD['Unnamed: 0'], KLD['0'], color='red', linewidth=2,label=r'\textit{Emulator}')
for parallelism in  range(18, 33, 2):
    plt.plot(KLD_t['Unnamed: 0'], KLD_t[format(parallelism)], color=listaCol[i], linewidth=2,label=r'\textit{'+format(parallelism)+  'bits}')   
    i += 1
plt.axhline(y = 0.05, color = 'r', linewidth=4,  linestyle = '--')   
plt.fill_between(KLD_t['Unnamed: 0'],0.05, 1, alpha=0.2, color='r') 
plt.ylim([-0.05, 1])  
plt.xlim([10, 187112]) 
plt.xscale("log")     
plt.title(r'\textbf{kld}',fontsize=20)
plt.xlabel(r'\textbf{File lenght}', fontsize=20)
plt.ylabel(r'\textbf{kld}', fontsize=20)
leg = plt.legend(loc='upper right', frameon=True, fontsize=15)
leg.get_frame().set_facecolor('white')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("Kld_nearest_truncation_less.eps", format='eps', bbox_inches='tight')
plt.savefig("Kld_nearest_truncation_less.png", format='png', bbox_inches='tight')
plt.savefig("Kld_nearest_truncation_less.pdf", format='pdf', bbox_inches='tight')
plt.close() 

i = 0 
plt.plot(MCD['Unnamed: 0'], MCD['0'], color='red', linewidth=2,label=r'\textit{Emulator}')
for parallelism in parallelisms:
    plt.plot(MCD_t['Unnamed: 0'], MCD_t[format(parallelism)], color=listaCol[i], linewidth=2,label=r'\textit{'+format(parallelism)+  'bits}')    
    i += 1
plt.axhline(y = 0.05, color = 'r', linewidth=4,  linestyle = '--')   
plt.fill_between(MCD_t['Unnamed: 0'],0.05, 1, alpha=0.2, color='r')     
plt.ylim([-0.05, 1])    
plt.xlim([10, 187112]) 
plt.xscale("log")   
plt.title(r'\textbf{Maximum complex distance}',fontsize=20)
plt.xlabel(r'\textbf{File lenght}', fontsize=20)
plt.ylabel(r'\textbf{Maximum complex distance}', fontsize=20)
leg = plt.legend(loc='upper right', frameon=True, fontsize=15)
leg.get_frame().set_facecolor('white')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("MCD_truncation.eps", format='eps', bbox_inches='tight')
plt.savefig("MCD_truncation.png", format='png', bbox_inches='tight')
plt.savefig("MCD_truncation.pdf", format='pdf', bbox_inches='tight')
plt.close()  

i = 0 
plt.plot(MCD['Unnamed: 0'], MCD['0'], color='red', linewidth=2,label=r'\textit{Emulator}')
for parallelism in range(18, 33, 2):
    plt.plot(MCD_t['Unnamed: 0'], MCD_t[format(parallelism)], color=listaCol[i], linewidth=2,label=r'\textit{'+format(parallelism)+  'bits}')    
    i += 1
plt.axhline(y = 0.05, color = 'r', linewidth=4,  linestyle = '--')   
plt.fill_between(MCD_t['Unnamed: 0'],0.05, 1, alpha=0.2, color='r')     
plt.ylim([-0.05, 1])    
plt.xlim([10, 187112]) 
plt.xscale("log")   
plt.title(r'\textbf{Maximum complex distance}',fontsize=20)
plt.xlabel(r'\textbf{File lenght}', fontsize=20)
plt.ylabel(r'\textbf{Maximum complex distance}', fontsize=20)
leg = plt.legend(loc='upper right', frameon=True, fontsize=15)
leg.get_frame().set_facecolor('white')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("MCD_truncation_less.eps", format='eps', bbox_inches='tight')
plt.savefig("MCD_truncation_less.png", format='png', bbox_inches='tight')
plt.savefig("MCD_truncation_less.pdf", format='pdf', bbox_inches='tight')
plt.close()  

i = 0 
plt.plot(ACD['Unnamed: 0'], ACD['0'], color='red', linewidth=2,label=r'\textit{Emulator}')
for parallelism in parallelisms:
    plt.plot(ACD_t['Unnamed: 0'], ACD_t[format(parallelism)], color=listaCol[i], linewidth=2,label=r'\textit{'+format(parallelism)+  'bits}') 
    i += 1
plt.axhline(y = 0.05, color = 'r', linewidth=4,  linestyle = '--')   
plt.fill_between(ACD_t['Unnamed: 0'],0.05, 1, alpha=0.2, color='r')     
plt.ylim([-0.05, 1])
plt.xlim([10, 187112]) 
plt.xscale("log")        
plt.title(r'\textbf{Average complex distance}',fontsize=20)
plt.xlabel(r'\textbf{File lenght}', fontsize=20)
plt.ylabel(r'\textbf{Average complex distance}', fontsize=20)
leg = plt.legend(loc='upper right', frameon=True, fontsize=15)
leg.get_frame().set_facecolor('white')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("ACD_truncation.eps", format='eps', bbox_inches='tight')
plt.savefig("ACD_truncation.png", format='png', bbox_inches='tight')
plt.savefig("ACD_truncation.pdf", format='pdf', bbox_inches='tight')
plt.close()

i = 0 
plt.plot(ACD['Unnamed: 0'], ACD['0'], color='red', linewidth=2,label=r'\textit{Emulator}')
for parallelism in range(18, 33, 2):
    plt.plot(ACD_t['Unnamed: 0'], ACD_t[format(parallelism)], color=listaCol[i], linewidth=2,label=r'\textit{'+format(parallelism)+  'bits}') 
    i += 1
plt.axhline(y = 0.05, color = 'r', linewidth=4,  linestyle = '--')   
plt.fill_between(ACD_t['Unnamed: 0'],0.05, 1, alpha=0.2, color='r')     
plt.ylim([-0.05, 1]) 
plt.xlim([10, 187112]) 
plt.xscale("log")       
plt.title(r'\textbf{Average complex distance}',fontsize=20)
plt.xlabel(r'\textbf{File lenght}', fontsize=20)
plt.ylabel(r'\textbf{Average complex distance}', fontsize=20)
leg = plt.legend(loc='upper right', frameon=True, fontsize=15)
leg.get_frame().set_facecolor('white')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("ACD_truncation_less.eps", format='eps', bbox_inches='tight')
plt.savefig("ACD_truncation_less.png", format='png', bbox_inches='tight')
plt.savefig("ACD_truncation_less.pdf", format='pdf', bbox_inches='tight')
plt.close()  



i = 0 
plt.plot(EmulatorTime['Unnamed: 0'], EmulatorTime['0'], color='red', linewidth=2,label=r'\textit{Emulator}')
for parallelism in parallelisms:
    plt.plot(EmulatorTime_ne['Unnamed: 0'], EmulatorTime_ne[format(parallelism)], color=listaCol[i], linewidth=2,label=r'\textit{'+format(parallelism)+  'bits}') 
    i +=1
plt.title(r'\textbf{Emulation Time}',fontsize=20)
plt.xlabel(r'\textbf{File lenght}', fontsize=20)
plt.ylabel(r'\textbf{Time [s]}', fontsize=20)
plt.yscale("log")
leg = plt.legend(loc='upper right', frameon=True, fontsize=15)
leg.get_frame().set_facecolor('white')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("EmulatorTime_nearest_even.eps", format='eps',bbox_inches='tight')
plt.savefig("EmulatorTime_nearest_even.png", format='png', bbox_inches='tight')
plt.savefig("EmulatorTime_nearest_even.pdf", format='pdf', bbox_inches='tight')
plt.close() 

i = 0 
plt.plot(HF['Unnamed: 0'], HF['0'], color='red', linewidth=2,label=r'\textit{Emulator}')
for parallelism in parallelisms:
    plt.plot(HF_ne['Unnamed: 0'], HF_ne[format(parallelism)], color=listaCol[i], linewidth=2,label=r'\textit{'+format(parallelism)+  'bits}') 
    i += 1
plt.axhline(y = 0.95, color = 'r', linewidth=4,  linestyle = '--')     
plt.fill_between(HF_ne['Unnamed: 0'], 0, 0.95, alpha=0.2, color='r')  
plt.ylim([0, 1.01]) 
plt.xlim([10, 187112]) 
plt.xscale("log")     
plt.title(r'\textbf{Fidelity}',fontsize=20)
plt.xlabel(r'\textbf{File lenght}', fontsize=20)
plt.ylabel(r'\textbf{Fidelity}', fontsize=20)
leg = plt.legend(loc='upper right', frameon=True, fontsize=15)
leg.get_frame().set_facecolor('white')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("HF_nearest_even.eps", format='eps', bbox_inches='tight')
plt.savefig("HF_nearest_even.png", format='png', bbox_inches='tight')
plt.savefig("HF_nearest_even.pdf", format='pdf', bbox_inches='tight')
plt.close()    

i = 0 
plt.plot(HF['Unnamed: 0'], HF['0'], color='red', linewidth=2,label=r'\textit{Emulator}')
for parallelism in range(18, 33, 2):
    plt.plot(HF_ne['Unnamed: 0'], HF_ne[format(parallelism)], color=listaCol[i], linewidth=2,label=r'\textit{'+format(parallelism)+  'bits}') 
    i += 1
plt.axhline(y = 0.95, color = 'r', linewidth=4,  linestyle = '--')     
plt.fill_between(HF_n['Unnamed: 0'], 0, 0.95, alpha=0.2, color='r')  
plt.ylim([0, 1.01])  
plt.xlim([10, 187112]) 
plt.xscale("log")    
plt.title(r'\textbf{Fidelity}',fontsize=20)
plt.xlabel(r'\textbf{File lenght}', fontsize=20)
plt.ylabel(r'\textbf{Fidelity}', fontsize=20)
leg = plt.legend(loc='upper right', frameon=True, fontsize=15)
leg.get_frame().set_facecolor('white')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("HF_nearest_even_less.eps", format='eps', bbox_inches='tight')
plt.savefig("HF_nearest_even_less.png", format='png', bbox_inches='tight')
plt.savefig("HF_nearest_even_less.pdf", format='pdf', bbox_inches='tight')
plt.close()  

i = 0 
plt.plot(KLD['Unnamed: 0'], KLD['0'], color='red', linewidth=2,label=r'\textit{Emulator}')
for parallelism in parallelisms:
    plt.plot(KLD_ne['Unnamed: 0'], KLD_ne[format(parallelism)], color=listaCol[i], linewidth=2,label=r'\textit{'+format(parallelism)+  'bits}')   
    i += 1
plt.axhline(y = 0.05, color = 'r', linewidth=4,  linestyle = '--')   
plt.fill_between(KLD_ne['Unnamed: 0'],0.05, 1, alpha=0.2, color='r') 
plt.ylim([-0.05, 1])  
plt.xlim([10, 187112]) 
plt.xscale("log")     
plt.title(r'\textbf{kld}',fontsize=20)
plt.xlabel(r'\textbf{File lenght}', fontsize=20)
plt.ylabel(r'\textbf{kld}', fontsize=20)
leg = plt.legend(loc='upper right', frameon=True, fontsize=15)
leg.get_frame().set_facecolor('white')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("Kld_nearest_even.eps", format='eps', bbox_inches='tight')
plt.savefig("Kld_nearest_even.png", format='png', bbox_inches='tight')
plt.savefig("Kld_nearest_even.pdf", format='pdf', bbox_inches='tight')
plt.close() 


i = 0 
plt.plot(KLD['Unnamed: 0'], KLD['0'], color='red', linewidth=2,label=r'\textit{Emulator}')
for parallelism in  range(18, 33, 2):
    plt.plot(KLD_ne['Unnamed: 0'], KLD_ne[format(parallelism)], color=listaCol[i], linewidth=2,label=r'\textit{'+format(parallelism)+  'bits}')   
    i += 1
plt.axhline(y = 0.05, color = 'r', linewidth=4,  linestyle = '--')   
plt.fill_between(KLD_ne['Unnamed: 0'],0.05, 1, alpha=0.2, color='r') 
plt.ylim([-0.05, 1])   
plt.xlim([10, 187112]) 
plt.xscale("log")    
plt.title(r'\textbf{kld}',fontsize=20)
plt.xlabel(r'\textbf{File lenght}', fontsize=20)
plt.ylabel(r'\textbf{kld}', fontsize=20)
leg = plt.legend(loc='upper right', frameon=True, fontsize=15)
leg.get_frame().set_facecolor('white')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("Kld_nearest_even_even_less.eps", format='eps', bbox_inches='tight')
plt.savefig("Kld_nearest_even_less.png", format='png', bbox_inches='tight')
plt.savefig("Kld_nearest_even_less.pdf", format='pdf', bbox_inches='tight')
plt.close() 

i = 0 
plt.plot(MCD['Unnamed: 0'], MCD['0'], color='red', linewidth=2,label=r'\textit{Emulator}')
for parallelism in parallelisms:
    plt.plot(MCD_ne['Unnamed: 0'], MCD_ne[format(parallelism)], color=listaCol[i], linewidth=2,label=r'\textit{'+format(parallelism)+  'bits}')    
    i += 1
plt.axhline(y = 0.05, color = 'r', linewidth=4,  linestyle = '--')   
plt.fill_between(MCD_ne['Unnamed: 0'],0.05, 1, alpha=0.2, color='r')     
plt.ylim([-0.05, 1])  
plt.xlim([10, 187112]) 
plt.xscale("log")     
plt.title(r'\textbf{Maximum complex distance}',fontsize=20)
plt.xlabel(r'\textbf{File lenght}', fontsize=20)
plt.ylabel(r'\textbf{Maximum complex distance}', fontsize=20)
leg = plt.legend(loc='upper right', frameon=True, fontsize=15)
leg.get_frame().set_facecolor('white')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("MCD_nearest_even.eps", format='eps', bbox_inches='tight')
plt.savefig("MCD_nearest_even.png", format='png', bbox_inches='tight')
plt.savefig("MCD_nearest_even.pdf", format='pdf', bbox_inches='tight')
plt.close()  

i = 0 
plt.plot(MCD['Unnamed: 0'], MCD['0'], color='red', linewidth=2,label=r'\textit{Emulator}')
for parallelism in range(18, 33, 2):
    plt.plot(MCD_ne['Unnamed: 0'], MCD_ne[format(parallelism)], color=listaCol[i], linewidth=2,label=r'\textit{'+format(parallelism)+  'bits}')    
    i += 1
plt.axhline(y = 0.05, color = 'r', linewidth=4,  linestyle = '--')   
plt.fill_between(MCD_ne['Unnamed: 0'],0.05, 1, alpha=0.2, color='r')     
plt.ylim([-0.05, 1])  
plt.xlim([10, 187112]) 
plt.xscale("log")     
plt.title(r'\textbf{Maximum complex distance}',fontsize=20)
plt.xlabel(r'\textbf{File lenght}', fontsize=20)
plt.ylabel(r'\textbf{Maximum complex distance}', fontsize=20)
leg = plt.legend(loc='upper right', frameon=True, fontsize=15)
leg.get_frame().set_facecolor('white')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("MCD_nearest_even_less.eps", format='eps', bbox_inches='tight')
plt.savefig("MCD_nearest_even_less.png", format='png', bbox_inches='tight')
plt.savefig("MCD_nearest_even_less.pdf", format='pdf', bbox_inches='tight')
plt.close()  

i = 0 
plt.plot(ACD['Unnamed: 0'], ACD['0'], color='red', linewidth=2,label=r'\textit{Emulator}')
for parallelism in parallelisms:
    plt.plot(ACD_ne['Unnamed: 0'], ACD_ne[format(parallelism)], color=listaCol[i], linewidth=2,label=r'\textit{'+format(parallelism)+  'bits}') 
    i += 1
plt.axhline(y = 0.05, color = 'r', linewidth=4,  linestyle = '--')   
plt.fill_between(ACD_ne['Unnamed: 0'],0.05, 1, alpha=0.2, color='r')     
plt.ylim([-0.05, 1])     
plt.xlim([10, 187112]) 
plt.xscale("log")   
plt.title(r'\textbf{Average complex distance}',fontsize=20)
plt.xlabel(r'\textbf{File lenght}', fontsize=20)
plt.ylabel(r'\textbf{Average complex distance}', fontsize=20)
leg = plt.legend(loc='upper right', frameon=True, fontsize=15)
leg.get_frame().set_facecolor('white')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("ACD_nearest_even.eps", format='eps', bbox_inches='tight')
plt.savefig("ACD_nearest_even.png", format='png', bbox_inches='tight')
plt.savefig("ACD_nearest_even.pdf", format='pdf', bbox_inches='tight')
plt.close()

i = 0 
plt.plot(ACD['Unnamed: 0'], ACD['0'], color='red', linewidth=2,label=r'\textit{Emulator}')
for parallelism in range(18, 33, 2):
    plt.plot(ACD_n['Unnamed: 0'], ACD_n[format(parallelism)], color=listaCol[i], linewidth=2,label=r'\textit{'+format(parallelism)+  'bits}') 
    i += 1
plt.axhline(y = 0.05, color = 'r', linewidth=4,  linestyle = '--')   
plt.fill_between(ACD_n['Unnamed: 0'],0.05, 1, alpha=0.2, color='r')     
plt.ylim([-0.05, 1])   
plt.xlim([10, 187112]) 
plt.xscale("log")     
plt.title(r'\textbf{Average complex distance}',fontsize=20)
plt.xlabel(r'\textbf{File lenght}', fontsize=20)
plt.ylabel(r'\textbf{Average complex distance}', fontsize=20)
leg = plt.legend(loc='upper right', frameon=True, fontsize=15)
leg.get_frame().set_facecolor('white')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("ACD_nearest_even_less.eps", format='eps', bbox_inches='tight')
plt.savefig("ACD_nearest_even_less.png", format='png', bbox_inches='tight')
plt.savefig("ACD_nearest_even_less.pdf", format='pdf', bbox_inches='tight')
plt.close()  
















plt.plot(EmulatorTime['Unnamed: 0'], EmulatorTime['0'], color='red', linewidth=2,label=r'\textit{Emulator}')
plt.plot(EmulatorTime_ne['Unnamed: 0'], EmulatorTime_ne[format(20)], color="gold", linewidth=2,label=r'\textit{20 bits nearest even}') 
plt.plot(EmulatorTime_n['Unnamed: 0'], EmulatorTime_n[format(20)], color="forestgreen", linewidth=2,label=r'\textit{20 bits nearest}') 
plt.plot(EmulatorTime_t['Unnamed: 0'], EmulatorTime_t[format(20)], color="royalblue", linewidth=2,label=r'\textit{20 bits truncation}') 
plt.title(r'\textbf{Emulation Time}',fontsize=20)
plt.xlabel(r'\textbf{File lenght}', fontsize=20)
plt.ylabel(r'\textbf{Time [s]}', fontsize=20)
plt.yscale("log")
leg = plt.legend(loc='upper right', frameon=True, fontsize=15)
leg.get_frame().set_facecolor('white')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("EmulatorTime_comparison_fixed.eps", format='eps',bbox_inches='tight')
plt.savefig("EmulatorTime_comparison_fixed.png", format='png', bbox_inches='tight')
plt.savefig("EmulatorTime_comparison_fixed.pdf", format='pdf', bbox_inches='tight')
plt.close() 

i = 0 
plt.plot(HF['Unnamed: 0'], HF['0'], color='red', linewidth=2,label=r'\textit{Emulator}')
plt.plot(HF_ne['Unnamed: 0'], HF_ne[format(20)], color="gold", linewidth=2,label=r'\textit{20 bits nearest even}') 
plt.plot(HF_n['Unnamed: 0'], HF_n[format(20)], color="forestgreen", linewidth=2,label=r'\textit{20 bits nearest}') 
plt.plot(HF_t['Unnamed: 0'], HF_t[format(20)], color="royalblue", linewidth=2,label=r'\textit{20 bits truncation}') 
plt.axhline(y = 0.95, color = 'r', linewidth=4,  linestyle = '--')     
plt.fill_between(HF_ne['Unnamed: 0'], 0, 0.95, alpha=0.2, color='r')  
plt.ylim([0, 1.01]) 
plt.xlim([10, 187112]) 
plt.xscale("log")     
plt.title(r'\textbf{Fidelity}',fontsize=20)
plt.xlabel(r'\textbf{File lenght}', fontsize=20)
plt.ylabel(r'\textbf{Fidelity}', fontsize=20)
leg = plt.legend(loc='upper right', frameon=True, fontsize=15)
leg.get_frame().set_facecolor('white')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("HF_comparison.eps", format='eps', bbox_inches='tight')
plt.savefig("HF_comparison.png", format='png', bbox_inches='tight')
plt.savefig("HF_comparison.pdf", format='pdf', bbox_inches='tight')
plt.close()    


i = 0 
plt.plot(KLD['Unnamed: 0'], KLD['0'], color='red', linewidth=2,label=r'\textit{Emulator}')
plt.plot(KLD_ne['Unnamed: 0'], KLD_ne[format(20)], color="gold", linewidth=2,label=r'\textit{20 bits nearest even}') 
plt.plot(KLD_n['Unnamed: 0'], KLD_n[format(20)], color="forestgreen", linewidth=2,label=r'\textit{20 bits nearest}') 
plt.plot(KLD_t['Unnamed: 0'], KLD_t[format(20)], color="royalblue", linewidth=2,label=r'\textit{20 bits truncation}') 
plt.axhline(y = 0.05, color = 'r', linewidth=4,  linestyle = '--')   
plt.fill_between(KLD_ne['Unnamed: 0'],0.05, 1, alpha=0.2, color='r') 
plt.ylim([-0.05, 1])  
plt.xlim([10, 187112]) 
plt.xscale("log")     
plt.title(r'\textbf{kld}',fontsize=20)
plt.xlabel(r'\textbf{File lenght}', fontsize=20)
plt.ylabel(r'\textbf{kld}', fontsize=20)
leg = plt.legend(loc='upper right', frameon=True, fontsize=15)
leg.get_frame().set_facecolor('white')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("Kld_comparison.eps", format='eps', bbox_inches='tight')
plt.savefig("Kld_comparison.png", format='png', bbox_inches='tight')
plt.savefig("Kld_comparison.pdf", format='pdf', bbox_inches='tight')
plt.close() 
 

i = 0 
plt.plot(MCD['Unnamed: 0'], MCD['0'], color='red', linewidth=2,label=r'\textit{Emulator}')
plt.plot(MCD_ne['Unnamed: 0'], MCD_ne[format(20)], color="gold", linewidth=2,label=r'\textit{20 bits nearest even}') 
plt.plot(MCD_n['Unnamed: 0'], MCD_n[format(20)], color="forestgreen", linewidth=2,label=r'\textit{20 bits nearest}') 
plt.plot(MCD_t['Unnamed: 0'], MCD_t[format(20)], color="royalblue", linewidth=2,label=r'\textit{20 bits truncation}') 
plt.axhline(y = 0.05, color = 'r', linewidth=4,  linestyle = '--')   
plt.fill_between(MCD_ne['Unnamed: 0'],0.05, 1, alpha=0.2, color='r')     
plt.ylim([-0.05, 1])  
plt.xlim([10, 187112]) 
plt.xscale("log")     
plt.title(r'\textbf{Maximum complex distance}',fontsize=20)
plt.xlabel(r'\textbf{File lenght}', fontsize=20)
plt.ylabel(r'\textbf{Maximum complex distance}', fontsize=20)
leg = plt.legend(loc='upper right', frameon=True, fontsize=15)
leg.get_frame().set_facecolor('white')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("MCD_comparison.eps", format='eps', bbox_inches='tight')
plt.savefig("MCD_comparison.png", format='png', bbox_inches='tight')
plt.savefig("MCD_comparison.pdf", format='pdf', bbox_inches='tight')
plt.close()  

 

i = 0 
plt.plot(ACD['Unnamed: 0'], ACD['0'], color='red', linewidth=2,label=r'\textit{Emulator}')
plt.plot(ACD_ne['Unnamed: 0'], ACD_ne[format(20)], color="gold", linewidth=2,label=r'\textit{20 bits nearest even}') 
plt.plot(ACD_n['Unnamed: 0'], ACD_n[format(20)], color="forestgreen", linewidth=2,label=r'\textit{20 bits nearest}') 
plt.plot(ACD_t['Unnamed: 0'], ACD_t[format(20)], color="royalblue", linewidth=2,label=r'\textit{20 bits truncation}') 
plt.axhline(y = 0.05, color = 'r', linewidth=4,  linestyle = '--')   
plt.fill_between(ACD_ne['Unnamed: 0'],0.05, 1, alpha=0.2, color='r')     
plt.ylim([-0.05, 1])     
plt.xlim([10, 187112]) 
plt.xscale("log")   
plt.title(r'\textbf{Average complex distance}',fontsize=20)
plt.xlabel(r'\textbf{File lenght}', fontsize=20)
plt.ylabel(r'\textbf{Average complex distance}', fontsize=20)
leg = plt.legend(loc='upper right', frameon=True, fontsize=15)
leg.get_frame().set_facecolor('white')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("ACD_comparison.eps", format='eps', bbox_inches='tight')
plt.savefig("ACD_comparison.png", format='png', bbox_inches='tight')
plt.savefig("ACD_comparison.pdf", format='pdf', bbox_inches='tight')
plt.close()
