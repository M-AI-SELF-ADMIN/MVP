from mvp.memory import VectorMemory


def test_vector_memory_upsert_and_get() -> None:
    memory = VectorMemory()
    memory.upsert("alpha", "hello world")

    record = memory.get("alpha")
    assert record is not None
    assert record.text == "hello world"
