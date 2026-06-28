from issuescout.models.analysis import PredictionResult


class ConsoleFormatter:

    def display(
        self,
        prediction: PredictionResult,
    ) -> None:

        if prediction.prediction is None:
            print("No prediction available.")
            return

        print("=" * 100)
        print("Candidate Ranking")

        for candidate in prediction.candidates:

            print(
                f"PR #{candidate.pull_request.number}"
                f" -> {candidate.score}"
            )

        print("=" * 100)

        print(
            f"Best candidate: "
            f"PR #{prediction.prediction.pull_request.number}"
        )

        print(
            f"Score: "
            f"{prediction.prediction.score}"
        )

        print(
            f"Confidence: "
            f"{prediction.confidence}"
        )

        if prediction.accepted:

            print(
                "Prediction accepted "
                f"(score >= {prediction.threshold})"
            )

        else:

            print(
                "Prediction rejected "
                f"(score below {prediction.threshold})"
            )