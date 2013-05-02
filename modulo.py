#(1) it is congruent to 372806624339965 modulo 37+10^15; (2) its decimal expansion begins 0.13869616280169693....
remainder = Mod(37+10^15,372806624339965)
#remainder + rational number starts decimal expasion with 0.13869616280169693... will be rational number
#sqrt(1.92) < r < sqrt(1.93)
#sqrt(1.92366159265) 0.138696162816..
r = float(remainder)  + sqrt(1.92366159265)
print(r)
#truncated to 2.54386751320108e14
