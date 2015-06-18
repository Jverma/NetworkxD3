# -*- coding: utf-8 -*-
# D3 JavaScript networkx Graphs 
# Author - Janu Verma
# jv367@cornell.edu
# @januverma


import networkx as nx 
from rpy2.robjects.packages import importr
import rpy2.robjects as ro
import pandas as p
import pandas.rpy.common as com


def simpleNetworkx(G):
	"""
	D3 JavaScript networkx graphs using python. 

	This is an python interface to Christopher Gandrud's R 
	package networkD3. 

	Parameters
	----------
	G : A networkx graph. 

	Returns
	-------
	An HTML page containing an interactive visual of the graph. 

	Example
	-------
	>>> G = nx.Graph()
	>>> H = ["A","B","C","D","E","F","G", "H","I","J"]
	>>> G.add_nodes_from(H)
	>>> G.add_edges_from([("A","B"), ("A","C"), ("A","D"), ("A","J"), ("B","E"), ("B","F"),
		("C","G"),("C","H"), ("D","I")])
	>>> simpleNetworkxD3(G)
	>>> Net.html


	References
	----------
	[1] Christorpher Gandrud - https://github.com/christophergandrud/networkD3

	"""

	ro.r('src = c()')
	ro.r('target =c()')
	ro.r('rdf=data.frame()')

	df = p.DataFrame(data=G.edges())

	df_r = com.convert_to_r_dataframe(df)

	ro.globalenv['src'] = df_r[0]
	ro.globalenv['target'] = df_r[1]

	ro.r('rdf=data.frame(src,target)')

	utils = importr('utils')
	utils.chooseCRANmirror(ind=1)


	try:
		networkD3 = importr('networkD3')
	except:
		utils.install_packages('networkD3')
		networkD3 = importr('networkD3')

	try:
		magrittr = importr('magrittr')
	except:
		utils.install_packages('magrittr')
		magrittr = importr('magrittr')


	ro.r('''simpleNetwork(rdf) %>% saveNetwork(file = 'Net.html')''')
	return None

