def top_student(records):
  tot=0
  n=""
  for name in records.keys():
    tot_marks = sum(records[name])
    if tot_marks > tot:
      tot = tot_marks
      n= name
  return n
