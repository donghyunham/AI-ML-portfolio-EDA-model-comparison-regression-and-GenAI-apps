import time
import json
import statistics

from agent import MeetingSummaryAgent
from eval_dataset import EVAL_DATASET

N_REPEATS_TFIDF = 20
N_REPEATS_EMBEDDING = 5


def measure(agent, method_fn, transcript, query, expected, n_repeats):
    times = []
    hit = False
    for _ in range(n_repeats):
        start = time.time()
        chunks = method_fn(transcript, query=query, top_k=3)
        times.append(time.time() - start)
        if any(expected in c for c in chunks):
            hit = True
    return {
        "hit": hit,
        "mean_time_sec": round(statistics.mean(times), 5),
        "stdev_time_sec": round(statistics.stdev(times), 5) if len(times) > 1 else 0.0,
    }


def run_comparison():
    agent = MeetingSummaryAgent()
    rows = []
    tfidf_hits = 0
    embedding_hits = 0
    total = 0

    for sample in EVAL_DATASET:
        transcript = sample["transcript"]
        for case in sample["cases"]:
            query = case["query"]
            expected = case["expected_substring"]
            total += 1

            tfidf_result = measure(
                agent, agent.retrieve_relevant_chunks_tfidf,
                transcript, query, expected, N_REPEATS_TFIDF
            )
            embedding_result = measure(
                agent, agent.retrieve_relevant_chunks_embedding,
                transcript, query, expected, N_REPEATS_EMBEDDING
            )

            if tfidf_result["hit"]:
                tfidf_hits += 1
            if embedding_result["hit"]:
                embedding_hits += 1

            rows.append({
                "sample_id": sample["id"],
                "query": query,
                "tfidf": tfidf_result,
                "embedding": embedding_result,
            })

    summary = {
        "total_cases": total,
        "tfidf_hit_rate": round(tfidf_hits / total, 3),
        "embedding_hit_rate": round(embedding_hits / total, 3),
        "rows": rows,
    }

    print("=== 동일 실행 내 TF-IDF vs Titan Embedding 비교 ===")
    print(f"TF-IDF hit rate: {summary['tfidf_hit_rate']:.1%} ({tfidf_hits}/{total})")
    print(f"Embedding hit rate: {summary['embedding_hit_rate']:.1%} ({embedding_hits}/{total})")
    print()
    for r in rows:
        t = "O" if r["tfidf"]["hit"] else "X"
        e = "O" if r["embedding"]["hit"] else "X"
        print(f"[TF-IDF {t} / Embedding {e}] {r['sample_id']} | Q: {r['query']}")
        print(f"    TF-IDF 평균 {r['tfidf']['mean_time_sec']}초 | Embedding 평균 {r['embedding']['mean_time_sec']}초")

    with open("comparison_results.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    print("\ncomparison_results.json 저장 완료")


if __name__ == "__main__":
    run_comparison()