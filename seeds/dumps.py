from seeds.schema.result import SeedsResult
import os



def save_seeds_result(result: SeedsResult, scenario: str):
    if not os.path.exists("dumps"):
        os.mkdir("dumps")

    with open(f"./dumps/{scenario}_seeds.json", "w+", encoding="utf-8") as file:
        file.write(result.model_dump_json())


def load_seeds_results(scenario: str) -> SeedsResult:
    with open(f"./dumps/{scenario}_seeds.json", "r", encoding="utf-8") as file:
        return SeedsResult.model_validate_json(file.read())
