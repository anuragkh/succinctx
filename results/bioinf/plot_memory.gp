# Note you need gnuplot 4.4 for the pdfcairo terminal.
set terminal pdfcairo font "Gill Sans,8" linewidth 4 rounded
set term postscript eps color linewidth 4 rounded

# Line style for axes
set style line 80 lt rgb "#808080"

set size 0.5, 0.5

# Line style for grid
set style line 81 lt 0  # dashed
set style line 81 lt rgb "#808080"  # grey

set style line 1 lt 1 linecolor rgb "#A00000"
set style line 2 lt 1 linecolor rgb "#00A000"
set style line 3 lt 1 linecolor rgb "#5060D0"

set grid back linestyle 81 noxtics ytics
set border 3 back linestyle 80 

set xtics nomirror
set ytics nomirror

set output "storage_bioinf.eps"
set ylabel "Storage Footprint (GB)"
set style data histogram
set boxwidth 0.4
set style fill solid 1.00 border 0
set yrange [0:]

plot 'memory.txt' every ::0 using 1:3:xtic(2) title "" lc rgb "#A00000" lw 0.1 with boxes,\
    'memory.txt' every ::1 using 1:3:xtic(2) title "" lc rgb "#5060D0" lw 0.1 with boxes
