import os
import sys
import ROOT as rt
import glob

if __name__ == '__main__':

    for sample in ["squarkdm"]:
        
        indir = "/mnt/hadoop/store/user/jduarte/LHE/%s_Undecayed"%sample
        outdir = "/mnt/hadoop/store/user/jduarte/LHE/%s_Merged"%sample
        
        for mDM in [1.0, 10.0, 50.0, 100.0, 150.0, 400.0, 600.0, 900.0, 1000.0]: 
            for mM in [200.0, 500.0, 700.0, 1000.0, 1500.0, 2000.0]:
                if (mM >= mDM):
                    GammaMin = (mM / (16*rt.TMath.Pi()) ) * rt.TMath.Power(1.0 - rt.TMath.Power(mDM/mM,2.0),2.0)
                    for gM in [GammaMin, mM/100.0, mM/3.0]:
                        if not glob.glob("%s/8TeV_%s_%i_%i_%f.lhe.gz"%(outdir,sample,mDM,mM,gM)):
                            for fileName in glob.glob("%s/8TeV_%s_2j_%i_%i_%f_run*.lhe.gz"%(outdir,sample,mDM,mM,gM)):
                                fileName = fileName.replace(".gz\n","")
                                print fileName
        
