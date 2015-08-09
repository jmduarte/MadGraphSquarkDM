import os
import sys
import ROOT as rt
import glob

def exec_me(cmd,dryRun=False):
    print cmd
    if not dryRun:
        os.system(cmd)    
    
if __name__ == '__main__':

    for sample in ['T2bH']:

        indir = '/mnt/hadoop/store/user/jduarte/LHE/T2_Undecayed'
        outdir = '/mnt/hadoop/store/user/jduarte/LHE/T2bH_Merged'
        paramcard = "T2bH.slha"
        
        for mM,mLSP in [(475,100),(600,200)]:
            mNLSP = mLSP+130
            for BR in [1.0,0.5]:
                if (mM > mNLSP):
                        if not glob.glob('%s/8TeV_%s_%i_%i_run1_%ievnt.lhe.gz'%(outdir,sample,mM,mLSP,400000)):
                            print '%s/8TeV_%s_%i_%i_run*.lhe.gz'%(indir,"T2tt_2j",mM,mLSP)
                            for fileName in glob.glob('%s/8TeV_%s_%i_%i_run*.lhe.gz'%(indir,"T2tt_2j",mM,mLSP)):
                                print 'copying %s'%fileName
                                exec_me('mkdir -p tmp_dir')
                                exec_me('cp %s tmp_dir/'%fileName)
                                fileName = fileName.split('/')[-1]
                                exec_me('gzip -d tmp_dir/%s'%fileName)
                                fileName = fileName.replace('.gz','')
                                exec_me('grep -c  "<event>" tmp_dir/%s >> 8TeV_%s_%i_%i.txt'%(fileName,sample,mM,mLSP))
                                exec_me('grep \'Integrated weight (pb)\' tmp_dir/%s >> loXsec.txt'%(fileName))
                            xsecFile = open('loXsec.txt')
                            xsecList = [xsecString.split(":")[-1] for xsecString in xsecFile.readlines()]
                            print xsecList
                            xsec = xsecList[-1].replace("\n","")
                            eventFile = open('8TeV_%s_%i_%i.txt'%(sample,mM,mLSP))
                            eventList = [int(eventString) for eventString in eventFile.readlines()]
                            print eventList
                            nEvents = sum(eventList)
                            print 'total events to merge is %i'%nEvents
                            print 'cross section is %s pb'%xsec
                            exec_me('rm 8TeV_%s_%i_%i.txt'%(sample,mM,mLSP))
                            exec_me('rm loXsec.txt')
                            exec_me('sed -e \'s/MSBOTTOM/%i/g\' -e \'s/MLSP/%i/g\' -e \'s/MNLSP/%i/g\' -e \'s/BRANCHINGRATIO2/%f/g\' -e \'s/BRANCHINGRATIO1/%f/g\' %s > banner.txt\n'%(mM,mLSP,mNLSP,BR,1-BR,paramcard))
                            exec_me('/opt/rocks/bin/perl merge-pl tmp_dir/8TeV_%s_%i_%i_*.lhe  8TeV_%s_%i_%i_run1_%ievnt.lhe.gz  banner.txt'%(sample,mM,mLSP,sample,mM,mLSP,nEvents))
                            sys.exit()
                            exec_me('gzip -d 8TeV_%s_%i_%i_run1_%ievnt.lhe.gz'%(sample,mM,mLSP,nEvents))
                            tagModel = "%s_%i_%i"%(sample,mM,mLSP)
                            f = open('com','w')
                            f.write('sed  -e \'s/<\/event>/# model %s %s\\n<\/event>/g\' 8TeV_%s_%i_%i_run1_%ievnt.lhe'%(tagModel,xsec,sample,mM,mLSP,nEvents))
                            f.close()
                            exec_me('source com > temp.lhe')
                            exec_me('mkdir -p PostProcessed')
                            qcut = 45
                            
                            exec_me('python  mgPostProcv2.py  -o temp2.lhe -j 5 -q %i -e 5 -s temp.lhe'%qcut)
                            exec_me('mv temp2.lhe PostProcessed/8TeV_%s_%i_%i_run1_%ievnt.lhe'%(sample,mM,mLSP,nEvents))
                            exec_me('gzip PostProcessed/8TeV_%s_%i_%i_run1_%ievnt.lhe'%(sample,mM,mLSP,nEvents))
                            exec_me('mv PostProcessed/8TeV_%s_%i_%i_run1_%ievnt.lhe.gz %s/'%(sample,mM,mLSP,nEvents,outdir))
                            # clean up
                            exec_me('rm *.lhe; rm tmp_dir/*.lhe')
                            
