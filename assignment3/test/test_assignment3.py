import assignment2.functions as r
import assignment3

mined_model = assignment3.alpha(r.read_from_file("./../files/extension-log.xes"))

def check_enabled(pn):
  ts = ["record issue", "inspection", "intervention authorization", "action not required", "work mandate", "no concession", "work completion", "issue completion"]
  for t in ts:
    print(pn.is_enabled(pn.transition_name_to_id(t))),
  print("")


trace = ["record issue", "inspection", "intervention authorization", "work mandate", "work completion", "issue completion"]
for a in trace:
  check_enabled(mined_model)
  mined_model.fire_transition(mined_model.transition_name_to_id(a))
