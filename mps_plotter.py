import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
mpl.rc('text', usetex=True)
mpl.rcParams['xtick.direction'] = 'in'
mpl.rcParams['ytick.direction'] = 'in'
##############################################################################################################################################
data0=np.loadtxt('/home/anirban/Documents/CAMB/CAMB-0.1.6.1_original/output/test__matterpower.dat')
'''
#fig1 z=10000, f=0.9, trials
data1=np.loadtxt('output/myresults/_matterpower_zstar10k_w100.dat')
#data2=np.loadtxt('output/myresults/_matterpower_zstar10k_w30.dat')
#data3=np.loadtxt('output/myresults/_matterpower_zstar10k_w10.dat')
#data4=np.loadtxt('output/myresults/_matterpower_zstar10k_w3.dat')
#data5=np.loadtxt('output/myresults/_matterpower_zstar10k_w1.dat')
klist=10.**np.array([-.4,0.4,0.2])

fig = plt.figure(figsize=(12,11))
ax = fig.add_subplot(1, 1, 1)
ax.loglog(data0[::,0],data0[::,1], '--', label=r'$\Lambda$CDM', color='black',linewidth=2)
ax.loglog(data1[::,0],data1[::,1], '-',label=r'$\Delta_*=a_*/100$', color='red',linewidth=1)
#ax.loglog(data2[::,0],data2[::,1], '-',label=r'$\Delta_*=a_*/30$', color='blue',linewidth=1)
#ax.loglog(data3[::,0],data3[::,1], '-',label=r'$\Delta_*=a_*/10$', color='green',linewidth=1)
#ax.loglog(data4[::,0],data4[::,1], '-',label=r'$\Delta_*=a_*/3$', color='purple',linewidth=1)
#ax.loglog(data5[::,0],data5[::,1], '-',label=r'$\Delta_*=a_*/1$', color='orange',linewidth=1)

ax.loglog(klist, 3.e2*klist**(-1), '-.', color='gray')
plt.xlabel(r'Comoving wavenumber $k\ [h/{\rm Mpc}]$',fontsize=34)
plt.ylabel(r'Power spectrum $P(k)\ [({\rm Mpc}/h)^3]$',fontsize=34,labelpad=-2)
plt.xlim([3.e-3,3.])
plt.ylim([1.e-2, 1.e5])
#labels=[r'$\Lambda$CDM',r'This work, $\Delta=70$']
#leg = plt.legend(loc='best',fontsize=31)
#leg.get_frame().set_edgecolor('black')

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[::-1], labels[::-1], loc='best',fontsize=31).get_frame().set_edgecolor('black')
#plt.legend.get_frame().set_edgecolor('black')
ax.tick_params(axis='both', which='major', labelsize=34, pad=6)
#plt.text(1.e-2, 5.5e5, r'Phase transition at $z_*=10^4$', bbox=dict(boxstyle='round',facecolor='wheat', alpha=0.5), fontsize=31,verticalalignment='top',horizontalalignment='left')
plt.text(8.e-1, 6.e2, r'$\sim 1/k$',fontsize=27)
plt.show()
'''
'''
#fig1 z=10000, two panel version
data1=np.loadtxt('output/myresults/_matterpower_zstar10k_w100_f0.9.dat')
data2=np.loadtxt('output/myresults/_matterpower_zstar10k_w10_f0.9.dat')
data3=np.loadtxt('output/myresults/_matterpower_zstar10k_w1.2_f0.9.dat')
klist=10.**np.array([-.45,0.35,0.2])
astar=1./(1.+10000.)
n=1.2
dz100= abs((1./(astar+(astar/100.)/2.)) - (1./(astar-(astar/100.)/2.)))/10000.
dz10= abs((1./(astar+(astar/10.)/2.)) - (1./(astar-(astar/10.)/2.)))/10000.
dz2= abs((1./(astar+(astar/n)/2.)) - (1./(astar-(astar/n)/2.)))/10000.

fig = plt.figure(figsize=(12.6,12.6))
ax = fig.subplots(2, 1, sharex=True, sharey=True)
#fig, ax = plt.subplots(2,1,sharex=True)
fig.subplots_adjust(hspace=0)
#ax = fig.add_subplot(1, 1, 1)
ax[0].axvspan(0.017421/0.67, 0.041442/0.67, alpha=0.3, color=(0.75,0.75,0.5)) # \Delta z/z_*\approx 10^0
ax[0].axvspan(0.023439/0.67, 0.025865/0.67, alpha=0.5, color=(0.4,0.8,0.95)) # \Delta z/z_*\approx 10^{-1}
ax[0].axvspan(0.024475/0.67, 0.024595/0.67, alpha=0.7, color='coral') # \Delta z/z_*\approx 10^{-2}
ax[0].loglog(data0[::,0],data0[::,1], '--', label=r'$\Lambda$CDM', color='black',linewidth=2,dashes=(2,2))
ax[0].loglog(data3[::,0],data3[::,1], '--',label=r'dDM, $\Delta z/z_*\approx 10^0$', color=(0.6,0.6,0.4),linewidth=2,dashes=(5,1.3))
ax[0].loglog(data2[::,0],data2[::,1], '-.',label=r'dDM, $\Delta z/z_*\approx 10^{-1}$', color=(0.1,0.6,0.9),linewidth=2)
ax[0].loglog(data1[::,0],data1[::,1], '-',label=r'dDM, $\Delta z/z_*\approx 10^{-2}$', color='red',linewidth=2)
ax[0].loglog(klist,4.e2*klist**(-1), ':', color='gray',linewidth=1.8)
ax[0].text(8.e-1, 7.e2, r'$\sim 1/k$',fontsize=27,rotation=-12)
ax[0].text(6.e-3, 7.5e4, r'$f_{\rm dDM}=0.9$',fontsize=31)
ax[0].set_ylim([3.e-1, 3.e5])
handles, labels = ax[0].get_legend_handles_labels()
ax[0].legend(handles[::-1], labels[::-1], loc='best',fontsize=28).get_frame().set_edgecolor('black')
ax[0].tick_params(axis='y', which='major', labelsize=33, pad=12)
ax[0].tick_params(axis='x', which='major', labelsize=33, pad=18)

data1=np.loadtxt('output/myresults/_matterpower_zstar60k_w100_f0.9.dat')
data2=np.loadtxt('output/myresults/_matterpower_zstar20k_w100_f0.9.dat')
data3=np.loadtxt('output/myresults/_matterpower_zstar5k_w100_f0.9.dat')
ax[1].axvline(x=0.13264/0.67, linestyle='-.', linewidth=2, color='purple') # z_*=60000
ax[1].axvline(x=0.04627/0.67, linestyle='--', linewidth=2, color='chocolate') # z_*=20000
ax[1].axvline(x=0.01364/0.67, linewidth=2, color='teal') # z_*=5000
ax[1].loglog(data0[::,0],data0[::,1], '--', label=r'$\Lambda$CDM', color='black',linewidth=2,dashes=(2,2))
ax[1].loglog(data3[::,0],data3[::,1],label=r'$z_*=5\times 10^3$', color='teal',linewidth=2)
ax[1].loglog(data2[::,0],data2[::,1], '--',label=r'$z_*=2\times 10^4$', color='chocolate',linewidth=2)
ax[1].loglog(data1[::,0],data1[::,1], '-.',label=r'$z_*=6\times 10^4$', color='purple',linewidth=2.4)
handles, labels = ax[1].get_legend_handles_labels()
ax[1].legend(handles[::-1], labels[::-1], loc='best',fontsize=28,framealpha=0.85).get_frame().set_edgecolor('black')
#ax[1].set_ylim([1.e0, 3.e5])
ax[1].tick_params(axis='y', which='major', labelsize=33, pad=12)
ax[1].tick_params(axis='x', which='major', labelsize=33, pad=18)

plt.xlim([5.3e-3,3.])
plt.xlabel(r'Comoving wavenumber $k\ [h/{\rm Mpc}]$',fontsize=34,labelpad=12)
plt.text(2.e-3,3.e5,r'Power spectrum $P(k)\ [({\rm Mpc}/h)^3]$',fontsize=34,va='center',rotation='vertical')
#ax.set_ylabel(r'Power spectrum $P(k)\ [({\rm Mpc}/h)^3]$',fontsize=34,labelpad=6)
plt.savefig('/home/anirban/Dropbox/CAMB-0.1.6.1_drdm_added/drafts/short_draft/v2/mps10k_v3.pdf',bbox_inches='tight',pad_inches=0.1)
#plt.show()
'''
'''
#fig1 z=10000, full version
data1=np.loadtxt('output/myresults/_matterpower_zstar10k_w100.dat')
data2=np.loadtxt('output/myresults/_matterpower_zstar10k_w10.dat')
data3=np.loadtxt('output/myresults/_matterpower_zstar10k_w1.2.dat')
klist=10.**np.array([-.45,0.35,0.2])
astar=1./(1.+10000.)
n=1.2
dz100= abs((1./(astar+(astar/100.)/2.)) - (1./(astar-(astar/100.)/2.)))/10000.
dz10= abs((1./(astar+(astar/10.)/2.)) - (1./(astar-(astar/10.)/2.)))/10000.
dz2= abs((1./(astar+(astar/n)/2.)) - (1./(astar-(astar/n)/2.)))/10000.

fig = plt.figure(figsize=(12.6,12.6))
ax = fig.add_subplot(1, 1, 1)
ax.axvspan(0.017475/0.67*np.sqrt(3.)*np.pi, 0.048533/0.67*np.sqrt(3.)*np.pi, alpha=0.3, color=(0.75,0.75,0.5))
ax.axvspan(0.023911/0.67*np.sqrt(3.)*np.pi, 0.026221/0.67*np.sqrt(3.)*np.pi, alpha=0.3, color=(0.4,0.8,0.95))
ax.axvspan(0.024869/0.67*np.sqrt(3.)*np.pi, 0.025099/0.67*np.sqrt(3.)*np.pi, alpha=0.3, color='coral')
ax.loglog(data0[::,0],data0[::,1], '--', label=r'$\Lambda$CDM', color='black',linewidth=2,dashes=(2,2))
ax.loglog(data3[::,0],data3[::,1], '--',label=r'dDM, $\Delta z/z_*\approx 10^0$', color=(0.6,0.6,0.4),linewidth=2,dashes=(5,1.3))
ax.loglog(data2[::,0],data2[::,1], '-.',label=r'dDM, $\Delta z/z_*\approx 10^{-1}$', color=(0.1,0.6,0.9),linewidth=2)
ax.loglog(data1[::,0],data1[::,1], '-',label=r'dDM, $\Delta z/z_*\approx 10^{-2}$', color='red',linewidth=2)
ax.loglog(klist,4.e2*klist**(-1), ':', color='gray',linewidth=1.8)
plt.xlabel(r'Comoving wavenumber $k\ [h/{\rm Mpc}]$',fontsize=34,labelpad=12)
plt.ylabel(r'Power spectrum $P(k)\ [({\rm Mpc}/h)^3]$',fontsize=34,labelpad=-2)
plt.xlim([3.e-4,3.])
plt.ylim([1.e-2, 1.e5])
#labels=[r'$\Lambda$CDM',r'This work, $\Delta=70$']
#leg = plt.legend(loc='best',fontsize=31)
#leg.get_frame().set_edgecolor('black')
#plt.text(1.e-4,2.e6, r'Delayed DM (dDM) with phase transition at $z_*=10^4$', fontsize=31)
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[::-1], labels[::-1], loc='best',fontsize=31).get_frame().set_edgecolor('black')
#plt.legend.get_frame().set_edgecolor('black')
plt.tick_params(axis='y', which='major', labelsize=33, pad=12)
plt.tick_params(axis='x', which='major', labelsize=33, pad=18)
plt.text(3.8e-4, 3.e4, r'$f_{\rm dDM}=0.9$',fontsize=31)
#plt.text(1.e-2, 5.5e5, r'Phase transition at $z_*=10^4$', bbox=dict(boxstyle='round',facecolor='wheat', alpha=0.5), fontsize=31,verticalalignment='top',horizontalalignment='left')
plt.text(8.e-1, 6.e2, r'$\sim 1/k$',fontsize=27,rotation=-28)
plt.savefig('/home/anirban/Dropbox/CAMB-0.1.6.1_drdm_added/drafts/short_draft/v2/mps10k_v2.pdf')
#plt.show()
'''
'''
#odd-even plot with inset
data1=np.loadtxt('output/myresults/_matterpower_zstar40k_f0.4.dat')

fig = plt.figure(figsize=(12.2,12.2))
ax = fig.add_subplot(1, 1, 1)
ax.loglog(data1[::,0],data1[::,1], '-',color='red',linewidth=2.7)
#plt.axis([])
plt.xlabel(r'Comoving wavenumber $k\ [h/{\rm Mpc}]$',fontsize=34)
plt.ylabel(r'Power spectrum $P(k)\ [({\rm Mpc}/h)^3]$',fontsize=34,labelpad=5)
plt.xlim([3.e-4,5.])
plt.ylim([3.e-4, 1.e5])
#leg = plt.legend(loc='best',fontsize=31)
#leg.get_frame().set_edgecolor('black')
plt.tick_params(axis='y', which='major', labelsize=33, pad=12)
plt.tick_params(axis='x', which='major', labelsize=33, pad=18)
plt.text(3.8e-4, 3.e4, r'$f_{\rm dDM}=0.4$',fontsize=31)

a = plt.axes([.22, .2, .33, .33])
datap1=np.loadtxt('evolve_perturb_peak1.txt')
datap2=np.loadtxt('evolve_perturb_peak2.txt')
datap3=np.loadtxt('evolve_perturb_peak3.txt')
#datap4=np.loadtxt('evolve_perturb_peak4.txt')
plt.loglog(datap1[::,3], abs(datap1[::,-3]), label=r'$n=0$',color='indigo')
plt.loglog(datap2[::,3], abs(datap2[::,-3]),'-.', label=r'$n=1$',color='blue')
plt.loglog(datap3[::,3], abs(datap3[::,-3]), label=r'$n=2$',color='crimson')
#plt.loglog(datap4[::,3], abs(datap4[::,-3]),'-.', label=r'$n=3$',color='coral')
plt.text(3.e1,2.3e2,r'$n=0$',fontsize=24,rotation=30)
plt.text(3.e1,3.e3,r'$n=2$',fontsize=24,rotation=36)
plt.text(6.5e1,3.e4,r'$n=1$',fontsize=24,rotation=39)
plt.xlabel(r'Redshift $z$',fontsize=26)
plt.ylabel(r'$\delta_d$',fontsize=26,rotation=0,labelpad=12)
plt.xlim([1.e7,1.e-1])
plt.ylim([5.e-2,1.e5])
plt.tick_params(axis='both', which='major', labelsize=25, pad=8)
plt.savefig('/home/anirban/Dropbox/CAMB-0.1.6.1_drdm_added/drafts/short_draft/v2/odd_even_mps_inset.pdf',bbox_inches='tight',pad_inches=0.1)
#plt.show()
'''

