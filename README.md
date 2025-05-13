# Flowy 🌊

**A modular, dynamic, and event-driven flow-based engine**

Orchestrate complex async logic with branching, conditions, events, and seamless integration with systems like ROS and Modbus.

---
## ✨ Features (planned)

* ✅ Flow-based JSON logic
* ✅ Modular Node system (each node is its own class)
* ✅ Event-driven execution
* ✅ Parallelism via `Fork` and `Join` nodes
* ✅ Built-in variable context for runtime data
* ✅ Supports external triggers (ROS, HTTP, MQTT, Modbus, etc.)
* ✅ Easy integration with ROS and robotics platforms
* ✅ CLI & API-ready runner (FastAPI-friendly)

---

## 📦 Folder Structure

```
flowy/
├── core/                 # Base logic, runner, message bus
├── nodes/                # All node types (fork, log, ROS, etc.)
├── examples/             # Flow JSONs
├── tests/                # Unit + flow tests
├── main.py               # Example CLI entry
└── requirements.txt
```

---

## 🧠 How It Works

Each flow is defined in JSON. Each node is:
* Instantiated as a class
* Communicates via a central `MessageBus`
* Executed asynchronously (for forked branches, triggers, etc.)

Example JSON:

```json
{
  "nodes": [
    {
      "id": "start",
      "type": "StartNode",
      "config": {
        "next": "log1"
      }
    },
    {
      "id": "log1",
      "type": "LogNode",
      "config": {
        "message": "Started!"
      }
    }
  ]
}
```

---

## ⚙️ Getting Started

### 1. Clone

```bash
git clone https://github.com/the-lost-explorer/flowy.git
cd flowy
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt # currently no deps
```

### 3. Run Example Flow

```bash
python main.py examples/hello_world.json
```

---

## 🧩 Node Types (Partial)

| Node           | Purpose                         |
| -------------- | ------------------------------- |
| `StartNode`    | Entry point                     |
| `LogNode`      | Prints message                  |
| `ForkNode`     | Async fan-out to multiple paths |
| `JoinNode`     | Wait for all inputs to finish   |
| `ConditionNode`| Branches based on condition     |
| `Delay`        | Adds a delay to the flow        |
| `Loop`         | Loops through a branch, then continues |
| `SetVariable`  | Sets a variable value           |
| `ROSPubNode`   | Publishes to a ROS topic (planned) |
| `ModbusNode`   | Reads/writes Modbus (planned)   |

More in [docs/nodes.md](docs/nodes.md) (coming soon)

---

## 🔌 Integrations (planned)

* ✅ ROS (pub/sub)
* ✅ Modbus (via `pymodbus`)
* ✅ HTTP (requests & webhooks)
* ✅ MQTT (coming soon)
* ✅ FastAPI for external control (coming soon)

---

## 🛠️ Contributing

Want to add a node? It’s easy!

1. Inherit from `BaseNode`
2. Implement `async receive(self, msg)`
3. Register in the node registry

---

## 📚 Roadmap

* [ ] Adding basic node types, events, and external triggers
* [ ] Visual Flow Editor (like Node-RED)
* [ ] Web dashboard
* [ ] Built-in retry, backoff, loop management
* [ ] Dynamic flow reloading
* [ ] Persistent state backend (Redis, SQLite)

---

## 💬 Example Use Cases (planned)

* Connect anything to anything via modular flow-based logic
* Coordinating robot actions with conditional logic
* Building automation control systems
* Triggering workflows based on sensor inputs
* Lightweight alternative to ROS Behavior Trees
* Prototyping pipelines with modular async control

---

## 🧑‍💻 Author & License

MIT Licensed
Built with ❤️ by \[Amey Parundekar] — PRs welcome!

---
