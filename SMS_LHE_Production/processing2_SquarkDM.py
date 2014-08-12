import os
import sys
import ROOT as rt
import glob

if __name__ == '__main__':
    
    indir = "/mnt/hadoop/store/user/jduarte/LHE/SquarkDM_Merged"
    outdir = "/mnt/hadoop/store/user/jduarte/LHE/SquarkDM"
    
    for mDM in [1.0, 10.0, 50.0, 100.0, 150.0, 400.0, 600.0, 900.0, 1000.0]: 
       for mM in [200.0, 500.0, 700.0, 1000.0, 1500.0, 2000.0]:
            if (mM >= mDM):
                GammaMin = (mM / (16*rt.TMath.Pi()) ) * rt.TMath.Power(1.0 - rt.TMath.Power(mDM/mM,2.0),2.0)
                for gM in [GammaMin, mM/100.0, mM/3.0]:
                    if not glob.glob("%s/8TeV_SquarkDM_%i_%i_%f.lhe.gz"%(outdir,mDM,mM,gM)):
                        for fileName in glob.glob("%s/8TeV_SquarkDM_2j_%i_%i_%f_run1_*.lhe.gz"%(outdir,mDM,mM,gM)):
                            fileName = fileName.replace(".gz\n","")
                            os.system("mkdir work_%i_%i_%f"%(mDM,mM,gM))
                            os.system("cd work_%i_%i_%f"%(mDM,mM,gM))
                            
                            os.system("cp ../pythia_decay_template_SquarkDM >  pythia.py")
                            os.system("cp %s.gz ."%fileName)
                            fileName = fileName.split("/")[-1]
                            os.system("gzip -d %s.gz"%fileName)
                            os.system("sed -i 's/FILEIN/%s/g' pythia.py"%fileName)
                            os.system("sed -i 's/DARKMATTERMASS/%i/g' pythia.py"%mDM)
                            os.system("sed -i 's/# Wsdr/# Wsdr\n   1.0   2  18        1/g' %s"%fileName)
                            os.system("sed -i 's/# Wssr/# Wssr\n   1.0   2  18        3/g' %s"%fileName)

                            os.sytem("cmsRun pythia.py")
                            
                            
                            print fileName

                                                        
                            
                        
                    
