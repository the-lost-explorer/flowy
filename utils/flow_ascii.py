def build_ascii_flow(flow_json):
    nodes = {node["id"]: node for node in flow_json["nodes"]}
    edges = []

    for node in flow_json["nodes"]:
        node_id = node["id"]
        node_type = node["type"]
        src = f"{node_type}:{node_id}"

        # collect next targets
        targets = []
        config = node.get("config", {})
        if "next_id" in config:
            targets.append(config["next_id"])
        if "next" in config:
            targets.append(config["next"])
        if "next_branches" in config:
            targets.extend(config["next_branches"])

        for target_id in targets:
            if target_id in nodes:
                target_type = nodes[target_id]["type"]
                tgt = f"{target_type}:{target_id}"
                edges.append((src, tgt))

    return generate_ascii(edges)


def generate_ascii(edges):
    from collections import defaultdict

    # Build adjacency list
    children = defaultdict(list)
    for src, tgt in edges:
        children[src].append(tgt)

    visited = set()
    lines = []

    def dfs(node, prefix="", is_last=True):
        if node in visited:
            return
        visited.add(node)

        connector = "└── " if is_last else "├── "
        lines.append(f"{prefix}{connector}{node}")

        next_prefix = prefix + ("    " if is_last else "│   ")
        for i, child in enumerate(children.get(node, [])):
            dfs(child, next_prefix, i == len(children[node]) - 1)


    all_targets = {tgt for _, tgt in edges}
    roots = [src for src, _ in edges if src not in all_targets]
    if not roots:
        roots = list(set(src for src, _ in edges)) 

    for i, root in enumerate(roots):
        dfs(root, "", i == len(roots) - 1)

    return "\n".join(lines)
