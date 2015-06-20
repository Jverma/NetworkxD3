# NetworkxD3
D3 JavaScript networkx Graphs 

This is an python high-level interface to [Christopher Gandrud](http://christophergandrud.blogspot.com/p/biocontact.html)'s R package [networkD3](https://christophergandrud.github.io/networkD3/). 
It renders [networkx](https://networkx.github.io/) graphs into HTML page containing a beautiful D3 visualization. Hence the name networkxD3 (shamelessly ripped from the original package networkD3), notice the x. 


**Requirements**
- python and R both installed on the system.
- rpy2
- pandas
- networkx



**Install**

	python setup.py install


**Usage**

    import networkx as nx
    from NetworkxD3 import simpleNetworkx
    
    G = nx.Graph()
    H = ["A","B","C","D","E","F","G", "H","I","J"]
    G.add_nodes_from(H)
    G.add_edges_from([("A","B"), ("A","C"), ("A","D"), ("A","J"), ("B","E"), ("B","F"),
	("C","G"),("C","H"), ("D","I")])
	  
	simpleNetworkx(G)
	
This will create an HTML page Net.html which contains the interactive plot. 

For a quick introduction to rpy2, check out [this post on my blog](https://januverma.wordpress.com/2015/05/17/calling-r-from-python-using-rpy2/).
    
    
    






