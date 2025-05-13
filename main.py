import json
import asyncio
from core.runner import run_flow
from utils.flow_ascii import build_ascii_flow

if __name__ == "__main__":
    with open("examples/hello_world.json") as f:
        flow_json = json.load(f)
    # ascii_diagram = build_ascii_flow(flow_json)
    # print(ascii_diagram)
    asyncio.run(run_flow(flow_json))
