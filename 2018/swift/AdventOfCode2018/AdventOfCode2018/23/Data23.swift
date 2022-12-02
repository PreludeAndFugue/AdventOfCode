//
//  Data23.swift
//  AdventOfCode2018
//
//  Created by gary on 28/11/2022.
//  Copyright © 2022 Gary Kerr. All rights reserved.
//

import Foundation

let input23_t1 = """
0,0,0,4
1,0,0,1
4,0,0,3
0,2,0,1
0,5,0,3
0,0,3,1
1,1,1,1
1,1,2,1
1,3,1,1
"""


let input23_t2 = """
10,12,12,2
12,14,12,2
16,12,12,4
14,14,14,6
50,50,50,200
10,10,10,5
"""


/// pos=<15758255,29323050,44252572>, r=75313061
let input23 = """
15758255,29323050,44252572,75313061
5716231,51688647,43848689,72530281
21596147,100862835,27344717,89320477
42881296,106156112,36404081,82387904
25343820,86985516,44353623,88704305
40173493,85226627,32024576,59786979
11123094,49515401,38938249,60039541
-1156839,55363785,11556673,75807482
6806193,55815713,30781098,62499689
802948,53873742,575055,83339160
9457727,63645853,25335465,62232892
41853559,120292299,28561553,89709482
49796279,15925926,46943095,57362724
49403603,64576219,-25548817,71564863
17937807,21990664,34484804,70698026
-32092024,48759501,32040849,95601595
22959356,12594347,58396671,98984687
89644373,20740955,50562164,88622192
90657565,42785010,33272831,50302029
32661717,53485347,67311049,70843665
93810914,60167039,48973732,78675625
44702109,3971244,38143449,65611781
1631201,64773199,29896433,75747462
-8359912,14635826,27249922,97115759
10910848,49200620,30428326,51427109
98651158,51534386,48250795,74160387
17511706,69690625,34515390,69403539
2216096,51709888,39884032,72087124
33965777,108897104,41152715,98793059
44644548,108216105,33657771,79938522
2620646,50118805,49774458,79982148
69359223,19907740,32452823,51060890
-17343792,127669407,82649494,90610896
35959276,49383993,64528651,60662518
29273218,63974286,63972660,81382854
44284950,48059580,21373936,80829003
49338383,-3672864,35702245,66178395
7757277,51819009,29531960,56302806
45247849,61615638,69750910,68827691
51912360,69850068,-6772244,55553618
-946503,60727588,29443239,73826877
8708854,47909097,54185367,76094613
-9983817,38346617,32751872,80530752
18008191,47893290,41038222,53632338
48257746,65812318,52333468,52597122
87317765,50349444,82971409,96362517
25051462,94523919,17108491,83207589
20783411,90066951,25782392,77775270
29680738,67824332,17215292,51771798
101062158,55804188,-5348643,86073410
42898327,25407439,47349975,55185884
45831343,51736584,94161462,82775874
45497346,79598319,32880809,49690770
14836499,57611207,32211378,57695171
45098954,54003173,94296674,85909938
51662071,71458882,84692434,87198379
48833346,53112842,26067073,72995147
23363301,48758707,3113154,53125678
-15513766,58115868,35160955,91499598
24807358,68501881,43623030,70026618
111847848,62926865,27887630,78386254
9989692,59478662,40768636,72966591
9191876,49503840,26946102,49967154
83330502,17652643,6637566,76331314
5747942,59432422,26903052,63296624
49624542,84862801,43616804,61564795
38906114,38533638,68434925,67136877
-4347971,48772965,33449262,69279664
-17905665,47798691,48817035,97230595
16111124,58343291,67928963,92870218
94011283,50689524,31860677,52285693
99461489,49093863,27384217,51663518
5510007,56572285,25561231,59332514
72651761,78709741,47731528,74816978
5261781,50318681,34203554,61969796
38366044,54134265,21821583,82175565
10352082,61251141,62392382,96000629
471808,61697885,29424173,73359241
78566578,55686010,-986598,59097555
9529068,76607184,38559622,88346851
36921776,50997806,32913286,60481518
44989642,50873084,28656850,60067133
29252355,56141274,40827212,50425160
-20244441,49952548,27679776,80585762
45912246,54475006,81931916,73203704
19906677,26415507,58644410,88464026
50964911,54544452,105418240,91706769
32904882,10197549,52898915,85938183
95743073,48041107,-15679072,83321736
51989504,43698650,85112684,65566390
-21353279,52065838,19810016,84452664
61349775,92406104,35795578,65275410
77000093,15129110,54030697,85058281
11001284,42550300,-1022393,71747101
23804592,56914919,47553229,63372611
36593136,44483599,40176561,97009671
3690589,49310963,9544564,66919487
32670174,111249635,28947500,90236064
29628619,69688272,15129489,55773748
24977198,79836954,27378607,64947527
106755777,59455154,28834628,70769539
30821345,80940973,40155397,72984080
12485511,79728859,44761738,94714091
55979100,87126151,53356802,72186289
137048856,48348030,33078098,94198915
71787782,48482918,-15086730,59215761
16238305,83829380,42005299,92305359
50201713,108318724,34158379,74984583
14525982,95040626,35159486,98383237
66463588,50616372,38773379,97306002
110434204,63789135,33826172,83773485
22946263,83281549,25341093,68385400
46299539,76847538,43255405,56512421
46208611,90996286,12596010,63035192
21616909,64118780,34044543,59255404
25832423,94462644,32866505,84205713
115521393,47730274,22694815,64415467
22290703,82827260,37272635,80518256
46506140,113980844,31345443,81529141
-16396810,57490107,34475889,91072144
-6949283,36954630,37805299,83941627
31517577,70019302,33117239,54328154
40038483,64319793,25583105,79597820
80530450,56740792,-9876091,71005675
28716785,75794972,43715398,73502736
36231158,90343642,37366141,74187610
27114035,33218451,34383280,50192505
35731023,4416509,47162147,83156302
11665173,63489932,59198178,93732216
50712916,116734617,10298475,86566707
93106977,37245792,13958120,59194104
18317123,66878054,48072832,79342775
61796679,82220422,39787306,59528353
47993808,49083206,34112969,67235396
44155946,62893485,-8119120,57700085
10313824,45190536,41262719,61900143
93361318,67924414,34146265,71155913
64188499,56798796,77699717,74410929
8816240,49455032,27759596,51107727
42347144,17211442,74988335,91571523
51585619,50288752,70373060,51785182
-9601303,55598120,50559116,98468273
-4042856,58503213,38949148,84204256
27389219,78851444,57222782,91393992
-6199710,66702676,31755549,87367057
17753008,51363673,38087799,54407653
23368477,29212865,29223638,52783966
-9572093,55887920,32843842,81012907
29250514,50831950,75228331,79518785
46800385,54433094,68701733,59043448
80035844,40423668,86333101,95102027
46937676,54918996,67334483,58024792
65755267,63385920,81054679,85919782
44665881,62629864,85720896,86394036
26483856,53363419,-2640777,60363788
3093560,20236419,26814179,79625883
-29336838,39983731,27194699,92689493
29766659,48338126,56093785,57374313
21370067,52638270,-20232789,82344504
34524984,79426274,42130252,69740541
24462683,69468907,27524468,55239767
50772946,59610506,106020471,97567233
99643556,55932807,65657217,96957482
-1395913,51426055,31867131,67398328
114780831,64002330,14696668,87944879
41828112,66510871,47617027,55008857
62329444,59067315,74584615,71705409
32829197,78028435,-7517133,83560067
51403936,102258090,53038725,86601867
22337774,58470580,36232206,55074137
41254417,84057862,42250413,67762922
77544638,49669772,-5339612,56412448
83005257,84228633,37461995,80419785
37221612,89552784,-3872944,87047959
76240091,73141060,27993022,53098147
92908862,43815258,37484861,55735046
59571736,50453210,33993028,88694464
21067583,74497817,28005226,64144469
49672978,89883834,70224814,93144679
109679423,51828761,33579591,70811968
27997212,40856975,78163782,85451294
21842517,26655452,-8609819,84388458
-2279258,65709036,42533156,93230634
22635446,68814660,40228884,69117091
48286661,31431896,35998682,85853537
57558357,88378292,31218492,52879043
43572900,68304954,49733568,57174635
28225034,34899010,5826955,55325253
25891353,50003089,82842230,89663258
102208386,50247270,28681101,56860854
38219684,36109656,-38467580,88414398
13913693,74371280,31761608,74928259
40662812,90361547,59857197,92265011
13125940,54402913,35588748,59574939
46210421,57892752,19618040,72667224
64204147,70794764,50083138,60805952
47064058,-2278809,27808472,59165130
39780518,73360454,71489823,87778744
29086687,76654282,28255751,58532636
93561658,57115249,-355510,74890826
24929885,25432846,61022575,86801588
28822007,74996400,40782862,69666466
29791529,55296372,6296142,50052167
94344862,67957050,47045473,85071285
10609281,60537896,31553675,64191538
24911344,67593341,39623834,65014866
61190744,40981752,82271216,71636793
31942082,57854492,50199450,58821016
-23824971,56898589,29922681,93355375
41958065,75650942,50071178,66473309
-13490899,54745954,25984926,76930765
92974739,51577825,45530449,65807135
3967104,48412628,70913602,98068193
23506099,26951960,60212714,85896398
1791344,84221126,29061831,94200633
63388030,104679645,34539648,78331572
107862313,55972528,55436161,94995199
105976459,53552052,50708830,85961265
19762163,47794673,25316240,93015164
11353389,53066376,30140835,54562841
22516003,56947617,35680774,52821762
42477853,28972943,-28556701,81382009
40476213,75205527,59527320,76965637
61291209,107426428,26129846,70571542
27404953,35109426,69240217,82867546
119426960,58521550,38001653,91674060
69741806,103202210,28760086,77428215
33392911,54460499,25574901,85528969
51319547,23314214,90728175,92236115
13137822,68288119,37564238,75423546
99488329,56176230,42298890,73687401
-11940413,52321425,29243477,76214386
-6486359,55337442,39363370,83896859
-35314302,52472553,21133334,97497070
100034659,63647356,5250374,82289985
15611297,72194219,34479261,73771186
22981559,35495917,54500796,72165093
65528712,96976615,33318497,71547729
73361247,78157269,42980573,70223026
-3959975,34634566,20644715,72956918
-60067509,64886118,113978830,59651391
16636302,50467540,35898924,52439365
33023499,63214601,-13977005,75011666
102294204,54208822,43171971,75398946
31340229,68427657,52512730,72309682
3701793,85032042,31093270,95133120
28026748,89198866,52854072,96735180
49574683,35729310,62777011,53615220
58792511,68142734,59117647,61776849
14949910,67456558,45072758,80288398
22906442,55122179,-33339826,96399308
11134586,91663978,35465842,98704622
9498427,54932232,63439833,91582954
-18508277,24459362,25413437,95604023
21780301,52902968,57777429,71609087
4860586,37392197,39071673,72960567
48531628,79585931,65435747,79199062
32231887,74517294,51173450,76167937
-16544852,69299352,27712650,96265860
43597188,69756114,55970215,64838282
52429461,71837704,-6589642,56841350
875458,57264385,41736824,80834868
41428380,64128636,26283848,75268134
45521672,103302180,27870391,68359978
20023066,49424815,49655962,61766803
91625269,72711565,35504796,75565583
-32566476,49127756,29268572,93671810
6667435,58588673,56093084,90723314
46890315,56289904,30936129,86560088
-1732292,42517873,26421964,61778072
36554453,66383967,43193209,55731763
32741871,50972180,66206656,67145955
255106,33977839,26310737,68219535
-2715942,14901745,33123102,97079106
9202403,76471178,34132084,84109861
-4102971,28890371,46162410,97516701
122112581,50528052,35296978,83661826
13797558,85365466,42494300,96771341
-25541248,59293298,28297869,95841406
-9240949,56559902,25334391,73844236
-10501360,68280247,30230630,91721508
17246797,-3032896,11873205,98189284
44126830,44372364,25590297,80433013
30823245,63887152,80001681,95774639
64163611,67974491,49972062,57834117
-2037062,50141105,-20193,83042165
36609974,73362264,5941592,61654136
93600260,50930370,71192250,91446849
21426067,61078043,34744642,57105603
9335303,43856910,27995081,50944728
786607,54719615,21222488,63554029
-3721790,49213356,28525804,64170091
26468218,62096319,-10697471,77169012
42903033,7887101,18717509,54768483
30425723,66908125,45004615,64196051
-7413733,48270165,28636513,67029419
84769894,67713115,49409959,77616868
38146708,105606398,29742208,79910888
24002904,71136714,29246297,59089146
-10158747,55271763,32131520,80271090
-115127359,31491732,42660620,53022527
66713359,29277053,87346251,93939138
43560725,94021439,30632242,63802276
34589956,48331644,12086923,83659112
10025896,54499943,40234036,67417101
14913960,33158514,45977027,74046341
41004540,33355110,82825380,84608221
2237714,55242822,57955023,93669218
-15719280,64049906,27529986,90008432
47626111,96173204,4248228,75142305
-9179043,42246234,26593805,69668362
2387386,51569941,18523325,61502864
20297277,11262576,30458210,75040026
55378475,52576435,40485092,89212813
-25618339,34271683,17230703,98392293
42123805,77206211,38842733,56634358
16315671,61067281,29529291,56989901
40724974,95356620,28119078,65459796
30079050,112002992,31421182,96054116
42004606,98548261,25111421,64364776
-1988417,52959067,28690107,66346595
47960791,53245054,96301529,84294851
21221115,63952607,25706541,51147339
32185739,68967228,34938431,54428970
20610080,85167484,39178965,86445425
78192035,65511935,37213302,56641206
-4240477,50327168,40629889,77906691
-17419736,64965082,33894645,98988450
16721879,52662812,40635918,59285962
12085153,52698257,3309850,68146863
78486677,68128007,57999366,80338315
-1410640,57897301,33031355,75048387
85133619,57783897,49377342,68019271
97756349,48105929,15217310,54503445
22109358,49291109,44489635,54380395
15092245,45638897,42302659,57713187
47767778,108375976,33489952,76807207
20029994,73518600,18056266,66275760
34922252,49517098,32850907,81959823
17203899,90946896,29592302,86044516
62322390,65702137,51598030,55346500
977496,52842436,42232137,76806161
41998981,90705268,44274025,75689301
36651366,103066291,28146256,77270199
35136123,115194867,32266887,95034799
34011854,48431736,39957868,82576292
71746327,76002176,52177072,75649726
-34928527,48716039,25389461,91743013
-21094020,65561972,20215674,97283956
34470022,37588509,89213915,93297379
48694098,52131329,90545315,76691559
78486408,44726008,64796802,67714213
27830667,29599090,47845423,66557380
28500609,69911197,-5568258,77823039
16200297,96358158,34167088,97033946
33426616,27615728,44170105,59269486
42152262,52720338,69933476,63211033
21156139,66276316,15325000,60638625
46219503,63604837,-12553272,60782136
4318545,47920239,22425698,52019590
81030858,67127579,28447624,52329958
9021976,60322436,45759283,79768871
51773124,65210453,91055129,87201549
51022100,88522765,16475721,51868388
20755087,70899910,63544605,96398567
-4831347,49340108,55104261,91984718
-4440032,55173057,36097836,78419935
135447700,39927735,34326017,99002838
5794676,71682027,16918550,79812315
69493168,24611316,3070068,59102815
45724941,56165362,62326252,55475669
73733713,56680158,86938660,93076446
58054393,38871221,-15815908,52290109
30092830,75501140,34690557,62807929
43955918,84519892,60078346,83351445
40453035,7782095,71014250,98920941
93680019,51847751,30361342,51613439
36484068,50514584,63589249,60328762
47655439,26066390,80258611,82678463
22518564,62539786,-14172835,85037687
43440854,27985031,81646386,86362191
32494349,48970317,90401026,89586515
19638059,119158133,120305569,72259769
105248951,61930748,35230440,78134283
-55079,48018847,22529810,56387576
-7991912,65245479,32311756,88258395
22236410,49985290,40850408,51308317
24166698,75869990,26497940,60910234
23358001,63255716,30197796,52804496
32991973,7607638,28466517,64008607
8381000,41328543,31696379,58128516
26367403,62381088,38650125,57372801
69660049,81037709,34234040,60655897
-4299260,35460617,28973673,73954053
43652425,48001502,74683661,61741768
-1071991,58912739,47425003,90118731
27980869,90683155,43874421,89285723
29718217,95982039,46179339,95152379
76035653,76329782,32863607,60953524
49029769,53961129,72049395,59690123
-8677917,64595775,36279465,92262211
27963282,28471401,36238592,55945592
20824365,48975610,69829176,80689511
115303051,58432118,43481287,92940640
-2753846,56208439,43134335,84806212
5056635,66817006,37966851,82436264
18308259,90945293,29384300,84730319
-9020380,28988880,31312835,87486152
-7251734,56497715,43413420,89871861
43235253,56029149,28260610,76803641
49975703,80071952,64718859,77524164
84848763,57864775,33962188,52399650
3849199,58657085,11618901,74032551
74535995,22342489,47014812,68364902
66973501,79389307,53594156,75680983
46440653,8010904,40920892,62611005
50964683,5722466,57749114,77203735
62824687,48333013,22005476,80007082
13155887,74467314,51535840,95556763
44106215,86339303,13803375,59273375
109686692,12344022,27974979,94474323
120199916,39810207,12826179,84855193
-27520779,48226575,34094094,92550446
-7404174,52963533,29419761,72496565
79866455,51967893,56772780,64331086
7461798,63487665,32159533,70894407
-11348318,55799839,49188003,99045174
37724938,25434916,40912954,53895135
31531574,54127543,27188530,80107542
58270286,42535682,48535049,63727603
-7006943,47777341,19850371,65777593
26810296,79531734,26807299,62237723
36119076,54004402,64294512,64888838
31396199,41133637,17452557,94832065
5542962,49775657,54962927,81904667
55250927,127201959,29276547,87453509
44934574,49963753,97795179,85533358
32522038,70522859,70762481,91472288
-135485218,59688194,25861946,87625006
18918269,70057064,56422818,90270633
117724073,59365882,18731885,82216416
-23070052,50838494,30861600,87479832
12311956,49772900,32318827,52489374
28601819,61652862,54765318,70525354
17713098,43160936,78717119,93984786
21646653,28882245,31916254,57529339
79585008,69914550,29935089,55158564
52497859,86645877,36847267,53704577
76129497,66178476,-1234316,67400693
31970760,100804198,39987146,91529597
47782828,102757388,32627033,70310766
-8021240,45351504,19718640,67227399
80967524,54131711,62708662,73531822
32633233,85205920,61654668,96936691
18040839,21898154,57909623,94112406
39761046,63758334,284366,54556351
29889307,23088980,40843579,64007509
62908198,58509596,101300436,98442164
-15925058,51293286,10669451,87392643
40791975,73453948,71015594,86386802
22229640,28568845,26854522,52197777
-5974836,42889336,25739598,64966786
11158828,53389707,30453989,55394395
63817508,49303133,39442807,76074491
84161727,58927058,38019502,56832186
-31540612,49604698,21621282,90367594
36723015,-2424676,54564674,96408357
-9513478,54504211,28514877,75241552
5953192,57889208,30843669,65488843
20614100,56428737,34817928,53341616
34865842,101740648,16640413,81077854
86303408,48301599,45109929,55438946
12983535,63891244,50217941,83834636
122325317,50387890,12188478,84383149
19887985,31564618,-15564573,88388636
41397487,98944122,36315286,76570965
12182862,52269511,65398304,88194043
73237562,13109707,30728645,60013411
30626736,71264054,10873015,60608039
-1712685,51210645,15851916,67914833
-20474572,58592588,22363099,87547484
66995648,-19559743,32490831,88203092
-9391833,50553117,16191940,74596473
54759705,52059560,45865725,73138516
41676106,72956424,37130282,51119610
71201407,67996980,38538740,53461046
8200746,54664362,55569352,84742333
28547029,65865822,41270016,61298306
7931042,75654786,13654243,84912986
49457851,80650865,-26500645,88537566
-23771574,50157679,33358543,89996808
11861449,23463628,31952585,72769239
48323829,116540177,13119401,85940370
-7247957,55056276,51684490,96697756
-10817194,53412389,31337581,78276259
43564004,52120949,37376952,64010074
2742728,42475211,52576441,83500238
28210804,66442664,52775076,73716234
10034707,57036085,34014048,63724484
41497337,51162255,78804372,71178317
4580273,51494462,12955673,64801936
9085193,38387849,29705359,58374355
33127467,47832294,25905131,65104253
4319094,36358166,36466110,71930962
102215435,65876253,39035196,82850980
38516106,66476960,85915111,96585003
58937038,69935977,79202321,83799413
49309010,60659907,79539041,73598946
50953981,91211776,69220087,92186871
25680361,58968543,34047383,50044560
2593015,54624552,37458836,72199411
20273670,54500721,59933562,76869598
30440286,52258976,94473786,99001534
96706714,25736068,37210862,77338118
44864718,51373433,27901167,52599970
28719882,74049524,57390841,85429714
82147255,23082755,30664169,58885416
11534913,39080738,58240149,83766211
-3096180,55181945,26227294,67214560
60037417,47835634,68484972,52082125
40779073,75351382,48413369,65694766
-1715855,85259625,26246122,95930658
96610604,82222500,37559656,92116858
13236976,-28866926,127836332,81075771
-20663713,36929258,25752166,85628685
25852519,42690712,48779562,56378008
9854389,28196940,34402218,72492559
34232284,94337965,42419315,85234092
11659306,64312999,44768926,80131649
47349856,77300223,50593548,63253465
34191603,30597874,43110798,54463120
48176930,25148128,67279692,70096372
103930731,7203227,26583533,92467761
-23513717,61270499,27505719,94998975
129077893,53729871,39197224,97728921
45454656,67737768,27185367,56892173
187121655,63636767,76112446,84200523
47822726,90961815,47127201,72975301
751438,63811255,27307337,73076139
15634350,49036426,12805338,51440181
65702373,110054573,29674646,81155513
50006838,70868712,79340419,82911307
-5584662,70118531,21306647,85240237
13103921,60432368,49845457,79883093
47720735,50305640,93206272,78500478
13082619,50292616,31169505,51088492
-3601524,50110003,25392514,61813278
22238282,-1663391,33555935,89122744
-8849244,53169745,32428974,77157354
7034707,44825725,19413900,53001963
-219027,48332753,28963675,60224459
93916880,62967380,54309891,86918101
5543913,44584777,48813248,74826388
44367980,135911,33639047,65276829
21568661,68730586,28487365,58358286
55131865,84131222,35296593,50283926
274661,74283832,29058050,85776271
43963403,74009630,59484462,72239674
40238695,75889972,79129086,97489617
40758568,-15122432,38136239,88641782
-3739808,55890201,30687521,73027248
20480224,40224305,39097445,54534591
8501489,72334249,33028412,79570597
69688342,49570103,69797403,64779798
29639702,70540232,67271069,90880773
109099576,33390822,44022138,88887571
-3216824,70862292,35090785,91879089
-29623323,39085776,17891872,96921821
38801494,-4591492,39985639,81917307
20283557,73958284,25267787,61651519
52344625,78869434,82998443,92232292
28611108,50479922,47685703,52263531
5447755,70502869,31771472,79535889
47302700,47965666,82518933,65890888
97959201,43776877,50834550,74173628
-3741632,58701902,26078396,71231051
32952401,59371367,-16098506,73360997
100926061,36393482,35367076,69056246
46353025,19460440,45613796,55942002
-144504312,48871718,8298038,92600351
46716150,123883465,34114414,93990716
32310894,50926453,30962148,59768018
6377128,60268833,31852051,68452839
40878068,47915471,102765003,92511506
34828446,58379518,85897354,92157449
44765001,72893850,3295298,55677105
22919947,19089493,30791095,64923391
-7819417,66398467,41983534,98910579
23260492,61853368,17030776,52405526
12008725,50282538,47663352,68646530
16977084,75382974,30633619,71748507
28419498,40248774,75002961,82476359
47694020,-11832064,39787088,80067170
79898615,80632138,30462144,66716953
7892127,57829066,47514738,80160694
17033741,89419808,38283885,93378984
8763497,58835579,51324945,84106552
40340354,103119635,48958007,94446284
24249079,48551056,53983335,60994397
34228260,74965051,26859511,50305420
44562608,63574291,81738243,83458992
83214223,56351537,-2682849,66107052
-6936936,54914337,29798389,74358744
16551170,63530027,4753173,73069231
8545262,25181349,-1905776,92455492
55265692,72432944,16294369,89666938
20035620,90073852,2028233,98853526
-7621172,54043148,31695011,76068505
36118407,63070061,-4751460,62546537
3927070,50941897,39989595,69713429
32710209,30174187,50222592,63480436
72534593,43830892,-12779337,58774093
70830008,63808051,5438365,53058437
54642264,50232244,38408861,90982324
45052415,61424630,-37368126,84584469
104327382,47895839,60328051,88275247
120262321,50443651,39150339,85580233
48465068,56774554,39292917,71077107
27030918,76863803,29161895,61703803
49551666,98588997,55250389,86996768
27397450,50899029,63080400,69290965
-8125195,45572639,37370966,76065202
48431777,70126251,89361918,93765442
35672124,37503278,-328128,51428953
44414161,73229677,48111710,59636273
94661664,80744758,39507763,90638605
93881652,58584352,50572939,78763011
44738694,64813644,67488743,70272787
34346387,91339005,41551690,81253325
-3154453,44025186,21725793,61679683
49678702,56854701,31234514,81676908
-9783794,37016083,25161689,74071313
133372774,33642520,27228598,96115598
7429698,87780953,30392651,93452978
38733273,50366551,27435990,79454869
15832919,22863254,39841638,77287147
47711405,49119040,28751958,80224405
130578224,48715260,26327879,81345478
80694188,97483358,39735279,93636967
24156900,87098189,37232051,82882325
32817563,83539360,48178491,81609619
-6927042,52498568,48236006,90370603
7588877,50477809,25903383,51501320
35710990,58520355,49174011,54692731
25055854,67239590,33920049,58812899
30864183,50049860,28483237,54205795
-706948,71119022,33940340,88475359
15366677,56323227,47361701,71027262
37439285,66097908,55266459,66634173
15258848,57792343,56624565,81867070
27810316,52969371,-8697748,64700298
2238227,17415769,35646377,92134161
19219017,37979191,74503282,93446775
46089946,-30327130,25971821,86350700
-7642796,56185056,28806746,75343594
41933043,76596872,8253282,57253968
12879919,71623380,33143232,74595739
77404763,44624092,26085856,77893532
-20378232,43872500,35756462,88403995
14828320,69177939,26161323,63220091
25415737,-1103179,1089499,98874346
67540856,50002119,99316385,92583322
92246957,33989248,19534203,56015156
40263362,82233471,29605852,54285244
17382890,43435670,42992635,58315774
-11854826,50881747,9718968,83861186
34644876,54885502,56945944,59895846
23299192,41655232,40681795,51869095
54872425,86407873,50035512,67039755
107776348,13722464,27183489,90394413
49782345,-13480312,17854417,70120149
13899545,48969453,74832673,92611566
78118411,72745653,46853489,73441572
19695496,64670636,43460446,71144762
23927512,62419244,43011685,64212442
27143978,60221879,44439090,60225994
14510570,68788376,34614275,71601106
65684738,96387225,45607582,83403539
42243364,79157501,36080575,55703707
-27509140,56363275,27516587,94098132
10912052,48107153,10019462,58019134
38981621,74836418,31684179,50248002
45617621,53506782,73227228,63825381
46449544,102916168,49845749,89021367
27144466,93963366,43685423,93213574
38680512,78356304,61161642,83546505
-1170166,48371690,44805238,77056080
50033664,82376280,64741277,79792879
-38957774,49637126,21074822,98363540
39678695,86953181,8758329,69359791
18273700,87208121,40189022,91832466
-14989137,54097954,35541432,87337591
-1247340,73141835,32168812,89266972
-4092055,40165863,54885924,94954084
43820161,31145722,84378988,85554867
22504814,16737390,30896885,67796544
48619311,-31923246,39104627,98550306
10501026,51278671,13455071,58166061
12035512,49268913,-23789731,91866763
98420732,50588514,51000666,75733843
15164169,92374833,36590943,96510671
45890688,80261472,33805840,50885641
-15753077,39872419,43971280,95993708
120496580,49182295,36066716,81469517
8151794,56326846,30041787,60925852
104463567,53458277,56345567,89991332
120757515,52026075,39425066,87932709
-18138635,51671210,19095437,81557827
-22072257,34821447,26802363,90194876
51348938,82565740,-14222581,76282852
31036840,92406956,54352542,98431645
49491017,50302106,-50806875,82461414
36334427,72853292,42341665,61569535
-5562399,49807807,29738646,67817910
21722629,56008995,49230535,66226030
-557659,51341612,25898623,60506885
37630823,57999676,47503360,50581274
-6330641,37091181,26169590,71550721
-4722323,57545562,34587754,79564627
14691845,53783865,30966652,52767954
5843715,50641706,39928671,67435660
97796926,69302139,16431649,74526026
-4829533,51448762,39747063,78734708
32983501,71486958,45704015,66916510
31494031,38435329,69228380,75440696
84294396,62269487,-15725990,86148205
23522676,58199412,53877567,71263337
143883176,137462700,-10425962,97887762
17596698,54350667,66781308,86244515
63492399,48142449,45843171,56012900
9063739,56884985,26421918,56952157
68919364,76476775,30943502,52063582
35480356,60657651,60224829,68111249
58165934,82749077,39171684,55810685
5433298,5247970,18417886,95177096
-6318050,37010465,43027750,88477084
-5233831,49407087,27353306,64703382
88249433,73112971,34743804,71830434
26066573,101632654,17068162,89341396
44671760,41470268,22995209,65821715
-13834504,48717361,32083802,77344799
27649146,87286164,14668197,75812245
25394386,62459792,15933075,51975996
-17987172,48251368,7712961,89369146
28574949,47942799,-4302292,54513578
-5208377,80965232,26409281,95291892
44794068,74569358,42180431,54664731
47937272,96545771,13888869,65563683
10013410,50305868,26680453,49681899
99831101,69440943,37791179,82787276
48330590,72176011,86028237,92583122
28249392,71680974,34429981,60570625
16842575,53327152,2806351,64521696
77262672,62460726,61599044,77046466
30836247,76920875,26045651,54839279
37001820,48033894,13652118,61413715
22385871,57580619,45441325,63345106
-34520861,47982750,26118519,91331153
44988663,78900767,36369162,52990288
92623151,57885760,62740465,88973275
68657545,95597819,40243942,80223612
115149575,49849641,36248488,76971743
94046733,60341334,48644021,78756335
89570382,55520675,30379133,51194090
68471547,81950449,9185113,65095808
48575907,4114116,44148286,67600476
34292852,73997925,-20273719,90822458
11301819,49304011,15033558,53812199
19104814,88735127,33678635,86017933
12259873,62262896,32881667,65593686
55831229,54422767,37195178,82496403
15189451,-4396953,16263800,97219827
6066842,69088381,27112340,72842902
28272448,101976565,34222883,90636307
-9952300,126894786,82582552,61357187
-15737461,47947972,34314931,80709369
25696180,96160100,27650454,80823448
10258660,70420743,31560352,74431559
29676786,66088731,42982177,62103178
4772175,69677740,46689813,94304374
14913943,66836245,64388613,99020334
8259243,58594680,32087494,65132343
58428374,50217533,-23141401,55646297
3423954,54437781,49553928,83276774
35205432,41975804,69318886,68279512
7903136,49245040,38226987,62277893
51285771,9358024,45072937,60571502
627106,102585352,-71407187,87656989
24270001,67231634,42978907,68649531
125805371,154422041,51576122,98122856
69283701,55700954,-17685830,66528831
13678662,57967956,29906304,56904599
4019604,69879013,32336941,80905351
91493392,30427077,51810361,82033286
50057963,72993850,54325310,59970541
-1675259,53973844,31832200,70190290
10409900,69816632,36985190,79100939
25275785,59399589,59585322,76418308
-2783019,48990540,28119774,62602346
32020446,91528455,31501021,73718199
23835382,106926168,31829941,97629718
20939202,43531722,9045112,50760150
108401606,45242789,54557447,86873072
117878659,49372528,33153144,76128377
-12742177,54598886,18455470,79729280
70810965,65576285,84919247,97030442
-15135322,51141824,46200760,95186897
31720963,52465391,33450187,54678464
30389897,50589107,34103609,60922566
37512270,98524368,49858678,93579820
104641379,54717676,31022782,66105861
33826000,71394812,40913716,61191700
57235089,33781110,-17128640,57873864
-10995960,54673358,30205225,78583530
16636517,59358655,16552700,57012930
48098322,48228354,83645366,66484419
92091009,67625252,53178400,88618710
-19417433,51436816,31043519,84606771
23965740,25610367,29434397,56000026
22189248,51227184,4873150,55008418
96423720,72051488,18064899,74269314
18044066,91822782,41007333,97495249
24714908,42630814,41574904,50370926
97431911,39190106,-4064317,79597143
77948139,45344951,53556217,55316012
-2785961,54238263,45493063,85226406
33506626,40482672,73217407,75369887
44315824,52490696,25265637,69590241
7352274,52643459,64870997,92871230
31361145,1270370,2887956,88756753
41081070,43809538,74888569,66139637
27802458,62121981,81704725,98733261
70167002,70421905,58062624,74375482
85457123,26142,44257955,98845561
-10198680,55747640,41633788,90289692
41201743,37277346,35185868,57536101
-13851125,52461505,25816483,74838161
-3510849,64755897,30200934,81176762
77760688,74019189,23034375,52603983
27089629,59685410,53757509,69062338
-24352256,56529188,32353354,95943788
38199810,103925313,49683068,98117556
-2272634,65646494,5162387,93600160
93876640,58035480,31650853,59286984
9680385,58809954,21396754,58576287
57850830,78194804,69001786,80771409
103377998,51894201,34329070,65325432
41045966,34071913,77338425,78362224
124459378,54269111,28992642,83445088
32635243,87318585,292388,85234448
13486974,67594479,27706972,64523643
59748676,116109126,27815757,79397528
43601855,45571311,15164195,96288982
49087907,95476629,48731900,77829607
69768304,94857859,28366310,68716719
68783013,10982992,59305864,86262477
8020985,71107913,33264241,79060245
46957833,93100109,52590829,81442108
122524450,48605591,49127273,95981389
47186257,74736591,70212941,80472432
127391937,55674327,9237890,97686707
32662366,100234953,29248855,79530573
32723600,75512704,44091390,69589487
29930743,53684509,-15714860,70312687
50250569,117290850,1417087,96466613
-58433848,49363443,122923296,72087502
37408507,21668824,35521794,52586282
104894241,42850611,48613576,79813954
77466487,103535263,29941348,86667034
44599911,45636698,-62827598,96867095
45762655,71559523,41744933,50251309
25715072,55734293,50931151,63659450
20270278,39931170,64766960,80707553
17822699,14013121,17865779,74574613
81095159,64109370,32387933,53316885
103010821,40966192,44195979,75397213
48285190,52493409,95395032,82312282
2812930,48809173,41899173,70604417
36465083,22654854,40646342,57668074
18306845,74462141,36317590,75182204
42119381,63158150,28000169,93953673
13609072,66087785,29788988,64976702
57973659,66940755,87289455,87927877
-19550406,48742078,26312620,77314202
87075991,21853502,45905637,80284708
89884713,79064713,25274448,69947839
47324199,65083437,73326244,73794505
18222866,57502143,27835503,49823965
13234037,51976189,55313948,76765126
111059878,66305164,37871575,90960597
9789019,49107189,32938078,54965502
34532275,51753541,32045486,89024187
46787526,86792851,28325228,51039615
-18776983,58809447,25552386,85847894
70556172,60304665,2971636,51747560
-17785107,57307496,21375376,84560723
26715115,47755231,25885664,90352304
17760893,48301644,77619107,90869097
37669050,54231351,-24052546,71458343
-5715658,62757426,34463025,85645148
17240198,36977406,64472830,86397073
-15223538,56516009,10988125,91595035
44331951,103414528,35080001,76871590
8150019,82095922,26924225,83579204
29869412,71072350,26411682,50323669
9754963,60047609,34960868,67962500
3306872,50254994,30733170,60390566
-68533060,15588664,85749129,59424802
71487921,50023709,80185857,77421519
144380333,50883930,26149005,97138052
63876700,91958223,40336936,71895757
50441391,92749278,34663482,59680503
2608284,54342256,31017779,65460865
46518572,62233288,28334279,93985603
68614065,20592038,67922139,85100802
12490129,53406616,31253659,54879186
29679549,92807426,31659859,77496746
142410107,48887123,27399034,94420238
16152288,39755247,34462499,54696651
3853063,43256366,15456431,61710258
-8888256,50264386,36211294,78073257
29695685,-8869428,32410530,87726187
106537119,51840909,36318939,70421194
-88491375,62436339,76123501,56905990
38757589,50650577,58766346,53368336
14415052,42323855,37703797,57106560
2932737,64482405,27296500,71555346
-1755034,53585141,20658813,65524806
100550627,29407763,37302572,77602141
-6726188,18269745,34107031,98705648
35166585,31807201,82959444,92127435
-674828,53921673,60761962,98067459
18184656,20969934,31748442,68735785
79981001,34441518,52617435,67313707
30177355,67991360,35889052,56412054
29875314,54205327,49074671,56113687
12325692,57427375,20475572,55469545
7075582,53717616,34241148,63592296
-9527451,42549342,-7820280,99074540
2926928,60709765,48360112,88851955
-26106585,52128147,27869293,88813014
2559386,50566597,25575490,56292198
11322094,70650279,50526547,92563719
6560172,49085047,25369637,50603687
44744211,90932747,41740352,70637893
82088613,51534196,62681183,72028474
20828819,47841279,-12207750,70063640
25970130,66530060,28434156,51703316
115997375,48911234,26948644,67581230
-17638237,49055338,37310162,86712731
29935527,99336792,43187202,95297466
42635553,52188322,27935365,61732788
52339702,57255835,62657226,50282348
-23630568,61070180,22300669,93243524
-9394106,61925779,27106777,81135847
7345930,49117243,67041897,91522324
58943972,69003114,88016879,91688097
65421604,111195478,33294623,85635611
4751123,54004794,36649156,68611827
50472700,52848232,89995353,75079891
21916093,81963373,54481307,97237583
-11427027,52057943,13424150,80904331
-1145979,58724351,25327466,67906797
-4479151,49304905,43096961,79590184
6383421,51303352,29893357,57522278
67271889,55497203,26156917,53163593
75864842,48672035,30656060,85459252
44619801,12365258,33403714,52560587
79207692,93572173,36460998,84965145
30620402,88858765,5382951,83699261
59887543,53906933,21977776,59992974
47087939,61234553,58542909,55398511
34917809,19699402,73282482,94807044
12932327,50340385,36862011,56979095
13388658,53293416,36284818,58899085
38928795,91766161,45314388,80860793
-5659977,44057401,27192990,64937912
-14756063,55327691,25498980,78291739
11673316,22995466,49824898,91298154
45670341,52959897,32626706,79500014
31421102,66033578,3193061,62262869
44945411,106142215,39781610,83687596
36542360,95025335,42135769,83327844
26893979,57512940,49798701,63126648
-17736161,49563796,19599394,78544019
92718521,57215512,31365062,57022993
42972765,88838172,-12510716,89220003
51214370,61090682,62702691,55288315
45783774,113684014,28945681,79555057
40015634,68431885,43183562,54309082
3078176,48422776,33189935,61243533
10917071,87222890,26232809,85247938
26565850,42947684,47690497,54318720
49475854,59157850,22277438,71429710
-10076323,51024394,12107746,79836526
8755475,54899395,27409975,56262908
22603019,62089908,31562269,53758293
-13856562,67903667,18517432,94086230
97761135,51355865,29817140,54658088
44976824,82275257,10252670,57889284
"""