# arbitrary numbers slices lists as odd and even elements. 
def slicer(*a):
  even_list= []
  odd_list= []
  for i in a:
    if i %2 == 0:
      even_list.append(i)
    else:
      odd_list.append(i)
  print("even: ",even_list, "odd list: ", odd_list)

slicer(1, 2, 3, 4, 5, 6,)

# arbitrary numbers with list comprehensiyon 
def org(** data):
  nam= [i for i in data.keys()]
  age = [i for i in data.values()]
  print("names: ", nam)
  print("ages: ", age)
org(beth=26, tak=34, tik=45, tok=34,fat=43)