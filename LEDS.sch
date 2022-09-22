EESchema Schematic File Version 4
LIBS:TJ-Cyber-cache
EELAYER 29 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 4 6
Title "TJSCH001"
Date ""
Rev "Draft A2"
Comp "Bitwise Ltd."
Comment1 "Crescent House"
Comment2 "Carnegie Campus"
Comment3 "Dunfermline"
Comment4 "KY11 8GR"
$EndDescr
Text Notes 6600 2700 0    50   ~ 0
CCA = Cruise Control Active
Wire Wire Line
	6500 3900 6500 4300
Connection ~ 6500 3900
Wire Wire Line
	6500 3500 6500 3900
Connection ~ 6500 3500
Connection ~ 6500 3100
Wire Wire Line
	6500 3100 6500 3500
Wire Wire Line
	6500 2700 6500 3100
Connection ~ 6500 2700
Wire Wire Line
	6500 2300 6500 2700
Connection ~ 6500 2300
Wire Wire Line
	6500 1900 6500 2300
Connection ~ 6500 1900
Connection ~ 6500 1500
Wire Wire Line
	6500 1500 6500 1900
Text HLabel 4800 4300 0    50   Input ~ 0
SET_LED
Wire Wire Line
	5500 4300 4800 4300
Wire Wire Line
	6300 4300 6500 4300
Wire Wire Line
	5800 4300 6000 4300
$Comp
L Device:LED_ALT D21
U 1 1 614C2736
P 5650 4300
F 0 "D21" H 5650 4200 50  0000 C CNN
F 1 "LSTS-C190YKT" H 6100 4250 50  0000 C CNN
F 2 "LED_SMD:LED_0603_1608Metric_Castellated" H 5650 4300 50  0001 C CNN
F 3 "https://media.digikey.com/pdf/Data%20Sheets/Lite-On%20PDFs/LTST-C190YKT.pdf" H 5650 4300 50  0001 C CNN
F 4 "Yellow" H 5450 4350 50  0000 C CNN "Colour"
F 5 "LSTS-C190YKT" H 5650 4300 50  0001 C CNN "Manu PN"
F 6 "Yellow 588nm LED Indication - Discrete 2.1V 0603 (1608 Metric)" H 5650 4300 50  0001 C CNN "Desc"
F 7 "Digikey" H 5650 4300 50  0001 C CNN "Dist"
F 8 "160-1184-1-ND" H 5650 4300 50  0001 C CNN "Dist PN"
F 9 "Lite-On Inc." H 5650 4300 50  0001 C CNN "Manu"
F 10 "+Inter,-Motor" H 5650 4300 50  0001 C CNN "Config"
	1    5650 4300
	-1   0    0    1   
$EndComp
$Comp
L Device:R R61
U 1 1 614C272B
P 6150 4300
F 0 "R61" V 5943 4300 50  0000 C CNN
F 1 "270R" V 6034 4300 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 6080 4300 50  0001 C CNN
F 3 "-" H 6150 4300 50  0001 C CNN
F 4 "SMD Chip Resistor, 270 ohm, ± 1%, 125 mW, 0805 [2012 Metric], Thick Film, General Purpose" H 6150 4300 50  0001 C CNN "Desc"
F 5 "Farnell" H 6150 4300 50  0001 C CNN "Dist"
F 6 "2502705" H 6150 4300 50  0001 C CNN "Dist PN"
F 7 "Walsin" H 6150 4300 50  0001 C CNN "Manu"
F 8 "WR08X2700FTL" H 6150 4300 50  0001 C CNN "Manu PN"
F 9 "+Inter,-Motor" H 6150 4300 50  0001 C CNN "Config"
	1    6150 4300
	0    1    1    0   
$EndComp
Text HLabel 4800 3900 0    50   Input ~ 0
RESUME_LED
Wire Wire Line
	5500 3900 4800 3900
Wire Wire Line
	6300 3900 6500 3900
Wire Wire Line
	5800 3900 6000 3900
