"""Documentation generation helpers."""

from __future__ import annotations


class DocGenerator:
    """Builds structured technical documents from supplied context."""

    def generate_runbook(
        self,
        title: str,
        owner: str,
        system_name: str,
        failure_modes: list[str],
    ) -> str:
        modes = "\n".join(f"- {mode}" for mode in failure_modes)
        return (
            f"# {title}\n\n"
            f"## Service\n- System: {system_name}\n- Owner: {owner}\n\n"
            "## Detection\n"
            "- Monitor freshness, runtime, error-rate, and row-count anomalies.\n\n"
            "## Common failure modes\n"
            f"{modes}\n\n"
            "## Triage steps\n"
            "- Confirm upstream delivery.\n"
            "- Inspect the latest execution log and validation evidence.\n"
            "- Check schema drift and null-rate alerts.\n\n"
            "## Remediation\n"
            "- Re-run after correcting the root cause.\n"
            "- Backfill missed partitions if required.\n"
            "- Escalate to the owning team if data contract drift persists.\n\n"
            "## Rollback\n"
            "- Disable downstream publication.\n"
            "- Restore the last known-good artifact version.\n"
        )
