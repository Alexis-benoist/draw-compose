from compose.config.config import ConfigFile
from pygraphviz import AGraph

template = \
    """
 digraph {{
    graph [rankdir=LR];
    node [label="\N",
        shape=box
    ];
    edge [color=gray50,
	arrowhead=normal,
        minlen=2,
    ];
{nodes}
{links}
}}
"""


def format_dest(dest_name):
    if ":" in dest_name:
        return dest_name.split(":")[0]
    return dest_name

def draw():
    cf = ConfigFile.from_filename('docker-compose.yml')
    links = [
        (container_name, link)
        for container_name, config in cf.config.iteritems()
        if 'links' in config.keys()
        for link in config['links']
    ]
    dot = template.format(
        nodes='\n'.join('"{}";'.format(container_name) for container_name in cf.config.keys()),
        links="\n".join('"{}" -> "{}"'.format(s, format_dest(d)) for s, d in links)
    )
    graph = AGraph().from_string(dot)
    graph.draw(path='test.pdf', prog='dot', format='pdf')

print ''
if __name__ == '__main__':
    draw()
