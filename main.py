'''
Created on Jun 9, 2014

@author: nectarios
'''
from WaveletTree import WaveletTree

def main():
    s = 'BANANA$'
    wavelet_tree = WaveletTree(s)
    print(s + '.ACCESS(3)', wavelet_tree.access(3))
    print(s + '.RANK(N, 4):', wavelet_tree.rank('N', 4))
    print(s + '.RANK(A, 3):', wavelet_tree.rank('A', 3))
    print(s + '.SELECT(A, 2):', wavelet_tree.select('A', 2))
    print(s + '.SELECT(N, 1):', wavelet_tree.select('N', 1))
    print(s + '.SELECT(B, 0):', wavelet_tree.select('B', 0))
    
if __name__ == '__main__':
    main()
