from core.flow_loader import load_flow

async def run_flow(flow_json):
    bus, _ = load_flow(flow_json)
    await bus.send("start", {})
