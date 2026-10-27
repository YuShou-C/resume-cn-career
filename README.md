# resume-cn-career

[![CI](https://github.com/YuShou-C/resume-cn-career/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/YuShou-C/resume-cn-career/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)

**简体中文** | [English](README.en.md)

中文简历生成与优化 skill，覆盖校招、社招、资深/管理岗、转行与中英双语投递场景。

## 能力概览

- 简历生成：按人群分流生成可投递版本
- 简历优化：对照 JD 做关键词与证据重排
- ATS 自检：检查格式和关键词覆盖风险
- PDF 导出：输出可复制文本、中文不乱码 PDF

## 目录结构

- SKILL.md：主入口与流程分流
- mcp_resume_cn_career.py：MCP 服务器，封装 generate / optimize / ats_check / export_pdf 四个动作
- references/：模板、最佳实践、评分清单、ATS 指南
- scripts/generate_resume_pdf.py：PDF 生成脚本
- examples/：示例输入 JSON（脱敏）
- tests/：最小测试

## 快速开始

1. 安装 Python 依赖（仅需 reportlab）

```bash
python -m pip install -r scripts/requirements.txt
```

2. 生成中文简历 PDF

```bash
python scripts/generate_resume_pdf.py --input examples/chinese_resume.json --output outputs/张三_高级软件工程师_2026.pdf --format chinese
```

3. 生成双语简历 PDF

```bash
python scripts/generate_resume_pdf.py --input examples/bilingual_resume.json --output outputs/ZhangSan_Senior_Engineer_2026.pdf --format bilingual
```

## MCP 服务器用法

安装依赖：

```bash
python -m pip install mcp
```

本地启动 MCP 服务器：

```bash
python mcp_resume_cn_career.py
```

Claude Desktop 配置示例（`claude_desktop_config.json`）：

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

工具 `resume_skill` 支持四个动作：

| action | 说明 |
| --- | --- |
| `generate` | 生成结构化简历草稿 |
| `optimize` | 按 JD 做关键词与证据重排 |
| `ats_check` | 静态 ATS 检查（分数、问题、关键词覆盖率） |
| `export_pdf` | 导出可复制文本、中文不乱码的 PDF |

## 输入格式说明

- `format`: `chinese` 或 `bilingual`
- `contact`: 必填，包含姓名、联系方式等
- `summary`: 中文版摘要（chinese 模式）
- `sections`: 中文版结构化段落（chinese 模式）
- `zh` / `en`: 双语模式下分别提供摘要和段落

详细字段见 examples 目录中的示例文件。

## 兼容性

- Windows 环境优先使用系统中文字体（微软雅黑/宋体/黑体）
- 如果系统字体不可用，会回退到 CJK 字体
- JSON 读取支持 UTF-8 与 UTF-8 BOM

## 测试

```bash
python -m pip install pytest mcp reportlab
python -m pytest tests/
```

CI（GitHub Actions）会在 Ubuntu 与 Windows 上以 Python 3.10 / 3.11 / 3.12 运行同一套测试。

## 注意事项

- 简历内容必须真实，不编造经历、学历、证书与指标
- 导出前建议先按 references/analysis-checklist.md 完成自检
- 针对每个 JD 产出定制版，不要一版通投

## 许可证

[MIT](LICENSE)
