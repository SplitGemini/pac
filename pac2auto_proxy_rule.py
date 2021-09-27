import re
import os
import json

#daiy_path = os.getcwd()
daiy_path = '../gh-pages/pac'
white_list = "whitelist.pac"

# patterns
china_domains_pattern = r"(?<=china_domains = )\{.+?\}"


with open(os.path.join(daiy_path, white_list), "r", encoding="utf-8") as f:
    result = re.search(china_domains_pattern, f.read(), re.S)

if result != None:
    jsonObj = json.loads(result.group())
    lines =  []
    for key in jsonObj:
        lines.append(key)
    with open(white_list, "w", encoding="utf-8") as f:
        f.write('@@||' + '\n@@||'.join(lines))
else:
    print("not matched")
