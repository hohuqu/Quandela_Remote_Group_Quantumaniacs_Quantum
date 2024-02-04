import numpy as np
import math
import perceval as pcvl

def get_CCZ():
    p = pcvl.Processor("SLOS", 10)

    p.add((0,1), pcvl.BS.H(pcvl.BS.r_to_theta(1/3)))
    # p.set_postselection(pcvl.PostSelect("[0] == 1"))
    p.add_herald(0, expected=1)

    p.add((3,4), pcvl.BS.H(pcvl.BS.r_to_theta(3/4)))

    p.add((2,3), pcvl.BS.H(pcvl.BS.r_to_theta(1/3)))

    p.add((3,4), pcvl.BS.H(pcvl.BS.r_to_theta(1/2)))

    p.add((4,5), pcvl.BS.H(pcvl.BS.r_to_theta(1/3)))

    p.add((3,4), pcvl.BS.H(pcvl.BS.r_to_theta(1/4)))
    p.set_postselection(pcvl.PostSelect("[4] == 1"))
    # p.add_herald(4, expected=1)

    p.add((6,7), pcvl.BS.H(pcvl.BS.r_to_theta(1/3)))
    # p.set_postselection(pcvl.PostSelect("[7] == 1"))
    p.add_herald(7, expected=1)

    p.add((8,9), pcvl.BS.H(pcvl.BS.r_to_theta(1/8)))
    # p.set_postselection(pcvl.PostSelect("[9] == 1"))
    p.add_herald(9, expected=1)

    p.set_postselection(pcvl.PostSelect("[1,2]==1 & [3, 8]==1 & [5,6]==1"))
    return p
