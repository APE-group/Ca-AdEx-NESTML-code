#
#  Ca-AdEx: example of usage of two-compartment neuron model
#
#  First version: 22/10/2025
#  Author: Elena Pastorelli, INFN, Rome (IT)
#
#  Description: Example of usage of the Ca-AdEx neuron stimulated with spike generators
#
#  Copyright © 2025   Elena Pastorelli          <elena.pastorelli@roma1.infn.it>
#  Copyright © 2025   Pier Stanislao Paolucci   <pier.paolucci@roma1.infn.it>
#
#  SPDX-License-Identifier: GPL-3.0-only
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.


import nest
import numpy as np
import matplotlib.pyplot as plt
import random
import statistics as stat
import sys
import yaml


default_param = {'C_m_d': 23.67372778891213, 'C_m_s': 246.7882968598874, 'Ca_0': 0.0001, 'Ca_th': 0.00043, 'V_reset': -61.73952230767877, 'd_BAP': 0.1195980511869619, 'delta_T': 2.0, 'e_K': -90.0, 'e_L_d': -55.000000000000014, 'e_L_s': -69.24596493128396, 'e_Na_Adex': -50.0, 'exp_K_Ca': 4.8, 'g_C_d': 19.777320239615996, 'g_L_d': 3.377855016658499, 'g_L_s': 5.0, 'g_w': 1.1156385639067352, 'gbar_Ca': 21.045506331690845, 'gbar_K_Ca': 13.199867205029523, 'h_half': -21.0, 'h_slope': -0.5, 'm_half': -9.0, 'm_slope': 0.5, 'phi': 3.92830985228413e-08, 't_ref': 0.0, 'tau_decay_Ca': 103.57233790866408, 'tau_h': 80.0, 'tau_m': 15.0, 'tau_m_K_Ca': 1.0, 'w_BAP': 27.995561755479308}

other_params = {'V_th': -40.,
               'tau_w': 500.,
                'a': 0.,
                'b': 40.,
                }

w_BAP = 27.995561755479308
d_BAP = 0.1195980511869619

cm_params = default_param
cm_params.update(other_params)

# Following lines can be used to change specific parameters from defaul ones
cm_params.update({
    #'w_BAP': 0., 
    #'g_C_d':5.,
})

print('')
print('Updated Ca-AdEd params: ', cm_params)
print('')

SimTime = 6000
brain_state = "awake"
stimulusStart = 0.
stimulusStop = SimTime
countWindow = stimulusStop-stimulusStart

I_s = 100
I_d = 50

#Creation of actual simulation starts herefrom
nest.ResetKernel()

nest.Install('ca_adex_module')
 
cm = nest.Create("ca_adex",params=cm_params)
receptor_types = cm.get("receptor_types")
print(" ")
print("cm neuron properties: ", cm.get())
print(" ")
print("receptor types: ", receptor_types)
print(" ")

# connect soma to distal with delay to reproduce back propagation currents
nest.Connect(cm, cm, syn_spec={'synapse_model': 'static_synapse',
                               'weight': w_BAP, 'delay': d_BAP,
                               'receptor_type': receptor_types["SPIKES_AMPA_D"]})
        
sg0 = nest.Create('spike_generator', 1, {'spike_times': [500]})
sg1 = nest.Create('spike_generator', 1, {'spike_times': [1500]})
sg2 = nest.Create('spike_generator', 1, {'spike_times': [2500]})
sg3 = nest.Create('spike_generator', 1, {'spike_times': [3500]})
sg4 = nest.Create('spike_generator', 1, {'spike_times': [4500]})
nest.Connect(sg0, cm, syn_spec={
    'synapse_model': 'static_synapse', 'weight': 300, 'delay': 1., 'receptor_type': receptor_types['EXC_SPIKES_SOMA']})
nest.Connect(sg1, cm, syn_spec={
    'synapse_model': 'static_synapse', 'weight': 1500, 'delay': 1., 'receptor_type': receptor_types['EXC_SPIKES_DISTAL']})
nest.Connect(sg2, cm, syn_spec={
    'synapse_model': 'static_synapse', 'weight': 500, 'delay': 1., 'receptor_type': receptor_types['EXC_SPIKES_SOMA']})
nest.Connect(sg2, cm, syn_spec={
    'synapse_model': 'static_synapse', 'weight': 300, 'delay': 1., 'receptor_type': receptor_types['SPIKES_AMPA_D']})
nest.Connect(sg3, cm, syn_spec={
    'synapse_model': 'static_synapse', 'weight': 300, 'delay': 1., 'receptor_type': receptor_types['EXC_SPIKES_SOMA']})
