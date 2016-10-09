# The built-in <string>.split() procedure works
# okay, but fails to find all the words on a page
# because it only uses whitespace to split the
# string. To do better, we should also use punctuation
# marks to split the page into words.

# Define a procedure, split_string, that takes two
# inputs: the string to split and a string containing
# all of the characters considered separators. The
# procedure should return a list of strings that break
# the source string up by the characters in the
# splitlist.


def split_string(source, splitlist):
  output = []
  atsplit = True
  for ele in source:
    if ele in splitlist:
      atsplit = True
    else:
      if atsplit:
        output.append(ele)
        atsplit = False
      else:
        output[-1] += ele
  return output


out0 = split_string("This is a test-of the,string separation-code!", " ,!-")
print(out0)
#>>> ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

out1 = split_string("After  the flood   ...  all the colors came out.", " .")
print(out1)
#>>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

out2 = split_string("First Name,Last Name,Street Address,City,State,Zip Code",",")
print(out2)
#>>>['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']
