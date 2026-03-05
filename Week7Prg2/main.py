def course_ends(courses):
  courses = tuple([x for x in courses if x])
  flc = []
  if len(courses) <= 0:
    pass
  elif len(courses) == 1:
    flc.append(courses[0])
    flc.append(courses[0])
  else:
    flc.append(courses[0])
    flc.append(courses[-1])
    
  return tuple(flc)
