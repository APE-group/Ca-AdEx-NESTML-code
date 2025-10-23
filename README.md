This repository contains the nestml description of the Ca-AdEx two-compartment neuron model [1]
with a few example of usage of this model in NEST simulations.

[1] Pastorelli E., Yegenoglu A., Kolodziej N., Wybo W., Simula F., Diaz-Pier S.,
    Storm J.F. Paolucci P.S. (2025). Simplified two-compartment neuron with calcium dynamics
    capturing brain-state specific apical-amplification, -isolation and -drive.
    Front. Comput. Neurosci. DOI: https://doi.org/10.3389/fncom.2025.1566196


Instructions:
1) Install NEST 3.9 in your environment, following NEST instruction
2) Install NESTML 8.2.0 in the same environment, following NESTML instruction
    (currently, "pip install nestml")
3) Download the current repository
4) In the same enviroment including NEST and NESTML previously installed, execute:
    > python build_ca_adex.py
5) Check the correct installation of the ca_adex module in NEST:
    the file ca_adex_module.so must be present in the folder <NEST-installation-path>/lib64/nest/
6) Execute the examples contained in this repository 
