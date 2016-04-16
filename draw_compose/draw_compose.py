import argparse

template = \
    """
 digraph {{
    graph [rankdir=LR];
    node [label="\N",
        shape=box,
        style=filled,
        color=".7 .3 1.0"
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


def iter_links(config_file):
    """
    :param config_file: Docker compose config file.
    :yields: the tuples (container-source_name (str), link-destination (str))
    """
    for container_name, config in config_file.config.iteritems():
        if 'links' in config.keys():
            for link in config['links']:
                yield container_name, link


def format_links(config_file):
    """
    :param config_file: Docker compose config file.
    :return: str, the links formatted in dot format.
    example output:
    "web" -> "app"
    "app" -> "db"
    """
    return "\n".join('"{}" -> "{}"'.format(s, format_dest(d)) for s, d in iter_links(config_file))


def format_nodes(config_file):
    """
    :param config_file: Docker compose config file.
    :return: str, the nodes formatted in dot format.
    example output:
    "web"
    "db"
    "app"
    """
    return '\n'.join('"{}";'.format(container_name) for container_name in config_file.config.keys())


def format_dot(yml_path):
    """
    :param yml_path: str, path of the docker-compose yml to draw.
    :return: str, formatted dot template describing the graph.
    """
    from compose.config.config import ConfigFile
    config_file = ConfigFile.from_filename(yml_path)
    return template.format(
            nodes=format_nodes(config_file),
            links=format_links(config_file)
    )


def dot_to_graph(dot, output_path):
    """
    Render by calling graphviz the figure on the output path.
    :param dot: str with the
    :param output_path:
    :return:
    """
    from pygraphviz import AGraph
    graph = AGraph().from_string(dot)
    graph.draw(path=output_path, prog='dot')


def write_dot_file(dot, dot_file):
    if dot_file:
        with open(dot_file, 'w') as f:
            f.write(dot)


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='Path of the docker-compose yml.', default='docker-compose.yml')
    parser.add_argument('-o', '--output', help='Path of the result image.')
    parser.add_argument('-d', '--dot-file', help='Path to write dot file (optional)')
    return parser


def cli():
    parser = get_parser()
    args = parser.parse_args()
    dot = format_dot(args.input)
    write_dot_file(dot, args.dot_file)
    dot_to_graph(dot, args.output)

if __name__ == '__main__':
    cli()
