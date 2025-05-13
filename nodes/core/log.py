from core.base_node import BaseNode

class LogNode(BaseNode):
    """
    LogNode class for logging messages.
    """

    async def receive(self, message: dict):
        """
        Log the received message.
        """
        print(f"[LOG] {self.config.get('message')}")
        # Optionally, you can send the message to the next node if needed
        next_id = self.config.get("next_id")
        if next_id:
            message["_source"] = self.node_id
            await self.bus.send(next_id, message)