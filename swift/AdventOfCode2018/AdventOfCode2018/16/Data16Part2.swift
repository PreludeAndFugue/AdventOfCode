//
//  Data16Part2.swift
//  AdventOfCode2018
//
//  Created by gary on 27/12/2018.
//  Copyright © 2018 Gary Kerr. All rights reserved.
//

import Foundation

let data16Part2 = """
7 3 2 0
7 2 1 1
7 1 0 3
8 1 0 1
14 1 2 1
1 2 1 2
7 3 3 1
7 2 0 0
14 3 0 3
13 3 2 3
0 1 0 1
14 1 1 1
1 1 2 2
7 2 2 1
7 3 1 0
7 1 0 3
1 3 3 3
14 3 3 3
1 2 3 2
3 2 1 0
14 3 0 3
13 3 0 3
7 2 3 2
14 2 0 1
13 1 0 1
6 3 2 2
14 2 2 2
1 0 2 0
7 3 1 1
7 2 2 3
14 3 0 2
13 2 0 2
7 2 1 3
14 3 3 3
1 0 3 0
7 0 0 3
14 0 0 2
13 2 3 2
14 0 0 1
13 1 1 1
10 3 2 3
14 3 2 3
1 0 3 0
3 0 1 1
7 0 1 0
7 1 1 2
7 3 1 3
9 3 2 0
14 0 1 0
1 1 0 1
3 1 0 3
14 0 0 2
13 2 2 2
7 3 2 1
14 2 0 0
13 0 1 0
3 0 2 0
14 0 2 0
1 0 3 3
3 3 2 1
7 2 1 0
14 2 0 2
13 2 3 2
14 0 0 3
13 3 2 3
8 0 2 2
14 2 2 2
1 1 2 1
14 0 0 2
13 2 0 2
14 1 0 3
13 3 1 3
15 3 0 2
14 2 1 2
1 2 1 1
3 1 0 0
14 2 0 1
13 1 3 1
7 2 1 3
7 2 0 2
5 2 3 3
14 3 2 3
14 3 3 3
1 0 3 0
3 0 0 3
7 1 1 2
7 2 1 1
7 3 0 0
8 1 0 1
14 1 2 1
14 1 3 1
1 3 1 3
3 3 0 1
7 0 0 3
14 1 0 0
13 0 0 0
7 2 2 2
7 3 2 0
14 0 2 0
1 1 0 1
7 1 1 2
14 2 0 3
13 3 2 3
7 3 3 0
9 0 2 2
14 2 1 2
1 2 1 1
3 1 2 2
14 1 0 1
13 1 0 1
7 1 2 0
7 3 1 3
13 0 1 1
14 1 1 1
1 2 1 2
3 2 0 1
7 2 0 3
7 2 3 2
7 2 3 0
5 0 3 2
14 2 2 2
1 1 2 1
3 1 1 0
14 0 0 1
13 1 2 1
14 0 0 2
13 2 3 2
14 2 0 3
13 3 3 3
8 1 2 1
14 1 1 1
1 1 0 0
3 0 0 2
7 3 3 0
7 2 3 3
7 0 0 1
0 0 3 3
14 3 2 3
1 3 2 2
3 2 0 3
14 3 0 2
13 2 2 2
7 1 1 1
12 2 0 0
14 0 2 0
1 0 3 3
3 3 3 1
7 0 2 3
7 3 0 2
7 2 3 0
8 0 2 3
14 3 3 3
1 3 1 1
7 3 3 3
2 0 2 2
14 2 2 2
14 2 1 2
1 2 1 1
3 1 3 3
7 1 0 0
7 3 2 1
7 2 3 2
3 0 2 1
14 1 1 1
14 1 3 1
1 1 3 3
3 3 1 0
14 1 0 1
13 1 0 1
7 3 2 2
7 0 1 3
7 2 1 1
14 1 1 1
1 0 1 0
3 0 0 1
7 2 0 0
7 2 2 2
7 2 2 3
11 0 3 2
14 2 3 2
1 1 2 1
14 1 0 2
13 2 3 2
7 0 3 3
2 0 2 0
14 0 2 0
14 0 3 0
1 1 0 1
3 1 2 0
7 2 3 2
7 3 3 1
7 3 2 3
12 2 1 1
14 1 3 1
1 1 0 0
7 0 0 1
7 0 2 2
7 2 0 3
10 2 3 2
14 2 3 2
1 2 0 0
3 0 3 1
14 3 0 0
13 0 0 0
7 2 2 2
5 2 3 3
14 3 1 3
1 3 1 1
3 1 2 2
7 1 0 3
14 0 0 1
13 1 2 1
7 2 1 0
4 0 3 1
14 1 2 1
1 2 1 2
3 2 3 0
7 3 1 3
7 3 3 1
7 1 0 2
9 3 2 1
14 1 3 1
14 1 1 1
1 0 1 0
3 0 0 2
7 0 3 3
14 2 0 1
13 1 3 1
7 2 2 0
12 0 1 0
14 0 1 0
1 0 2 2
14 0 0 0
13 0 2 0
5 0 3 0
14 0 2 0
1 2 0 2
3 2 2 0
7 2 1 3
7 2 1 2
12 2 1 1
14 1 2 1
1 0 1 0
3 0 2 2
7 0 3 1
7 2 3 0
11 0 3 0
14 0 3 0
14 0 2 0
1 0 2 2
3 2 3 1
7 1 0 0
7 3 2 2
7 3 3 3
14 0 2 2
14 2 2 2
1 2 1 1
3 1 3 2
7 1 0 3
7 3 1 1
7 2 0 0
15 3 0 3
14 3 3 3
1 3 2 2
3 2 3 1
7 1 0 3
7 1 0 0
14 1 0 2
13 2 2 2
1 0 3 3
14 3 2 3
14 3 2 3
1 3 1 1
3 1 2 3
14 0 0 2
13 2 3 2
7 0 3 1
13 0 1 1
14 1 2 1
1 1 3 3
3 3 2 2
14 3 0 3
13 3 1 3
7 2 0 1
7 3 3 0
1 3 3 1
14 1 3 1
1 1 2 2
3 2 1 1
7 2 2 0
7 0 3 3
7 2 1 2
6 3 2 3
14 3 1 3
1 3 1 1
3 1 1 3
7 1 1 0
7 1 0 1
7 3 3 2
14 1 2 2
14 2 3 2
14 2 1 2
1 2 3 3
7 3 3 1
7 2 2 2
3 0 2 2
14 2 3 2
1 2 3 3
3 3 2 1
7 0 3 3
7 2 2 2
7 3 2 0
12 2 0 3
14 3 3 3
1 1 3 1
7 0 3 3
7 3 0 2
14 1 0 0
13 0 2 0
2 0 2 2
14 2 2 2
1 1 2 1
7 3 1 3
7 3 0 2
0 3 0 3
14 3 1 3
1 3 1 1
14 2 0 3
13 3 1 3
4 0 3 3
14 3 2 3
14 3 1 3
1 1 3 1
3 1 1 0
14 1 0 2
13 2 2 2
7 1 2 1
7 0 2 3
6 3 2 3
14 3 1 3
1 3 0 0
3 0 2 3
14 3 0 1
13 1 0 1
7 1 3 0
3 0 2 0
14 0 2 0
14 0 2 0
1 0 3 3
14 0 0 0
13 0 1 0
7 0 0 2
14 0 2 2
14 2 1 2
1 3 2 3
7 2 2 2
3 0 2 2
14 2 3 2
1 3 2 3
3 3 2 2
7 2 1 0
7 2 0 3
11 0 3 3
14 3 2 3
1 3 2 2
3 2 0 0
7 2 3 1
7 0 2 3
7 2 1 2
6 3 2 3
14 3 3 3
14 3 1 3
1 0 3 0
7 0 3 3
6 3 2 2
14 2 1 2
1 0 2 0
14 0 0 3
13 3 1 3
7 1 0 1
7 0 2 2
14 1 2 2
14 2 2 2
14 2 2 2
1 0 2 0
3 0 1 3
7 2 1 0
7 3 3 2
14 1 2 0
14 0 2 0
1 3 0 3
3 3 0 0
14 0 0 3
13 3 2 3
7 0 2 2
10 2 3 2
14 2 1 2
1 2 0 0
3 0 1 1
14 0 0 2
13 2 3 2
14 1 0 3
13 3 0 3
7 3 2 0
7 2 0 0
14 0 1 0
1 0 1 1
7 0 1 2
7 0 0 0
7 2 1 3
10 2 3 3
14 3 2 3
1 1 3 1
7 2 0 3
10 2 3 0
14 0 1 0
1 1 0 1
7 2 3 2
7 0 2 3
7 3 1 0
8 2 0 0
14 0 3 0
1 1 0 1
7 3 0 3
14 0 0 2
13 2 0 2
7 1 3 0
9 3 2 3
14 3 1 3
1 1 3 1
7 0 3 3
7 3 2 2
7 0 1 0
10 3 2 3
14 3 2 3
1 1 3 1
3 1 3 3
7 3 3 0
7 1 3 1
7 0 2 2
2 2 0 2
14 2 1 2
1 3 2 3
3 3 1 1
7 2 3 2
7 2 0 0
7 0 3 3
6 3 2 2
14 2 2 2
1 2 1 1
3 1 3 2
7 1 2 1
7 2 3 3
15 1 0 3
14 3 2 3
14 3 3 3
1 2 3 2
7 1 0 3
7 2 3 1
4 0 3 0
14 0 2 0
1 0 2 2
3 2 2 0
14 2 0 2
13 2 1 2
7 0 3 3
5 1 3 3
14 3 1 3
1 0 3 0
3 0 2 1
7 2 1 0
7 1 3 3
15 3 0 3
14 3 3 3
14 3 1 3
1 1 3 1
3 1 3 3
7 1 2 1
7 0 2 2
7 1 1 0
14 0 2 1
14 1 2 1
1 1 3 3
3 3 1 2
7 3 0 1
7 2 0 0
14 2 0 3
13 3 1 3
13 3 1 3
14 3 2 3
14 3 3 3
1 3 2 2
3 2 2 0
7 0 0 2
7 3 0 3
9 3 2 1
14 1 2 1
14 1 3 1
1 0 1 0
7 0 1 3
7 3 3 1
7 2 0 2
12 2 1 3
14 3 1 3
14 3 1 3
1 3 0 0
7 1 2 3
14 0 0 2
13 2 3 2
1 3 3 3
14 3 1 3
1 3 0 0
3 0 0 2
7 2 2 3
7 2 1 0
11 0 3 0
14 0 3 0
1 0 2 2
3 2 3 3
7 3 1 2
7 1 3 0
13 0 1 2
14 2 2 2
1 3 2 3
7 1 0 1
7 2 1 0
7 1 3 2
15 1 0 1
14 1 1 1
14 1 1 1
1 1 3 3
3 3 3 0
7 3 1 1
7 3 1 3
14 2 0 2
13 2 0 2
9 3 2 3
14 3 2 3
14 3 3 3
1 3 0 0
3 0 1 1
7 2 1 0
7 1 2 2
7 2 1 3
11 0 3 2
14 2 2 2
14 2 1 2
1 1 2 1
7 2 0 2
7 0 2 0
7 1 0 3
1 3 3 3
14 3 1 3
1 1 3 1
3 1 0 0
14 2 0 1
13 1 3 1
7 0 2 2
7 1 3 3
1 3 3 2
14 2 1 2
1 0 2 0
3 0 3 2
7 0 3 0
7 0 3 3
7 2 2 1
7 3 0 3
14 3 1 3
14 3 3 3
1 2 3 2
3 2 1 1
7 2 2 2
7 2 0 3
7 3 0 0
12 2 0 0
14 0 3 0
14 0 1 0
1 0 1 1
7 1 3 2
7 2 0 0
7 1 3 3
4 0 3 3
14 3 1 3
1 3 1 1
14 2 0 3
13 3 0 3
7 3 1 0
14 0 0 2
13 2 2 2
6 3 2 3
14 3 2 3
1 3 1 1
3 1 2 2
7 0 0 1
14 3 0 3
13 3 1 3
7 2 2 0
15 3 0 0
14 0 3 0
1 2 0 2
3 2 2 1
7 0 0 2
14 3 0 0
13 0 3 0
9 0 2 0
14 0 2 0
1 0 1 1
7 2 2 0
7 0 3 3
7 3 1 2
8 0 2 2
14 2 1 2
14 2 3 2
1 2 1 1
3 1 1 0
14 1 0 1
13 1 3 1
7 2 0 2
6 3 2 2
14 2 3 2
1 0 2 0
3 0 1 1
7 1 1 3
7 2 0 0
7 3 1 2
7 2 3 0
14 0 2 0
1 0 1 1
7 0 0 3
14 0 0 0
13 0 1 0
10 3 2 2
14 2 1 2
1 2 1 1
3 1 0 0
14 3 0 2
13 2 0 2
7 0 2 1
7 2 2 3
10 2 3 1
14 1 1 1
1 0 1 0
3 0 1 1
14 2 0 0
13 0 2 0
7 3 1 2
7 1 2 3
8 0 2 0
14 0 3 0
1 1 0 1
3 1 2 2
7 2 3 1
7 2 1 3
7 2 3 0
11 0 3 1
14 1 1 1
1 2 1 2
3 2 0 1
14 2 0 2
13 2 2 2
14 3 0 0
13 0 3 0
7 0 0 3
6 3 2 2
14 2 1 2
1 1 2 1
7 0 2 0
7 2 1 2
7 3 0 0
14 0 3 0
1 0 1 1
3 1 0 3
7 3 1 0
7 3 3 2
14 0 0 1
13 1 2 1
8 1 0 0
14 0 3 0
1 3 0 3
3 3 2 1
7 0 2 0
7 0 2 3
7 2 0 2
6 3 2 2
14 2 2 2
14 2 3 2
1 2 1 1
3 1 1 0
7 3 3 1
7 1 3 3
7 0 1 2
9 1 2 1
14 1 2 1
1 0 1 0
3 0 0 3
7 2 0 1
7 3 2 0
9 0 2 2
14 2 3 2
1 2 3 3
14 1 0 2
13 2 2 2
7 1 2 1
12 2 0 1
14 1 3 1
14 1 1 1
1 1 3 3
3 3 1 2
7 2 0 0
7 1 2 3
7 1 3 1
4 0 3 1
14 1 2 1
14 1 3 1
1 1 2 2
7 3 3 1
7 2 2 3
12 0 1 0
14 0 3 0
1 0 2 2
3 2 2 1
7 3 1 2
7 3 2 0
0 0 3 2
14 2 3 2
1 1 2 1
3 1 0 0
7 2 1 2
7 1 2 1
15 1 3 2
14 2 1 2
14 2 2 2
1 2 0 0
3 0 2 1
7 1 0 3
7 1 2 2
7 1 1 0
1 3 3 2
14 2 3 2
14 2 2 2
1 2 1 1
3 1 0 2
7 0 1 0
7 2 3 1
1 3 3 0
14 0 1 0
1 0 2 2
3 2 0 0
7 1 1 1
7 2 0 3
7 3 3 2
15 1 3 3
14 3 3 3
1 0 3 0
7 2 0 2
7 0 1 3
7 0 3 1
6 3 2 1
14 1 2 1
14 1 1 1
1 0 1 0
3 0 2 3
7 3 1 2
7 3 3 0
7 3 2 1
7 2 0 2
14 2 1 2
1 2 3 3
7 3 2 2
7 1 2 1
9 0 2 0
14 0 2 0
14 0 3 0
1 3 0 3
3 3 0 1
7 1 3 3
14 1 0 0
13 0 3 0
7 2 3 2
12 2 0 3
14 3 3 3
1 1 3 1
3 1 2 0
7 3 1 2
7 3 0 1
7 1 1 3
14 3 2 3
14 3 2 3
14 3 1 3
1 0 3 0
3 0 3 1
7 1 3 3
7 0 2 2
7 2 3 0
4 0 3 2
14 2 2 2
1 2 1 1
7 1 2 0
7 2 3 3
7 0 0 2
10 2 3 3
14 3 1 3
1 3 1 1
7 3 1 3
7 3 2 0
2 2 0 2
14 2 1 2
14 2 1 2
1 2 1 1
14 2 0 0
13 0 1 0
7 3 0 2
7 0 2 3
7 2 0 0
14 0 2 0
1 0 1 1
3 1 0 3
14 1 0 0
13 0 3 0
7 2 0 2
7 2 2 1
8 2 0 1
14 1 3 1
14 1 3 1
1 1 3 3
3 3 2 2
7 2 3 0
7 2 1 3
7 3 3 1
0 1 0 3
14 3 2 3
14 3 1 3
1 3 2 2
3 2 3 1
7 0 0 2
7 3 0 0
7 2 2 3
9 0 2 0
14 0 1 0
1 0 1 1
7 2 3 2
7 0 1 3
7 0 2 0
5 2 3 2
14 2 2 2
1 1 2 1
3 1 1 2
7 2 0 1
5 1 3 1
14 1 1 1
1 2 1 2
3 2 3 1
7 3 0 3
7 0 0 2
14 2 0 0
13 0 1 0
14 0 2 0
14 0 3 0
1 1 0 1
3 1 1 3
7 2 2 1
7 3 2 0
8 1 0 1
14 1 3 1
1 1 3 3
3 3 2 1
14 2 0 3
13 3 0 3
14 1 0 0
13 0 0 0
14 0 0 2
13 2 3 2
10 3 2 2
14 2 1 2
14 2 2 2
1 1 2 1
3 1 3 2
7 2 3 0
14 2 0 3
13 3 1 3
7 0 1 1
1 3 3 1
14 1 3 1
1 1 2 2
3 2 2 1
14 0 0 2
13 2 2 2
7 1 1 0
7 0 0 3
3 0 2 0
14 0 3 0
1 0 1 1
3 1 1 2
7 2 2 3
7 2 0 0
7 3 0 1
5 0 3 0
14 0 3 0
1 2 0 2
7 2 3 0
14 1 0 3
13 3 0 3
14 1 0 1
13 1 1 1
15 1 0 3
14 3 1 3
1 3 2 2
3 2 2 1
7 2 1 2
14 0 0 3
13 3 1 3
7 0 1 0
7 3 0 0
14 0 2 0
1 0 1 1
3 1 1 2
7 2 1 3
7 3 0 1
7 2 3 0
11 0 3 3
14 3 3 3
1 2 3 2
3 2 1 1
7 2 2 3
7 0 1 2
14 1 0 0
13 0 0 0
10 2 3 2
14 2 1 2
14 2 3 2
1 2 1 1
7 3 3 0
7 3 0 3
7 3 2 2
9 3 2 2
14 2 1 2
1 2 1 1
3 1 2 2
14 0 0 1
13 1 0 1
7 0 0 3
7 1 1 0
13 0 1 0
14 0 1 0
14 0 2 0
1 2 0 2
14 2 0 0
13 0 2 0
7 2 3 3
11 0 3 1
14 1 2 1
1 1 2 2
3 2 1 1
7 3 3 3
7 3 3 2
2 0 2 3
14 3 1 3
14 3 3 3
1 1 3 1
3 1 0 3
7 1 1 2
7 3 0 1
12 0 1 1
14 1 2 1
1 1 3 3
3 3 3 1
14 3 0 2
13 2 0 2
7 2 2 3
11 0 3 3
14 3 2 3
1 1 3 1
3 1 1 2
7 3 3 1
7 1 2 3
4 0 3 3
14 3 3 3
14 3 2 3
1 2 3 2
3 2 0 0
7 0 2 2
14 2 0 3
13 3 1 3
1 3 3 1
14 1 2 1
14 1 2 1
1 1 0 0
3 0 2 2
7 2 1 0
7 1 0 1
15 1 0 1
14 1 2 1
14 1 2 1
1 2 1 2
3 2 2 1
7 3 3 3
7 3 2 2
8 0 2 0
14 0 3 0
1 0 1 1
7 0 2 2
7 2 1 3
14 1 0 0
13 0 3 0
2 2 0 0
14 0 3 0
14 0 3 0
1 0 1 1
3 1 0 2
7 2 2 0
7 2 3 1
11 0 3 0
14 0 3 0
14 0 1 0
1 0 2 2
3 2 2 3
7 2 2 0
7 1 3 2
14 3 0 1
13 1 3 1
12 0 1 0
14 0 2 0
14 0 3 0
1 3 0 3
3 3 2 0
7 2 2 2
7 0 1 3
6 3 2 3
14 3 1 3
1 3 0 0
"""