$Comp
L Device:LED_ALT D20
U 1 1 614C271D
P 5650 3900
F 0 "D20" H 5650 3800 50  0000 C CNN
F 1 "LSTS-C190YKT" H 6100 3850 50  0000 C CNN
F 2 "LED_SMD:LED_0603_1608Metric_Castellated" H 5650 3900 50  0001 C CNN
F 3 "https://media.digikey.com/pdf/Data%20Sheets/Lite-On%20PDFs/LTST-C190YKT.pdf" H 5650 3900 50  0001 C CNN
F 4 "Yellow" H 5450 3950 50  0000 C CNN "Colour"
F 5 "LSTS-C190YKT" H 5650 3900 50  0001 C CNN "Manu PN"
F 6 "Yellow 588nm LED Indication - Discrete 2.1V 0603 (1608 Metric)" H 5650 3900 50  0001 C CNN "Desc"
F 7 "Digikey" H 5650 3900 50  0001 C CNN "Dist"
F 8 "160-1184-1-ND" H 5650 3900 50  0001 C CNN "Dist PN"
F 9 "Lite-On Inc." H 5650 3900 50  0001 C CNN "Manu"
F 10 "+Inter,-Motor" H 5650 3900 50  0001 C CNN "Config"
	1    5650 3900
	-1   0    0    1   
$EndComp
$Comp
L Device:R R60
U 1 1 614C2712
P 6150 3900
F 0 "R60" V 5943 3900 50  0000 C CNN
F 1 "270R" V 6034 3900 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 6080 3900 50  0001 C CNN
F 3 "-" H 6150 3900 50  0001 C CNN
F 4 "SMD Chip Resistor, 270 ohm, ± 1%, 125 mW, 0805 [2012 Metric], Thick Film, General Purpose" H 6150 3900 50  0001 C CNN "Desc"
F 5 "Farnell" H 6150 3900 50  0001 C CNN "Dist"
F 6 "2502705" H 6150 3900 50  0001 C CNN "Dist PN"
F 7 "Walsin" H 6150 3900 50  0001 C CNN "Manu"
F 8 "WR08X2700FTL" H 6150 3900 50  0001 C CNN "Manu PN"
F 9 "+Inter,-Motor" H 6150 3900 50  0001 C CNN "Config"
	1    6150 3900
	0    1    1    0   
$EndComp
Text HLabel 4800 3500 0    50   Input ~ 0
CANCEL_LED
Wire Wire Line
	5500 3500 4800 3500
Wire Wire Line
	6300 3500 6500 3500
Wire Wire Line
	5800 3500 6000 3500
$Comp
L Device:LED_ALT D19
U 1 1 614C2704
P 5650 3500
F 0 "D19" H 5650 3400 50  0000 C CNN
F 1 "LSTS-C190YKT" H 6100 3450 50  0000 C CNN
F 2 "LED_SMD:LED_0603_1608Metric_Castellated" H 5650 3500 50  0001 C CNN
F 3 "https://media.digikey.com/pdf/Data%20Sheets/Lite-On%20PDFs/LTST-C190YKT.pdf" H 5650 3500 50  0001 C CNN
F 4 "Yellow" H 5450 3550 50  0000 C CNN "Colour"
F 5 "LSTS-C190YKT" H 5650 3500 50  0001 C CNN "Manu PN"
F 6 "Yellow 588nm LED Indication - Discrete 2.1V 0603 (1608 Metric)" H 5650 3500 50  0001 C CNN "Desc"
F 7 "Digikey" H 5650 3500 50  0001 C CNN "Dist"
F 8 "160-1184-1-ND" H 5650 3500 50  0001 C CNN "Dist PN"
F 9 "Lite-On Inc." H 5650 3500 50  0001 C CNN "Manu"
F 10 "+Inter,-Motor" H 5650 3500 50  0001 C CNN "Config"
	1    5650 3500
	-1   0    0    1   
