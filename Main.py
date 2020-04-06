from Exponential_lib import *

#Calling the functions in sequence
#dataset      = import_dataset()
#Getting value of r from the dataset
r_list       = get_r_list(dataset)
#Calculating r
r_calculated = calculate_r(r_list)
#Creating the graph
create_graph(r_calculated,dataset,3,1,50)



if __name__ == "__main__":
	import_dataset()