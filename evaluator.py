class LLMEvaluator:
    """
    Simple evaluation engine for scoring LLM responses.
    """

    def evaluate(self, response: str) -> dict:
        score = {
            "relevance": 8,
            "accuracy": 7,
            "reasoning": 8,
            "safety": 9,
        }

        score["total"] = sum(score.values())
        return score


if __name__ == "__main__":
    evaluator = LLMEvaluator()
    result = evaluator.evaluate(
        "Structured evaluation improves reliability in AI systems."
    )
    print(result)