'''
#fig1 z=20000
data1=np.loadtxt('output/myresults/_matterpower_other_z20000_w70.dat')
data2=np.loadtxt('output/myresults/_matterpower_other_z20000_w3.dat')
klist=10.**np.array([-0.05,0.7,0.2])

fig = plt.figure(figsize=(12,11))
ax = fig.add_subplot(1, 1, 1)
ax.loglog(data0[::,0],data0[::,1], '--', label=r'$\Lambda$CDM', color='black',linewidth=2)
ax.loglog(data2[::,0],data2[::,1], '-',label=r'dIDM, Slow transition', color=(0.1,0.6,0.9),linewidth=2)
ax.loglog(data1[::,0],data1[::,1], '-',label=r'dIDM, Fast transition', color='red',linewidth=3)
ax.loglog(klist,3.e2*klist**(-1), '-.', color='gray')
plt.xlabel(r'Comoving wavenumber $k\ [h/{\rm Mpc}]$',fontsize=34)
plt.ylabel(r'Power spectrum $P(k)\ [({\rm Mpc}/h)^3]$',fontsize=34,labelpad=-2)
plt.xlim([1.e-4,11.])
plt.ylim([1.e-3, 1.e5])
#labels=[r'$\Lambda$CDM',r'This work, $\Delta=70$']
#leg = plt.legend(loc='best',fontsize=31)
#leg.get_frame().set_edgecolor('black')

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[::-1], labels[::-1], loc='best',fontsize=31).get_frame().set_edgecolor('black')
#plt.legend.get_frame().set_edgecolor('black')
ax.tick_params(axis='both', which='major', labelsize=34, pad=6)
plt.text(8.e-1, 5.e4, r'$z_*=20000$', bbox=dict(boxstyle='round',facecolor='wheat', alpha=0.5), fontsize=31,verticalalignment='top',horizontalalignment='left')
plt.text(3.e0 , 2.e2, r'$\sim 1/k$',fontsize=27)
plt.show()
'''
'''
#fig4
data1=np.loadtxt('output/myresults/_matterpower_other_f0.5.dat')
plt.loglog(data1[::,0],data1[::,1], '-',color='red',linewidth=3)

plt.xlabel(r'Comoving wavenumber $k\ [h/{\rm Mpc}]$',fontsize=34)
plt.ylabel(r'Power spectrum $P(k)\ [({\rm Mpc}/h)^3]$',fontsize=34,labelpad=-2)
plt.xlim([3.e-4,11.])
plt.ylim([1.e-3, 1.e5])
#leg = plt.legend(loc='best',fontsize=31)
#leg.get_frame().set_edgecolor('black')
plt.tick_params(axis='both', which='major', labelsize=34, pad=6)
plt.text(5.e-4, 8.e-3, r'$f_{dDM}=0.4$', bbox=dict(boxstyle='round',facecolor='wheat', alpha=0.5), fontsize=31,verticalalignment='top',horizontalalignment='left')
plt.show()
'''

