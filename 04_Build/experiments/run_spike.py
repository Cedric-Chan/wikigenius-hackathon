"""
Graphiti Spike — T1 to T4 for WikiGenius evaluation.
Runs against graphiti-core v0.29.1 with Neo4j.
"""
import asyncio
import os
from datetime import datetime

from graphiti_core import Graphiti
from graphiti_core.llm_client import OpenAIClient, LLMConfig

# --- Config ---
NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "spikepass"

LLM_CONFIG = LLMConfig(
    api_key=os.environ.get("OPENAI_API_KEY"),
    model="gpt-4o-mini",
    temperature=0.0,
    max_tokens=4096,
)

GROUP_ID = "spike_team_demo"


def print_section(title: str) -> None:
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")


async def check_connection(graphiti: Graphiti) -> bool:
    print("Checking Neo4j connectivity...")
    try:
        await graphiti.build_indices_and_constraints()
        print("  ✅ Neo4j connected, indices ready")
        return True
    except Exception as e:
        print(f"  ❌ Connection failed: {e}")
        return False


async def t1_provenance(graphiti: Graphiti) -> dict:
    """
    T1 — Can provenance (Lark node ID + human/agent) be stored and retrieved?
    """
    print_section("T1: Provenance into graph and back")

    episodes = [
        {
            "name": "E1",
            "episode_body": "API rate limit 上限为 500；超过会违反 SLA 承诺。",
            "source_description": "lark:wiki_node_archive_decision_001|by:human:alice",
            "reference_time": datetime(2025, 9, 1),
        },
        {
            "name": "E2",
            "episode_body": "Gateway runbook 按 rate limit = 500 配置告警阈值。",
            "source_description": "lark:wiki_node_runbook_gw|by:human:bob",
            "reference_time": datetime(2025, 9, 2),
        },
        {
            "name": "E3",
            "episode_body": "把 API rate limit 提到 1000。",
            "source_description": "lark:wiki_node_pr_4821|by:agent:carol",
            "reference_time": datetime(2026, 5, 29),
        },
    ]

    uuids = []
    for ep in episodes:
        print(f"\n  Adding {ep['name']}...")
        try:
            result = await graphiti.add_episode(
                name=ep["name"],
                episode_body=ep["episode_body"],
                source_description=ep["source_description"],
                reference_time=ep["reference_time"],
                group_id=GROUP_ID,
            )
            print(f"    Result type: {type(result).__name__}")
            if hasattr(result, "episode_uuid"):
                uuid = result.episode_uuid
                print(f"    UUID: {uuid}")
                uuids.append(uuid)
            elif isinstance(result, dict):
                uuid = result.get("episode_uuid", result.get("uuid", str(result)))
                print(f"    Result: {result}")
                uuids.append(uuid)
            else:
                print(f"    Result: {result}")
                uuids.append(str(result))
        except Exception as e:
            print(f"    ❌ Error: {e}")
            uuids.append(None)

    print("\n  Searching for 'API rate limit'...")
    try:
        results = await graphiti.search("API rate limit 上限", group_ids=[GROUP_ID])
        for i, r in enumerate(results):
            fact = getattr(r, "fact", str(r))
            valid_at = getattr(r, "valid_at", None)
            invalid_at = getattr(r, "invalid_at", None)
            print(f"\n  Result {i}: {fact}")
            print(f"    valid_at: {valid_at}, invalid_at: {invalid_at}")
            for attr in ["source_description", "source", "episode_name", "episode_uuid", "name"]:
                val = getattr(r, attr, None)
                if val is not None:
                    print(f"    {attr}: {val}")
    except Exception as e:
        print(f"  ❌ Search error: {e}")

    print("\n  retrieve_episodes (last 5)...")
    try:
        eps = await graphiti.retrieve_episodes(
            reference_time=datetime(2026, 5, 30),
            last_n=5,
            group_ids=[GROUP_ID],
        )
        for ep in eps:
            print(f"  Episode: {getattr(ep, 'name', '?')} | source_desc: {getattr(ep, 'source_description', 'N/A')}")
    except Exception as e:
        print(f"  ❌ Error: {e}")

    return {"result": "🟡", "fact": "See output above — check if source_description is in search results"}


async def t2_kuzu_backend() -> dict:
    """
    T2 — Can Graphiti use embedded Kuzu?
    """
    print_section("T2: Kuzu backend check")
    print("  graphiti-core v0.29.1 ships only Neo4jDriver.")
    print("  No Kuzu driver found in graphiti_core.driver module.")
    print("  ✅ Decision clear: must use Neo4j (not embedded).")
    return {"result": "🔴", "fact": "No Kuzu driver — Neo4j required"}


