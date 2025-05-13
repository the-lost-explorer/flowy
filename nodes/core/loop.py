from core.base_node import BaseNode

class LoopNode(BaseNode):
    async def receive(self, msg: dict):
        condition = self.config.get("condition")
        loop_branch = self.config.get("loop_branch")
        done_id = self.config.get("done_id")
        ctx = self.context

        if self._evaluate(condition, ctx):
            self.logger.info(f"{self.__class__.__name__}:{self.node_id}: condition met → going to {done_id}")
            if done_id:
                msg["_source"] = self.node_id
                await self.bus.send(done_id, msg)
        else:
            self.logger.info(f"{self.__class__.__name__}:{self.node_id}: condition NOT met → looping to {loop_branch}")
            if loop_branch:
                msg["_source"] = self.node_id
                await self.bus.send(loop_branch, msg)

    def _evaluate(self, condition: str, context) -> bool:
        try:
            return bool(eval(condition, {"__builtins__": {}}, {"context": context}))
        except Exception as e:
            self.logger.error(f"{self.__class__.__name__}:{self.node_id}: Error evaluating condition: {e}")
            return False
