#!python3

'''Data for day 8.'''

from collections import defaultdict
import operator

INPUT = '''j inc -19 if jhb >= 10
es inc -432 if gbu <= -5
es inc 278 if ib > -9
es inc -835 if ib >= -6
q dec 420 if buw == -2
ytr dec -258 if xzn < 9
okl inc -49 if j > -10
s inc 156 if fzu >= -1
eb inc -304 if gbu < 2
ae inc 220 if zd >= -5
gbu inc -659 if xzn < 5
wf dec -590 if cpq <= -3
xzn inc 690 if fij <= 5
q dec 414 if eb > -311
ae dec 841 if fzu != -3
jhb dec 632 if r <= 2
fzu inc 383 if s > 159
eb inc -915 if wf != 0
ytr inc 374 if cpq <= 1
on inc 974 if q < -404
es dec -729 if iuz <= -4
xzn inc -502 if zd > -9
on dec -345 if xzn > 186
xzn dec -775 if zd == 0
jhb inc 980 if es < -551
iuz dec 226 if buw > -1
xzn dec -606 if es != -555
fij inc 162 if s > 150
ytr dec -884 if ytr > 623
iy dec -132 if xzn < 1578
s dec 435 if yvh > 7
buw inc -379 if okl >= -52
zd dec 18 if ae != -622
xzn inc 801 if q < -407
xzn inc -688 if fij >= 171
iy inc 291 if ytr > 1522
r dec -438 if iuz != -226
gbu inc 402 if rtu < -4
iy inc 541 if laz > -8
gbu dec -843 if q >= -416
ytr inc -953 if ib > 3
iy dec -487 if zd >= -21
j inc -444 if fzu != 0
fij inc 254 if ytr >= 1511
ae inc -849 if fzu <= 6
laz dec 831 if r != 0
s inc -700 if laz == 0
buw inc -211 if q == -414
q inc 333 if yvh == 0
on inc 223 if q >= -86
iuz inc -632 if q < -72
yvh inc 103 if jhb >= 346
ae inc -493 if iuz >= -863
r inc -245 if yvh > 94
gbu dec -417 if ib <= 8
su dec 911 if s == -536
es dec -812 if jhb != 357
jhb dec 265 if q <= -80
s inc 964 if j < 8
buw dec 184 if buw == -590
buw inc 940 if buw >= -774
buw inc -739 if eb >= -304
s dec 219 if fij >= 416
su inc 32 if h != -8
fzu inc -341 if su < 31
r inc -946 if r <= -236
on inc 469 if yvh == 103
xzn inc -213 if es == 255
r dec -35 if q > -78
xzn dec -879 if zd <= -9
jhb dec 616 if fij <= 422
laz inc -925 if s >= 196
jhb dec 121 if buw != -578
iy inc 50 if ae != -1954
rtu inc 834 if h < 1
ib inc -653 if fzu <= -8
fzu dec 736 if iy != 1210
es inc -850 if buw != -565
ae dec 457 if cpq == 0
ytr dec -283 if su == 30
h inc -398 if fij == 416
j inc 163 if xzn == 3036
ae dec 263 if rtu != 827
su dec 259 if iy != 1210
r inc 300 if s != 208
rtu inc 181 if ae <= -2684
ib dec -545 if laz < -915
zd dec -27 if okl > -56
r inc 243 if r >= -895
fzu inc -238 if iuz > -866
cpq dec 98 if su != 32
yvh dec -422 if wf <= 2
cpq inc -873 if laz == -925
cpq dec -315 if rtu > 825
es inc -899 if eb != -304
ytr dec -966 if on < 2016
jhb dec 678 if ae != -2690
h dec 316 if rtu == 834
s inc -950 if jhb >= -1338
fij inc 434 if es > -597
cpq inc -673 if zd <= 10
ytr dec -33 if ae > -2688
h inc 593 if jhb <= -1331
su inc -743 if okl <= -45
gbu inc 315 if es >= -601
h dec 919 if gbu != 916
xzn inc -972 if iuz != -860
q dec -267 if s < -740
q dec 441 if laz <= -922
r inc 511 if on <= 2012
on dec 626 if q != -260
yvh inc -338 if yvh >= 535
rtu dec -950 if rtu == 844
gbu dec -970 if ytr > 2512
fij inc 867 if q > -265
su dec 95 if su >= -719
xzn inc -487 if okl <= -46
okl inc -173 if h <= -114
laz dec -723 if su == -806
on dec 172 if q > -246
zd dec -229 if s < -744
jhb inc 90 if okl >= -213
fzu inc 572 if okl < -225
eb dec 90 if jhb == -1332
ib inc 955 if ae >= -2686
fzu dec -151 if eb <= -390
fzu dec -844 if r <= -131
buw dec -741 if s >= -751
h dec -324 if rtu != 828
s dec 86 if rtu < 842
okl dec -423 if su == -806
ytr dec -89 if okl < 202
rtu dec 487 if s > -829
ib dec 176 if zd > 234
r dec -827 if ae >= -2679
okl inc 985 if rtu == 834
buw inc -118 if gbu >= 1881
laz inc -443 if iy != 1202
iy dec -722 if iuz > -868
xzn inc -408 if ib >= 1323
on inc 509 if on == 1385
okl dec 705 if buw <= 54
h dec 918 if eb != -398
ae dec -701 if okl == 481
es inc 715 if rtu <= 827
laz dec 142 if zd < 239
ytr inc 689 if zd <= 247
yvh inc -644 if zd < 244
iy inc -469 if eb < -385
rtu inc -91 if xzn == 1169
eb dec 9 if su <= -816
s inc -418 if es == -595
r inc 320 if jhb >= -1340
q inc 87 if iy != 1465
yvh dec 184 if ae == -1976
es inc -231 if okl == 478
cpq inc -658 if s > -1257
fij dec 344 if fzu < 758
cpq dec -911 if yvh <= -118
j dec 699 if h > -723
laz dec -356 if okl > 474
on dec 989 if yvh >= -122
ae dec 634 if zd <= 235
s dec -361 if ib <= 1322
ytr dec 735 if zd >= 235
h dec 897 if fzu < 750
fzu dec 838 if j > -541
q inc -588 if h > -724
h dec 37 if laz < -423
ytr inc 247 if es != -601
fij inc 51 if jhb >= -1335
h dec 20 if wf != 10
r inc -563 if rtu <= 744
ae dec 406 if zd > 234
fzu inc -341 if ytr == 2805
iy dec -595 if ytr <= 2802
iy inc -948 if jhb < -1331
su inc -377 if h <= -769
fzu inc 977 if fij == 1424
es dec 555 if s != -1258
ae inc -925 if zd != 238
laz inc -348 if ib == 1324
eb dec 748 if ae == -2388
r dec -344 if wf < 2
fzu dec -498 if ae >= -2383
jhb inc 4 if fij != 1424
ae inc -828 if iy <= 522
ae dec -633 if ib > 1322
h dec -81 if fzu <= 557
ytr inc 542 if es < -1141
j dec -539 if fzu != 557
jhb dec -356 if fzu < 560
laz inc -895 if laz >= -781
q dec 732 if eb == -1142
yvh inc 221 if ib != 1326
h inc -216 if okl == 481
jhb dec 355 if iy > 520
ib inc 651 if r >= -44
r inc -947 if j > -1
ytr dec 292 if es < -1141
gbu dec 161 if h < -904
xzn dec 33 if fzu > 549
zd dec 781 if buw != 56
yvh dec 836 if j < 9
zd dec 385 if q != -1488
ib inc 402 if xzn == 1136
cpq dec 876 if iy <= 509
cpq dec -94 if cpq <= -972
s inc -609 if r == -983
ytr inc 59 if h > -909
okl inc -854 if wf <= 4
ib inc -284 if ae > -2584
ytr dec -359 if ytr > 3112
su dec 236 if rtu <= 748
xzn inc 103 if q == -1491
wf inc -701 if q == -1488
jhb inc 954 if on == 905
iy dec 135 if es >= -1141
q dec -904 if buw >= 49
xzn dec 459 if su > -1429
jhb inc -282 if q == -584
gbu dec 239 if cpq < -881
zd inc 987 if rtu <= 750
ae inc -31 if yvh < -725
fij inc 841 if q < -574
j inc -720 if okl <= -373
rtu dec 906 if iuz >= -865
h inc 137 if su <= -1425
okl dec 690 if fzu <= 545
q inc -508 if rtu >= -163
fij dec -751 if rtu > -166
fij inc 763 if laz >= -1677
fzu dec 42 if q < -1088
okl dec -156 if fij != 3786
iy inc -977 if ib >= 2087
laz dec -31 if su <= -1412
buw inc -358 if r == -983
eb dec 743 if fzu > 508
fzu dec 3 if eb >= -1876
yvh dec -190 if wf <= -696
okl inc -168 if h <= -901
su dec -704 if wf < -706
eb dec 587 if fzu >= 512
su inc -778 if zd == 444
ae inc -134 if laz < -1637
on inc -92 if fzu < 519
ib inc 217 if s > -1864
cpq inc 46 if q > -1098
cpq dec 321 if xzn <= 673
fij dec -633 if zd != 443
zd dec 869 if on == 807
buw inc -506 if laz > -1647
q inc 640 if s <= -1862
zd dec 943 if okl < -378
rtu inc -498 if buw >= -814
cpq dec 651 if fzu > 507
fij inc -636 if j < -714
zd inc -167 if ae != -2754
eb dec 369 if fzu >= 505
su dec -549 if q != -454
cpq inc -755 if okl > -391
ib inc 810 if su <= -1652
wf dec 159 if laz > -1651
buw dec -978 if okl != -377
cpq dec -288 if j != -715
buw inc -470 if okl == -380
cpq inc -997 if iuz > -867
cpq inc -855 if on < 815
es dec -372 if buw != 173
r inc -503 if ae > -2753
buw dec 963 if ae == -2755
r inc 70 if cpq > -3816
eb inc -39 if fij != 3786
q inc 696 if jhb < -295
laz dec -643 if j <= -718
gbu dec 767 if cpq > -3815
buw dec 571 if es > -785
on dec -220 if rtu <= -657
fij dec -286 if zd > -675
iuz dec -790 if ae >= -2751
buw inc -457 if rtu <= -652
h inc -345 if laz != -1653
es dec 996 if su <= -1644
es dec 594 if iy >= -467
s dec 981 if wf == -860
zd inc -828 if cpq >= -3808
laz inc -245 if r <= -1416
su inc -61 if j >= -726
gbu dec -409 if on >= 1029
fzu dec 182 if eb != -2875
fij dec 440 if iy == -462
jhb dec -21 if su <= -1704
iuz dec -627 if r != -1425
ib dec 787 if jhb < -292
r dec 624 if yvh > -546
buw inc 625 if jhb <= -289
jhb inc -874 if on >= 1025
ib dec 224 if iy != -455
r inc 482 if gbu <= 1126
fij inc -848 if okl != -393
es dec -513 if gbu != 1127
fzu dec -189 if iuz < 569
ae inc 317 if cpq <= -3804
h inc -214 if eb < -2873
zd inc 124 if wf > -865
r dec 892 if gbu <= 1137
ytr inc -92 if fij > 2770
iy inc 302 if rtu == -661
iy dec 503 if yvh < -549
yvh inc 276 if fij < 2775
q inc -612 if jhb <= -1151
q inc 949 if iy != -159
jhb dec 771 if h == -1458
yvh inc 389 if on == 1033
s inc 167 if jhb >= -1160
gbu inc 194 if jhb >= -1165
fzu inc 678 if laz >= -1893
iuz inc -226 if zd != -1360
okl dec -490 if ib >= 2077
su dec -478 if fij < 2784
s inc 540 if s >= -2677
fij dec 555 if buw <= -858
cpq dec -261 if fij != 2220
rtu inc -378 if okl >= 103
zd dec 991 if fzu == 1198
fzu dec 464 if xzn < 678
xzn inc -28 if ae > -2432
wf dec 84 if rtu >= -1041
okl dec 670 if s <= -2128
h inc -548 if yvh < 123
wf dec 579 if cpq < -3544
su inc -160 if ae >= -2439
wf dec -845 if zd < -2361
es dec -19 if q != 573
j dec 763 if fij >= 2214
wf dec -486 if su < -1384
ae dec -887 if cpq >= -3541
xzn dec 879 if es != -1836
iuz inc 840 if iuz == 333
on dec -251 if j != -1471
ib inc -65 if fij <= 2224
fzu inc -673 if r >= -2932
r inc -319 if su < -1390
es dec 730 if s >= -2145
yvh inc 593 if q != 571
ytr inc 367 if ib >= 2031
wf inc -546 if zd >= -2369
yvh inc -814 if fzu != 61
xzn inc -798 if on == 1284
j dec 832 if okl != -565
q dec 210 if zd >= -2366
j inc -392 if r >= -3257
jhb dec -490 if ytr < 3381
buw inc 173 if rtu < -1035
okl inc 81 if j > -1877
ib inc -207 if wf == -1583
ib dec -494 if cpq == -3547
laz dec -331 if rtu >= -1042
cpq inc -697 if jhb <= -1157
ib dec 601 if eb != -2889
ib dec 613 if yvh == 714
xzn dec -948 if jhb > -1160
su inc 651 if q > 376
okl dec 613 if rtu > -1045
eb dec -348 if gbu == 1322
iy inc -508 if cpq == -4235
q inc -768 if su <= -1383
s dec -612 if on >= 1283
iuz inc 942 if gbu != 1322
okl dec -707 if ytr != 3379
on inc -658 if buw <= -689
on dec -246 if es == -2566
j inc -335 if eb == -2532
wf inc 341 if cpq != -4248
fzu inc 297 if rtu > -1042
cpq inc 624 if ib >= 1091
q dec -961 if wf < -1233
h inc -688 if okl == -390
yvh inc 378 if iuz <= 1182
q inc -177 if ib <= 1095
ib dec -52 if s > -1520
su dec -822 if on <= 878
wf inc -962 if cpq <= -3629
fzu inc -481 if okl > -386
iy inc -146 if rtu > -1048
ib dec -523 if s < -1522
fzu dec 121 if fzu == 358
j dec -112 if ae != -2434
laz dec 967 if laz >= -1566
gbu dec -825 if on > 876
wf dec 658 if su <= -570
q dec -247 if jhb <= -1155
r dec -781 if eb <= -2524
zd inc 363 if fzu != 244
q dec 139 if jhb < -1147
es dec 185 if iuz >= 1171
iuz inc 267 if su > -573
jhb dec 745 if es > -2745
ib inc 646 if s == -1524
okl inc 139 if h < -2700
j dec -199 if wf < -1233
gbu inc -848 if r != -2466
es dec -570 if xzn == 799
rtu dec -990 if ytr != 3379
ae dec -48 if yvh != 1089
iy inc 143 if buw > -695
eb dec -645 if q > 485
xzn dec -295 if yvh != 1090
es dec -302 if on < 879
ib dec 222 if wf < -1233
eb inc 587 if wf > -1244
zd dec 896 if su < -567
ib dec -405 if q < 502
buw inc -282 if r < -2460
fij inc 810 if gbu > 468
h inc 322 if ae > -2388
su inc -843 if j == -1896
jhb dec 896 if yvh >= 1089
h dec 961 if cpq >= -3624
laz dec -799 if ae > -2375
zd inc -490 if h <= -3332
fij inc 639 if q > 489
ib inc 160 if rtu < -47
yvh dec 82 if eb != -1302
cpq dec -219 if eb <= -1291
es dec 713 if okl > -260
s inc -314 if wf != -1242
s inc -366 if ytr != 3386
zd inc -332 if zd != -3393
iy dec -669 if ae > -2390
j dec 151 if su == -1412
wf inc 354 if jhb >= -2056
xzn dec 580 if iy == 510
laz inc 692 if iuz >= 1441
fzu inc -913 if on <= 875
s inc -855 if buw == -975
zd inc 68 if gbu > 466
iuz inc -729 if iuz == 1440
gbu inc 261 if j != -2056
q inc -977 if su != -1421
laz dec 451 if r != -2473
okl inc 93 if rtu == -49
eb inc 98 if j != -2052
ae inc -176 if buw == -973
j dec 492 if rtu <= -50
j dec -806 if buw < -964
laz dec 407 if eb != -1195
iy inc -77 if s == -1890
q dec 900 if yvh >= 1003
r dec -530 if es <= -2591
iy dec -612 if buw <= -972
zd dec 615 if buw < -967
ytr inc 541 if xzn >= 1086
gbu inc 62 if gbu <= 739
gbu inc 283 if r != -1934
ytr dec -282 if cpq < -3391
yvh inc 48 if gbu < 1088
jhb dec 412 if yvh >= 1052
es dec 417 if yvh >= 1051
fzu inc -660 if cpq < -3397
h inc -545 if h <= -3332
fij inc -179 if iuz > 707
zd inc -217 if okl == -158
laz inc -342 if yvh != 1057
on inc -856 if buw <= -969
xzn dec 188 if su < -1404
cpq dec 916 if xzn > 904
eb inc 642 if wf != -884
okl dec 64 if iy >= 1044
xzn inc -694 if gbu != 1075
ae dec -478 if yvh <= 1061
iuz dec 374 if fzu <= -1335
zd dec 910 if r == -1940
gbu dec 543 if su < -1409
okl inc 523 if laz != -3732
ytr inc -898 if jhb != -2465
su dec -593 if ytr != 4204
buw dec -56 if gbu <= 542
zd inc -348 if wf <= -895
iuz inc 264 if buw != -913
okl inc 702 if wf <= -879
q dec 283 if wf > -892
laz dec -901 if wf != -892
on inc 256 if rtu <= -48
iy inc 57 if su == -1408
fzu inc -732 if su != -1408
ytr dec 559 if eb >= -563
iuz dec 967 if es > -3016
j inc 849 if wf > -883
xzn inc -764 if q != -1671
ib dec -555 if r == -1946
r dec -205 if yvh == 1058
laz inc 826 if ae >= -2085
gbu inc -43 if buw >= -926
j inc -341 if wf > -889
s dec -343 if gbu >= 504
iuz dec 306 if fij >= 3486
fij dec -905 if iuz >= -667
ae dec 174 if fzu >= -2073
on dec -861 if buw > -920
jhb inc -513 if iuz >= -672
okl dec -389 if j == -1582
ib inc 419 if iy == 1041
xzn inc -271 if eb < -568
buw inc 230 if on <= 1139
rtu inc 745 if su <= -1406
gbu dec -430 if iy != 1046
s inc 357 if su >= -1417
r dec -370 if rtu > 694
buw dec 989 if r < -1373
okl dec -817 if iuz < -665
h dec 435 if laz != -2005
jhb inc -142 if iy < 1036
rtu inc -375 if fzu <= -2059
zd inc -974 if j < -1572
es dec -330 if yvh == 1058
on dec 661 if fzu < -2068
j inc 59 if on == 1133
cpq inc -503 if q >= -1673
iuz dec -123 if j < -1521
yvh inc -749 if su > -1416
cpq dec 847 if zd != -6359
laz inc 940 if iuz > -553
su dec -999 if on > 1128
cpq dec 43 if h > -4325
j dec -869 if ib != 3032
zd dec 871 if xzn != -552
j dec 986 if laz != -1067
buw inc -723 if cpq < -5700
eb dec 153 if iy >= 1035
fij inc -182 if j < -1636
on dec 148 if su != -419
buw dec 923 if xzn < -549
cpq inc 35 if h >= -4330
fij dec 755 if es < -2671
q dec 745 if buw >= -2340
wf inc -49 if ae == -2255
zd dec 631 if j == -1640
jhb dec 902 if eb != -723
iy inc 408 if ib <= 3033
iuz inc 948 if on <= 989
zd inc -991 if laz < -1055
xzn dec -294 if ib >= 3032
wf dec 797 if iy == 1449
iy dec 467 if fzu >= -2073
fij dec -491 if fzu >= -2075
es dec 946 if eb != -714
ib dec -726 if gbu < 934
fij inc -705 if eb < -704
ytr dec -143 if jhb < -3870
buw dec -381 if iuz <= 408
on inc 275 if iy == 991
ib dec 37 if laz != -1057
eb inc -456 if xzn < -543
okl dec 91 if cpq != -5666
fzu dec 520 if fij < 2339
j dec -910 if ib <= 3747
zd inc 661 if fij <= 2341
r inc -620 if es > -3629
rtu dec 907 if buw > -1951
es inc -151 if jhb == -3880
s dec 777 if q != -2410
r inc -582 if jhb < -3871
rtu dec 487 if r >= -2576
es dec 532 if xzn > -546
su dec -289 if rtu == -166
rtu inc -33 if iuz <= 400
rtu inc 566 if rtu < -189
yvh inc 752 if on != 988
buw dec 856 if s >= -1536
q dec 64 if rtu >= 358
cpq inc 324 if j <= -1640
jhb inc -359 if r > -2570
q dec -325 if es < -3770
ib inc 893 if eb != -1165
laz inc 811 if jhb != -4248
yvh inc -744 if fij <= 2345
ae inc -830 if s >= -1536
cpq inc 773 if ytr <= 3790
cpq inc 936 if gbu >= 931
jhb dec -944 if eb >= -1172
j dec 987 if gbu > 920
s dec 560 if r <= -2562
jhb inc -435 if eb > -1171
s dec 922 if es < -3772
ae inc -5 if yvh < 327
buw inc 83 if r > -2563
ytr dec 167 if rtu > 365
fzu dec 144 if okl > 2173
fij dec -248 if ytr > 3613
h dec 406 if zd < -7324
j dec -807 if fzu != -2741
xzn inc -58 if gbu != 924
jhb dec -878 if es > -3773
cpq dec 525 if yvh != 327
okl dec -555 if s != -3011
wf dec 395 if su <= -121
r dec 231 if ae < -3089
iy inc 57 if ae > -3088
buw inc -862 if cpq < -5098
cpq dec -191 if su != -120
r dec 18 if zd == -7325
cpq dec -156 if fij >= 2586
su dec 743 if on != 987
xzn inc 493 if cpq >= -4753
r dec 847 if ib != 4642
h inc 675 if ytr == 3625
iy inc 934 if xzn < -545
fzu dec -982 if ae == -3090
iuz dec 500 if iy != 1911
eb dec 676 if xzn > -560
s inc -440 if ib >= 4650
s dec 662 if ae != -3092
buw inc -625 if rtu != 357
es dec -936 if iuz != -100
ib inc -849 if cpq < -4750
s dec 544 if cpq != -4758
zd inc -432 if es < -2845
gbu inc -787 if okl < 2741
gbu dec -336 if buw < -4287
on dec -790 if gbu <= 474
buw dec -627 if q <= -2145
h inc -142 if q != -2156
cpq dec 264 if iuz > -98
ib inc 19 if q >= -2157
zd dec -579 if q != -2140
es dec 567 if j <= -1820
rtu dec -213 if iy != 1926
zd dec 546 if iy < 1922
buw inc -847 if wf >= -2134
laz dec -136 if xzn >= -560
xzn inc 516 if zd != -7292
wf inc -560 if ib >= 3807
gbu dec 828 if wf == -2689
on dec -126 if gbu >= -361
yvh inc -153 if r != -3660
iuz inc 277 if r != -3663
yvh inc -941 if iuz > -108
j inc -176 if iuz >= -104
jhb dec -124 if rtu < 581
r inc -456 if rtu != 583
buw inc 346 if cpq > -4765
yvh inc 841 if yvh == -777
buw inc 806 if eb > -1853
eb inc -821 if zd < -7285
s dec -257 if j <= -2000
buw inc 734 if r != -4111
q dec 299 if fzu >= -1756
ytr dec 363 if su < -870
gbu inc 812 if jhb != -3616
q inc -373 if fij <= 2587
xzn dec 954 if r == -4119
jhb dec 275 if okl < 2738
fij inc -894 if fzu != -1752
wf inc -122 if okl > 2738
laz dec -942 if q > -2820
gbu dec -297 if jhb >= -3885
r dec -994 if zd <= -7285
ytr inc 544 if es >= -3416
jhb dec 326 if wf <= -2688
h dec 949 if yvh == 64
wf dec -884 if zd == -7292
rtu inc -456 if ib >= 3805
es inc -375 if h == -5817
cpq dec 675 if q > -2828
fzu dec 706 if buw != -2639
h dec -230 if h >= -5821
ae inc 576 if su != -866
j inc 903 if fij >= 1686
buw dec -693 if h <= -5583
fij inc -416 if jhb > -4210
q inc -648 if okl < 2739
fij inc 736 if su != -876
ytr dec 869 if cpq < -5435
ytr inc 126 if eb > -2664
buw dec 702 if eb > -2664
es dec 392 if xzn == -1506
rtu dec 837 if r != -3132
ytr dec 729 if s > -4228
buw dec -760 if fij >= 2008
cpq dec -358 if q != -3477
s dec -292 if jhb > -4214
laz inc -77 if rtu > -720
es inc 427 if zd == -7292
r inc 179 if jhb >= -4209
gbu inc -163 if q != -3460
buw inc 381 if laz >= -187
okl inc -167 if su > -865
fzu dec 289 if laz >= -183
ytr inc 544 if gbu < 601
fzu dec 706 if q < -3464
rtu inc -605 if eb < -2658
buw dec 199 if iuz < -96
su dec 599 if h < -5585
on inc 895 if rtu == -1310
on dec -661 if yvh != 58
su dec 995 if q <= -3469
buw dec -471 if q <= -3466
wf dec -487 if ae > -2524
buw inc 542 if es > -3381
fij dec 599 if okl >= 2734
ae inc 295 if xzn <= -1511
s inc -293 if ytr < 3985
s inc 571 if ae < -2506
ytr inc -199 if wf < -1313
zd inc -155 if on <= 2568
su dec -221 if buw <= 23
s inc 961 if ytr <= 3790
zd inc -200 if es > -3375
ae dec -266 if fzu <= -3160
fzu inc -197 if h < -5583
q dec 765 if es <= -3366
j inc -967 if yvh > 57
iuz inc -111 if laz <= -181
es dec 403 if j >= -2065
wf dec -542 if eb < -2665
zd inc -518 if eb <= -2664
r dec 593 if s != -2700
jhb dec -422 if gbu < 594
ae inc -399 if xzn >= -1503
ib dec -244 if h != -5583
fzu dec 412 if es != -3773
rtu dec -620 if r < -3542
ytr dec -342 if yvh < 65
iy inc 303 if rtu <= -1314
rtu inc 602 if on != 2562
buw dec 546 if fzu <= -3766
fij dec -376 if zd == -8165
eb inc 332 if xzn <= -1510
ae inc 231 if iuz != -212
j dec 703 if rtu <= -1316
su dec -636 if on <= 2561
iy dec 260 if r != -3544
ae dec 744 if ae <= -2248
jhb inc -128 if ae <= -2985
s dec -692 if yvh <= 72
buw dec -419 if wf < -777
j dec 627 if rtu != -1312
wf inc -736 if gbu == 591
buw inc 532 if jhb <= -3914
j inc 290 if yvh != 55
zd inc -920 if wf > -1518
es inc 48 if es >= -3781
xzn dec -88 if s >= -2004
okl inc 263 if iy == 1959
es dec -584 if iuz <= -205
rtu dec 211 if okl <= 2996
buw dec -580 if ae >= -2999
fij inc 992 if iuz >= -220
q dec 685 if zd == -9085
wf dec 406 if r <= -3532
cpq dec 336 if fzu <= -3769
ytr dec 813 if cpq > -5414
iuz dec 456 if zd >= -9086
fij dec -372 if on == 2562
zd inc -182 if wf < -1916
jhb inc 992 if xzn < -1408
es inc 899 if ib != 4049
iy inc 88 if iy > 1951
su dec 363 if rtu > -1323
es inc -311 if wf < -1911
cpq inc 328 if iuz <= -659
es dec 349 if r < -3534
eb dec 488 if ib < 4065
r inc 639 if r >= -3542
wf dec 105 if wf < -1913
laz inc 95 if buw >= 52
wf inc -260 if buw > 53
wf dec 975 if gbu <= 598
iuz inc 788 if on != 2555
jhb dec -717 if wf <= -2992
rtu dec -551 if rtu <= -1315
fij inc -392 if wf == -2990
eb inc -267 if okl == 3000
su dec 884 if iuz > 118
fzu inc 704 if iuz < 123
xzn dec 810 if laz <= -90
cpq dec 961 if ytr > 3310
on inc -936 if on != 2562
on dec -968 if s >= -1994
eb inc -240 if q <= -4912
ib dec -760 if okl < 2991
cpq dec 692 if iy < 2051
es inc 477 if j != -3100
fzu dec 832 if fzu <= -3063
okl inc 30 if gbu <= 596
su dec 607 if eb == -3661
xzn inc 829 if ib < 4060
iy dec -895 if wf != -2990
wf dec 481 if cpq > -5768
okl dec -432 if jhb < -2199
yvh inc -765 if su < -4086
iy inc -903 if r < -2892
h dec -145 if iuz <= 121
zd dec 392 if on <= 2569
okl inc -36 if rtu != -773
xzn dec -551 if r >= -2909
j inc 461 if s <= -1993
iuz inc 889 if zd < -9651
yvh dec 269 if iuz <= 1012
fzu dec -330 if ib <= 4067
fij dec -931 if su != -4096
yvh inc 277 if h > -5446
iy inc -316 if es == -2904
q dec 57 if cpq != -5773
jhb dec 784 if yvh == -686
yvh dec -785 if ib != 4058
s inc 13 if ib != 4066
rtu dec 372 if iy < 1731
h inc -901 if buw > 48
cpq inc -295 if ytr == 3310
gbu dec 460 if j >= -2638
ib dec 942 if rtu >= -1143
r inc -231 if ib > 3121
h inc 275 if ib == 3108
iuz dec -599 if xzn == -848
fzu dec -293 if rtu != -1139
ae dec -911 if yvh < -687
on dec -969 if ae >= -2084
jhb dec 432 if iy != 1723
cpq dec 369 if iuz >= 1602
cpq inc 161 if q == -4919
su dec -818 if buw > 49
r inc 176 if rtu <= -1138
su inc 19 if xzn < -841
gbu inc -987 if laz >= -100
ytr inc 349 if j >= -2643
wf dec 371 if q < -4909
rtu dec 203 if xzn >= -852
wf dec 410 if rtu < -1339
ib dec 448 if gbu < -392
yvh dec 130 if iy == 1723
ytr inc -363 if zd >= -9663
cpq dec -69 if okl >= 3422
iy dec 250 if ae <= -2080
cpq dec -273 if iy > 1465
gbu dec 37 if ib > 2673
q dec -552 if laz == -92
q inc 600 if ib <= 2669
ib dec 570 if gbu != -392
wf inc -299 if fij > 4080
buw inc -756 if s <= -1984
gbu inc -707 if gbu == -401
gbu inc -937 if gbu != -398
fzu dec 265 if r != -2724
r dec -786 if s >= -1993
wf dec 607 if laz <= -92
eb dec 424 if wf < -4675
xzn dec 17 if fij >= 4083
on dec -829 if gbu >= -1333
h inc -669 if xzn <= -860
j dec 393 if ib < 2106
es dec -958 if fzu > -3568
es inc 943 if rtu == -1342
xzn dec -274 if rtu > -1349
buw inc 88 if laz == -92
yvh dec 865 if laz > -87
gbu inc -415 if laz > -96
jhb inc -555 if yvh > -830
on inc -442 if ae == -2081
iy dec 504 if iuz > 1599
q inc 132 if yvh >= -818
yvh inc 642 if yvh == -823
yvh inc 54 if yvh <= -176
yvh inc 799 if wf == -4685
gbu inc -861 if on == 3918
jhb dec 435 if r < -1929
fzu dec -180 if iy <= 976
j dec -462 if xzn > -596
q inc 268 if cpq > -5944
ae inc 154 if gbu < -2604
laz dec 484 if q <= -3499
iy dec -127 if iuz <= 1609
ae inc 119 if h > -7018
s dec 723 if s < -1981
buw inc 124 if fzu > -3390
r dec -947 if su < -3265
ytr dec -851 if ib <= 2089
r dec 267 if j != -2562
r dec 289 if ae == -1808
es dec 489 if gbu != -2601
okl dec -2 if q == -3499
jhb inc -486 if buw != -485
fij inc -38 if h <= -7022
zd inc -910 if r >= -2500
yvh dec -457 if wf >= -4685
es inc -458 if yvh >= 1129
eb dec -851 if buw >= -500
xzn inc -983 if on >= 3914
iuz dec 137 if rtu > -1343
su inc 723 if okl <= 3434
s dec -254 if zd > -10577
iy dec -304 if buw < -482
su dec 405 if r != -2492
buw inc 419 if es != -2906
rtu dec 360 if r <= -2493
gbu inc 178 if xzn == -1574
iuz inc 349 if q < -3489
fij inc -484 if zd == -10574
buw inc -211 if ytr != 3299
ae dec -387 if es != -2899
h dec 384 if wf > -4683
ib dec 100 if xzn != -1573
s dec 540 if r > -2502
ib dec 217 if ytr != 3301
okl inc -560 if on > 3912
buw inc 220 if wf > -4687
buw inc -904 if iuz >= 1819
xzn inc -474 if es == -2905
fij dec 671 if laz < -569
r inc 842 if okl >= 2878
fzu inc 889 if rtu == -1702
buw dec -334 if buw > -975
buw dec -758 if su < -2942
rtu inc 719 if ae == -1421
iuz inc 295 if fzu <= -2496
es inc 713 if xzn <= -1572
es dec 987 if eb > -3237
j inc 704 if cpq == -5934
ytr inc -74 if fzu > -2503
s dec -958 if xzn != -1569
fzu inc -53 if ytr == 3222
fzu dec 937 if okl == 2877
ae inc 980 if yvh > 1119
r inc 293 if q > -3504
ae dec 199 if fzu == -2555
xzn inc 87 if r >= -2206
eb dec 557 if r >= -2200
on inc -612 if wf > -4690
j dec 234 if ib < 1783
eb inc 261 if okl < 2869
gbu inc 796 if cpq > -5936
xzn dec -149 if gbu < -1631
es inc 693 if rtu > -989
j inc -61 if q == -3503
r dec -227 if okl <= 2874
cpq inc -245 if fzu == -2553
s dec -299 if ae > -434
j dec 593 if s > -2041
xzn dec -398 if on < 3304
on inc 663 if h <= -7012
jhb dec 592 if iuz > 2119
iy inc -666 if ytr > 3219
gbu inc -563 if iy <= 740
xzn dec -77 if es < -2484
su inc 590 if q <= -3499
jhb dec -17 if on <= 3965
okl dec -106 if su < -2353
buw dec 554 if h > -7017
eb dec -279 if ytr != 3212
buw inc 950 if eb != -2699
j dec 297 if j != -2698
r inc -507 if q != -3494
q inc -838 if xzn == -1261
iuz dec -632 if cpq <= -6171
laz inc -863 if okl >= 2865
zd dec 764 if jhb != -3682
iuz inc -193 if wf < -4684
xzn dec -672 if iuz > 2556
fij inc 800 if okl == 2868
q dec 699 if eb == -2694
q inc -126 if fij >= 4208
j dec 413 if j <= -2982
r dec 528 if on <= 3969
iy dec -849 if fzu < -2553
wf dec 21 if xzn < -1267
on inc 273 if ae <= -447
eb inc 59 if iy == 732
q dec 392 if s != -2042
wf inc -589 if laz < -1431
su inc 39 if q <= -5546
q inc 755 if rtu >= -988
on dec -501 if es > -2498
gbu inc 439 if yvh != 1131
es dec 730 if h >= -7013
xzn dec 641 if gbu > -1762
ib inc -610 if j != -3403
xzn inc 557 if ae != -441
fij dec 453 if su != -2307
su inc 748 if gbu <= -1753
rtu dec 140 if okl != 2858
h inc 619 if j != -3403
s dec 466 if yvh == 1129
iy dec -639 if okl <= 2873
on dec 725 if q < -4790
gbu inc -256 if cpq == -6184
laz dec 58 if jhb != -3680
gbu dec 352 if eb < -2687
s dec -151 if gbu >= -2112
fzu dec -791 if zd != -11327
fij dec 368 if yvh > 1126
okl inc -951 if es >= -3225
jhb dec 419 if q < -4808
rtu dec 100 if s < -2350
es inc 894 if rtu >= -1227
q dec 613 if s >= -2355
r inc -691 if q < -5408
xzn dec -546 if iy <= 1370
ae inc 996 if su >= -1564
buw inc 559 if okl <= 1919'''


