from core.base_node import BaseNode

class SetVariableNode(BaseNode):
    async def receive(self, message: dict):
        key = self.config.get("key")
        value = self.config.get("value")
        self.context.set_var(key, value)
        next_id = self.config.get("next_id")
        if next_id:
            message["_source"] = self.node_id
            await self.bus.send(next_id, message)
