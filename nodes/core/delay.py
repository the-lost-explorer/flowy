import asyncio
from core.base_node import BaseNode

class DelayNode(BaseNode):
    def __init__(self, node_id, type, config, bus, context):
        super().__init__(node_id, type, config, bus, context)
        self.delay_time = config.get("delay_time", 0)

    async def receive(self, message:dict):
        """Delay execution for the specified time."""
        self.logger.info(f"DelayNode {self.node_id}: Delaying for {self.delay_time} seconds")
        await asyncio.sleep(self.delay_time)
        next_id = self.config.get("next_id")
        if next_id:
            message["_source"] = self.node_id
            await self.bus.send(next_id, message)
