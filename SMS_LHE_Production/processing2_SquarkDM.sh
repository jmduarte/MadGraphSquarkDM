######### This step will do the Pythia Decays and puts the banner...Assumes that the in put is a gz file 

for i in `seq $1 $5 $2`
do
for j in `seq $3 $5 $4`

do
echo $i
echo $j
echo $k

dif=` echo "scale=1;$i-$j" |bc`

echo $dif
cent=99


###find file

if [  $dif -gt $cent  ] ;then

unset OUTDIR
OUTDIR=/mnt/hadoop/store/user/jduarte/LHE/SquarkDM/

if  [  ! -f $OUTDIR/8TeV_SquarkDM_${i}_${j}.lhe.gz  ] ; then

unset file

file=`ls /mnt/hadoop/store/user/jduarte/LHE/SquarkDM_Merged/8TeV_SquarkDM_2j_${i}_${j}_run1_*.lhe.gz | awk -F ".gz" '{print $1}'`


echo $file
unset name
name=SquarkDM_2j_${i}_${j}


##prepare pythia decay , each point one working dir which will be deleted at the end
mkdir work_${i}_${j}
cd work_${i}_${j}


cp ../pythia_decay_template pythia.py
cp $file.gz .

file=`echo  $file| awk -F "/" '{print $9}'`
gzip -d $file.gz


sed -i 's/6     1.74300000E+02/6     1.72500000E+02/g' $file
#sed -i 's/DECAY   1000024     0.10000000E+00/DECAY   1000024     1.00000000E-05/g' $file
sed -i 's/FILEIN/'$file'/g' pythia.py



FILEOUT=${file}_pythia
echo for $file and $FILEOUT

### run decays in pythia and rename fort.69 - This step assumes that you have already setup the correct CMSSE env with the patches provides by Steve - If not , first do this 


#   cvs co UserCode/Mrenna/GeneratorInterface
#   cp -r UserCode/Mrenna/GeneratorInterface/ .
#   cd GeneratorInterface/Pythia6Interface
#   scramv1 b ; cd ../..

pwd
cmsRun pythia.py
mv fort.69 $FILEOUT


#sed -i 's/QCUT/'$qcut'/'  banner
##ready to hashtag model and matching scales

cp ../hashtag_py hashtag${i}_${j}.py

##put the matching scales into file

#first stip the model hash tag

sed -i '/model SquarkDM_/d' $file
sed -i 's/first/'$file'/g' hashtag${i}_${j}.py
sed -i 's/second/'$FILEOUT'/g' hashtag${i}_${j}.py
python hashtag${i}_${j}.py
rm hashtag${i}_${j}.py


##tag model
tag_model=SquarkDM_${i}_${j}


##put model hastag into <event> block
echo  sed -e '1d'   -e 's/<\/event>/# model '${tag_model}' \n<\/event>/g' $FILEOUT > com${i}_${j} ; sed -i "s/ s/ 's/g" com${i}_${j} ; sed -i "s/g/ g'/g" com${i}_${j}
source com${i}_${j} > temp${i}_${j} ; 
cat ../banner_template_SquarkDM > ../files/8TeV_SquarkDM_${i}_${j}.lhe
cat temp${i}_${j} >> ../files/8TeV_SquarkDM_${i}_${j}.lhe
#sed -e '1d'  -e '1r banner'  ../files/8TeV_SquarkDM_${i}_${j}.lhe > temp${i}_${j}${i}_${j}  ; mv temp${i}_${j}${i}_${j}   ../files/8TeV_SquarkDM_${i}_${j}.lhe 

rm $FILEOUT
rm $FILEOUT~

gzip ../files/8TeV_SquarkDM_${i}_${j}.lhe 
mv ../files/8TeV_SquarkDM_${i}_${j}.lhe.gz $OUTDIR


#echo please check that the model is ${tag_model} and the xsec is $nlo for $i GeV mass

cd ..

ls work_${i}_${j}
rm -fr work_${i}_${j}
rm $file
fi
fi
done
done