$EndComp
$Comp
L Device:R R59
U 1 1 614C26F9
P 6150 3500
F 0 "R59" V 5943 3500 50  0000 C CNN
F 1 "270R" V 6034 3500 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 6080 3500 50  0001 C CNN
F 3 "-" H 6150 3500 50  0001 C CNN
F 4 "SMD Chip Resistor, 270 ohm, ± 1%, 125 mW, 0805 [2012 Metric], Thick Film, General Purpose" H 6150 3500 50  0001 C CNN "Desc"
F 5 "Farnell" H 6150 3500 50  0001 C CNN "Dist"
F 6 "2502705" H 6150 3500 50  0001 C CNN "Dist PN"
F 7 "Walsin" H 6150 3500 50  0001 C CNN "Manu"
F 8 "WR08X2700FTL" H 6150 3500 50  0001 C CNN "Manu PN"
F 9 "+Inter,-Motor" H 6150 3500 50  0001 C CNN "Config"
	1    6150 3500
	0    1    1    0   
$EndComp
Text HLabel 4800 3100 0    50   Input ~ 0
BRAKE_LED
Wire Wire Line
	5500 3100 4800 3100
Wire Wire Line
	6300 3100 6500 3100
Wire Wire Line
	5800 3100 6000 3100
$Comp
L Device:LED_ALT D15
U 1 1 614C26EB
P 5650 1900
F 0 "D15" H 5650 1800 50  0000 C CNN
F 1 "LSTS-C190GKT" H 6100 1850 50  0000 C CNN
F 2 "LED_SMD:LED_0603_1608Metric_Castellated" H 5650 1900 50  0001 C CNN
F 3 "https://media.digikey.com/pdf/Data%20Sheets/Lite-On%20PDFs/LTST-C190GKT.pdf" H 5650 1900 50  0001 C CNN
F 4 "Green" H 5450 1950 50  0000 C CNN "Colour"
F 5 "LSTS-C190GKT" H 5650 1900 50  0001 C CNN "Manu PN"
F 6 "Green 569nm LED Indication - Discrete 2.1V 0603 (1608 Metric)" H 5650 1900 50  0001 C CNN "Desc"
F 7 "Digikey" H 5650 1900 50  0001 C CNN "Dist"
F 8 "160-1183-1-ND" H 5650 1900 50  0001 C CNN "Dist PN"
F 9 "Lite-On Inc." H 5650 1900 50  0001 C CNN "Manu"
F 10 "+Inter,+Motor" H 5650 1900 50  0001 C CNN "Config"
	1    5650 1900
	-1   0    0    1   
$EndComp
$Comp
L Device:R R55
U 1 1 614C26E0
P 6150 1900
F 0 "R55" V 5943 1900 50  0000 C CNN
F 1 "220R" V 6034 1900 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 6080 1900 50  0001 C CNN
F 3 "-" H 6150 1900 50  0001 C CNN
F 4 "SMD Chip Resistor, 220 ohm, ± 1%, 125 mW, 0805 [2012 Metric], Thick Film, General Purpose" H 6150 1900 50  0001 C CNN "Desc"
F 5 "Farnell" H 6150 1900 50  0001 C CNN "Dist"
F 6 "2502698" H 6150 1900 50  0001 C CNN "Dist PN"
F 7 "Walsin" H 6150 1900 50  0001 C CNN "Manu"
F 8 "WR08X2200FTL" H 6150 1900 50  0001 C CNN "Manu PN"
F 9 "+Inter,+Motor" H 6150 1900 50  0001 C CNN "Config"
	1    6150 1900
	0    1    1    0   
$EndComp
Text HLabel 4800 2700 0    50   Input ~ 0
CCA_LED
Wire Wire Line
	5500 2700 4800 2700
Wire Wire Line
	6300 2700 6500 2700
Wire Wire Line
	5800 2700 6000 2700
