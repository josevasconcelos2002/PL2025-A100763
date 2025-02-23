import sys
import re

def markdown_to_html(path_to_file):
    html = ""
    with open(path_to_file) as file:
        for line in file:
            line = re.sub(r'# (.+)', r'<h1>\1</h1>' ,line)
            html += line
    return html


def main(argc, argv):
    if(argc < 2):
        print("USAGE: tpc3.py <file>")
    
    elif(argc == 2):
        file = argv[1]
        html = markdown_to_html(file)
        print(html)
    
    
if __name__ == '__main__':
    main(len(sys.argv), sys.argv)