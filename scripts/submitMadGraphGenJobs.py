
import sys # Obviously some module (does argv which is kind of important).
import os # Another module; seems to get environment info.
import ROOT as rt # Root is root duh.

def writeScript(outputName,pwd,tarBall,mDM,mM,GammaM):
    # OutputName is the name of the file with the events to generate....or not? We write what would be like command line
    # commands to it, it seems. So is it something that gets read to the command line?
    # tarBall = tared file. Presumably name not actual file.
    # pwd is where you are in the directory, it seems. A little wierd because it isn't a password?
    # mDM is the mass of the dark matter. 
    # mM is the mass of the mediator molecule (a squark in this case).
    # GammaM is the width of the mediator.
    
    user = os.environ['USER'] # This gives the current user.
    
    directory = tarBall.replace('.tar.gz','') # Puts us in the correct directory.
    # Why do we also do this in the main file; instead just get the output file name from here?
    outputFile = open(outputName,'w') # Opens the output file in write mode.
    outputFile.write('#!/bin/sh\n')
    # Shebang, says to run the script /bin/sh. Is this the reason we put command line code? Honestly don't really get this.
    outputFile.write('#$ -S /bin/sh\n') # What does this do?
    outputFile.write('#$ -V\n') # What does this do?
    outputFile.write('#$ -q all.q@compute-2-4.local,all.q@compute-3-10.local,all.q@compute-3-11.local,all.q@compute-3-12.local,all.q@compute-3-3.local,all.q@compute-3-5.local,all.q@compute-3-7.local,all.q@compute-3-8.local,all.q@compute-3-9.local\n') # What does this do?
    outputFile.write('hostname -f\n') # What does this do?
    outputFile.write('mkdir -p /wntmp/%s\n'%(user)) # So you make the directory of the current user. What is wntmp?
    outputFile.write('cd /wntmp/%s/\n'%(user)) # Then cd into it.
    outputFile.write('cp %s/%s .\n'%(pwd,tarBall)) # Sends pwd and tared file to t3.
    # Or does this just send the name and the tared file is already there?
    outputFile.write('tar -xvzf %s\n'%tarBall) # Untars the tared file.
    outputFile.write('cd %s/Cards/\n'%directory) # We cd into the Cards directory.
    outputFile.write('sed -e \'s/DARKMATTERMASS/%i/g\' -e \'s/MEDIATORMASS/%i/g\' -e \'s/MEDIATORWIDTH/%f/g\' param_card_default.dat > param_card.dat\n'%(mDM,mM,GammaM)) # Replace and shove in the masses.
    outputFile.write('cd ..\n') # Back up to the previous directory.
    outputFile.write('time ./bin/generate_events\n') # So you generate events with the time.
    outputFile.write('cp Events/run_01/unweighted_events.lhe.gz /mnt/hadoop/store/user/jduarte/LHE/%s_Undecayed/8TeV_%s_%i_%i_%f_run_01_unwt.lhe.gz\n'%(directory,directory,mDM,mM,GammaM)) # Copy the events generated into the hadoop store.
    outputFile.write('cd ..; rm -r /wntmp/%s/*'%(user)) #??? Just edits the filename or something?
    outputFile.close() # Close the output file. 
    

if __name__ == '__main__':
    tarBall = sys.argv[1] # tarBall. Argv takes in strings, so presumably the name, not the actual tarBall.
    # Name of tared version of--in this case dmdm--the file that was created by madgraph with the events and such.
    pwd = os.environ['PWD'] # This is where you are in the directory I think, but I could be wrong.

    for mDM in [100.0]: # Dark matter mass up to 100.
        for mM in [200.0]: # Mediator mass up to 200.
            GammaM = (mM / (16*rt.TMath.Pi()) ) * rt.TMath.Power(1.0 - rt.TMath.Power(mDM/mM,2.0),2.0)
            # Calculates the min width based on the masses given, as in that one paper.
            directory = tarBall.replace('.tar.gz','')
            outputName = "%s_mDM_%i_mM_%i_GammaM_%f.sge"%(directory,mDM,mM,GammaM)
            # Gets to the directory and the filename from it.
            writeScript(outputName,pwd,tarBall,mDM,mM,GammaM) # Calls write script.
            os.system('qsub %s'%outputName) # I believe this submits the job????
            # If not, how to submit a job???
    

# Questions:
#    1. What exactly does the tarBall represent?
#    2. What is all the commented command line code and the long thingy??
#    3. How to submit a job?
# Basically number 2. I'm pretty sure the tarBall is just a string name of the tared file...but if so why don't we just
# pass in the name of the file? Also, what are we actually passing where with this? No idea on two; google's giving me
# nothing. Don't really understand the shebang thing either? Is os.sy... submitting the job? BEcause from my command line
# history memory it seems to submit jobs we just did python thisfile tarfile.
