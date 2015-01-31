#!/bin/bash

#change tarName to match the name of the .tar file where the new reco code is sitting
tarName=forSLHC23_Jan_15

#change relName to match the CMSSW release which should be used in reconstruction
relName=CMSSW_6_2_0_SLHC23

#increase max such that all of the xrootd file names pasted into "step3...TEMP.py"
#are uncommented when this for loop is executed
for i in {0..1}
do
	#adjust the constant added to 'i' such that 'i+32' corresponds to the line of the 
	#first file name in the step3 python file
	line=$((i+32))

	#create one condor job submission file, one run .csh script, and one step3 python file
	#for each file that needs to be re-reco'd over xrootd 
	eval "sed 's/NUM/$i/g' reReco_TEMP > reReco_temp "
	eval "sed 's/newRecoCode_with_date/$tarName/g' reReco_temp > reReco_$i"
	
	eval "sed 's/NUM/$i/g' run_reReco_TEMP.csh > run_reReco_temp.csh"
	eval "sed 's/newRecoCode_with_date/$tarName/g' run_reReco_temp.csh > run_reReco_updatedTar.csh"
	eval "sed 's/cmsswRelease/$relName/g' run_reReco_updatedTar.csh > run_reReco_$i.csh"
	
	eval "sed 's/NUM/$i/g' step3_TEMP_RAW2DIGI_L1Reco_RECO.py > step3_RAW2DIGI_L1Reco_RECO_intermediate.py"
	eval "sed '${line}s/#//' step3_RAW2DIGI_L1Reco_RECO_intermediate.py > step3_RAW2DIGI_L1Reco_RECO_int_2.py"
	eval "sed 's/newRecoCod_with_date/$tarName/' step3_RAW2DIGI_L1Reco_RECO_int_2.py > step3_RAW2DIGI_L1Reco_RECO_$i.py "

	rm step3_RAW2DIGI_L1Reco_RECO_intermediate.py step3_RAW2DIGI_L1Reco_RECO_int_2.py
	rm reReco_temp
	rm run_reReco_temp.csh run_reReco_updatedTar.csh 

done
