"""resume-cn-career 的最小回归测试。

运行：
    python -m pip install pytest mcp reportlab
    python -m pytest tests/
"""
from __future__ import annotations

import sys
from pathlib import Path

# 允许直接 import 仓库根目录下的 mcp_resume_cn_career
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import mcp_resume_cn_career as mod


def _sample() -> dict:
    return {
        "name": "张三",
        "target_role": "后端开发工程师",
        "job_type": "社招",
        "industry": "互联网",
        "city": "上海",
        "experience_years": "3 年",
        "phone": "13800000000",
        "email": "zhangsan@example.com",
        "education": "某大学 | 计算机科学与技术 | 本科 | 2020.09 - 2024.06",
        "summary": "3 年后端研发经验，熟悉 Java 与高并发服务。",
        "experiences": [
            "负责订单服务开发，通过缓存优化使接口 P95 延迟下降 40%。",
            "建设监控告警体系，故障恢复时长缩短 35%。",
        ],
        "projects": ["校园即时配送平台 | 核心研发 | 负责订单状态流转设计。"],
        "skills": ["Java", "Python", "MySQL", "Redis"],
        "certifications": ["计算机三级证书"],
        "jd": "Java 后端 高并发 性能优化",
        "bilingual": False,
    }


def test_build_resume_defaults():
    resume = mod._build_resume(
        "", "", "", "", "", "", "", "", "", "", [], [], [], [], "", False
    )
    assert resume["format"] == "chinese"
    assert resume["contact"]["name"] == "未填写姓名"


def test_extract_keywords():
    keywords = mod._extract_keywords("负责 Java 后端开发，优化接口性能")
    assert "java" in keywords


def test_ats_check_scoring():
    resume = mod._build_resume(
        name="张三",
        target_role="后端开发",
        job_type="社招",
        industry="互联网",
        city="上海",
        experience_years="3 年",
        phone="13800000000",
        email="zhangsan@example.com",
        education="某大学 | 计算机 | 本科",
        summary="后端研发",
        experiences=["负责 Java 后端开发与性能优化。"],
        projects=[],
        skills=["Java"],
        certifications=[],
        jd="Java 后端 性能优化",
        bilingual=False,
    )
    report = mod._ats_check(resume, "Java 后端 性能优化")
    assert 0 <= report["score"] <= 100
    assert "keyword_coverage_percent" in report


def test_resume_skill_generate():
    result = mod.resume_skill(action="generate", **_sample())
    assert result["ok"] is True
    assert result["resume"]["contact"]["name"] == "张三"
    assert result["ats_report"]["score"] >= 0


def test_resume_skill_ats_check():
    result = mod.resume_skill(action="ats_check", **_sample())
    assert result["ok"] is True
    assert "keyword_coverage_percent" in result["ats_report"]


def test_tools_declare_required_annotations():
    """目录审核要求每个工具都显式声明四个布尔提示。"""
    import asyncio

    tools = asyncio.run(mod.mcp.list_tools())
    assert tools, "MCP 服务器未注册任何工具"
    for tool in tools:
        annotations = getattr(tool, "annotations", None)
        assert annotations is not None, f"{tool.name} 缺少 annotations"
        for hint in (
            "read_only_hint",
            "destructive_hint",
            "idempotent_hint",
            "open_world_hint",
        ):
            value = getattr(annotations, hint, None)
            assert isinstance(value, bool), f"{tool.name} 的 {hint} 必须是显式布尔值"

