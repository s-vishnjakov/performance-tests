from abc import ABC, abstractmethod

from seeds.builder import build_grpc_seeds_builder
from seeds.dumps import save_seeds_result, load_seeds_result
from seeds.schema.plan import SeedsPlan
from seeds.schema.result import SeedsResult


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
        save_seeds_result(result=result, scenario=self.scenario)

    def load(self) -> SeedsResult:
        """
        Loads seeding results from a file.
        :return: A SeedsResult object containing the data loaded from the file.
        """
        return load_seeds_result(scenario=self.scenario)

    def build(self) -> None:
        """
        Generates data using the builder, using the seeding plan, and saves the result.
        """
        result = self.builder.build(self.plan)
        self.save(result)
