# Note you need gnuplot 4.4 for the pdfcairo terminal.
set terminal pdfcairo font "Gill Sans,8" linewidth 4 rounded
set term postscript eps color linewidth 4 rounded

# Line style for axes
set style line 80 lt rgb "#808080"

set size 0.5, 0.5

# Line style for grid
set style line 81 lt 0  # dashed
set style line 81 lt rgb "#808080"  # grey

set grid back linestyle 81 noxtics ytics
set border 3 back linestyle 80 

set xtics nomirror
set ytics nomirror

set output "latency_bioinf.eps"
set ylabel "Latency (ms)"
set style fill solid 1.00 border 0
set style histogram errorbars gap 2 lw 0.8
set style data histograms
set xtics rotate by -45
set bars 0.5
set log y
set mxtics 10

set key top right

plot 'latency.txt' using 2:3:4:xtic(1) ti "ScanProsite" lw 0.1 lt 1 lc rgb "#A00000", \
         '' using 5:6:7 ti "SuccinctX" lw 0.1 lt 1 lc rgb "#5060D0"
