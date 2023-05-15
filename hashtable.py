class hashtable_user: 
  def __init__(self, bucket_size):
    self.buckets = []
    for _ in range(bucket_size):
      self.buckets.append([])

  def append(self,key,value): # append("coucou",3)
    hash_key = hash(key)
    indice_bucket = hash_key % len(self.buckets)
    self.buckets[indice_bucket].append((key,value))

  def get(self, key):
    hashed_key = hash(key)
    indice_bucket = hashed_key % len(self.buckets)
    for bucket_key,bucket_value in self.buckets[indice_bucket]:
      if bucket_key == key:
        return bucket_value
      return None
    
  def contains_key(self, key):
    hashed_key = hash(key)
    bucket_index = hashed_key % len(self.buckets)
    for k, v in self.buckets[bucket_index]:
        if k == key:
            return True
    return False