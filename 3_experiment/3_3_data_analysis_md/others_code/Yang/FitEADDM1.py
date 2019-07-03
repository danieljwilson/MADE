#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 21:34:58 2018

@author: teohyiyang
"""
import os
import scipy as sp
from scipy import io as input
import numpy as np
import sys
import scipy.stats as sps
import time
import concurrent.futures
import numba as nb
from numba import jit
import pickle
#from sklearn.neighbors import KernelDensity
#from sklearn.grid_search import GridSearchCV

#
##@jit(nopython = True, nogil = True)
#def noisey(s, precision, nsims, finalsim):
#    noise = s*np.sqrt(precision)*np.random.normal(0,1, (nsims, finalsim))
#    return(noise)
#
#
##@jit(nopython = True, nogil = True)
#def newmatrix(nsims, finalsim):
#    newmat = np.zeros((nsims,finalsim))
#    return(newmat)

#@jit
def eyetodriftvec(eye, finalsim, nfix,timevec, percept, wself, selfamt, wother, otheramt, wfair, theta):
    if not np.equal(eye.size,0):
        eye2 = eye[0]
        for i in range(1,nfix):
            eye2 = np.vstack([eye2, eye[i]])
        prev = nfix -1
        fillfix = nfix + 1
        if np.equal(nfix,  1):
            nextrow = np.asarray([eye2[0],fillfix, eye2[3] + 1, finalsim, eye2[4], eye2[5]])
        else:
            nextrow = np.asarray([eye2[prev,0],fillfix, eye2[prev,3] + 1, finalsim, eye2[prev,4], eye2[prev,5]])
        
        eye2 = np.vstack([eye2,nextrow])
        
        for i in range(fillfix):
            p = int(eye2[i,2])
            if p == 0:
                p = 1
            q = int(eye2[i,3]) + 1
            timevec[p:q] = eye2[i,5]
        selfproc = np.where(np.equal(eye2[:,5] , 1))
    
        if np.greater(np.size(selfproc[0]) , 1):
            selfproc = selfproc[0][0]
            selfprocblindstart = np.int(eye2[selfproc, 2])
            selfprocblindend = np.int(selfprocblindstart + (percept*1000))
            if np.greater(selfprocblindend , finalsim):
                selfprocblindend = finalsim + 1
            timevec[selfprocblindstart:selfprocblindend] = np.nan
    
        otherproc = np.where(eye2[:,5] == 2)
    
    
        if np.greater(np.size(otherproc[0]) , 1):
            otherproc = otherproc[0][0]
            otherprocblindstart = np.int(eye2[otherproc, 2])
            otherprocblindend = np.int(otherprocblindstart + (percept*1000))
            if np.greater(otherprocblindend , finalsim):
                otherprocblindend = finalsim + 1
            timevec[otherprocblindstart:otherprocblindend] = np.nan
    
    
        driftvec = np.zeros(finalsim) 
    
        
        p = np.where(np.isfinite(timevec))
        if np.size(p[0]) == 0:
            dstart = 0
        else: 
            dstart = p[0][1]
            AOIs  = np.arange(1,3)
        
            selfonly = wself*selfamt
            otheronly = wother*otheramt
            notfocusself = (1-theta)*wself*selfamt
            notfocusother = (1-theta)*wother*otheramt
            notfocusboth = (1-theta)*wself*selfamt + (1-theta)*wother*otheramt \
                           - wfair*(np.abs(selfamt-otheramt))
            selfdom = wself*selfamt + (1-theta)*wother*otheramt - wfair*(np.abs(selfamt-otheramt))
            otherdom = (1-theta)*wself*selfamt + wother*otheramt - wfair*(np.abs(selfamt-otheramt))
            
            driftvec = filldriftvecjit(driftvec,dstart,AOIs,timevec,selfdom,otherdom,notfocusboth,notfocusself,notfocusother,otheronly,selfonly)
       
    else:
        driftvec = np.zeros(finalsim)
        dstart = 0
          
    return(driftvec,dstart)
    
@jit(nb.float64[:](nb.float64[:], nb.int64, nb.int64[:], nb.float64[:], nb.float64, nb.float64, nb.float64, nb.float64, nb.float64, nb.float64, nb.float64), nopython = True,nogil=True,cache =True) 
def filldriftvecjit(driftvec,dstart,AOIs,timevec,selfdom,otherdom,notfocusboth,notfocusself,notfocusother,otheronly,selfonly):
    if np.isfinite(dstart):
        info2 = AOIs[np.where(np.not_equal(AOIs, timevec[dstart]))[0][0]]
        infot2 = np.where(np.equal(timevec, info2))[0]
    if np.equal(infot2.size ,0):
        aoiswitch = np.nan
        first = driftvec
        firsttime = timevec
    else:
        aoiswitch = infot2[0]
        first = driftvec[0:aoiswitch]
        firsttime = timevec[0:aoiswitch]
        bothtime = timevec[aoiswitch:]
        both = driftvec[aoiswitch:]
        for j in np.arange(both.size):
            if np.isfinite(bothtime[j]):
                if np.equal(bothtime[j],1):
                    both[j] = selfdom
                elif np.equal(bothtime[j],2):
                    both[j] = otherdom
            else:
                both[j] = notfocusboth

    if np.equal(timevec[dstart] ,1):
        for j in np.arange(first.size):
            if np.isfinite(firsttime[j]):
                first[j] = selfonly
            else:
                first[j] = notfocusself
    elif np.equal(timevec[dstart] ,2):
        for j in np.arange(first.size):
            if np.isfinite(firsttime[j]):
                first[j] = otheronly
            else:
                first[j] = notfocusother

    if np.greater(dstart , 1):
        first[0:dstart] = 0

    if np.isfinite(aoiswitch):
        driftvec[0:aoiswitch] = first
        driftvec[aoiswitch:] = both
    else:
        driftvec = first 
        
    return driftvec 


#def filldriftvec(driftvec,dstart,AOIs,timevec,selfdom,otherdom,notfocusboth,notfocusself,notfocusother,otheronly,selfonly):
#    if np.isfinite(dstart):
#        info2 = AOIs[np.where(np.not_equal(AOIs, timevec[dstart]))[0][0]]
#        infot2 = np.where(np.equal(timevec, info2))[0]
#    if np.equal(infot2.size ,0):
#        aoiswitch = np.nan
#        first = driftvec
#        firsttime = timevec
#    else:
#        aoiswitch = infot2[0]
#        first = driftvec[0:aoiswitch]
#        firsttime = timevec[0:aoiswitch]
#        bothtime = timevec[aoiswitch:]
#        both = driftvec[aoiswitch:]
#        both[np.where(np.equal(bothtime,1))[0]] = selfdom
#        both[np.where(np.equal(bothtime,2))[0]] = otherdom
#        both[np.where(np.isnan(bothtime))[0]] = notfocusboth
#
#    if np.equal(timevec[dstart] ,1):
#        first[np.where(np.equal(firsttime ,1))[0]]  = selfonly
#        first[np.where(np.isnan(firsttime))[0]] = notfocusself
#    elif np.equal(timevec[dstart] ,2):
#        first[np.where(np.equal(firsttime,2))[0]] = otheronly
#        first[np.where(np.isnan(firsttime))[0]] = notfocusother
#
#    if np.greater(dstart , 1):
#        first[0:dstart] = 0
#
#    if np.isfinite(aoiswitch):
#        driftvec[0:aoiswitch] = first
#        driftvec[aoiswitch:] = both
#    else:
#        driftvec = first 
#        
#    return(driftvec)
#    
#def ddmloop(nsims, boundaries, dstart, driftvec,stbias, finalsim,precision,s):
#    
#    ddms = np.zeros(nsims) + stbias
#    t = dstart-1
#    withinbounds = np.ones(nsims, dtype=bool)
#    resp = np.full(nsims, np.nan)
#    rt = np.full(nsims, np.nan)
#    while (np.logical_and(np.less(t,finalsim-1), np.any(withinbounds))):
#        t += 1
#        stillgoing = np.where(np.equal(withinbounds,True))[0]
#        dy = driftvec[t]*precision + np.random.normal(0,1,np.size(stillgoing))*s*np.sqrt(precision)
#        ddms[stillgoing] += dy
#        boundcompare = np.where(np.greater_equal(np.abs(ddms), boundaries[t]))[0]
#        withinbounds[boundcompare] = False
#        justdone = np.where(np.logical_and(np.equal(withinbounds,False),np.isnan(resp)))[0]
#        resp[justdone] = np.sign(ddms[justdone])
#        rt[justdone] = t + 1        
#    return(resp,rt)
#    
@jit(nb.types.UniTuple(nb.float64[:],2)(nb.int64, nb.float64[:], nb.int64, nb.float64[:], nb.float64,nb.int64,nb.float64,nb.float64), nopython = True,nogil=True,cache =True)    
def ddmloopjit(nsims, boundaries, dstart, driftvec,stbias, finalsim,precision,s):
    ddms = np.zeros(nsims) + stbias
    t = dstart-1
    withinbounds = np.ones(nsims)
    resp = np.full(nsims,np.nan)
    rt = np.full(nsims,np.nan)
    while (np.logical_and(np.less(t,finalsim-1), np.any(withinbounds))):
        t += 1
        stillgoing = np.where(np.equal(withinbounds,1))[0]
        dy = np.full(stillgoing.size,driftvec[t]*precision)
        for j in np.arange(0, stillgoing.size):
            dy[j] += np.random.normal(0,1)*s*np.sqrt(precision)
        ddms[stillgoing] += dy
        bcoll = boundaries[t]
        boundcompare = np.where(np.greater_equal(np.abs(ddms), bcoll))[0]
        withinbounds[boundcompare] = 0
        justdone = np.where(np.logical_and(np.equal(withinbounds,0),np.isnan(resp)))[0]
        resp[justdone] = np.sign(ddms[justdone])
        rt[justdone] = t + 1
    return(resp,rt)
   
#@jit(nopython = True, nogil = True)
def maxmax(finish,maxRT):
    if not(np.isnan(finish)):
        out = np.ceil(finish*10)/10
    else:
        out = maxRT
    return(out)

@jit(nb.float64[:](nb.float64, nb.float64, nb.int64),nopython = True,nogil=True,cache=True)
def collapseboundjit(bound,collapse,finalsim):
    out = np.full(finalsim, bound)
    for j in np.arange(finalsim):
        out[j] *= np.exp(-1* collapse * (j+1))
    return out

def collapsebound(bound,collapse,finalsim):
    bound *= np.exp(-1* collapse * (np.arange(finalsim) + 1))
    return bound
#
##@jit(nopython = True, nogil = True)
#def findone(mat):        
#    out = np.where(mat==1)
#    return(out)
#    
##@jit(nopython = True, nogil = True)
#def findoverbound(mat1,mat2):
#    out = np.greater_equal(np.abs(mat1),mat2)
#    return(out)
    
##@jit
#def simulEADDM(params,Sims):
#    #s1 = time.perf_counter()
#    precision = float(.001)
#    s = float(.1)
#    nsims = int(Sims)
#
#    selfamt =  params['selfamt']
#    otheramt =  params['otheramt']
#    eye = params['eye']
#    respoptions = (0,1)
#
#    wself = params['self']
#    wother = params['other']
#    wfair = params['fair']
#    bound = params['bound']
#    collapse = params['collapse']
#    stbias = params['modbias']
#    percept = params['percept']
#    theta = params['theta']
#
#    nfix = len(eye)    
#    finalsim = int(params['simmaxrt']*1000)
#    timevec = np.full(finalsim, np.nan)
#    
#
#   # driftvar = np.zeros(finalsim, dtype = float)
#   # startvar = 0
#    
##    eye2 = eye[0]
##    for i in range(1,nfix):
##        eye2 = np.vstack((eye2, eye[i]))
##
##    eye2 = np.vstack((eye2, [eye2[nfix-1,0],nfix+1, eye2[nfix-1,3] + 1, finalsim, eye2[nfix-1,4], eye2[nfix-1,5]]))
##
##    for i in range(nfix+1):
##        p = int(eye2[i,2])
##        if p == 0:
##            p = 1
##        q = int(eye2[i,3]) + 1
##        timevec[p:q] = eye2[i,5]
##
##    selfproc = np.where(eye2[:,5] == 1)
##
##
##    if len(selfproc[0]) > 1:
##        selfproc = selfproc[0][0]
##        selfprocblindstart = int(eye2[selfproc, 2])
##        selfprocblindend = int(selfprocblindstart + (percept*1000))
##        if selfprocblindend > finalsim:
##            selfprocblindend = finalsim + 1
##        timevec[selfprocblindstart:selfprocblindend] = np.nan
##
##    otherproc = np.where(eye2[:,5] == 2)
##
##
##    if len(otherproc[0]) > 1:
##        otherproc = otherproc[0][0]
##        otherprocblindstart = int(eye2[otherproc, 2])
##        otherprocblindend = int(otherprocblindstart + (percept*1000))
##        if otherprocblindend > finalsim:
##            otherprocblindend = finalsim + 1
##        timevec[otherprocblindstart:otherprocblindend] = np.nan
##
##
##    driftvec = np.zeros(finalsim, dtype = float) 
##    crazybound = np.zeros(finalsim, dtype = float)   
##
##
##    if np.isnan(timevec[0]):
##        p = np.where(~np.isnan(timevec))
##        if len(p[0]) == 0:
##            dstart = np.nan
##        else: 
##            dstart = p[0][1]
##    else:
##        dstart = 0 
##    AOIs  = [1,2]
##
##    selfonly = wself*selfamt
##    otheronly = wother*otheramt
##    notfocusself = (1-theta)*wself*selfamt
##    notfocusother = (1-theta)*wother*otheramt
##    notfocusboth = (1-theta)*wself*selfamt + (1-theta)*wother*otheramt \
##                   - wfair*(abs(selfamt-otheramt))
##    selfdom = wself*selfamt + (1-theta)*wother*otheramt - wfair*(abs(selfamt-otheramt))
##    otherdom = (1-theta)*wself*selfamt + wother*otheramt - wfair*(abs(selfamt-otheramt))
##
##
##    if ~np.isnan(dstart):
##        info2 = AOIs[np.where(AOIs != timevec[dstart])[0][0]]
##        infot2 = np.where(timevec == info2)
##        if len(infot2[0]) == 0:
##            aoiswitch = np.nan
##        else:
##            aoiswitch = infot2[0][0]
##        if not np.isnan(aoiswitch):
##            first = driftvec[0:aoiswitch]
##            firsttime = timevec[0:aoiswitch]
##            both = driftvec[aoiswitch:]
##            bothtime = timevec[aoiswitch:]
##            both[np.where(bothtime==1)] = selfdom
##            both[np.where(bothtime==2)] = otherdom
##            both[np.where(np.isnan(bothtime))] = notfocusboth
##
##        else:
##            first = driftvec
##            firsttime = timevec
##
##        if timevec[dstart] == 1:
##            first[np.where(firsttime ==1)]  = selfonly
##            first[np.where(np.isnan(firsttime))] = notfocusself
##        elif timevec[dstart] ==2:
##            first[np.where(firsttime ==2)] = otheronly
##            first[np.where(np.isnan(firsttime))] = notfocusother
##
##        if dstart > 1:
##            first[0:dstart] = 0
##
##        if not np.isnan(aoiswitch):
##            driftvec[0:aoiswitch] = first
##            driftvec[aoiswitch:] = both
##        else:
##            driftvec = first
#    
#    driftvec,dstart = eyetodriftvec(eye, finalsim, nfix,timevec, percept, wself, selfamt, wother, otheramt, wfair, theta)
#    
##    
##    crazybound = newmatrix(nsims, finalsim)
#    stbias *= bound
#    boundaries = collapsebound(bound,collapse,finalsim,precision)
#    
#    resp,rt = ddmloop(nsims, boundaries, dstart, driftvec,stbias, finalsim,precision,s)
#     
#    
#    
# #   drbtwt = np.random.normal(0,1,nsims)
# #   stbtwt = np.random.normal(0,1,nsims)
#    
#    #e1 = time.perf_counter()
#    #d1 = e1  -s1
###    
##    ss = time.perf_counter()
##    crazydrift = driftvec
##    crazydrift = np.repeat(crazydrift[np.newaxis,:], nsims,axis = 0)*precision
##    noise = noisey(s, precision, nsims, finalsim)
##    crazydrift += noise
##    
##    if dstart != 0:    
##        crazydrift[:,0:dstart] = 0
##        crazydrift[:,dstart-1] = stbias # + stbtwt*startvar
##    else:
##        crazydrift[:,dstart] += stbias
##    
##    
##    crazydriftf = np.add.accumulate(crazydrift,axis = 1,dtype =float)
##    
##    #s4 = time.perf_counter()
##    crazybound = collapsebound(bound,collapse,finalsim, precision)
##    crazybound = np.repeat(crazybound[np.newaxis,:], nsims, axis = 0)
##    
##
##    crazydrift0 = findoverbound(crazydriftf, crazybound)
##    
##    crazydrift1 = newmatrix(nsims, finalsim)
##    crazydrift1 = np.add.accumulate(crazydrift0,axis = 1,dtype = float)
##    coords = findone(crazydrift1)
##    #e4 = time.perf_counter()
##    #time4 = e4-s4
##    rt[coords[0]] = coords[1].copy() + 1
##    resp[coords[0]] = np.sign(crazydrift[coords])
##    ee = time.perf_counter()
##    time2 = ee-ss
##    
#    
##    ddms = np.zeros(nsims) + stbias #+ stbtwt*startvar
##    upper = bound
##    withinBounds = np.ones(nsims,dtype=bool)
##
##    if dstart != 0:
##        t = dstart - 1
##    else:
##        t = -1
##        
##    s2 = time.perf_counter()
##    while (t < (finalsim -1) and sum(withinBounds) > 0):
##        t = t + 1    
##        stillgoing = np.where(withinBounds == True)
##        
##        dy = driftvec[t]*precision \
##        + s*np.sqrt(precision)*np.random.normal(0,1, len(stillgoing[0]))
##        
##        ddms[stillgoing] = ddms[stillgoing] + dy 
##
##        current = np.where(np.greater_equal(abs(ddms) ,upper))[0]
##        withinBounds[current] = False 
##        
##        justDone = np.where(np.logical_and(np.greater_equal(abs(ddms) ,upper), np.isnan(resp1)))[0]
##
##        resp1[justDone] = np.sign(ddms[justDone])
##        rt1[justDone] = t + 1
##        
##        upper = bound * np.exp(-1*collapse*(t +1)*1000*precision)
##    e2 = time.perf_counter()   
##    d2= e2 - s2
#    
#    rt = rt*precision
#    resp[np.where(resp == -1)] = respoptions[0]
#    resp[np.where(resp == 1)] = respoptions[1]
##    rt1 = rt1*precision
##    resp1[np.where(resp1 == -1)] = respoptions[0]
##    resp1[np.where(resp1 == 1)] = respoptions[1]
##    
#    outcomes = {'resp' : resp, 'rt' : rt}
#    return(outcomes)
    
def simulEADDMjit(params,Sims):
    #s1 = time.perf_counter()
    precision = float(.001)
    s = float(.1)
    nsims = int(Sims)

    selfamt =  params['selfamt']
    otheramt =  params['otheramt']
    eye = params['eye']
    respoptions = (0,1)

    wself = params['self']
    wother = params['other']
    wfair = params['fair']
    bound = params['bound']
    collapse = params['collapse']
    stbias = params['modbias']
    percept = params['percept']
    theta = params['theta']

    nfix = len(eye)    
    finalsim = int(params['simmaxrt']*1000)
    timevec = np.full(finalsim, np.nan)
    

   # driftvar = np.zeros(finalsim, dtype = float)
   # startvar = 0
    
#    eye2 = eye[0]
#    for i in range(1,nfix):
#        eye2 = np.vstack((eye2, eye[i]))
#
#    eye2 = np.vstack((eye2, [eye2[nfix-1,0],nfix+1, eye2[nfix-1,3] + 1, finalsim, eye2[nfix-1,4], eye2[nfix-1,5]]))
#
#    for i in range(nfix+1):
#        p = int(eye2[i,2])
#        if p == 0:
#            p = 1
#        q = int(eye2[i,3]) + 1
#        timevec[p:q] = eye2[i,5]
#
#    selfproc = np.where(eye2[:,5] == 1)
#
#
#    if len(selfproc[0]) > 1:
#        selfproc = selfproc[0][0]
#        selfprocblindstart = int(eye2[selfproc, 2])
#        selfprocblindend = int(selfprocblindstart + (percept*1000))
#        if selfprocblindend > finalsim:
#            selfprocblindend = finalsim + 1
#        timevec[selfprocblindstart:selfprocblindend] = np.nan
#
#    otherproc = np.where(eye2[:,5] == 2)
#
#
#    if len(otherproc[0]) > 1:
#        otherproc = otherproc[0][0]
#        otherprocblindstart = int(eye2[otherproc, 2])
#        otherprocblindend = int(otherprocblindstart + (percept*1000))
#        if otherprocblindend > finalsim:
#            otherprocblindend = finalsim + 1
#        timevec[otherprocblindstart:otherprocblindend] = np.nan
#
#
#    driftvec = np.zeros(finalsim, dtype = float) 
#    crazybound = np.zeros(finalsim, dtype = float)   
#
#
#    if np.isnan(timevec[0]):
#        p = np.where(~np.isnan(timevec))
#        if len(p[0]) == 0:
#            dstart = np.nan
#        else: 
#            dstart = p[0][1]
#    else:
#        dstart = 0 
#    AOIs  = [1,2]
#
#    selfonly = wself*selfamt
#    otheronly = wother*otheramt
#    notfocusself = (1-theta)*wself*selfamt
#    notfocusother = (1-theta)*wother*otheramt
#    notfocusboth = (1-theta)*wself*selfamt + (1-theta)*wother*otheramt \
#                   - wfair*(abs(selfamt-otheramt))
#    selfdom = wself*selfamt + (1-theta)*wother*otheramt - wfair*(abs(selfamt-otheramt))
#    otherdom = (1-theta)*wself*selfamt + wother*otheramt - wfair*(abs(selfamt-otheramt))
#
#
#    if ~np.isnan(dstart):
#        info2 = AOIs[np.where(AOIs != timevec[dstart])[0][0]]
#        infot2 = np.where(timevec == info2)
#        if len(infot2[0]) == 0:
#            aoiswitch = np.nan
#        else:
#            aoiswitch = infot2[0][0]
#        if not np.isnan(aoiswitch):
#            first = driftvec[0:aoiswitch]
#            firsttime = timevec[0:aoiswitch]
#            both = driftvec[aoiswitch:]
#            bothtime = timevec[aoiswitch:]
#            both[np.where(bothtime==1)] = selfdom
#            both[np.where(bothtime==2)] = otherdom
#            both[np.where(np.isnan(bothtime))] = notfocusboth
#
#        else:
#            first = driftvec
#            firsttime = timevec
#
#        if timevec[dstart] == 1:
#            first[np.where(firsttime ==1)]  = selfonly
#            first[np.where(np.isnan(firsttime))] = notfocusself
#        elif timevec[dstart] ==2:
#            first[np.where(firsttime ==2)] = otheronly
#            first[np.where(np.isnan(firsttime))] = notfocusother
#
#        if dstart > 1:
#            first[0:dstart] = 0
#
#        if not np.isnan(aoiswitch):
#            driftvec[0:aoiswitch] = first
#            driftvec[aoiswitch:] = both
#        else:
#            driftvec = first
    
    driftvec,dstart = eyetodriftvec(eye, finalsim, nfix,timevec, percept, wself, selfamt, wother, otheramt, wfair, theta)
    
#    
#    crazybound = newmatrix(nsims, finalsim)
    stbias *= bound
    boundaries = collapsebound(bound,collapse,finalsim)
    
    resp,rt = ddmloopjit(nsims, boundaries, dstart, driftvec,stbias, finalsim,precision,s)
    
    
 #   drbtwt = np.random.normal(0,1,nsims)
 #   stbtwt = np.random.normal(0,1,nsims)
    
    #e1 = time.perf_counter()
    #d1 = e1  -s1
##    
#    ss = time.perf_counter()
#    crazydrift = driftvec
#    crazydrift = np.repeat(crazydrift[np.newaxis,:], nsims,axis = 0)*precision
#    noise = noisey(s, precision, nsims, finalsim)
#    crazydrift += noise
#    
#    if dstart != 0:    
#        crazydrift[:,0:dstart] = 0
#        crazydrift[:,dstart-1] = stbias # + stbtwt*startvar
#    else:
#        crazydrift[:,dstart] += stbias
#    
#    
#    crazydriftf = np.add.accumulate(crazydrift,axis = 1,dtype =float)
#    
#    #s4 = time.perf_counter()
#    crazybound = collapsebound(bound,collapse,finalsim, precision)
#    crazybound = np.repeat(crazybound[np.newaxis,:], nsims, axis = 0)
#    
#
#    crazydrift0 = findoverbound(crazydriftf, crazybound)
#    
#    crazydrift1 = newmatrix(nsims, finalsim)
#    crazydrift1 = np.add.accumulate(crazydrift0,axis = 1,dtype = float)
#    coords = findone(crazydrift1)
#    #e4 = time.perf_counter()
#    #time4 = e4-s4
#    rt[coords[0]] = coords[1].copy() + 1
#    resp[coords[0]] = np.sign(crazydrift[coords])
#    ee = time.perf_counter()
#    time2 = ee-ss
#    
    
#    ddms = np.zeros(nsims) + stbias #+ stbtwt*startvar
#    upper = bound
#    withinBounds = np.ones(nsims,dtype=bool)
#
#    if dstart != 0:
#        t = dstart - 1
#    else:
#        t = -1
#        
#    s2 = time.perf_counter()
#    while (t < (finalsim -1) and sum(withinBounds) > 0):
#        t = t + 1    
#        stillgoing = np.where(withinBounds == True)
#        
#        dy = driftvec[t]*precision \
#        + s*np.sqrt(precision)*np.random.normal(0,1, len(stillgoing[0]))
#        
#        ddms[stillgoing] = ddms[stillgoing] + dy 
#
#        current = np.where(np.greater_equal(abs(ddms) ,upper))[0]
#        withinBounds[current] = False 
#        
#        justDone = np.where(np.logical_and(np.greater_equal(abs(ddms) ,upper), np.isnan(resp1)))[0]
#
#        resp1[justDone] = np.sign(ddms[justDone])
#        rt1[justDone] = t + 1
#        
#        upper = bound * np.exp(-1*collapse*(t +1)*1000*precision)
#    e2 = time.perf_counter()   
#    d2= e2 - s2
    
    rt = rt*precision
    resp[np.where(resp == -1)] = respoptions[0]
    resp[np.where(resp == 1)] = respoptions[1]
#    rt1 = rt1*precision
#    resp1[np.where(resp1 == -1)] = respoptions[0]
#    resp1[np.where(resp1 == 1)] = respoptions[1]
#    
    outcomes = {'resp' : resp, 'rt' : rt}
    return(outcomes)
    
#@njit    
def NLLSimTest(params2, Sims, SelfProposal, OtherProposal, Fixations, modbias, TimeLimit, finish, choice): #, kde):   
    NLLDataProb = np.zeros(len(finish), dtype=float)
    params = params2
    maxRT = TimeLimit
    for i in range(len(finish)):
        params['selfamt'] = (SelfProposal[i]-50)/5
        params['otheramt'] = (OtherProposal[i]-50)/5
        params['modbias'] = modbias[i]
        params['eye'] = Fixations[i]
        precision = .001
        
        params['simmaxrt'] = maxmax(finish[i], maxRT)  
        
        sims = simulEADDMjit(params,Sims) 
        
        yes = np.asarray(np.where(sims['resp'] == 1))[0]
        no = np.asarray(np.where(sims['resp'] == 0))[0]
        fail = np.where(np.isnan(sims['resp']))
        nsims = len(sims['resp'])
        
        nyes = yes.size
        nno = no.size
        nfail = fail[0].size
        
#        nodist = sps.gaussian_kde(nort)
#        yesdist = sps.gaussian_kde(yesrt)
#        motoryes =  yesdist.integrate_box_1d(finish[i]-params['motor'], params['simmaxrt'])
#        motorno = nodist.integrate_box_1d(finish[i]-params['motor'], params['simmaxrt'])
#        if kde == 'sps':
        if choice[i]==0:
            if nno < 4:
                prob = (nno/nsims)/(params['simmaxrt']*1000)
            else:
                hsmooth = (nno*(3)/4)**(-1/5)/2
                nort = sims['rt'][no]
                try:
                    nodist = sps.gaussian_kde(nort,hsmooth)
                    prob = nodist.evaluate(finish[i]-params['motor'])*precision
                    if prob > 1:
                        prob = 1
                    elif prob < 0:
                        prob = 0
                except:
                    if np.equal(finish[i]-params['motor'],np.unique(nort)):
                        prob = 1
                    else:
                        prob = 0
                prob *= (nno/nsims)
        elif choice[i]==1:
            if nyes < 4:
                prob = (nyes/nsims)/(params['simmaxrt']*1000)
            else:
                hsmooth = (nyes*(3)/4)**(-1/5)/2
                yesrt = sims['rt'][yes]
                try:
                    yesdist = sps.gaussian_kde(yesrt,hsmooth)
                    prob = yesdist.evaluate(finish[i]-params['motor'])*precision
                    if prob > 1:
                            prob = 1
                    elif prob < 0:
                            prob = 0
                except:
                    if np.equal(finish[i]-params['motor'], np.unique(yesrt)):
                        prob = 1
                    else:
                        prob = 0
                prob*=(nyes/nsims)
        else:
            if nno < 4:
                motorno = (nno/nsims)/(params['simmaxrt']*1000)*(params['motor'])/precision
            else:
                hsmooth = (nno*(3)/4)**(-1/5)/2
                nort = sims['rt'][no]
                try:
                    nodist = sps.gaussian_kde(nort,hsmooth)
                    motorno = nodist.integrate_box_1d(params['simmaxrt']-params['motor'], params['simmaxrt'])
                    if motorno > 1:
                        motorno=1
                    elif motorno <1:
                        motorno = 0
                except:
                    if np.logical_and(np.less(params['simmaxrt']-params['motor'],np.unique(nort)),np.greater(np.unique(nort),params['simmaxrt'])):
                        motorno = 1
                    else:
                        motorno = 0
                motorno *= (nno/nsims)
            if nyes < 4:
                motoryes = (nyes/nsims)/(params['simmaxrt']*1000)*(params['motor'])/precision
            else:
                hsmooth = (nyes*(3)/4)**(-1/5)/2
                yesrt = sims['rt'][yes] 
                try:
                    yesdist = sps.gaussian_kde(yesrt,hsmooth)
                    motoryes =  yesdist.integrate_box_1d(params['simmaxrt']-params['motor'], params['simmaxrt'])
                    if motoryes > 1:
                        motoryes=1
                    elif motoryes <1:
                        motoryes = 0
                except:
                    if np.logical_and(np.less(params['simmaxrt']-params['motor'],np.unique(yesrt)),np.greater(np.unique(yesrt),params['simmaxrt'])):
                        motoryes = 1
                    else:
                        motoryes = 0
                motoryes *= (nyes/nsims)
            prob = motoryes + motorno + nfail/nsims
            
#        elif kde == 'sklearn':
#            fpts = np.linspace(finish[i]-params['motor'], params['simmaxrt'],100)
#            if choice[i]==0:
#                if nno < 2:
#                    prob = 0
#                else:
#                    if nno < 20:
#                        cv = nno
#                    else:
#                        cv = 20
#                    grid = GridSearchCV(KernelDensity(),
#                        {'bandwidth': np.linspace(0.001, 0.20, 30)},
#                        cv=cv) # 20-fold cross-validation
#                    grid.fit(nort[:, None])
#                    bw = grid.best_params_['bandwidth']
#                    kde_skl = KernelDensity(bandwidth=bw)
#                    kde_skl.fit(nort[:, np.newaxis])    
#                    prob = np.exp(kde_skl.score_samples(finish[i]-params['motor']))
#                    prob *= precision*(nno/nsims)
#            elif choice[i]==1:
#                if nyes < 2:
#                    prob = 0
#                else:
#                    if nyes < 20:
#                        cv = nyes
#                    else:
#                        cv = 20
#                    grid = GridSearchCV(KernelDensity(),
#                                        {'bandwidth': np.linspace(0.001, 0.20, 30)},
#                                        cv=cv) # 20-fold cross-validation
#                    grid.fit(yesrt[:, None])
#                    bw = grid.best_params_['bandwidth']
#                    kde_skl = KernelDensity(bandwidth=bw)
#                    kde_skl.fit(yesrt[:, np.newaxis])    
#                    prob = np.exp(kde_skl.score_samples(finish[i]-params['motor']))
#                    prob *= precision*(nyes/nsims)
#            else:
#                if nno < 2:
#                    motorno = 0
#                else:
#                    if nno < 20:
#                        cv = nno
#                    else:
#                        cv = 20
#                    grid = GridSearchCV(KernelDensity(),
#                        {'bandwidth': np.linspace(0.001, 0.20, 30)},
#                        cv=cv) # 20-fold cross-validation
#                    grid.fit(nort[:, None])
#                    bw = grid.best_params_['bandwidth']
#                    nkde_skl = KernelDensity(bandwidth=bw)
#                    nkde_skl.fit(nort[:, np.newaxis])   
#                    motorno = sp.integrate.trapz(np.exp(nkde_skl.scores_samples(fpts)),fpts)
#                if nyes < 2:
#                    motoryes = 0
#                else:
#                    if nyes < 20:
#                        cv = nyes
#                    else:
#                        cv = 20
#                    grid = GridSearchCV(KernelDensity(),
#                        {'bandwidth': np.linspace(0.001, 0.20, 30)},
#                        cv=cv) # 20-fold cross-validation
#                    grid.fit(yesrt[:, None])
#                    bw = grid.best_params_['bandwidth']
#                    ykde_skl = KernelDensity(bandwidth=bw)
#                    ykde_skl.fit(yesrt[:, np.newaxis])    
#                    motoryes = sp.integrate.trapz(np.exp(ykde_skl.scores_samples(fpts)),fpts)
#                prob = motoryes  + motorno + nfail/nsims
        NLLDataProb[i] = -1* np.log(prob + sys.float_info.min) 
    out = sum(NLLDataProb)
    return (out)

def getNLLs(splitparams, Sims, timelimit, tempselfamt,tempotheramt, tempfinish, tempfix, tempchoice):
    simParams = splitparams
    modbias = np.zeros(len(tempfinish), dtype = float)
    modbias[np.where(np.greater(tempselfamt,  tempotheramt))] = simParams[5] - simParams[7]
    modbias[np.where(np.less(tempselfamt, tempotheramt))] = simParams[5] + simParams[7]
    params2 = {'self' : simParams[0], 'other' : simParams[1],'fair' : simParams[2],\
              'bound' : simParams[3],'collapse' : simParams[4],\
              'theta': simParams[8],'percept' : simParams[9], 'motor': simParams[10]}
    
    Output1 = NLLSimTest(params2, Sims, tempselfamt, tempotheramt, tempfix, modbias, timelimit, tempfinish, tempchoice)
    
    Output = [Output1,int(simParams[11])]
    return(Output)
        

subject = int(sys.argv[1])
substr = str(subject)
path1 = '/scratch/c/chutcher/teohyi2'
path = '/TPEAltruism/SubjectData/'

direct = path1 + '/TPEAltruism/Analysis/EADDM1/' + substr 

if not os.path.exists(direct):
    os.makedirs(direct)
    
temp = input.loadmat(path1 + path + substr + '/Data.' + substr + '.wfix.choice.mat',\
                     struct_as_record = False)
x = temp['Data']

selfcandidate = np.arange(-0.01, 0.07, 0.01, dtype = float)
othercandidate = np.arange(-0.01, 0.07, 0.01, dtype = float)
faircandidate = np.arange(-0.01, 0.05, 0.01, dtype = float)
boundcandidate =  np.unique(np.arange(0.04, 0.44, 0.04, dtype = float))
collapsecandidate = np.unique(np.arange(0, 0.0024, 0.0003, dtype = float))
stbiascandidate = np.unique(np.append(np.arange(-0.3, 0.4, 0.3, dtype = float),np.arange(-0.1, 0.15, .05, dtype = float)))
ndtcandidate =  np.asarray([0])
genbiascandidate = np.asarray([0])
thetacandidate = np.asarray([0.3])
perceptcandidate = np.asarray([0.08])
motorcandidate = np.asarray([0.08])

combovars = np.asarray([selfcandidate, othercandidate, faircandidate,boundcandidate,collapsecandidate, stbiascandidate, ndtcandidate, genbiascandidate, thetacandidate, perceptcandidate,motorcandidate])
ncombo = len(selfcandidate)*len(othercandidate)*len(faircandidate)*len(boundcandidate)*len(collapsecandidate)*len(stbiascandidate) \
    *len(ndtcandidate)*len(genbiascandidate)*len(thetacandidate)*len(perceptcandidate)*len(motorcandidate)

paramset = np.zeros([ncombo, len(combovars)+1], dtype = float)

for i in range(len(combovars)):
    times = ncombo/len(combovars[i])
    paramset[:,i] = np.tile(combovars[i], np.int(times))
    paramset = np.round(paramset[paramset[:,i].argsort(kind = 'mergesort')],5)
    
    
    
paramset[:,len(combovars)] = np.arange(ncombo)   
paramset = tuple(paramset)


finish = np.round(x[0,0].ChoiceRT[0].astype(float),3)
finish = tuple(finish)
choice = x[0,0].Resp[0]
choice[np.where(np.asarray(choice == 'NULL'))] = np.asarray([[np.nan]])
choice[np.where(np.equal(choice,1))] = 0
choice[np.where(np.equal(choice,2))] = 1
choice = tuple(choice.astype(float))
SelfProposal = tuple(x[0,0].SelfProposal[0].astype(int))
OtherProposal = tuple(x[0,0].OtherProposal[0].astype(int))
TimeLimit = tuple(x[0,0].TimeLimit[0].astype(float))
Fixations = tuple(x[0,0].Fix[0])

cond = {0:'long', 1:'short'}
maxtime = {0: 10, 1: 1.5}
nsimspfit = 1000
chunky = np.ceil(ncombo/(10*80))

for t in range(1):
    selected = np.where(np.equal(TimeLimit,maxtime[t]))
    tempchoice = tuple(np.asarray(choice)[selected])
    tempfinish = tuple(np.asarray(finish)[selected])
    tempselfamt = tuple(np.asarray(SelfProposal)[selected])
    tempotheramt = tuple(np.asarray(OtherProposal)[selected])
    tempfix = tuple(np.asarray(Fixations)[selected])
    
    #@jit
    def iterate1(splitparams):
        ss = time.perf_counter()
        Output = getNLLs(splitparams, nsimspfit, maxtime[t],tempselfamt,tempotheramt,tempfinish,tempfix,tempchoice)
        ee = time.perf_counter() 
        timeee = ee-ss
        outout = np.hstack([Output, [timeee]])
        print(outout)
        return(outout)
    
    ss = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor(max_workers = 80) as executor:
        future = executor.map(iterate1, paramset,chunksize = int(chunky))#int(ncombo/100))
    ee = time.perf_counter()     
    
    simnlldata = tuple(future)
    savefilename = path1 + '/TPEAltruism/' + 'Analysis/EADDM1/' + substr + '/simnll_'+substr+'_'+cond[t]
    with open(savefilename, 'wb') as f:
        pickle.dump(simnlldata, f)
