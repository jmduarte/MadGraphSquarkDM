import os
import sys
import ROOT as rt
import glob

if __name__ == '__main__':
    
    indir = "/mnt/hadoop/store/user/jduarte/LHE/T2bH_Merged"
    outdir = "/mnt/hadoop/store/user/jduarte/LHE/T2bH"

    for sample in ['T2bH']:
        for mM,mLSP in [(475,100),(600,200)]:
            mNLSP = mLSP+130
            for BR in [1.0,0.5]:
                if not glob.glob("%s/8TeV_%s_%i_%i_BR%.1f.lhe.gz"%(outdir,sample,mM,mLSP,BR)):
                    for fileName in glob.glob("%s/8TeV_%s_%i_%i_BR%.1f_run1_*.lhe.gz"%(indir,sample,mM,mLSP,BR)):
                        fileName = fileName.replace(".gz","")
                        os.system("rm -r work_%i_%i_BR%.1f"%(mM,mLSP,BR))
                        os.system("cp %s.gz ."%fileName) 
                        os.system("mkdir work_%i_%i_BR%.1f"%(mM,mLSP,BR))
                        os.chdir("work_%i_%i_BR%.1f"%(mM,mLSP,BR))
                        os.system("cp ../pythia_decay_template_T2bH pythia.py")
                        os.system("cp %s.gz ."%fileName)
                        fileName = fileName.split("/")[-1]
                        pathName = "work_%i_%i_BR%.1f\/%s"%(mM,mLSP,BR,fileName)
                        os.system("gzip -d %s.gz"%fileName)
                        os.system("gzip -d ../%s.gz"%fileName)
                        os.system("sed -i 's/FILEIN/%s/g' pythia.py"%fileName)
                        #os.system("sed -i 's/DARKMATTERMASS/%i/g' pythia.py"%mDM)
                        #os.system("sed -i 's/# Wsdr/# Wsdr\\n   1.0   2  18        1/g' %s"%fileName)
                        #os.system("sed -i 's/# Wssr/# Wssr\\n   1.0   2  18        3/g' %s"%fileName)
                        os.system("cmsRun pythia.py")
                        os.system("mv fort.69 %s/8TeV_%s_%i_%i_BR%.1f.lhe.gz"%(outdir,sample,mM,mLSP,BR)
                        os.chdir("..")
                        os.system("rm -r work_%i_%i_BR%.1f"%(mDM,mM,mLSP))
                        os.system("rm %s"%fileName)
