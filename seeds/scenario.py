from abc import ABC, abstractmethod

from seeds.builder import build_grpc_seeds_builder
from seeds.dumps import save_seeds_result, load_seeds_result
from seeds.schema.plan import SeedsPlan
from seeds.schema.result import SeedsResult
from tools.logger import get_logger

logger = get_logger("SEEDS_SCENARIO")


class SeedsScenario(ABC):
    """
    An abstract class for working with seeding scenarios.
    This class encapsulates the general logic for generating, saving, and loading data for tests.
    """
    def __init__(self):
        """
        SeedsScenario class initialization.
        Creates a builder instance for generating seeding data via gRPC.
        """
        self.builder = build_grpc_seeds_builder()


    @property
    @abstractmethod
    def plan(self) -> SeedsPlan:
        """
        Abstract property for getting the seeding plan.
        Must be overridden in child classes.
        """
        ...

    @property
    @abstractmethod
    def scenario(self) -> str:
        """
        Abstract property for getting the seeding scenario name.
        Must be overridden in child classes.
        """
        ...


    def save(self, result: SeedsResult) -> None:
        """
        Saves the seeding result to a file.
        :param result: A SeedsResult object containing the generated data.
        """
        logger.info(f"[{self.scenario}] Saving seeding result to file.")
        save_seeds_result(result=result, scenario=self.scenario)
        logger.info(f"[{self.scenario}] Seeding result saved successfully.")

    def load(self) -> SeedsResult:
        """
        Loads seeding results from a file.
        :return: A SeedsResult object containing the data loaded from the file.
        """
        logger.info(f"[{self.scenario}] Loading seeding result from file.")
        result = load_seeds_result(scenario=self.scenario)
        logger.info(f"[{self.scenario}] Seeding result loaded successfully.")
        return result


    def build(self) -> None:
        """
        Generates data using the builder, using the seeding plan, and saves the result.
        """
        # Преобразуем план сидинга в JSON для логов (без значений по умолчанию)
        plan_json = self.plan.model_dump_json(indent=2, exclude_defaults=True)
        # Логируем начало генерации
        logger.info(f"[{self.scenario}] Starting seeding data generation for plan: {plan_json}")
        # Запускаем генерацию
        result = self.builder.build(self.plan)
        # Логируем завершение генерации
        logger.info(f"[{self.scenario}] Seeding data generation completed.")
        # Сохраняем результат
        self.save(result)