nest.Connect(sg3, cm, syn_spec={
    'synapse_model': 'static_synapse', 'weight': 50, 'delay': 1., 'receptor_type': receptor_types['SPIKES_AMPA_NMDA_D']})
nest.Connect(sg4, cm, syn_spec={
    'synapse_model': 'static_synapse', 'weight': 100, 'delay': 1., 'receptor_type': receptor_types['SPIKES_AMPA_NMDA_D']})


# create multimeters to record compartment voltages and various state variables
rec_list = ['V_m_s', 'V_m_d', 'w',
            'm_Ca', 'h_Ca', 'I_Ca', 'c_Ca', 'e_Ca',
            'm_K',  'I_K']
mm_cm = nest.Create('multimeter', 1, {'record_from': rec_list, 'interval': .1})
nest.Connect(mm_cm, cm)

# create and connect a spike recorder
sr_cm = nest.Create('spike_recorder')
nest.Connect(cm, sr_cm)

nest.Simulate(SimTime)

res_cm = nest.GetStatus(mm_cm, 'events')[0]
events_cm = nest.GetStatus(sr_cm)[0]['events']

totalSpikes_cm = sum(map(lambda x: x>stimulusStart and x<stimulusStop, events_cm['times']))
print("Total spikes multiComp = ", totalSpikes_cm)
print("FR multiComp           = ", totalSpikes_cm*1000/countWindow)

print("Spike times multiComp:\n")
print(events_cm['times'])

xlimStart = 0
xlimEnd = SimTime

plt.figure('Ca-AdEx')
###############################################################################
plt.subplot(411)
plt.plot(res_cm['times'], res_cm['V_m_s'], c='b', label='v_m soma cm')
plt.plot(res_cm['times'], res_cm['V_m_d'], c='g', label='v_m dist cm')
plt.legend()
plt.xlim(xlimStart, xlimEnd)
plt.ylabel('Vm [mV]')
plt.title('MultiComp (blue) and adex (red) voltage')

plt.subplot(412)
plt.plot(res_cm['times'], res_cm['m_Ca'], c='b', ls='--', lw=2., label='m')
plt.plot(res_cm['times'], res_cm['h_Ca'], c='r', ls='--', lw=2., label='h')
plt.plot(res_cm['times'], res_cm['m_Ca']*res_cm['h_Ca'], c='k', ls='--', lw=2., label='g')
plt.legend()
plt.xlim(xlimStart, xlimEnd)
plt.ylabel('Ca')
plt.title('Distal Ca activation')

plt.subplot(413)
plt.plot(res_cm['times'], res_cm['w'], c='b', ls='--', lw=2., label='W cm')
#plt.legend()
plt.xlim(xlimStart, xlimEnd)
plt.ylabel('W')
plt.title('Adaptation')

plt.subplot(414)
plt.plot(res_cm['times'], res_cm['e_Ca'], c='b', ls='--', lw=2., label='e_Ca')
plt.ylabel('e_Ca')
plt.title('Ca reversal potential')
plt.xlim(xlimStart, xlimEnd)
plt.xlabel('Time [ms]')

plt.figure('NESTML SC DIST')
###############################################################################
plt.subplot(511)
plt.plot(res_cm['times'], res_cm['I_Ca'], c='b', label='I_Ca')
plt.legend()
plt.xlim(xlimStart, xlimEnd)

plt.subplot(512)
plt.plot(res_cm['times'], res_cm['m_Ca'], c='b', ls='--', lw=2., label='m_Ca')
plt.plot(res_cm['times'], res_cm['h_Ca'], c='r', ls='--', lw=2., label='h_Ca')
plt.plot(res_cm['times'], res_cm['m_Ca']*res_cm['h_Ca'], c='k', ls='--', lw=2., label='g_Ca')
plt.legend()
plt.xlim(xlimStart, xlimEnd)

plt.subplot(513)
plt.plot(res_cm['times'], res_cm['c_Ca'], c='b', label='[Ca]')
plt.legend()
plt.xlim(xlimStart, xlimEnd)

plt.subplot(514)
plt.plot(res_cm['times'], res_cm['I_K'], c='b', label='I_K')
plt.legend()
plt.xlim(xlimStart, xlimEnd)

plt.subplot(515)
plt.plot(res_cm['times'], res_cm['m_K'], c='b', ls='--', lw=2., label='m_K')
plt.legend()
plt.xlim(xlimStart, xlimEnd)
plt.xlabel('Time [ms]')



plt.show()
