class MessageBus:
    """
    A simple message bus for sending and receiving messages.
    """

    def __init__(self):
        self.nodes = {}

    def register_node(self, node):
        """
        Register a node to the message bus.
        """
        if node.node_id not in self.nodes:
            self.nodes[node.node_id] = node
        else:
            raise ValueError(f"Node with ID {node.node_id} is already registered.")
        
    async def send(self, node_id: str, message: dict):
        """
        Send a message to a node.
        """
        if node_id in self.nodes:
            await self.nodes[node_id].handle(message)
        else:
            raise ValueError(f"Node with ID {node_id} is not registered.")
        
    # TODO: Possibly add a method to broadcast messages to all nodes?
        