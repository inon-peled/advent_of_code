'''
Solution idea:
This is a Voronoi diagram in L1, not Euclidean distance. So:
1. Form a bounding box.
2. Do multi-source BFS from the data points, namely:
2.1. Initialize the FIFO with all the data points.
2.2. Continue BFS:
2.2.1. Keep track of source root and min. distance from it.
2.2.2. When reaching an already closed point from a different source with the same min. distance,
       change the root of p to '.'.
3. A data point has an infinitely large Voronoi cell if-and-only-if it lies on an edge of the bounding box.
'''

DATA = [(162, 168), (86, 253), (288, 359), (290, 219), (145, 343), (41, 301), (91, 214), (166, 260), (349, 353),
        (178, 50), (56, 79), (273, 104), (173, 118), (165, 47), (284, 235), (153, 69), (116, 153), (276, 325),
        (170, 58), (211, 328), (238, 346), (333, 299), (119, 328), (173, 289), (44, 223), (241, 161), (225, 159),
        (266, 209), (293, 95), (89, 86), (281, 289), (50, 253), (75, 347), (298, 241), (88, 158), (40, 338), (291, 156),
        (330, 88), (349, 289), (165, 102), (232, 131), (338, 191), (178, 335), (318, 107), (335, 339), (153, 156),
        (88, 119), (163, 268), (159, 183), (162, 134)]
TEST = [(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9)]