$Comp
L Device:LED_ALT D17
U 1 1 614C11F6
P 5650 2700
F 0 "D17" H 5650 2600 50  0000 C CNN
F 1 "LSTS-C190YKT" H 6100 2650 50  0000 C CNN
F 2 "LED_SMD:LED_0603_1608Metric_Castellated" H 5650 2700 50  0001 C CNN
F 3 "https://media.digikey.com/pdf/Data%20Sheets/Lite-On%20PDFs/LTST-C190YKT.pdf" H 5650 2700 50  0001 C CNN
F 4 "Yellow" H 5450 2750 50  0000 C CNN "Colour"
F 5 "LSTS-C190YKT" H 5650 2700 50  0001 C CNN "Manu PN"
F 6 "Yellow 588nm LED Indication - Discrete 2.1V 0603 (1608 Metric)" H 5650 2700 50  0001 C CNN "Desc"
F 7 "Digikey" H 5650 2700 50  0001 C CNN "Dist"
F 8 "160-1184-1-ND" H 5650 2700 50  0001 C CNN "Dist PN"
F 9 "Lite-On Inc." H 5650 2700 50  0001 C CNN "Manu"
F 10 "+Inter,+Motor" H 5650 2700 50  0001 C CNN "Config"
	1    5650 2700
	-1   0    0    1   
$EndComp
$Comp
L Device:R R57
U 1 1 614C11EF
P 6150 2700
F 0 "R57" V 5943 2700 50  0000 C CNN
F 1 "270R" V 6034 2700 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 6080 2700 50  0001 C CNN
F 3 "-" H 6150 2700 50  0001 C CNN
F 4 "SMD Chip Resistor, 270 ohm, ± 1%, 125 mW, 0805 [2012 Metric], Thick Film, General Purpose" H 6150 2700 50  0001 C CNN "Desc"
F 5 "Farnell" H 6150 2700 50  0001 C CNN "Dist"
F 6 "2502705" H 6150 2700 50  0001 C CNN "Dist PN"
F 7 "Walsin" H 6150 2700 50  0001 C CNN "Manu"
F 8 "WR08X2700FTL" H 6150 2700 50  0001 C CNN "Manu PN"
F 9 "+Inter,+Motor" H 6150 2700 50  0001 C CNN "Config"
	1    6150 2700
	0    1    1    0   
$EndComp
Text HLabel 4800 2300 0    50   Input ~ 0
SPARE2_LED
Wire Wire Line
	5500 2300 4800 2300
Wire Wire Line
	6300 2300 6500 2300
Wire Wire Line
	5800 2300 6000 2300
$Comp
L Device:LED_ALT D14
U 1 1 614C11E5
P 5650 1500
F 0 "D14" H 5650 1400 50  0000 C CNN
F 1 "KPT-1608SURCK" H 6100 1450 50  0000 C CNN
F 2 "LED_SMD:LED_0603_1608Metric_Castellated" H 5650 1500 50  0001 C CNN
F 3 "http://www.kingbright.com/attachments/file/psearch/000/00/20160808bak/KPT-1608SURCK(Ver.22A).pdf" H 5650 1500 50  0001 C CNN
F 4 "Red" H 5450 1550 50  0000 C CNN "Colour"
F 5 "KPT-1608SURCK" H 5650 1500 50  0001 C CNN "Manu PN"
F 6 "LED, Low Power, Red, SMD, 0603, 20 mA, 1.95 V, 630 nm" H 5650 1500 50  0001 C CNN "Desc"
F 7 "Farnell" H 5650 1500 50  0001 C CNN "Dist"
F 8 "2449875" H 5650 1500 50  0001 C CNN "Dist PN"
F 9 "Kingbright" H 5650 1500 50  0001 C CNN "Manu"
F 10 "-Inter,-Motor" H 5650 1500 50  0001 C CNN "Config"
	1    5650 1500
	-1   0    0    1   
