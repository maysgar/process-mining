import assignment2.functions as r

log = r.read_from_file("./../files/extension-log.xes")

# general statistics: for each case id the number of events contained
for case_id in sorted(log):
    print(case_id, len(log[case_id]))

# details for a specific event of one case
case_id = "case_123"
event_no = 0
print(log[case_id][event_no]["concept:name"], log[case_id][event_no]["org:resource"],
      log[case_id][event_no]["time:timestamp"],  log[case_id][event_no]["cost"])
