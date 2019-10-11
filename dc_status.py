import subprocess
import re
from datetime import datetime
Hubs = {
    "LegendHub": "172.16.71.71",
    "Paradise": "172.16.48.114",
    "Exotica": "172.16.120.250"
}
command = "/usr/local/bin/nmap -p411 --open -Pn"
#replace path of nmap with your output of 'which nmap'
for Hub in Hubs:
    command += " "+Hubs[Hub]
output = subprocess.check_output(command,shell=True)
ActiveIpList = re.findall(r"\b172\.16\.\d{1,3}\.\d{1,3}\b", str(output))
with open("README.md","w") as MarkDownFile:
    MarkDownFile.write(f'## Last Updated: {datetime.now().date()}  {datetime.now().strftime("%X")}  \n\n')
    MarkDownFile.write('Hub | Address | Status  \n')
    MarkDownFile.write('--- | --- | ---  \n')
    for Hub in Hubs:
        if Hubs[Hub] in ActiveIpList:
            MarkDownFile.write(Hub+'  |  '+Hubs[Hub]+'  |  '+"**online**"+"\n")
    for Hub in Hubs:
        if Hubs[Hub] not in ActiveIpList:
            MarkDownFile.write(Hub+'  |  '+Hubs[Hub]+'  |  '+"offline"+"\n")
    MarkDownFile.write("\n<br><br><br><br>\n")
    MarkDownFile.write("[Github page](https://github.com/manohar-voggu/BPHC-DChubs)<br>")
    MarkDownFile.write("[Web page](https://manohar-voggu.github.io/BPHC-DChubs/)<br>")
    MarkDownFile.write("Inspired by [ShadowKat](https://github.com/katzNplotkin/IIT-Madras-DC-Hubs)")
#To find Active Hubs via command-line: nmap 172.16.71.71 172.16.48.114 172.16.120.250 -p411 --open -Pn | grep -E -o "172[\.]16[\.][0-9]{1,3}[\.][0-9]{1,3}"