OPERATORS = {
    '>': operator.gt,
    '<': operator.lt,
    '>=': operator.ge,
    '<=': operator.le,
    '!=': operator.ne,
    '==': operator.eq
}

OPERATORS_INV = {v: k for k, v in OPERATORS.items()}


CHANGE = {
    'dec': operator.sub,
    'inc': operator.add
}

CHANGE_INV = {
    operator.sub: '-',
    operator.add: '+'
}


class Instruction(object):
    '''An instruction.'''

    def __init__(self, register, change, amount, condition):
        self.register = register
        self.change = change
        self.amount = amount
        self.condition = condition

    def __str__(self):
        change = CHANGE_INV[self.change]
        return f'Instruction({self.register} {change} {self.amount}, {self.condition})'

    def __repr__(self):
        return str(self)

    def update(self, amount):
        '''Update value of amount with change.'''
        return self.change(amount, self.amount)

    @staticmethod
    def create(row):
        '''Create an instruction from a row.'''
        change = CHANGE[row[1]]
        amount = int(row[2])
        condition = Condition.create(row)
        return Instruction(row[0], change, amount, condition)


class Condition(object):
    '''A condition.'''

    def __init__(self, register, op, amount):
        self.register = register
        self.op = op
        self.amount = amount

    def __str__(self):
        op = OPERATORS_INV[self.op]
        return f'Condition({self.register} {op} {self.amount})'

    def check(self, amount):
        '''Check amount against condition.'''
        return self.op(amount, self.amount)

    @staticmethod
    def create(row):
        '''Create a condition from a row.'''
        op = OPERATORS[row[5]]
        amount = int(row[6])
        return Condition(row[4], op, amount)


class Registers(object):
    '''Container for registers.'''

    def __init__(self):
        self.registers = defaultdict(int)

    def __str__(self):
        return str(self.registers)

    def __iter__(self):
        return iter(self.registers.items())

    def check(self, condition):
        '''Check a condition.'''
        register_amount = self.registers[condition.register]
        return condition.check(register_amount)

    def update(self, instruction):
        '''Update registers with instruction.'''
        if self.check(instruction.condition):
            current_amount = self.registers[instruction.register]
            new_amount = instruction.update(current_amount)
            self.registers[instruction.register] = new_amount


def parse_input(input):
    '''Parse input data.'''
    rows = (row.strip().split(' ') for row in input.split('\n'))
    instructions = [Instruction.create(row) for row in rows]
    return instructions


instructions = parse_input(INPUT)
