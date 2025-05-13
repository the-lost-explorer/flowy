from nodes.core.start import StartNode
from nodes.core.log import LogNode
from nodes.core.set_variable import SetVariableNode
from nodes.core.fork import ForkNode
from nodes.core.join import JoinNode
from nodes.core.delay import DelayNode
from nodes.core.condition import ConditionNode
from nodes.core.loop import LoopNode

NODE_TYPES = {
    "StartNode": StartNode,
    "LogNode": LogNode,
    "SetVariable": SetVariableNode,
    "ForkNode": ForkNode,
    "JoinNode": JoinNode,
    "DelayNode": DelayNode,
    "ConditionNode": ConditionNode,
    "LoopNode": LoopNode,
}
