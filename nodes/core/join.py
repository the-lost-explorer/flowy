from core.base_node import BaseNode

class JoinNode(BaseNode):
    def __init__(self, node_id, type, config, bus, context):
        super().__init__(node_id, type, config, bus, context)
        self.completed = set()

    async def receive(self, message):
        source = message.get("_source")
        if source:
            self.completed.add(source)

        expected = set(self.config.get("wait_for", []))

        if expected.issubset(self.completed):
            next_id = self.config.get("next_id")
            if next_id:
                message["_source"] = self.node_id
                await self.bus.send(next_id, message)
