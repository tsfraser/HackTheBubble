#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 09:24:01 2019
N body code but with CM calculations
@author: tristanfraser
"""

def CM(r,m,i):
    #given the index of the oribting obj
    # take all other masses, and their x,y,z
    # find CM, return the necessary coords for Nbody integration
    N = np.size(m)
    mex = np.zeros(N-1)
    for j in range(N):
        
        if j != i :
            mex[j] = m[j]
            rex[0,j] = r[j]
    
    r= r
    cm = np.sum(r*m)
    
    return(rN,cm)