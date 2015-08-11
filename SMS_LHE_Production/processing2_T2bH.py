import os
import sys
import ROOT as rt
import glob

def exec_me(cmd,dryRun=False):
    print cmd
    if not dryRun:
        os.system(cmd)
        
if __name__ == '__main__':
    
    indir = "/mnt/hadoop/store/user/jduarte/LHE/T2bH_Merged"
    outdir = "/mnt/hadoop/store/user/jduarte/LHE/T2bH"
    paramcard = "T2bH.slha"

    for sample in ['T2bH']:
        for mM,mLSP in [(475,100),(600,200)]:
            mNLSP = mLSP+130
            for BR in [1.0,0.5]:
                if not glob.glob("%s/8TeV_%s_%i_%i_BR%.1f.lhe.gz"%(outdir,sample,mM,mLSP,BR)):
                    for fileName in glob.glob("%s/8TeV_%s_%i_%i_BR%.1f_run1_*.lhe.gz"%(indir,sample,mM,mLSP,BR)):
                        fileName = fileName.replace(".gz","")
                        exec_me("rm -r work_%i_%i_BR%.1f"%(mM,mLSP,BR))
                        exec_me("cp %s.gz ."%fileName) 
                        exec_me("mkdir work_%i_%i_BR%.1f"%(mM,mLSP,BR))
                        os.chdir("work_%i_%i_BR%.1f"%(mM,mLSP,BR))
                        exec_me("cp ../pythia_decay_template_T2bH pythia.py")
                        exec_me("cp %s.gz ."%fileName)
                        fileName = fileName.split("/")[-1]
                        pathName = "work_%i_%i_BR%.1f\/%s"%(mM,mLSP,BR,fileName)
                        exec_me("gzip -d %s.gz"%fileName)
                        exec_me("gzip -d ../%s.gz"%fileName)                        
                        exec_me('sed -e \'s/MSBOTTOM/%i/g\' -e \'s/MLSP/%i/g\' -e \'s/MNLSP/%i/g\' -e \'s/BRANCHINGRATIO2/%f/g\' -e \'s/BRANCHINGRATIO1/%f/g\' ../%s > ../%s_%i_%i_BR%.1f.slha\n'%(mM,mLSP,mNLSP,BR,1-BR,paramcard,sample,mM,mLSP,BR))
                        exec_me("sed -i 's/FILEIN/%s/g' pythia.py"%fileName)
                        exec_me("sed -i 's/SLHAIN/%s_%i_%i_BR%.1f.slha/g' pythia.py"%(sample,mM,mLSP,BR))
                        #exec_me("sed -i 's/DARKMATTERMASS/%i/g' pythia.py"%mDM)
                        #exec_me("sed -i 's/# Wsdr/# Wsdr\\n   1.0   2  18        1/g' %s"%fileName)
                        #exec_me("sed -i 's/# Wssr/# Wssr\\n   1.0   2  18        3/g' %s"%fileName)
                        exec_me("cmsRun pythia.py")
                        exec_me("mv fort.69 8TeV_%s_%i_%i_BR%.1f.lhe"%(sample,mM,mLSP,BR))
                        exec_me("gzip 8TeV_%s_%i_%i_BR%.1f.lhe"%(sample,mM,mLSP,BR))
                        exec_me("mv 8TeV_%s_%i_%i_BR%.1f.lhe.gz %s"%(sample,mM,mLSP,BR,outdir))
                        os.chdir("..")
                        #exec_me("rm -r work_%i_%i_BR%.1f"%(mM,mLSP,BR))
                        #exec_me("rm %s"%fileName)
