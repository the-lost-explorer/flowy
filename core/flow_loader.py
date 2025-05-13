from nodes.registry import NODE_TYPES
from core.message_bus import MessageBus
from core.context import FlowContext

def load_flow(flow_json):
    bus = MessageBus()
    context = FlowContext()
    node_instances = {}

    for node_def in flow_json["nodes"]:
        node_type = node_def["type"]
        node_cls = NODE_TYPES[node_type]
        node = node_cls(node_def["id"],node_def["type"], node_def["config"], bus, context)
        node_instances[node_def["id"]] = node
        bus.register_node(node)

    return bus, node_instances
