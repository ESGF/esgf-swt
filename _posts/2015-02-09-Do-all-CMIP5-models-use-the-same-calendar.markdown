---
layout: post
title:  "Do all CMIP5 models use the same calendar?"
categories: data
date: 2015-08-13 18:30:00
author: Peter Lenzen, Torsten Rathmann
---

No, see table below. The values in the table have been taken from the calendar attributes of the NetCDF files. Since the calendars "standard" and "gregorian" are identical as well as "noleap" and "365_day", only the latter are used in the table. CMIP5 calendars are defined in the [CF standard](http://cfconventions.org/Data/cf-conventions/cf-conventions-1.6/build/cf-conventions.html#calendar) and in the [CMIP5 Model Output Requirements](http://cmip-pcmdi.llnl.gov/cmip5/docs/CMIP5_output_metadata_requirements.pdf).

|Model          |Calendar            |For experiments                                           |
|:--------------|:-------------------|:---------------------------------------------------------|
|ACCESS1.0      |proleptic_gregorian |all                                                       |
|ACCESS1.3      |proleptic_gregorian |all                                                       |
|BCC-CSM1.1     |365_day             |all                                                       |
|BCC-CSM1.1(m)  |365_day             |all                                                       |
|BNU-ESM        |365_day             |all                                                       |
|CanAM4         |365_day             |all                                                       |
|CanCM4         |365_day             |all                                                       |
|CanESM2        |365_day             |all                                                       |
|CCSM4          |365_day             |all                                                       |
|CESM1(BGC)     |365_day             |all                                                       |
|CESM1(CAM5)    |365_day             |all                                                       |
|CESM1(FASTCHEM)|365_day             |all                                                       |
|CESM1(WACCM)   |365_day             |all                                                       |
|CFSv2-2011     |gregorian           |all                                                       |
|CMCC-CESM      |gregorian           |all                                                       |
|CMCC-CM        |gregorian           |all                                                       |
|CMCC-CMS       |gregorian           |all                                                       |
|CNRM-CM5       |gregorian           |all                                                       |
|CNRM-CM5-2     |gregorian           |all                                                       |
|CSIRO-Mk3.6.0  |365_day             |all                                                       |
|CSIRO-Mk3L-1-2 |365_day             |all                                                       |
|EC-EARTH       |gregorian           |all                                                       |
|GEOS-5         |gregorian           |all                                                       |
|FGOALS-g2      |365_day             |all                                                       |
|FGOALS-gl      |365_day             |all                                                       |
|FGOALS-s2      |365_day             |all                                                       |
|GFDL-CM2.1     |julian              |all                                                       |
|GFDL-CM3       |365_day             |all but amip: julian                                      |
|GFDL-ESM2G     |365_day             |all                                                       |
|GFDL-ESM2M     |365_day             |all                                                       |
|GISS-E2-H      |365_day             |all                                                       |
|GISS-E2-H-CC   |365_day             |all                                                       |
|GISS-E2-R      |365_day             |all                                                       |
|GISS-E2-R-CC   |365_day             |all                                                       |
|HadCM3         |360_day             |all                                                       |
|HadGEM2-A      |360_day             |all                                                       |
|HadGEM2-AO     |360_day             |all                                                       |
|HadGEM2-CC     |360_day             |all                                                       |
|HadGEM2-ES     |360_day             |all                                                       |
|INM-CM4        |365_day             |all                                                       |
|IPSL-CM5A-LR   |365_day             |all but aqua4K, aqua4xCO2, aquaControl, past1000: 360_day |
|IPSL-CM5A-MR   |365_day             |all                                                       |
|IPSL-CM5B-LR   |365_day             |all but aquaControl: 360_day                              |
|MIROC-ESM      |proleptic_gregorian |1pctCO2, abrupt4xCO2, past1000                            |
|MIROC-ESM      |gregorian           |esmControl, esmFixClim2, esmHistorical, lgm, midHolocene, piControl, rcp26, rcp45, rcp60, rcp85, esmrcp85, historical, historicalGHG, historicalNat|
|MIROC-ESM-CHEM |gregorian           |all                                                       |
|MIROC4h        |gregorian           |all but piControl: 365_day                                |
|MIROC5         |360_day             |aqua4K, aqua4xCO2, aquaControl                            |
|MIROC5         |365_day             |1pctCO2, abrupt4xCO2, amip, amip4K, amip4xCO2, amipFuture,|
|               |                    |historical, piControl, rcp26, rcp45, rcp60, rcp85,        |
|               |                    |sstClim, sstClim4xCO2, sstClimAerosol, sstClimSulfate     |
|MIROC5         |gregorian           |decadals                                                  |
|MPI-ESM-LR     |proleptic_gregorian |all                                                       |
|MPI-ESM-MR     |proleptic_gregorian |all                                                       |
|MPI-ESM-P      |proleptic_gregorian |all                                                       |
|MRI-AGCM3-2H   |gregorian           |all                                                       |
|MRI-AGCM3-2S   |gregorian           |all                                                       |
|MRI-CGCM3      |gregorian           |all                                                       |
|MRI-ESM1       |gregorian           |all                                                       |
|NorESM1-M      |365_day             |all                                                       |
|NorESM1-ME     |                    |                                                          |
