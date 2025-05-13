from core.base_node import BaseNode

class ConditionNode(BaseNode):
    async def receive(self, msg: dict):
        ctx = self.context

        # Check the `if` condition
        if_config = self.config.get("if")
        if if_config and self._evaluate(if_config["condition"], ctx):
            next_id = if_config["next_id"]
            self.logger.info(f"{self.__class__.__name__}:{self.node_id}: IF matched, going to {next_id}")
            msg["_source"] = self.node_id
            await self.bus.send(next_id, msg)
            return

        # Check all `else_if` conditions
        for elif_conf in self.config.get("else_if", []):
            if self._evaluate(elif_conf["condition"], ctx):
                next_id = elif_conf["next_id"]
                self.logger.info(f"{self.__class__.__name__}:{self.node_id}: ELSE IF matched, going to {next_id}")
                msg["_source"] = self.node_id
                await self.bus.send(next_id, msg)
                return

        # Default `else`
        else_conf = self.config.get("else")
        if else_conf:
            next_id = else_conf["next_id"]
            self.logger.info(f"{self.__class__.__name__}:{self.node_id}: ELSE fallback, going to {next_id}")
            msg["_source"] = self.node_id
            await self.bus.send(next_id, msg)

    def _evaluate(self, condition: str, context: dict) -> bool:
        try:
            return bool(eval(condition, {"__builtins__": {}}, {"context": context}))
        except Exception as e:
            self.logger.error(f"{self.__class__.__name__}:{self.node_id}: Condition error: {e}")
            return False