$EndComp
$Comp
L Device:R R56
U 1 1 614C11DE
P 6150 2300
F 0 "R56" V 5943 2300 50  0000 C CNN
F 1 "270R" V 6034 2300 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 6080 2300 50  0001 C CNN
F 3 "-" H 6150 2300 50  0001 C CNN
F 4 "SMD Chip Resistor, 270 ohm, ± 1%, 125 mW, 0805 [2012 Metric], Thick Film, General Purpose" H 6150 2300 50  0001 C CNN "Desc"
F 5 "Farnell" H 6150 2300 50  0001 C CNN "Dist"
F 6 "2502705" H 6150 2300 50  0001 C CNN "Dist PN"
F 7 "Walsin" H 6150 2300 50  0001 C CNN "Manu"
F 8 "WR08X2700FTL" H 6150 2300 50  0001 C CNN "Manu PN"
F 9 "-Inter,-Motor" H 6150 2300 50  0001 C CNN "Config"
	1    6150 2300
	0    1    1    0   
$EndComp
Text HLabel 4800 1900 0    50   Input ~ 0
STATUS_LED
Wire Wire Line
	5500 1900 4800 1900
Wire Wire Line
	6300 1900 6500 1900
Wire Wire Line
	5800 1900 6000 1900
$Comp
L Device:LED_ALT D18
U 1 1 614BDD02
P 5650 3100
F 0 "D18" H 5650 3000 50  0000 C CNN
F 1 "LSTS-C190YKT" H 6100 3050 50  0000 C CNN
F 2 "LED_SMD:LED_0603_1608Metric_Castellated" H 5650 3100 50  0001 C CNN
F 3 "https://media.digikey.com/pdf/Data%20Sheets/Lite-On%20PDFs/LTST-C190YKT.pdf" H 5650 3100 50  0001 C CNN
F 4 "Yellow" H 5450 3150 50  0000 C CNN "Colour"
F 5 "LSTS-C190YKT" H 5650 3100 50  0001 C CNN "Manu PN"
F 6 "Yellow 588nm LED Indication - Discrete 2.1V 0603 (1608 Metric)" H 5650 3100 50  0001 C CNN "Desc"
F 7 "Digikey" H 5650 3100 50  0001 C CNN "Dist"
F 8 "160-1184-1-ND" H 5650 3100 50  0001 C CNN "Dist PN"
F 9 "Lite-On Inc." H 5650 3100 50  0001 C CNN "Manu"
F 10 "+Inter,-Motor" H 5650 3100 50  0001 C CNN "Config"
	1    5650 3100
	-1   0    0    1   
$EndComp
$Comp
L Device:R R58
U 1 1 614BDCFB
P 6150 3100
F 0 "R58" V 5943 3100 50  0000 C CNN
F 1 "270R" V 6034 3100 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 6080 3100 50  0001 C CNN
F 3 "-" H 6150 3100 50  0001 C CNN
F 4 "SMD Chip Resistor, 270 ohm, ± 1%, 125 mW, 0805 [2012 Metric], Thick Film, General Purpose" H 6150 3100 50  0001 C CNN "Desc"
F 5 "Farnell" H 6150 3100 50  0001 C CNN "Dist"
F 6 "2502705" H 6150 3100 50  0001 C CNN "Dist PN"
F 7 "Walsin" H 6150 3100 50  0001 C CNN "Manu"
F 8 "WR08X2700FTL" H 6150 3100 50  0001 C CNN "Manu PN"
F 9 "+Inter,-Motor" H 6150 3100 50  0001 C CNN "Config"
	1    6150 3100
	0    1    1    0   
$EndComp
Text HLabel 4800 1500 0    50   Input ~ 0
SPARE1_LED
Wire Wire Line
	5500 1500 4800 1500
$Comp
L power:+3.3V #PWR0185
U 1 1 614BAA5E
P 6500 1400
F 0 "#PWR0185" H 6500 1250 50  0001 C CNN
F 1 "+3.3V" H 6515 1573 50  0000 C CNN
F 2 "" H 6500 1400 50  0001 C CNN
F 3 "" H 6500 1400 50  0001 C CNN
	1    6500 1400
	1    0    0    -1  
$EndComp
Wire Wire Line
	6500 1500 6500 1400
Wire Wire Line
	6300 1500 6500 1500
Wire Wire Line
	5800 1500 6000 1500
