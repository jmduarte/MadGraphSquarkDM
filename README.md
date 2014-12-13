MadGraphSquarkDM
================

scripts for MadGraph5 generation of SquarkDM t-channel model

```
cmsrel CMSSW_5_3_22
cd CMSSW_5_3_22/src
cmsenv
git clone https://github.com/jmduarte/MadGraphSquarkDM
wget https://launchpad.net/mg5amcnlo/2.0/2.2.0/+download/MG5_aMC_v2.2.2.tar.gz --no-check-certificate
tar xvzf MG5_aMC_v2.2.2.tar.gz
rm MG5_aMC_v2.2.2.tar.gz
cd MG5_aMC_v2.2.2
cp -r ../models/SM_Squark_udcs_chi models
./bin/mg5 ../Cards/dmdm_proc_card.dat
cp ../Cards/dmdm_param_card.dat dmdm/Cards/param_card_default.dat
cp ../Cards/dmdm_run_card.dat dmdm/Cards/run_card.dat
tar cvzf dmdm.tar.gz dmdm
rm -r dmdm
```