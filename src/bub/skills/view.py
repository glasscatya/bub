"""Skill prompt rendering."""

from __future__ import annotations

from bub.prompt_escape import escape_prompt_text
from bub.skills.loader import SkillMetadata


def render_compact_skills(skills: list[SkillMetadata], expanded_skills: set[str]) -> str:
    """Render compact skill metadata for system prompt."""

    if not skills:
        return ""
    channel_skills: list[SkillMetadata] = [
        skill for skill in skills if skill.metadata and skill.metadata.get("channel")
    ]
    lines = ["<basic_skills>"]
    for skill in skills:
        if skill.metadata and skill.metadata.get("channel"):
            continue
        lines.append(escape_prompt_text(f"=== [{skill.name}]({skill.location}): {skill.description} ==="))
        if skill.name in expanded_skills:
            lines.append(f"{escape_prompt_text(skill.body.rstrip())}\n")
    lines.append("</basic_skills>")
    if channel_skills:
        lines.append("<channel_skills>")
        for skill in channel_skills:
            lines.append(escape_prompt_text(f"=== [{skill.name}]({skill.location}): {skill.description} ==="))
            if skill.name in expanded_skills:
                lines.append(f"{escape_prompt_text(skill.body.rstrip())}\n")
        lines.append("</channel_skills>")
    return "\n".join(lines)
