from core.base_node import BaseNode

class StartNode(BaseNode):
    async def receive(self, message: dict):
        """
        Start node that initializes the flow and sends a message to the next node.
        """
        next_id = self.config.get("next_id")
        if next_id:
            # Send a message to the next node
            message["_source"] = self.node_id
            await self.bus.send(next_id, message)