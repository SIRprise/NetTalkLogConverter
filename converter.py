#!/usr/bin/env python

"""converter.py: Das Programm strukturiert NetTalk Logdateien neu, sodass diese nach Channels/Querys geordnet sind anstatt nach Zeit."""


__author__ = 'SIRprise'

import sys
import os.path

if len(sys.argv) > 1:
    logfile=(str(sys.argv[1]))

    if os.path.isfile(logfile):
        with open(logfile, 'r', encoding='utf-8', errors='replace') as ins:
            content = []
            for line in ins:
                templine=(line.strip()[1:])
                #templine.decode(encoding='UTF-8', errors='strict')
                templine=templine.split(':', 1)
                content.append(templine)

        ins.close()


        content=sorted(content,key=lambda x: x[0])

        outfile = open('konvertiert'+logfile+'.txt', 'w', encoding='utf-8', errors='replace')


        for item in content:
            templine=("\t".join(str(e) for e in item))
            templine=templine.lstrip(' \t\r\n\0')
            outfile.write("%s\n" % templine)

        outfile.close()
    else:
        print("Logdatei nicht gefunden.")
else:
    print("Bitte Dateiname der Quell-Logdatei als Parameter angeben.")