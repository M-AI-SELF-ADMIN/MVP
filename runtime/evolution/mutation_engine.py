def propose_mutation(memory):
    print("[evolution] generating adaptive mutation proposal")

    memory.record(
        "mutation_proposal", {"target": "orchestration_layer", "strategy": "adaptive_scaling"}
    )
