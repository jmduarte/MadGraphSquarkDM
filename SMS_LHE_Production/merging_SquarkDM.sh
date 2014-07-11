model=$6

for i in `seq $1 $5 $2`; 

do

tops="90"

for j in `seq $3 $5 $4`; 

do
unset diff

diff=`echo "scale=2;${i} - ${j}" |bc`
unset n1stop
n1stop=`echo "scale=2;${i} - 90" |bc`
echo  model $model and $diff

if [ $diff -ge $tops  ] ; then


echo Working for SquarkDM_2j_${i}_${j}...

name=${model}_${i}_${j}
OUTDIR=/mnt/hadoop/store/user/jduarte/LHE/SquarkDM_Merged/

if [ ! -f $OUTDIR/8TeV_${name}_run1_*.lhe* ] ; then

ls /mnt/hadoop/store/user/jduarte/LHE/SquarkDM_Undecayed/8TeV_SquarkDM_2j_${i}_${j}_*.lhe*  > files.txt
#just 400k per point...
cat files.txt | head -4 > files2.txt ; mv files2.txt files.txt

if [ ! -f PostProcessd/8TeV_${name}_run1_*.lhe* ] ; then

if [ ! -d temp_dir ] 
then 
mkdir temp_dir
fi
while read line
do
cp $line temp_dir/.
echo files..
done<files.txt
gzip -d temp_dir/8TeV_SquarkDM_2j_${i}_${j}*.gz
echo Done with copying, and unzipping files...

ls temp_dir/8TeV_SquarkDM_2j_${i}_${j}*.lhe > files.txt

read -r firstline<files.txt

#perl extract_banner.pl $firstline banner.txt

echo MODEL ===== $model  , $name
grep -c "<event>" temp_dir/8TeV_${name}_run*.lhe >> 8TeV_${name}
unset events
#events=`cat 8TeV_${name}  | head -4 | awk -F ":" '{print $2}' | gawk '{ sum += $1 }; END { print sum }'`
events=`cat 8TeV_${name}  | awk -F ":" '{print $2}' | gawk '{ sum += $1 }; END { print sum }'`
rm 8TeV_${name}

echo Now will merge all events...for a total of $events
#skip this if you want to use a template banner for a specific Model

#preparing the banner

paramcard="param_card_${model}_template.dat"

echo using parameter card ${paramcard}

cp ${paramcard} banner.txt

while read line
do
unset stop
unset n1
echo $line
stop=`echo $line | awk '{print $1}'`
n1=`echo $line | awk '{print $2}'`
num=5
ch1=$(($n1+$num))
if [[ $i == $stop && $j == $n1 ]] ; then

	echo $i = stop $j= $n1 
	echo chargino = $ch1
	
	sed -i 's/LSP/'$n1'/g'  banner.txt
	sed -i 's/GLUINO/'$stop'/g'  banner.txt
	sed -i 's/CHARGINO/'$ch1'/g'  banner.txt
fi
done<Widths_incl


echo perl merge-pl temp_dir/8TeV_SquarkDM_2j_${i}_${j}_*.lhe  8TeV_${name}_run1_${events}evnt.lhe.gz  banner.txt
perl merge-pl temp_dir/8TeV_SquarkDM_2j_${i}_${j}_*.lhe  8TeV_${name}_run1_${events}evnt.lhe.gz  banner.txt

cat 8TeV_GoGo_new |  awk 'BEGIN{FS=" '$i' GeV"}//{print $2}' |  awk 'BEGIN{FS="+-"}//{print $1}' > xsec
#sed -i '/^$/d' xsec
unset nlo
nlo=`cat xsec`
rm xsec
#echo $nlo


#events="400000"
unset file
file=8TeV_${name}_run1_${events}evnt.lhe
gzip -d $file.gz


#slha_line=`awk '/<slha>/{print NR }' 8TeV_${name}_run1_${events}evnt.lhe`
#sed -e '/<slha>/,/<\/slha>/d' 8TeV_${name}_run1_${events}evnt.lhe > temp_lhe
#sed -i ''$slha_line'r param_card_${i}_${j}.dat' temp_lhe
tag_model=SquarkDM_${i}_${j}
echo please check that the model is $model , $name  and the xsec is $nlo for $i GeV mass
#sed  -e 's/<\/event>/# model '${tag_model}'  '${nlo}' \n<\/event>/g' $file > temp 

echo sed  -e 's/<\/event>/# model '${tag_model}' '${nlo}'\n<\/event>/g' $file  > com ; sed -i "s/ s/ 's/g" com ; sed -i "s/g/ g'/g" com
source com > temp.lhe

mkdir -p PostProcessed

if [ $i -lt 550 ]
then
	qcut=44
fi

if [ $i -gt 550 ]
then
	qcut=46
fi
python  mgPostProcv2.py  -o temp2.lhe -j 5 -q $qcut -e 5 -s temp.lhe
mv temp2.lhe PostProcessed/8TeV_${name}_run1_${events}evnt.lhe
gzip PostProcessed/8TeV_${name}_run1_${events}evnt.lhe
mv PostProcessed/8TeV_${name}_run1_${events}evnt.lhe.gz $OUTDIR/

rm *.lhe
rm *.lhe.gz
rm temp_dir/*

#slha_line=`awk '/<slha>/{print NR }' 8TeV_${name}_run1_${events}evnt.lhe`
#sed -e '/<slha>/,/<\/slha>/d' 8TeV_${name}_run1_${events}evnt.lhe > temp_lhe
#sed -i ''$slha_line'r param_card_${i}_${j}.dat' temp_lhe

fi
fi
fi
done
done
