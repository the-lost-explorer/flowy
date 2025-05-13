# BaseNode class for all nodes in the pipeline
from core.context import FlowContext
from core.message_bus import MessageBus
from core.logger import get_logger
import time

class BaseNode:
    """
    Base class for all nodes in the pipeline.
    """

    def __init__(self, node_id: str = None, type = None, config: dict = None, bus: MessageBus = None, context: FlowContext = None):
        """
        Initialize the base node with a name.

        Args:
            name (str): The name of the node.
        """
        self.node_id = node_id
        self.type = type
        self.config = config if config is not None else {} 
        self.bus = bus # For message passing between nodes
        self.context = context # For shared state between nodes
        self.output = None
        self.logger = get_logger(f"{self.type}:{self.node_id}")

    async def handle(self, msg):
        self.logger.info(f"→ START {self.type}:{self.node_id}")
        start = time.time()
        await self.receive(msg)
        duration = (time.time() - start) * 1000  # ms
        self.logger.info(f"✓ END {self.type}:{self.node_id} in {duration:.2f} ms")

    async def receive(self):
        """
        Run the node. This method should be overridden by subclasses.
        """

        raise NotImplementedError("Subclasses should implement this method.")