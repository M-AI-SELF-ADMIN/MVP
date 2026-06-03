from mvp.core import Event, EventBus


def test_event_bus_publish_and_replay() -> None:
    bus = EventBus()
    bus.publish(Event(topic="agent.events", payload={"id": 1}))
    bus.publish(Event(topic="telemetry", payload={"status": "ok"}))

    assert len(bus.replay()) == 2
    assert bus.replay("agent.events")[0].payload["id"] == 1
