import copy
import json
import pathlib
import unittest

import jsonschema
import yaml


ROOT = pathlib.Path(__file__).resolve().parents[2]
EXTENSION = ROOT / "experimental" / "agentic-build-handoff"


class BlueprintContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = json.loads((EXTENSION / "agent-blueprint.schema.json").read_text())
        cls.example = yaml.safe_load((EXTENSION / "examples/toy-scout-blueprint.example.yaml").read_text())
        jsonschema.Draft202012Validator.check_schema(cls.schema)
        cls.validator = jsonschema.Draft202012Validator(cls.schema)

    def test_example_matches_current_schema(self):
        self.assertEqual([], list(self.validator.iter_errors(self.example)))

    def test_old_version_and_missing_profile_are_rejected(self):
        old = copy.deepcopy(self.example)
        old["schema_version"] = "0.3-experimental"
        self.assertTrue(list(self.validator.iter_errors(old)))

        missing = copy.deepcopy(self.example)
        missing.pop("assurance_profile")
        self.assertTrue(list(self.validator.iter_errors(missing)))

    def test_unknown_profile_is_rejected(self):
        unknown = copy.deepcopy(self.example)
        unknown["assurance_profile"] = "automatic_production"
        self.assertTrue(list(self.validator.iter_errors(unknown)))


class FictionalScenarioContractTests(unittest.TestCase):
    def test_lean_result_fixture_has_consistent_math_and_stop(self):
        fixture = json.loads((ROOT / "tests/scenarios/lean_result_stop_v04.json").read_text())
        scope = fixture["approved_scope"]
        result = fixture["reported_result"]
        expected = fixture["expected"]

        self.assertTrue(fixture["fictional"])
        self.assertEqual("lean_internal_test", scope["profile"])
        self.assertEqual(
            result["manual_total_minutes"] + result["template_total_minutes"],
            expected["known_minutes_across_methods"],
        )
        self.assertEqual(
            result["manual_total_minutes"] - result["template_total_minutes"],
            expected["difference_across_five_cases_minutes"],
        )
        self.assertIsNone(result["other_team_minutes"])
        self.assertLess(expected["known_minutes_across_methods"], scope["team_time_cap_minutes"])
        self.assertEqual("unproven", expected["cap_exceeded"])
        self.assertIsNone(result["weekly_case_volume"])
        self.assertEqual("unproven", expected["weekly_saving_threshold_met"])
        self.assertGreater(result["known_condition_warnings_missed"], 0)
        self.assertEqual("stop", expected["current_trial"])
        self.assertFalse(scope["external_action_allowed"])


if __name__ == "__main__":
    unittest.main()
