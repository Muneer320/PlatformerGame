import pickle
import pprint

pickle_in = open(f"level4_data", "rb")
world_data = pickle.load(pickle_in)

pprint.pprint(world_data)