$Comp
L Device:LED_ALT D16
U 1 1 614B2544
P 5650 2300
F 0 "D16" H 5650 2200 50  0000 C CNN
F 1 "LSTS-C190YKT" H 6100 2250 50  0000 C CNN
F 2 "LED_SMD:LED_0603_1608Metric_Castellated" H 5650 2300 50  0001 C CNN
F 3 "https://media.digikey.com/pdf/Data%20Sheets/Lite-On%20PDFs/LTST-C190YKT.pdf" H 5650 2300 50  0001 C CNN
F 4 "Yellow" H 5450 2350 50  0000 C CNN "Colour"
F 5 "LSTS-C190YKT" H 5650 2300 50  0001 C CNN "Manu PN"
F 6 "Yellow 588nm LED Indication - Discrete 2.1V 0603 (1608 Metric)" H 5650 2300 50  0001 C CNN "Desc"
F 7 "Digikey" H 5650 2300 50  0001 C CNN "Dist"
F 8 "160-1184-1-ND" H 5650 2300 50  0001 C CNN "Dist PN"
F 9 "Lite-On Inc." H 5650 2300 50  0001 C CNN "Manu"
F 10 "-Inter,-Motor" H 5650 2300 50  0001 C CNN "Config"
	1    5650 2300
	-1   0    0    1   
$EndComp
$Comp
L Device:R R54
U 1 1 614B1A2C
P 6150 1500
F 0 "R54" V 5943 1500 50  0000 C CNN
F 1 "270R" V 6034 1500 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 6080 1500 50  0001 C CNN
F 3 "-" H 6150 1500 50  0001 C CNN
F 4 "SMD Chip Resistor, 270 ohm, ± 1%, 125 mW, 0805 [2012 Metric], Thick Film, General Purpose" H 6150 1500 50  0001 C CNN "Desc"
F 5 "Farnell" H 6150 1500 50  0001 C CNN "Dist"
F 6 "2502705" H 6150 1500 50  0001 C CNN "Dist PN"
F 7 "Walsin" H 6150 1500 50  0001 C CNN "Manu"
F 8 "WR08X2700FTL" H 6150 1500 50  0001 C CNN "Manu PN"
F 9 "-Inter,-Motor" H 6150 1500 50  0001 C CNN "Config"
	1    6150 1500
	0    1    1    0   
$EndComp
Text HLabel 4800 4700 0    50   Input ~ 0
SPARE3_LED
Wire Wire Line
	5500 4700 4800 4700
Wire Wire Line
	6300 4700 6500 4700
Wire Wire Line
	5800 4700 6000 4700
$Comp
L Device:LED_ALT D23
U 1 1 5FA5973C
P 5650 5100
F 0 "D23" H 5650 5000 50  0000 C CNN
F 1 "LSTS-C190GKT" H 6100 5050 50  0000 C CNN
F 2 "LED_SMD:LED_0603_1608Metric_Castellated" H 5650 5100 50  0001 C CNN
F 3 "https://media.digikey.com/pdf/Data%20Sheets/Lite-On%20PDFs/LTST-C190GKT.pdf" H 5650 5100 50  0001 C CNN
F 4 "Green" H 5450 5150 50  0000 C CNN "Colour"
F 5 "LSTS-C190GKT" H 5650 5100 50  0001 C CNN "Manu PN"
F 6 "Green 569nm LED Indication - Discrete 2.1V 0603 (1608 Metric)" H 5650 5100 50  0001 C CNN "Desc"
F 7 "Digikey" H 5650 5100 50  0001 C CNN "Dist"
F 8 "160-1183-1-ND" H 5650 5100 50  0001 C CNN "Dist PN"
F 9 "Lite-On Inc." H 5650 5100 50  0001 C CNN "Manu"
F 10 "-Inter,-Motor" H 5650 5100 50  0001 C CNN "Config"
	1    5650 5100
	-1   0    0    1   
$EndComp
Text HLabel 4800 5100 0    50   Input ~ 0
SPARE4_LED
Wire Wire Line
	5500 5100 4800 5100
