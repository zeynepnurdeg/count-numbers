def count_numbers(string):
 
  dictionary = {}
  
  for num in string:
    if num.isdigit():
      
      if dictionary.get(num) is None:
           dictionary[num] = 0
      
      dictionary[num] += 1
  return dictionary

print(count_numbers("1001000111101"))
print(count_numbers("Math is fun! 2+2=4"))
print(count_numbers("This is a sentence."))
print(count_numbers("4th sentence is 17th line overall"))