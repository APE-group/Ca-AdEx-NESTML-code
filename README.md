This repository contains the nestml description of the Ca-AdEx two-compartment neuron model [1]
with a few example of usage of this model in NEST simulations.

[1] Pastorelli E., Yegenoglu A., Kolodziej N., Wybo W., Simula F., Diaz-Pier S.,
    Storm J.F., Paolucci P.S. (2025). Simplified two-compartment neuron with calcium dynamics
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
    the file ca_adex_module.so must be present in the folder
   >  < NEST-installation-path >/lib64/nest/
7) Execute the examples contained in this repository 

Note: The example `Ca-AdEx_Example3.py` contains the simulation of an alternative version of the `ca_adex` model, which replaces the convolution calls in the original model to second-order ODEs and corresponding `onReceive` blocks for the spike events.

FUNDINGS ACKNOWLEDGEMENT. The author(s) declare that financial support was received for the research that led to the publication of this model. This work has been co-funded by the European Next Generation EU through Italian MUR grants CUP I53C22001400006 (FAIR PE0000013 PNRR Project) and CUP B51E22000150006 (EBRAINS-Italy IR00011 PNRR Project) and by the European Union Horizon 2020 Research and Innovation program under the FET Flagship Human Brain Project (grant agreement SGA3 n. 945539). This research has also been partially funded by the Helmholtz Association through the Helmholtz Portfolio Theme Supercomputing and Modeling for the Human Brain. We acknowledge the use of computing time on the JUSUF system at Forschungszentrum Jülich, which as part of the Fenix Infrastructure has been partially funded by the European Union’s Horizon 2020 research and innovation programme through the ICEI project under grant agreement no. 800858 (resources attributed to Chiara De Luca, ICEI- hbp-2022-0015). The authors gratefully acknowledge the Gauss Centre for Supercomputing e.V. (https://www.gauss-centre.eu) for funding this project by providing computing time through the John von Neumann Institute for Computing (NIC) on the GCS Supercomputer JUWELS at Jülich Supercomputing Centre (JSC).
