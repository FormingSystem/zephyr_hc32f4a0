---
id: zephyr-vscode-slide-source
title: Zephyr IDE 演示文稿维护
kind: reference
status: maintained
domains: [documentation]
---

<!-- SPDX-License-Identifier: Apache-2.0 -->

# 演示文稿维护

正式文件在本目录上一级，名称为 `P001_VSCode_Zephyr_IDE接入已有工程_Windows.pptx`，共 48 页。正文、代码和关系图保持原生可编辑，代码是一段连续文本。封面背景和界面示意使用图片；署名在母版，正文页码采用自动字段。

## 保留 PowerPoint 手工修改

用户在 PowerPoint 保存的最新正式文件优先。后续维护先同步原生源，再调整；不要用旧 content.json 覆盖已经保存的手工修改。

操作位置：Windows UCRT64 Bash，资料仓库根；需要 Python 3.10 或以上，无额外依赖。

```bash
cd /f/git_storage/zephyr_hc32f4a0
python learning/zephyr_vscode/slides/build.py sync
python learning/zephyr_vscode/slides/build.py build \
  --output .local/zephyr-vscode-rebuilt.pptx
```

`sync` 从正式 PPT 提取 XML、媒体和关系到 `src/`，并更新 `source.json`。`build` 按清单重建，默认拒绝覆盖已有输出。重建后应逐 ZIP 部件比较内容，并用 PowerPoint 原生打开和渲染确认。

## 初始作者源

`author.mjs` 与 `content.json` 是本次首次创作的可维护输入，使用 `@oai/artifact-tool`。运行时需要设置 `RUNTIME_NODE_MODULES` 为包含该包的 node_modules，`TOPIC_DIR` 为当前专题绝对路径，`TMP_DIR` 为私有候选输出目录。

`finish_package.py` 接受三个参数：候选输入 PPTX、候选输出 PPTX、系列参考 PPTX。它使用 lxml，同步系列母版署名、自动页码、120% 段落行距与配套文档链接。参考文件为 `learning/P01_zephyr_make_project/slides/P003_SDK准备与编译器选型_Windows.pptx`。

作者源重新导出后应先检查候选稿，再发布正式文件并执行 sync。当前正式版本可直接用标准库脚本从 `src/` 重建，不需要重新运行作者工具。验证边界见 [VALIDATION](../VALIDATION.md)。
