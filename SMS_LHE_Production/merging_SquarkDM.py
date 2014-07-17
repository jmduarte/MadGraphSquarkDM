import os
import sys
import ROOT as rt
import glob

if __name__ == '__main__':

    for sample in ['squarkdm']:
        
        indir = '/mnt/hadoop/store/user/jduarte/LHE/%s_Undecayed'%sample
        outdir = '/mnt/hadoop/store/user/jduarte/LHE/%s_Merged'%sample
        paramcard = "../Cards/dmdm_param_card.dat"
        
        #for mDM in [1.0, 10.0, 50.0, 100.0, 150.0, 400.0, 600.0, 900.0, 1000.0]:
        for mDM in [1000.0]: 
            #for mM in [200.0, 500.0, 700.0, 1000.0, 1500.0, 2000.0]:
            for mM in [2000.0]:
                if (mM > mDM):
                    GammaMin = (mM / (16*rt.TMath.Pi()) ) * rt.TMath.Power(1.0 - rt.TMath.Power(mDM/mM,2.0),2.0)
                    #for gM in [GammaMin, mM/100.0, mM/3.0]:
                    for gM in [GammaMin]:
                        if not glob.glob('%s/8TeV_%s_%i_%i_%i.lhe.gz'%(outdir,sample,mDM,mM,gM)):
                            for fileName in glob.glob('%s/8TeV_%s_%i_%i_%i_run*.lhe.gz'%(indir,sample,mDM,mM,gM)):
                                print 'copying %s'%fileName
                                os.system('mkdir -p tmp_dir')
                                os.system('cp %s tmp_dir/'%fileName)
                                fileName = fileName.split('/')[-1]
                                os.system('gzip -d tmp_dir/%s'%fileName)
                                fileName = fileName.replace('.gz','')
                                os.system('grep -c  "<event>" tmp_dir/%s >> 8TeV_%s_%i_%i_%i.txt'%(fileName,sample,mDM,mM,gM))
                                os.system('grep \'Integrated weight (pb)\' tmp_dir/%s >> loXsec.txt'%(fileName))
                            xsecFile = open('loXsec.txt')
                            xsecList = [xsecString.split(":")[-1] for xsecString in xsecFile.readlines()]
                            print xsecList
                            xsec = xsecList[-1].replace("\n","")
                            eventFile = open('8TeV_%s_%i_%i_%i.txt'%(sample,mDM,mM,gM))
                            eventList = [int(eventString) for eventString in eventFile.readlines()]
                            print eventList
                            nEvents = sum(eventList)
                            print 'total events to merge is %i'%nEvents
                            print 'cross section is %s pb'%xsec
                            os.system('rm 8TeV_%s_%i_%i_%i.txt'%(sample,mDM,mM,gM))
                            os.system('rm loXsec.txt')
                            os.system('sed -e \'s/DARKMATTERMASS/%i/g\' -e \'s/MEDIATORMASS/%i/g\' -e \'s/MEDIATORWIDTH/%i/g\' %s > banner.txt\n'%(mDM,mM,gM,paramcard))
                            os.system('/opt/rocks/bin/perl merge-pl tmp_dir/8TeV_%s_%i_%i_%i_*.lhe  8TeV_%s_%i_%i_%i_run1_%ievnt.lhe.gz  banner.txt'%(sample,mDM,mM,gM,sample,mDM,mM,gM,nEvents))
                            os.system('gzip -d 8TeV_%s_%i_%i_%i_run1_%ievnt.lhe.gz'%(sample,mDM,mM,gM,nEvents))
                            tagModel = "%s_%i_%i_%f"%(sample,mDM,mM,gM)
                            f = open(com,'w')
                            f.write('sed  -e \'s/<\/event>/# model %s %s\\n<\/event>/g\' 8TeV_%s_%i_%i_%i_run1_%ievnt.lhe  > com'%(tagModel,xsec,sample,mDM,mM,gM,nEvents))
                            f.close()
                            os.system('source com > temp.lhe')
                            os.system('mkdir -p PostProcessed')
                            qcut = 45
                            
                            os.system('python  mgPostProcv2.py  -o temp2.lhe -j 5 -q %i -e 5 -s temp.lhe'%qcut)
                            os.system('mv temp2.lhe PostProcessed/8TeV_%s_%i_%i_%i_run1_%ievnt.lhe'%(sample,mDM,mM,gM,nEvents))
                            os.system('gzip PostProcessed/8TeV_%s_%i_%i_%i_run1_%ievnt.lhe'%(sample,mDM,mM,gM,nEvents))
                            os.system('mv PostProcessed/8TeV_%s_%i_%i_%i_run1_%ievnt.lhe.gz %s/'%(sample,mDM,mM,gM,nEvents,outdir))
                            # clean up
                            os.system('rm *.lhe; rm tmp_dir/*.lhe')
                            
