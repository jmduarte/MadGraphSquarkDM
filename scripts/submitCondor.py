

import sys
import os 
import ROOT as rt 

def writeScript(outputName,pwd,tarBall,mDM,mM,GammaM,run_number):

    #Executable = sleep.sh 
    #Universe = vanilla 
    #Output = sleep.out.$(Process)
    #Log = sleep.log
    #Error = sleep.err
    #getenv = True

    
    user = os.environ['USER'] # This gives the current user.
    
    directory = tarBall.replace('.tar.gz','') 
    submitCards=outputName+".sub"
    submitScript=outputName+".ssh"
    outFile=outputName+".out"
    logFile=outputName+".log"
    errFile=outputName+".err"
    

    # script
    outputFile = open(submitScript,'w')
    outputFile.write('#!/bin/sh\n')
    outputFile.write('hostname -f\n') 
    outputFile.write('mkdir -p wntmp\n') # Added by me; we'll see.
    outputFile.write('mkdir -p wntmp/%s\n'%(user))
    outputFile.write('mkdir -p wntmp/%s/%s\n'%(user,outputName)) 
    outputFile.write('cd wntmp/%s/%s\n'%(user,outputName))
    outputFile.write('cp %s/%s .\n'%(pwd,tarBall)) 
    outputFile.write('tar -xvf %s\n'%tarBall) # Neends to be xvf, not xvzf
    outputFile.write('cd %s/Cards/\n'%directory)
    outputFile.write('sed -e \'s/DARKMATTERMASS/%i/g\' -e \'s/MEDIATORMASS/%i/g\' -e \'s/MEDIATORWIDTH/%i/g\' param_card_default.dat > param_card.dat\n'%(mDM,mM,GammaM)) 
    outputFile.write('cd ..\n')
    outputFile.write('time ./bin/generate_events run_%i -f\n'%(run_number))
    outputFile.write('cp Events/run_%i/unweighted_events.lhe.gz /mnt/hadoop/store/user/jduarte/LHE/%s_Undecayed/8TeV_%s_%i_%i_%i_run_%i_unwt.lhe.gz\n'%(run_number,directory,directory,mDM,mM,GammaM,run_number))
    outputFile.write('cp Events/run_%i/unweighted_events.lhe.gz /home/nsirohi/MG5/CMSSW_5_3_18/src/MG5_aMC_v2_1_1/events/%s_Undecayed/8TeV_%s_%i_%i_%f_run_%i_unwt.lhe.gz\n'%(run_number,directory,directory,mDM,mM,GammaM,run_number))
    outputFile.write('cd ../..; rm -r wntmp/%s/%s/*'%(user,outputName)) # Needed to go one more directory up. 
    outputFile.close()

    # cards
    outputFile = open(submitCards,'w')
    outputFile.write('Executable = %s\n'%submitScript)
    outputFile.write('Universe = vanilla\n')
    outputFile.write('Output = %s\n'%outFile)
    outputFile.write('Log = %s\n'%logFile)
    outputFile.write('Error = %s\n'%errFile)
    outputFile.write('getenv = True\n')
    outputFile.write('Queue')
    outputFile.close()
    

if __name__ == '__main__':
    tarBall = sys.argv[1] 
    pwd = os.environ['PWD']

#   for mDM in [900.0]:
    for mDM in [1.0, 10.0, 50.0, 100.0, 150.0, 400.0, 600.0, 900.0, 1000.0]: 
       for mM in [700.0]: 
 #     for mM in [200.0, 500.0, 700.0, 1000.0, 1500.0, 2000.0]:
            if (mM >= mDM):
                GammaMin = (mM / (16*rt.TMath.Pi()) ) * rt.TMath.Power(1.0 - rt.TMath.Power(mDM/mM,2.0),2.0)
                for gM in [GammaMin, mM/100.0, mM/3.0]:
 #              for gM in [mM/3.0]: 
   #                for run_number in [1003, 1004]:
                    for run_number in [1001, 1002, 1003, 1004]:
                        directory = tarBall.replace('.tar.gz','')
                        outputName = "%s_mDM_%i_mM_%i_GammaM_%f_RunNumber%i"%(directory,mDM,mM,gM,run_number)
                        writeScript(outputName,pwd,tarBall,mDM,mM,gM,run_number) 
#                       print '%s.sub'%outputName
                        os.system('condor_submit %s.sub'%outputName)


# Just scanned all mDM, largest mM.
# All mDm, mM 1500
# mM 1000
