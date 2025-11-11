import sys
if len(sys.argv) == 3:
  script_name = sys.argv[0]
  name = sys.argv[1]
  rollno = sys.argv[2]
  print("user provided input values:")
  print("script name:", script_name)
  print("name:", name)
  print("roll number:", rollno)
else:
  script_name = sys.argv[0]
  name = "soumya"
  rollno = "003"
  print("no input given:")
  print("script name:", script_name)
  print("name:", name)
  print("roll number:", rollno)
