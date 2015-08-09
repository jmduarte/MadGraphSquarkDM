import os
import sys
import ROOT as rt
import glob

if __name__ == '__main__':

    for sample in ['T2bH']:

        indir = '/mnt/hadoop/store/user/jduarte/LHE/T2_Undecayed'%sample
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
                                os.system('mkdir -p tmp_dir')
                                os.system('cp %s tmp_dir/'%fileName)
                                fileName = fileName.split('/')[-1]
                                os.system('gzip -d tmp_dir/%s'%fileName)
                                fileName = fileName.replace('.gz','')
                                os.system('grep -c  "<event>" tmp_dir/%s >> 8TeV_%s_%i_%i.txt'%(fileName,sample,mM,mLSP))
                                os.system('grep \'Integrated weight (pb)\' tmp_dir/%s >> loXsec.txt'%(fileName))
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
                            os.system('rm 8TeV_%s_%i_%i.txt'%(sample,mM,mLSP))
                            os.system('rm loXsec.txt')
                            os.system('sed -e \'s/MSBOTTOM/%i/g\' -e \'s/MLSP/%i/g\' -e \'s/MNLSP/%i/g\' -e \'s/BRANCHINGRATIO2/%f/g\' -e \'s/BRANCHINGRATIO1/%f/g\' %s > banner.txt\n'%(mM,mLSP,mNLSP,BR,1-BR,paramcard))
                            os.system('/opt/rocks/bin/perl merge-pl tmp_dir/8TeV_%s_%i_%i_*.lhe  8TeV_%s_%i_%i_run1_%ievnt.lhe.gz  banner.txt'%(sample,mM,mLSP,sample,mM,mLSP,nEvents))
                            os.system('gzip -d 8TeV_%s_%i_%i_run1_%ievnt.lhe.gz'%(sample,mM,mLSP,nEvents))
                            tagModel = "%s_%i_%i"%(sample,mM,mLSP)
                            f = open('com','w')
                            f.write('sed  -e \'s/<\/event>/# model %s %s\\n<\/event>/g\' 8TeV_%s_%i_%i_run1_%ievnt.lhe'%(tagModel,xsec,sample,mM,mLSP,nEvents))
                            f.close()
                            os.system('source com > temp.lhe')
                            os.system('mkdir -p PostProcessed')
                            qcut = 45
                            
                            os.system('python  mgPostProcv2.py  -o temp2.lhe -j 5 -q %i -e 5 -s temp.lhe'%qcut)
                            os.system('mv temp2.lhe PostProcessed/8TeV_%s_%i_%i_run1_%ievnt.lhe'%(sample,mM,mLSP,nEvents))
                            os.system('gzip PostProcessed/8TeV_%s_%i_%i_run1_%ievnt.lhe'%(sample,mM,mLSP,nEvents))
                            os.system('mv PostProcessed/8TeV_%s_%i_%i_run1_%ievnt.lhe.gz %s/'%(sample,mM,mLSP,nEvents,outdir))
                            # clean up
                            os.system('rm *.lhe; rm tmp_dir/*.lhe')
                            
