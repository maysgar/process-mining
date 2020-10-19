import assignment2.functions as r

log = r.read_from_file("./../files/extension-log.xes")
dg = r.dependency_graph(log)

for ai in sorted(dg.keys()):
    for aj in sorted(dg[ai].keys()):
        print(ai, '->', aj, ':', dg[ai][aj])

