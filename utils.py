import re


def repair_header_income(filename_rd="./US Fundamental DATA/Annual Data/Income Statement Annual Data.csv", filename_wr="./US Fundamental DATA/Annual Data/temp.csv"):
    
    with open(filename_rd) as f:
        lines = f.readlines()
    print(lines[0])
    lines[0].replace('"', '')
    print(lines[0])
    re.sub("\"","",lines[0])

    with open(filename_wr, "w") as f:
        f.writelines(lines)

