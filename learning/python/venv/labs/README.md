<!-- SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors -->
<!-- SPDX-License-Identifier: Apache-2.0 -->

# venv 实验源码

从[第一章](../P01_创建并认识虚拟环境.md)开始操作，不需要先研究自动验收脚本。

| 文件 | 用途 |
| --- | --- |
| [inspect_environment.py](inspect_environment.py) | 只读输出解释器、前缀、包目录和激活变量 |
| [package_v1/pyproject.toml](package_v1/pyproject.toml) | 第一版包的打包配置，源码在同目录的 src 中 |
| [package_v2/pyproject.toml](package_v2/pyproject.toml) | 第二版，同一分发名，不同版本与问候语 |
| [requirements-v1.txt](requirements-v1.txt) | 第一版的最小安装要求 |

两个包没有第三方运行依赖；构建需要 setuptools 80.9.0。安装构建工具需要网络或预先下载的包，两个 wheel 准备好后，隔离、卸载与重建实验可离线执行。源码、环境、wheel 是三种不同对象，章节按此顺序解释它们。

运行产物放入 `build/learning-tools/venv/`，不能提交。重新实验时换环境名；删除前只核对本次生成的目录。自动检查会使用另外的随机目录保留证据，执行方式见[验证记录](../../../VALIDATION.md)。