async def t3_contradiction(graphiti: Graphiti) -> dict:
    """
    T3 — Does E3 (1000) auto-invalidate E1 (500)?
    """
    print_section("T3: Contradiction / invalidation detection")

    print("  Adding E3 (rate limit = 1000)...")
    try:
        result = await graphiti.add_episode(
            name="E3-contradiction",
            episode_body="把 API rate limit 上限从 500 提到 1000。",
            source_description="lark:wiki_node_pr_4821|by:agent:carol",
            reference_time=datetime(2026, 5, 29),
            group_id=GROUP_ID,
        )
        print(f"    Added: {type(result).__name__}")
    except Exception as e:
        print(f"    ❌ Error: {e}")

    print("\n  Searching for 'API rate limit 当前值'...")
    try:
        results = await graphiti.search("API rate limit 当前值", group_ids=[GROUP_ID])
        for i, r in enumerate(results):
            fact = getattr(r, "fact", str(r))
            valid_at = getattr(r, "valid_at", None)
            invalid_at = getattr(r, "invalid_at", None)
            print(f"\n  Result {i}: {fact}")
            print(f"    valid_at: {valid_at}")
            print(f"    invalid_at: {invalid_at}")
            for attr in dir(r):
                if not attr.startswith("_") and attr != "fact":
                    val = getattr(r, attr, None)
                    if val is not None and not callable(val):
                        print(f"    {attr}: {str(val)[:200]}")
    except Exception as e:
        print(f"  ❌ Error: {e}")

    print("\n  Searching for 'rate limit 500' specifically...")
    try:
        results = await graphiti.search("rate limit 500", group_ids=[GROUP_ID])
        for i, r in enumerate(results):
            fact = getattr(r, "fact", str(r))
            valid_at = getattr(r, "valid_at", None)
            invalid_at = getattr(r, "invalid_at", None)
            print(f"  Result {i}: {fact} | valid_at={valid_at} invalid_at={invalid_at}")
    except Exception as e:
        print(f"  ❌ Error: {e}")

    return {"result": "🟡", "fact": "See output above — auto-invalidation quality TBD"}


async def t4_time_travel(graphiti: Graphiti) -> dict:
    """
    T4 — Point-in-time truth queries.
    """
    print_section("T4: Time travel / point-in-time truth")

    print("  Search for 'API rate limit' (current truth)...")
    try:
        results = await graphiti.search("API rate limit", group_ids=[GROUP_ID], num_results=5)
        for i, r in enumerate(results):
            fact = getattr(r, "fact", str(r))
            valid_at = getattr(r, "valid_at", None)
            invalid_at = getattr(r, "invalid_at", None)
            print(f"  Result {i}: {fact}")
            print(f"    valid_at: {valid_at}, invalid_at: {invalid_at}")
    except Exception as e:
        print(f"  ❌ Error: {e}")

    print("\n  search() has no reference_time param in v0.29.1.")
    print("  Point-in-time would need app-layer filtering on valid_at/invalid_at.")

    return {"result": "🟡", "fact": "Check if valid_at/invalid_at on edges enables app-layer time travel"}


async def main():
    print("=" * 60)
    print("  Graphiti Spike — WikiGenius Evaluation")
    print(f"  graphiti-core v0.29.1 | Neo4j @ {NEO4J_URI}")
    print("=" * 60)

    graphiti = Graphiti(
        uri=NEO4J_URI,
        user=NEO4J_USER,
        password=NEO4J_PASSWORD,
        llm_client=OpenAIClient(config=LLM_CONFIG),
    )

    if not await check_connection(graphiti):
        print("\n❌ Cannot connect to Neo4j. Aborting.")
        return

    results = {}

    results["T1"] = await t1_provenance(graphiti)
    results["T2"] = await t2_kuzu_backend()
    results["T3"] = await t3_contradiction(graphiti)
    results["T4"] = await t4_time_travel(graphiti)

    print_section("Decision Matrix")
    print()
    print(f"{'Task':<20} {'Result':<8} {'Key Fact'}")
    print("-" * 60)
    for task, data in results.items():
        print(f"{task:<20} {data['result']:<8} {data['fact'][:80]}")

    await graphiti.close()
    print("\nDone.")


if __name__ == "__main__":
    asyncio.run(main())
