# resume-cn-career

[![CI](https://github.com/YuShou-C/resume-cn-career/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/YuShou-C/resume-cn-career/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![M8ven Score](https://m8ven.ai/badge/mcp/yushou-c-resume-cn-career-nvpiq1?v=8e0510e7ddc6eef5466f0a5d9582f743)](https://m8ven.ai/mcp/yushou-c-resume-cn-career-nvpiq1?s=readme)

[简体中文](README.md) | **English**

A skill for generating and optimizing Chinese resumes. It covers campus recruiting, experienced-hire applications, senior/management roles, career changes, and bilingual (Chinese/English) submissions.

## Capabilities

- **Generate** — pick the right template for the candidate profile and produce a ready-to-send draft.
- **Optimize** — reorder keywords and evidence against a target job description.
- **ATS check** — score the resume and flag formatting or keyword-coverage risks.
- **PDF export** — produce a PDF with selectable text and no garbled Chinese characters.

## Repository layout

| Path | Purpose |
| --- | --- |
| `SKILL.md` | Main entry point and profile-based routing |
| `mcp_resume_cn_career.py` | MCP server exposing `generate` / `optimize` / `ats_check` / `export_pdf` |
| `references/` | Templates, best practices, scoring checklist, ATS guide |
| `scripts/generate_resume_pdf.py` | PDF generation script |
| `examples/` | Sample input JSON (anonymized) |
| `tests/` | Minimal regression tests |

## Quick start

1. Install the Python dependencies (only `reportlab` is required):

```bash
python -m pip install -r scripts/requirements.txt
```

2. Generate a Chinese resume PDF:

```bash
python scripts/generate_resume_pdf.py --input examples/chinese_resume.json --output outputs/张三_高级软件工程师_2026.pdf --format chinese
```

3. Generate a bilingual resume PDF:

```bash
python scripts/generate_resume_pdf.py --input examples/bilingual_resume.json --output outputs/ZhangSan_Senior_Engineer_2026.pdf --format bilingual
```

## MCP server usage

Install the MCP SDK:

```bash
python -m pip install mcp
```

Start the server locally:

```bash
python mcp_resume_cn_career.py
```

Example Claude Desktop configuration (`claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "resume-cn-career": {
      "command": "python",
      "args": ["path/to/mcp_resume_cn_career.py"],
      "cwd": "path/to/resume-cn-career"
    }
  }
}
```

The `resume_skill` tool supports four actions:

| action | Description |
| --- | --- |
| `generate` | Build a structured resume draft |
| `optimize` | Reorder keywords and evidence against a job description |
| `ats_check` | Static ATS check (score, issues, keyword coverage) |
| `export_pdf` | Export a PDF with selectable, non-garbled Chinese text |

The tool also declares all four MCP behavior hints (`annotations`), so hosts can warn users before calling it:

| Hint | Value | Rationale |
| --- | --- | --- |
| `readOnlyHint` | `false` | `output_json_path` / `output_pdf_path` write to disk |
| `destructiveHint` | `true` | Existing output files are overwritten |
| `idempotentHint` | `true` | Repeating the call with the same input yields the same result |
| `openWorldHint` | `false` | No network access; only local files and local scripts |

## Input format

- `format`: `chinese` or `bilingual`
- `contact`: required; name, phone, email, and other contact details
- `summary`: Chinese summary (used in `chinese` mode)
- `sections`: structured Chinese sections (used in `chinese` mode)
- `zh` / `en`: separate summaries and sections for bilingual mode

See the files in `examples/` for the full field list.

## Compatibility

- On Windows, system CJK fonts (Microsoft YaHei / SimSun / SimHei) are preferred.
- If no system font is found, the script falls back to the built-in `STSong-Light` CID font, so Chinese text never renders as garbage.
- JSON input supports both UTF-8 and UTF-8 with BOM.

## Testing

```bash
python -m pip install pytest mcp reportlab
python -m pytest tests/
```

CI runs the suite on Ubuntu and Windows across Python 3.10–3.12.

## Notes

- All resume content must be truthful — never invent experience, education, certificates, or metrics.
- Run through `references/analysis-checklist.md` before exporting.
- Tailor a version per job description instead of sending one generic resume everywhere.

## License

[MIT](LICENSE)