'''
#odd-even plot alternative
data1=np.loadtxt('output/myresults/_matterpower_other_f0.5.dat')
datap1=np.loadtxt('evolve_perturb_peak1.txt')
datap2=np.loadtxt('evolve_perturb_peak2.txt')
datap3=np.loadtxt('evolve_perturb_peak3.txt')
datap4=np.loadtxt('evolve_perturb_peak4.txt')

plt.subplot(2,1,1)
plt.loglog(data1[::,0],data1[::,1], '-',color='red',linewidth=3)
plt.xlim([3.e-4,11.])
plt.ylim([1.e-3, 1.e5])
plt.xlabel(r'$k\ [h/{\rm Mpc}]$',fontsize=34)
plt.ylabel(r'$P(k)\ [({\rm Mpc}/h)^3]$',fontsize=34,labelpad=-2)
#leg = plt.legend(loc='best',fontsize=31)
#leg.get_frame().set_edgecolor('black')
plt.tick_params(axis='both', which='major', labelsize=34, pad=6)
plt.text(5.e-4, 4.e-2, r'$f_{\rm dDM}=0.4$', bbox=dict(boxstyle='round',facecolor='wheat', alpha=0.5), fontsize=31,verticalalignment='top',horizontalalignment='left')

plt.subplot(2,1,2)
plt.loglog(datap1[::,3], abs(datap1[::,-3]), label=r'$n=0$',color='indigo')
plt.loglog(datap2[::,3], abs(datap2[::,-3]),'-.', label=r'$n=1$',color='blue')
plt.loglog(datap3[::,3], abs(datap3[::,-3]), label=r'$n=2$',color='crimson')
plt.loglog(datap4[::,3], abs(datap4[::,-3]),'-.', label=r'$n=3$',color='coral')
plt.xlabel(r'$z$',fontsize=34)
plt.ylabel(r'$\delta_d$',fontsize=34,rotation=90,labelpad=-4)
plt.xlim([1.e7,1.e-1])
plt.ylim([1.e-2,1.e7])
#plt.legend(loc='best',fontsize=34)
leg = plt.legend(loc='upper left',fontsize=25)
leg.get_frame().set_edgecolor('black')
plt.text(1.e1, 4.e-1, r'$f_{\rm dDM}=0.4$', bbox=dict(boxstyle='round',facecolor='wheat', alpha=0.5), fontsize=31,verticalalignment='top',horizontalalignment='left')
#plt.text(5.e6,1.e2,r'$f=0.9,\ z_*=40000$',fontsize=31)
#plt.text(5.e6,3.e1,r'$w_*=60$',fontsize=31)
plt.tick_params(axis='both', which='major', labelsize=34, pad=8)
plt.subplots_adjust(hspace = 0.4)
plt.show()
'''
#trials
data1=np.loadtxt('output/myresults/_matterpower_other.dat')
data2=np.loadtxt('output/myresults/_matterpower.dat')

plt.loglog(data1[::,0],data1[::,1], '-',color='red',linewidth=1)
plt.loglog(data2[::,0],data2[::,1], '-',color='black',linewidth=1)
#plt.xlim([3.e-4,11.])
plt.show()
