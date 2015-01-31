#!/bin/bash

#the max value of i should match the max value of i in makeRunFiles.sh 
for i in {0..1}
do
	#reduce request_disk and request_memory by 30% when running re-reco jobs
	#on zero PU input files
	eval 'condor_submit request_disk=30000000 request_memory=8000000 reReco_$i'

done

