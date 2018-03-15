from collections import OrderedDict
import re
from config import read_config


def do_convert(text, labeled):
    i = 0
    result = list()
    while i < len(text):
        entity = 'O'
        if (labeled and int(labeled[0][2]) == i):
            for j in range(int(labeled[0][3]) - int(labeled[0][2])):
                if j == 0:
                    entity = 'B-' + str(labeled[0][1]).upper()
                else:
                    entity = 'I-' + str(labeled[0][1]).upper()
                line = text[i] + ' ' + entity
                result.append(line)
                i += 1
            else:
                del labeled[0]
        else:
            line = text[i] + ' ' + entity
            i += 1
            result.append(line)
    return result


def main():
    files = list(read_config.brat_files)
    for file in files:
        data_labeled = open(read_config.brat_path + file[0], 'r')
        data_orig = open(read_config.brat_path + file[1], 'r')
        result = list()
        text = data_orig.read().strip()
        for line in data_labeled.readlines():
            line = line.strip()
            if not len(line) or line.startswith('#'):
                continue
            line = re.split(r'[\s]', line)
            result.append(line)

        result.sort(key=lambda x: int(x[2]))
        ref_data = do_convert(text, result)
        data_labeled.close()
        data_orig.close()
        with open(read_config.ref_path + 'ref.' + file[0].split('.')[0], 'w') as fw:
            fw.write('%s' % '\n'.join(ref_data))
    else:
        print("Convert complete %d files" % len(files))


if __name__ == "__main__":
    main()
