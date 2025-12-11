from glob import glob

import matplotlib.pyplot as plt
import networkx as nx


def plot(data_fname):
    with open(data_fname) as f:
        text = f.read()

    # Parse edges
    edges = []
    for line in text.splitlines():
        if ":" not in line:
            continue
        src, dsts = line.split(":", 1)
        src = src.strip()
        for d in dsts.split():
            edges.append((src, d))

    G = nx.DiGraph()
    G.add_edges_from(edges)

    # Compute DAG layering (longest-path rank)
    rank = {}
    for node in nx.topological_sort(G):
        preds = list(G.predecessors(node))
        if not preds:
            rank[node] = 0
        else:
            rank[node] = 1 + max(rank[p] for p in preds)

    # Group by layers
    layers = {}
    for n, r in rank.items():
        layers.setdefault(r, []).append(n)

    # Assign vertical layout
    pos = {}
    for layer, nodes in layers.items():
        for i, n in enumerate(nodes):
            pos[n] = (i, -layer)

    # Node colors
    colors = []
    for n in G.nodes():
        if n == "dac":
            colors.append("red")
        elif n == "fft":
            colors.append("skyblue")
        else:
            colors.append("lightgrey")

    plt.figure(figsize=(20, 40))
    nx.draw(
        G, pos,
        with_labels=True,
        node_size=1200 if len(edges) < 100 else 600,
        font_size=24 if len(edges) < 100 else 8,
        arrowsize=40 if len(edges) < 100 else 20,
        arrows=True,
        node_color=colors,
        edge_color="black",
        linewidths=0.3
    )
    plt.axis("off")
    plt.tight_layout()

    plt.savefig(data_fname.replace('..', '.').replace('.txt', '.png'), dpi=150)

if __name__ == '__main__':
    for f in glob('../*.txt'):
        plot(f)
