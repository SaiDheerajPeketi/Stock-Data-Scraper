#Convert IP:PORT:USER:PASSWORD to USER:PASSWORD@IP:PORT
def convert(line):
    line = line.replace("\n","")
    split_list = line.split(":")
    converted_line = ""
    converted_line = split_list[2] + ":" + split_list[3] + "@" + split_list[0] + ":" + split_list[1]
    return converted_line

fr = open('Webshare 10 proxies.txt','r')
fo = open('entire_list.txt','a+')
fom = open('entire_list_modified.txt','a+')

extracted_list = []

while True:
    line = fr.readline()
    fo.write(line)
    if line=="":
        break
    else:
        converted_line = convert(line)
        fom.write(converted_line)
        fom.write("\n")
        extracted_list.append(converted_line)

fr.close()
fo.close()
fom.close()
print(extracted_list)