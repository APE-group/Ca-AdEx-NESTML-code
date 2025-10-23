This repository contains the nestml description of the Ca-AdEx two-compartment neuron model [1]
with a few example of usage of this model in NEST simulations.

[1] Brette R and Gerstner W (2005). Adaptive exponential
    integrate-and-fire model as an effective description of neuronal
    activity. Journal of Neurophysiology. 943637-3642
    DOI: https://doi.org/10.1152/jn.00686.2005


Instructions:
1- Install NEST 3.9 in your environment, following NEST instruction
2- Install NESTML 8.2.0 in the same environment, following NESTML instruction
    (currently, "pip install nestml")
4- Download the current repository
3- In the same enviroment including NEST and NESTML previously installed, execute:
    > python build_ca_adex.py
4- Check the correct installation of the ca_adex module in NEST:
    the file ca_adex_module.so must be present in the folder <NEST-installation-path>/lib64/nest/
5- Execute the examples contained in this repository 
