from tyr.planners.model.apptainer_planner import ApptainerPlanner


# pylint: disable=too-many-ancestors
class LinearComplexPlanner(ApptainerPlanner):
    """The LinearComplex planner wrapped into local apptainer planner."""

    def _file_extension(self) -> str:
        return "hddl"

    def _get_apptainer_file_name(self) -> str:
        return "config-sat-1.sif"


__all__ = ["LinearComplexPlanner"]
