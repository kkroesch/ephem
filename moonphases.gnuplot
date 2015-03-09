set terminal png truecolor nocrop font "/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans.ttf" 12 size 640,480
set output 'moon.png'
set grid xtics nomxtics ytics nomytics noztics nomztics \
 nox2tics nomx2tics noy2tics nomy2tics nocbtics nomcbtics
set grid layerdefault   linetype 0 linewidth 1.000,  linetype 0 linewidth 1.000
set xtics border in scale 1,0.5 mirror norotate  offset character 0, 0, 0
set xtics 45 norangelimit
set ytics border in scale 1,0.5 mirror norotate  offset character 0, 0, 0
set ytics autofreq  norangelimit
set xlabel "Azimuth (compass direction, in degrees)"
set xlabel  offset character 0, 0, 0 font "" textcolor lt -1 norotate
set xrange [ 45.0000 : 315.000 ] noreverse nowriteback
set ylabel "Elevation (degrees above horizon)"
set ylabel  offset character 0, 0, 0 font "" textcolor lt -1 rotate by -270
set yrange [ 0.000000 : 90.0000 ] noreverse nowriteback
plot '/tmp/s.dat'u 3:2 w l lc rgb "yellow" lw 2 t "sun path", '/tmp/s.dat' u 3:2:(10) every 4 w circles t "" lc rgb "yellow", '/tmp/m.dat'u 3:2 w l lc 4 lw 2 t "moon path", '/tmp/m.dat' u 3:2:(10) every 4 w circles t "" lc rgb "#ddddff", '/tmp/m.dat' u 3:2:6 every 4 w labels offset character 0,character -1 font "/home/karsten/ephem/moon_phases.ttf,30"   t "", '/tmp/m.dat'u 3:2:4 every 4 w labels font "/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans.ttf,8" tc rgb "#dd0000" t ""
#    EOF
