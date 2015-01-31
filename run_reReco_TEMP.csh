#!/bin/csh

setenv HOME /AbsPathToOutputDir
setenv PATH /bin:/usr/bin:/usr/local/bin:/usr/krb5/bin:/usr/afsws/bin:/usr/krb5/bin/aklog

#source /uscmst1/prod/sw/cms/cshrc prod
source /cvmfs/cms.cern.ch/cmsset_default.csh prod
setenv SCRAM_ARCH slc6_amd64_gcc472

cmsrel cmsswRelease 

mv newRecoCode_with_date.tar step3_RAW2DIGI_L1Reco_RECO_NUM.py cmsswRelease/src/.

cd cmsswRelease/src/
tar -xvf newRecoCode_with_date.tar
rm newRecoCode_with_date.tar

cmsenv
eval `scramv1 runtime -csh`
eval 'scram b -j 8'

cmsRun step3_RAW2DIGI_L1Reco_RECO_NUM.py

mv outputRereco_using_newRecoCode_with_date_NUM.root $HOME/.

echo "finished job"
