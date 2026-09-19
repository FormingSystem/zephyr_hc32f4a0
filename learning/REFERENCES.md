<!-- SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors -->
<!-- SPDX-License-Identifier: Apache-2.0 -->

# 资料来源与采用范围

核对日期：2026-09-19。正文在关键规则附近链接官方依据；本页记录材料来源、版本与使用边界，便于后续维护。

## 用户提供的参考材料

已读取用户提供的 `zephyr_west_book` 下载资料，其中 README 标注面向已有 C/C++ 与嵌入式经验的读者，教学 Zephyr 基线为 v4.2.0。资料仅用于参考，不是本教程的运行依赖。

重点吸收了工作区/清单仓库的角色区分、update 与 Git 开发的关系、配置覆盖、冻结时 manifest-rev 与 HEAD 的区别，以及扩展声明链。阅读了相关第 2、8、9、11、13、14 章，并浏览目录定位其他主题。没有复制下载包、沿用其章节模板，或将其 Zephyr v4.2.0 当成本项目版本要求。

本次改用完全本地的多仓库实验，将原材料的核心工具边界交叉验证。硬件构建、烧录、多镜像等超出本次 venv/west 通用教学范围，没有据此生成本项目硬件配置。

## 官方依据与本地观测

| 依据 | 本次使用问题 | 版本边界 |
| --- | --- | --- |
| [Python venv](https://docs.python.org/3.12/library/venv.html) | 创建、激活、解释器身份、可重建性 | Python 3.12 文档；本机 3.12.10 |
| [Python Packaging](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/) | 构建后端、项目元信息 | 本例 setuptools 80.9.0 |
| [pip 文档](https://pip.pypa.io/en/stable/) | 配置、安装、冻结、本地可编辑项目 | 在线 stable 随时间变化；命令实测 pip 25.0.1 |
| [west 文档](https://docs.zephyrproject.org/latest/develop/west/index.html) | 清单、配置、工作区、扩展 | 在线 latest 可能包含更新特性；主线实测 west 1.5.0 |
| 已安装工具的 `-h` 与实验结果 | 精确命令选项和失败分支 | 以 [VALIDATION.md](VALIDATION.md) 为准 |

继续更新时，先重新记录工具版本，再运行实验和检查帮助；不要把滚动网页内容默认为旧安装版本的能力。

UCRT64 主线环境差异核对：[MSYS2 Environments](https://www.msys2.org/docs/environments/)。这里区分 shell 与 Python 的来源，不要求更改现有系统默认解释器。
