
#http://chainladder-python.readthedocs.io/en/master/quickstart.html
import chainladder as chainl
import numpy as numpi
import pyliferisk as pylife
import matplotlib.pyplot as plt
##%matplotlib inline
###############vars####################
s = "This is a test"


##############objects###############
RAA = chainl.load_dataset('RAA')
RAA_TriangleObj = chainl.Triangle(RAA)
RAA_ChainL = chainl.Chainladder(RAA_TriangleObj)
#############calls##############
RAA.round(0)

############ sys out #####################

def main():
    # my code here
    print(s + " 1")
    print(RAA.round(0))
    print("\n\n\n\n")
    print(s + " 2")
    plt.plot(RAA_TriangleObj.cum_to_incr())
    plt.ylabel("Aggregate Claim")
    plt.xlabel("Year")
    plt.show()
    print("\n\n\n\n")
    print(s + " 3")
    print(RAA_TriangleObj.data_as_table().head())
    print("\n\n\n\n")
    print(s + " 4")
    print(RAA_ChainL.age_to_age())


if __name__ == "__main__":

    main()



#s = "hello world"
#str(s)
#print(s)