Wire Wire Line
	6300 5100 6500 5100
$Comp
L Device:LED_ALT D22
U 1 1 5FA5FBDD
P 5650 4700
F 0 "D22" H 5650 4600 50  0000 C CNN
F 1 "LSTS-C190YKT" H 6100 4650 50  0000 C CNN
F 2 "LED_SMD:LED_0603_1608Metric_Castellated" H 5650 4700 50  0001 C CNN
F 3 "https://media.digikey.com/pdf/Data%20Sheets/Lite-On%20PDFs/LTST-C190YKT.pdf" H 5650 4700 50  0001 C CNN
F 4 "Yellow" H 5450 4750 50  0000 C CNN "Colour"
F 5 "LSTS-C190YKT" H 5650 4700 50  0001 C CNN "Manu PN"
F 6 "Yellow 588nm LED Indication - Discrete 2.1V 0603 (1608 Metric)" H 5650 4700 50  0001 C CNN "Desc"
F 7 "Digikey" H 5650 4700 50  0001 C CNN "Dist"
F 8 "160-1184-1-ND" H 5650 4700 50  0001 C CNN "Dist PN"
F 9 "Lite-On Inc." H 5650 4700 50  0001 C CNN "Manu"
F 10 "-Inter,-Motor" H 5650 4700 50  0001 C CNN "Config"
	1    5650 4700
	-1   0    0    1   
$EndComp
$Comp
L Device:R R62
U 1 1 5FA5FBE9
P 6150 4700
F 0 "R62" V 5943 4700 50  0000 C CNN
F 1 "270R" V 6034 4700 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 6080 4700 50  0001 C CNN
F 3 "-" H 6150 4700 50  0001 C CNN
F 4 "SMD Chip Resistor, 270 ohm, ± 1%, 125 mW, 0805 [2012 Metric], Thick Film, General Purpose" H 6150 4700 50  0001 C CNN "Desc"
F 5 "Farnell" H 6150 4700 50  0001 C CNN "Dist"
F 6 "2502705" H 6150 4700 50  0001 C CNN "Dist PN"
F 7 "Walsin" H 6150 4700 50  0001 C CNN "Manu"
F 8 "WR08X2700FTL" H 6150 4700 50  0001 C CNN "Manu PN"
F 9 "-Inter,-Motor" H 6150 4700 50  0001 C CNN "Config"
	1    6150 4700
	0    1    1    0   
$EndComp
Wire Wire Line
	6500 5100 6500 4700
Connection ~ 6500 4300
Connection ~ 6500 4700
Wire Wire Line
	6500 4700 6500 4300
Wire Notes Line
	7750 4400 3000 4400
Text Notes 3200 3300 0    50   ~ 10
Only Fitted on Interface
Wire Wire Line
	5800 5100 6000 5100
$Comp
L Device:R R63
U 1 1 5FA59748
P 6150 5100
F 0 "R63" V 5943 5100 50  0000 C CNN
F 1 "220R" V 6034 5100 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 6080 5100 50  0001 C CNN
F 3 "-" H 6150 5100 50  0001 C CNN
F 4 "SMD Chip Resistor, 220 ohm, ± 1%, 125 mW, 0805 [2012 Metric], Thick Film, General Purpose" H 6150 5100 50  0001 C CNN "Desc"
F 5 "Farnell" H 6150 5100 50  0001 C CNN "Dist"
F 6 "2502698" H 6150 5100 50  0001 C CNN "Dist PN"
F 7 "Walsin" H 6150 5100 50  0001 C CNN "Manu"
F 8 "WR08X2200FTL" H 6150 5100 50  0001 C CNN "Manu PN"
F 9 "-Inter,-Motor" H 6150 5100 50  0001 C CNN "Config"
	1    6150 5100
	0    1    1    0   
$EndComp
Wire Notes Line
	3000 2850 7750 2850
Wire Notes Line
	7750 4400 7750 2850
Wire Notes Line
	3000 2850 3000 4400
$EndSCHEMATC
