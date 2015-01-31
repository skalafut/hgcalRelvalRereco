# Auto generated configuration file
# using: 
# Revision: 1.20 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step3_TEMP --conditions auto:upgradePLS3 -n -1 --eventcontent FEVTDEBUGHLT -s RAW2DIGI,L1Reco,RECO --datatier GEN-SIM-RECO --customise SLHCUpgradeSimulations/Configuration/combinedCustoms.cust_2023HGCalMuon --geometry Extended2023HGCalMuon,Extended2023HGCalMuonReco --magField 38T_PostLS1 --filein file:input.root --fileout file:outputRereco_using_newRecoCode_with_date_NUM.root --no_exec
import FWCore.ParameterSet.Config as cms

process = cms.Process('RECO')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2023HGCalMuonReco_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(75)
)

# Input source
process.source = cms.Source("PoolSource",
    secondaryFileNames = cms.untracked.vstring(),
	fileNames = cms.untracked.vstring(
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/02A9D980-189C-E411-B8A0-0025905964A2.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/049513A9-189C-E411-8CD3-002354EF3BE0.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/08575EE9-129C-E411-A7ED-00261894394F.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/08D311AA-189C-E411-9E58-0026189437F0.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/0A5D05A8-189C-E411-80B1-002618FDA28E.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/0AA89556-119C-E411-B6E9-0026189438EF.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/0CBFACAB-189C-E411-8260-0026189438DC.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/0E59DD59-119C-E411-A470-0025905938B4.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/0E821CD2-129C-E411-BC4C-002618943910.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/12C11957-119C-E411-AF95-0025905964A2.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/1442C253-119C-E411-8FDC-00261894395C.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/14926BA8-189C-E411-A7AA-0026189437FD.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/14D5C535-119C-E411-8D08-002618943982.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/1675E2A6-189C-E411-B2D0-0026189438A7.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/1E239356-119C-E411-8750-00259059649C.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/1E7DA1AA-189C-E411-8FEE-00261894393A.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/20353852-119C-E411-8C07-002618943865.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/2461D848-189C-E411-8E03-00261894386F.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/2851CA2D-119C-E411-8831-002618943860.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/2A36D531-119C-E411-88C0-00261894396D.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/3401E141-119C-E411-B6F4-0025905B8562.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/367F51C3-129C-E411-A1EA-003048FFD740.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/3853854A-189C-E411-A748-002618943807.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/3A2CD931-119C-E411-88E3-00261894396D.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/3EC4DED4-129C-E411-8DD7-00248C0BE005.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/4083F431-119C-E411-AD80-00261894396D.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/447B6D53-119C-E411-A37F-00261894388B.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/46A5C858-119C-E411-B680-0025905B8598.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/46DCC632-119C-E411-9562-00261894396D.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/4A7038A9-189C-E411-BBE5-0026189438B4.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/4A8EA8FC-189C-E411-A651-002590593920.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/52466F28-119C-E411-8FCE-002618943898.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/52756D55-119C-E411-91E7-0026189438A9.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/54CC5F49-189C-E411-B64C-0025905B858E.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/5818584C-189C-E411-BDBD-00261894394A.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/58AF1E55-119C-E411-ADD9-0026189437F0.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/620DD980-189C-E411-ACA3-0025905964A2.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/62336277-189C-E411-9380-0025905A4964.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/626B9955-119C-E411-915E-0025905A60F2.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/662D7653-119C-E411-8154-00248C0BE012.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/70395455-119C-E411-96F4-0025905A4964.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/70728554-119C-E411-8C82-002618943886.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/707C10F9-189C-E411-A71A-00259059391E.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/78BAE3A8-189C-E411-9A72-0025905A48D8.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/78E6324C-189C-E411-AF5D-0026189437FD.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/8402BA35-119C-E411-A8DF-002354EF3BCE.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/8472D0A7-189C-E411-B73A-0025905A60B4.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/84AF28D2-129C-E411-A8DD-002618943910.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/88B3DD34-119C-E411-9D6D-0026189437F8.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/88C98855-119C-E411-A356-002618943860.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/8C35F4EB-129C-E411-BECF-0025905A6094.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/8C3ED2E1-129C-E411-AFFE-002618943826.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/906ECC05-119C-E411-9395-0025905B858C.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/9070733E-119C-E411-B818-0025905964A2.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/924738EF-129C-E411-9518-0026189438B5.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/929326BA-129C-E411-8F38-002618943947.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/92D29D55-119C-E411-A6BD-0025905A610C.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/9402CAD2-129C-E411-8A15-002618943829.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/987B47D8-129C-E411-AED1-0025905A60FE.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/98B4E935-119C-E411-99F9-0025905B8610.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/9CDFB8C2-129C-E411-9EA7-003048FFD796.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/9EF29B53-119C-E411-A233-002618943982.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/A246DA47-189C-E411-93CB-002618943959.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/A277ABBE-129C-E411-BBC1-002354EF3BE0.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/A8521BD2-129C-E411-BEFC-002354EF3BCE.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/A855AD34-119C-E411-AC49-0026189438AD.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/A898BECF-129C-E411-BD35-00261894397F.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/ACED1ED5-129C-E411-B7E9-002618943821.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/AE484053-119C-E411-B46D-0026189438AD.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/BA80C953-119C-E411-957E-002354EF3BCE.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/BAA17257-119C-E411-898B-002354EF3BDC.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/BCF1A6BB-129C-E411-AD2C-0025905B8576.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/BE94FC35-119C-E411-BE9A-0025905A610C.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/C266ABD2-129C-E411-B1EE-002618943916.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/C26A0E54-119C-E411-8B00-0025905A612A.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/C2868435-119C-E411-BBE0-00261894395C.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/CC923274-189C-E411-A63D-0025905A4964.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/CE60E5A0-189C-E411-9E1D-003048D25BA6.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/D0A7747D-189C-E411-8467-0025905938D4.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/D22721D2-129C-E411-B4C4-002618943947.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/D227C435-119C-E411-AA6B-0025905A60EE.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/D47B7F2E-119C-E411-BD0A-0025905A60F8.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/D67F8923-119C-E411-ADD8-0025905B85B2.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/D6A098F0-189C-E411-B78F-0025905938A4.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/DC1CE939-119C-E411-B2D8-002618943865.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/DC8D294A-189C-E411-AE4D-0026189438EB.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/DCC15DBA-129C-E411-9F74-002618943868.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/DCECFED9-129C-E411-875F-0025905938B4.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/DCFB01A9-189C-E411-A25E-0026189438BC.root',
       #'root://cms-xrd-global.cern.ch//store/relval/CMSSW_6_2_0_SLHC23/RelValQCD_Pt_80_120_14TeV/GEN-SIM-DIGI-RAW/PU_PH2_1K_FB_V6_HGCalV5PU140-v1/00000/E24B2878-189C-E411-BEFE-0025905938AA.root'

		)
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.20 $'),
    annotation = cms.untracked.string('step3 nevts:1500'),
    name = cms.untracked.string('Applications')
)

# Output definition

process.FEVTDEBUGHLToutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.FEVTDEBUGHLTEventContent.outputCommands + cms.untracked.vstring('keep *_*RecHit*_*_*'),
    fileName = cms.untracked.string('file:outputRereco_using_newRecoCode_with_date_NUM.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM-RECO')
    )
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:upgradePLS3', '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstruction)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGHLToutput_step = cms.EndPath(process.FEVTDEBUGHLToutput)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.L1Reco_step,process.reconstruction_step,process.endjob_step,process.FEVTDEBUGHLToutput_step)

# customisation of the process.

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.combinedCustoms
from SLHCUpgradeSimulations.Configuration.combinedCustoms import cust_2023HGCalMuon 

#call to customisation function cust_2023HGCalMuon imported from SLHCUpgradeSimulations.Configuration.combinedCustoms
process = cust_2023HGCalMuon(process)

# End of customisation functions
