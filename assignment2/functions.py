import xml.etree.ElementTree as ET
from datetime import datetime


def log_as_dictionary(log):
    strip_log = log.strip()
    strip_log = strip_log.replace("\n\n", "\n")
    separated = strip_log.split('\n')
    string_dict = {}
    for i in separated:
        text = i.split(';')
        if not string_dict.get(text[1]):
            string_dict[text[1]] = [text[:1] + text[2:]]
        else:
            string_dict[text[1]] = string_dict[text[1]] + [text[:1] + text[2:]]

    return string_dict


def dependency_graph(log):
    new_dic = {}
    for case in log:
        # for every list of tasks in a case
        for i in range(len(log[case])-1):
            if not new_dic.get(log[case][i]["concept:name"]):
                new_dic[log[case][i]["concept:name"]] = {log[case][i+1]["concept:name"]: 1}
            # if the value is in the new dic
            else:

                if log[case][i+1]["concept:name"] not in new_dic[log[case][i]["concept:name"]]:
                    inside_dic = new_dic[log[case][i]["concept:name"]]
                    inside_dic[log[case][i+1]["concept:name"]] = 1
                else:
                    small_dic = new_dic[log[case][i]["concept:name"]]
                    small_dic[log[case][i+1]["concept:name"]] += 1
    return new_dic


def read_from_file(file):
    opened = open(file)
    contents = opened.read()
    root = ET.fromstring(contents)
    case_dic = {}
    for i in range(5, len(root)):
        aux_list = []
        for j in range(1, len(root[i])):
            values = {}
            for child in root[i][j]:
                if child.attrib["key"] == "time:timestamp":
                    child.attrib["value"] = datetime.strptime(child.attrib["value"], '%Y-%m-%dT%H:%M:%S+01:00')
                if child.attrib["key"] == "cost":
                    child.attrib["value"] = int(child.attrib["value"])
                values[child.attrib["key"]] = child.attrib["value"]
            aux_list.append(values)
        case_dic[root[i][0].attrib["value"]] = aux_list
    return case_dic
