def bad_hash_string(keyword, buckets):
  return ord(keyword[0]) % buckets   #take the first letter of the keyword and trun into numbers
