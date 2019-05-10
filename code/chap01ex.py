"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2


def main(script):
    """Tests the functions in this module.

    script: string script name
    """

    df = ReadFromResp()
    pregnum = df.pregnum
    print(pregnum.value_counts().sort_index())

    print('Validating pregnum from resp aginst preg')
    print(ValidatePregnum(df))


    print('%s: All tests passed.' % script)


def ReadFromResp(dct_file = '2002FemResp.dct',
                dat_file = '2002FemResp.dat.gz'):
            dct = thinkstats2.ReadStataDct(dct_file)
            df = dct.ReadFixedWidth(dat_file, compression = 'gzip')
            return df


def ValidatePregnum(resp):

    df = nsfg.ReadFemPreg()
    preg_map = nsfg.MakePregMap(df)


    for i, pregnum in resp.pregnum.items():
        caseid = resp.caseid[i]
        indcies = preg_map[caseid]

        if len(indcies) != pregnum:
            print('case: '+ caseid+' has invalid number of preg')
            return False
    return True


if __name__ == '__main__':
    main(*sys.argv)
