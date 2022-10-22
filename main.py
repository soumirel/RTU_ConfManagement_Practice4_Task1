def make_parse(file_input_name, file_output_name):
    with open(file_input_name, "r") as graph:
        dependencies = {}
        infos_blocks = graph.read().split(';')[2:-1]
        for block in infos_blocks:
            tokens = block.split()
            if block.find('->') != -1:
                dependencies[tokens[2].lower()].append(tokens[0].lower())
            else:
                dependencies[tokens[0].lower()] = []
        with open(file_output_name, "w") as make:
            research = ""
            for key in dependencies:
                research += str(key + " ")
            make.write('RESEARCH = ' + research + '\n\n')
            make.write(".PHONY = clean\n\n")
            make.write('clean:\n\t@rm -f $^\n\n')
            for key in dependencies:
                current_dependencies = dependencies.get(key)
                make.write(key + ": " + ' '.join(current_dependencies) + '\n')
                make.write('\t' + "@echo " + '\"' + key + '\"' + '\n')
                make.write('\t' + "@touch " + '\"' + key + '\"' + '\n\n')

if __name__ == '__main__':
    make_parse("graph.txt", "make")