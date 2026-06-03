from cognition.reflection_engine import reflect
from memory.memory_store import MemoryStore
from evolution.mutation_engine import propose_mutation


def boot():
    print("🧠 PAEP Runtime Booting")

    memory = MemoryStore()
    memory.record("runtime_boot", {"status": "online"})

    reflect(memory)
    propose_mutation(memory)

    print("🌱 Runtime stable")


if __name__ == "__main__":
    boot()
