def total_healing(medkits, bandages):
  """Calculates the total health restored."""
  medkit_score = get_medkit_score(medkits)
  bandage_score = get_bandage_score(bandages)
  return medkit_score + bandage_score

def get_medkit_score(num_medkits):
  """Calculates health points from medkits (20 HP each)."""
  num_medkits = num_medkits * 20
  return num_medkits

def get_bandage_score(num_bandages):
  """Calculates health points from pairs of bandages (5 HP per pair)."""
  num_pairs = num_bandages // 2
  score = num_pairs * 5 
  return score

p1_recovery = total_healing(3, 5)

print("Total health recovered: " + str(p1_recovery))
