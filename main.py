# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
  # [assignment] Add your code here 
  f = open(filename, 'r')
  return f.read()


def count_words():
  text = read_file_content("reading_text_files\story.txt")
  # [assignment] Add your code here
  punc_marks = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

  # removing all punctuation marks
  for item in text:
    if item in punc_marks:
      text = text.replace(item, '')

  words_array = text.split(" ")
  words_dict = {}
  count = 0
  
  for i in range(len(words_array)):
    words_array[i] = words_array[i].replace('\n', '')
    words_dict[words_array[i]] = count
    for word in words_array:
      if words_array[i] == word:
        words_dict[words_array[i]] = words_dict[words_array[i]] + 1
    
  return words_dict 
  # return {"as": 10, "would": 20}

print(count_words())