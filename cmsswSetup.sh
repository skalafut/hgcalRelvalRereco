#!/bin/bash

#####################
#use this script once the new reconstruction code has been checked out from github
#####################

#use this to save all collections of RecHit objects
addRecHits=Content.outputCommands+cms.untracked.vstring('keep *_*RecHit*_*_*') 

#change relName to match the CMSSW release which should be used in reconstruction
relName=CMSSW_6_2_0_SLHC23

cd $relName/src/
cmsenv

cmsDriver.py step3_TEMP_intermediate --conditions auto:upgradePLS3 -n -1 --eventcontent FEVTDEBUGHLT -s RAW2DIGI,L1Reco,RECO --datatier GEN-SIM-RECO --customise SLHCUpgradeSimulations/Configuration/combinedCustoms.cust_2023HGCalMuon --geometry Extended2023HGCalMuon,Extended2023HGCalMuonReco --magField 38T_PostLS1 --filein file:input.root --fileout file:outputRereco_using_newRecoCode_with_date_NUM.root --no_exec

eval "sed 's/Content.outputCommands/$addRecHits/' step3_TEMP_intermediate_RAW2DIGI_L1Reco_RECO.py > step3_TEMP_RAW2DIGI_L1Reco_RECO.py"

mv step3_TEMP_RAW2DIGI_L1Reco_RECO.py ../../.
cd ../../.

