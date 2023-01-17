import ast

def parse_init_file(filepath) -> dict:
    
    dict_lines = []
    
    with open(filepath, 'r') as file:
        lines = file.readlines()
        
        add_lines = False
        
        for line in lines:
            
            if add_lines:
                dict_lines.append(adjust_line(line))
            
            if "{" in line:
                dict_lines.append(adjust_line("{" + line.split("{")[1]))
                add_lines = True
            if "}" in line:
                add_lines = False
    
    dict_string = "".join(dict_lines)
    return ast.literal_eval(dict_string)
    
def adjust_line(line):
    return line.rstrip().strip(" ") 




