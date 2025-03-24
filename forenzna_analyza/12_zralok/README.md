1. Outlook msg files are structred storage files, that is why i desassambled it

2. After going through files i noticed file vbaProject.bin which is not usual file in email msg

3. Once i opened this file there was note about flag being sender ip

4. I converted msg into eml, this allowed me to grep for string "Recieved"

5. In the output there was line with flag: ```flag_ip```
