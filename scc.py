import networkx as nx
import matplotlib.pyplot as plt
import csv
import numpy as np
import subprocess
import sys


def plot_graph(scc_data):
    G = nx.Graph()
    for tuple in scc_data:
        for i in range(len(tuple)-1):
            if tuple[i+1] == '':
                if i == 0:
                    G.add_node(tuple[i])
            else:
                G.add_edge(tuple[i], tuple[i+1])

    g = nx.read_edgelist('./data.txt',create_using=nx.DiGraph())
    plt.figure("DiGraph", figsize=(30, 30))
    nx.draw_circular(g, node_size=2000, \
    node_color='lightgreen', linewidths=0.25, font_size=7, \
    font_weight='bold', with_labels=True)

    pos = nx.spring_layout(G, k=0.3*1/np.sqrt(len(G.nodes())), iterations=600)
    plt.figure("SCC",figsize=(30, 30))
    nx.draw(G, pos=pos, node_size=2000, \
    node_color='lightblue', linewidths=0.25, font_size=7, \
    font_weight='bold', with_labels=True)
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No arguments passed\n',
        'Use the syntax: python scc.py input_filename')
        sys.exit()

    elif len(sys.argv) > 2:
        print('Incorrect syntax\n',
        'Use the syntax: python scc.py input_filename')
        sys.exit()

    elif str(sys.argv[1]) == "--help" or str(sys.argv[1]) == "-H" or str(sys.argv[1]) == "-h" or str(sys.argv[1]) == "--options" :
        print('Use the syntax: python scc.py input_filename')
        sys.exit()
        

    else:
        val = str(sys.argv[1])
        with open("output.txt", "w+") as output:
            subprocess.call(["python", "./scc_algo.py", val], stdout=output)

        with open("output.txt", "r") as f:
            output_data = []
            csv_reader = csv.reader(f, delimiter=',')
            for row in csv_reader:
                output_data.append(tuple(row))

        plot_graph(output_data)