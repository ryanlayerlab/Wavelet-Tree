Wavelet Tree
========

### References 
Reference for the ([Wavelet Tree](http://alexbowe.com/wavelet-trees/)).

Reference for the ([Node-RRR](http://alexbowe.com/wavelet-trees/)) of the Wavelet Tree. 

### Algorithm

###### Rank query
`Reporting the number of occurrences of a given character in a given prefix of the text.`
###### Select query
`Reporting the position of a given occurrence of a given character.`
###### Track symbol
`Reporting the character of a given position.`

### Code

```python
from WaveletTree import WaveletTree
s = 'BANANA$'
wavelet_tree = WaveletTree(s)
print(s + '.ACCESS(3)', wavelet_tree.access(3))
print(s + '.RANK(N, 4):', wavelet_tree.rank('N', 4))
print(s + '.RANK(A, 3):', wavelet_tree.rank('A', 3))
print(s + '.SELECT(A, 2):', wavelet_tree.select('A', 2))
print(s + '.SELECT(N, 1):', wavelet_tree.select('N', 1))
print(s + '.SELECT(B, 0):', wavelet_tree.select('B', 0))
```
