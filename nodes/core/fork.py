from core.base_node import BaseNode
import asyncio

class ForkNode(BaseNode):
    async def receive(self, message: dict):
        branches = self.config.get("next_branches", [])
        if not branches:
            return
        message["_source"] = self.node_id
        await asyncio.gather(*(self.bus.send(branch_id, dict(message)) for branch_id in branches))
