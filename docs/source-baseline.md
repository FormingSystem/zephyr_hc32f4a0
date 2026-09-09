<!--
SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors
SPDX-License-Identifier: Apache-2.0
-->

# 源码基线与导入边界

本工程在仓库根目录保存完整 Zephyr 受版本控制的源文件快照，同时保存 HC32 构建需要的
CMSIS_6 和华大 HAL 完整源码快照。导入不包含原仓库的 `.git` 对象库、分支、标签或提交历史；
本仓库建立和维护自己的 Git 历史。机器可读记录见
[dependencies.lock.json](../dependencies.lock.json)。

| 来源 | 基线提交 | 本仓库位置 | 导入受控文件数 |
| --- | --- | --- | ---: |
| [Zephyr](https://github.com/zephyrproject-rtos/zephyr) | `f19d03c78ba70a670e3dadc2121523d33984a5c7` | 仓库根目录 | 66244 |
| [CMSIS_6](https://github.com/zephyrproject-rtos/CMSIS_6) | `b2dfbe1a20bbd49c2d2c605073799671074bbb30` | `modules/hal/cmsis_6` | 793 |
| [hal_xhsc](https://github.com/zephyrproject-rtos/hal_xhsc) | `a84e04900616f68097d80cda2e89eaa8af3afadd` | `modules/hal/xhsc` | 224 |

Zephyr 基线版本为 **4.4.99**。文件数是导入时的基线清单数量，不是当前项目总文件数。
HC32 SoC、板卡、驱动、工程入口与治理文件在此基础上继续演进，本仓库 HEAD 不等于上游 Zephyr 提交。

[source-manifest.tsv](../governance/architecture/source-manifest.tsv) 保存 67261 个基线文件的
相对路径、Git 文件模式和原始内容对象 ID。这是源码清单，不包含上游提交或历史对象。
导入时已检查文件零缺失，并保留 1230 个源文件的可执行位；特殊换行测试数据按原始字节保存。
根 LICENSE 仅去掉末尾多余空行，许可正文不变。

`project.py check` 使用清单识别原封导入，避免把上游既有格式和测试数据当成本地新代码整改。
只有新增、内容/模式与基线完全一致且没有未暂存修改的源文件可跳过重复格式检查；
所有自研、被改动文件，以及以后对 HEAD 既有文件的修改，仍进行正常 Git 差异检查。

## 构建使用的源码

`ZEPHYR_BASE` 固定为本仓库根。构建通过直接 CMake 调用，显式使用上述两个内置模块；
不要求 `.west`，不扫描相邻官方源码仓库，也不依赖外部 west 工作区完成模块发现。
`hal_xhsc` 的硬件集成已启用，SoC 从其中显式编译最小所需 DDL 文件，并使用本地配置和启动钩子。

Zephyr 的 `west.yml` 作为上游源文件保留，包含更多可选库与其他芯片的 HAL 清单。
这些模块不属于当前 HC32 目标的内置依赖；后续功能确实需要它们时再导入并记录来源与版本。
“完整 Zephyr 源码”指 Zephyr 仓库自身完整受控源码，不表示已下载清单中的全部外部项目。

SDK 1.0.1、ARM GCC 14.3.0、Python 虚拟环境和系统构建工具由本机环境提供。
`Setup-Environment.ps1` 负责创建仓库内虚拟环境并记录现有 SDK 位置，doctor 检查依赖。
SDK、`.venv`、`.local`、`build` 以及资料 PDF 都不纳入源码提交。

## 许可证与后续更新

导入的 Zephyr、CMSIS_6 与华大 HAL 文件保留各自的版权、SPDX 和 LICENSE 信息。
不将第三方文件统一改标为本项目 Apache-2.0。自研文件与继承治理框架的许可分别按其文件头和
[框架来源记录](../governance/architecture/framework_provenance.md) 处理。

更新任一源码快照时，核对来源提交与文件清单，先区分本地适配和上游变化，保留必要补丁，
更新 dependencies.lock.json 与本文，并重新执行 HC32 构建、工具检查、QEMU 回归及 pyOCD 离线检查。
硬件验证只记录实际进行的操作和结果。
