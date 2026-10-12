<!-- SPDX-License-Identifier: Apache-2.0 -->

# P004 Windows 完整操作

对应 [正文](../../P004_CMSIS选择与下载_Windows.md)。使用 Windows MSYS2 UCRT64；每个 TXT 是一个可独立恢复目录和必要环境的操作单元。按正文正在进行的阶段选择，不能把整个目录串行执行。只读检查、下载、创建文件和构建分别说明；已有工作区、HAL 与自有文件优先复用。

| 完整操作 | 正文 | 用途 |
| --- | --- | --- |
| [probe-soc-board.txt](probe-soc-board.txt) | [4.1.1](../../P004_CMSIS选择与下载_Windows.md#section-4-1-1) | 下载依赖前只读查询已知 SoC 与官方板目标 |
| [probe-cmsis-config.txt](probe-cmsis-config.txt) | [4.1.2](../../P004_CMSIS选择与下载_Windows.md#section-4-1-2) | 下载依赖前追踪 SoC、CPU 与 CMSIS 配置规则 |
| [check-git-python.txt](check-git-python.txt) | [4.2](../../P004_CMSIS选择与下载_Windows.md#section-4-2) | 核对 Bash 与 Windows Python 选中的 Git |
| [install-ucrt-git.txt](install-ucrt-git.txt) | [4.2](../../P004_CMSIS选择与下载_Windows.md#section-4-2) | 仅缺少 UCRT64 原生 Git 时安装 |
| [select-ucrt-git.txt](select-ucrt-git.txt) | [4.2](../../P004_CMSIS选择与下载_Windows.md#section-4-2) | 当前窗口选错 Git 时切换到 UCRT64 原生 Git |
| [select-git-for-windows.txt](select-git-for-windows.txt) | [4.2](../../P004_CMSIS选择与下载_Windows.md#section-4-2) | 使用已安装 Git for Windows 的备选分支 |
| [init-or-reuse-west.txt](init-or-reuse-west.txt) | [4.2](../../P004_CMSIS选择与下载_Windows.md#section-4-2) | 复用现有 west 工作区，缺失时才初始化 |
| [list-west-projects.txt](list-west-projects.txt) | [4.2](../../P004_CMSIS选择与下载_Windows.md#section-4-2) | 查看当前清单、活动项目和全部项目 |
| [query-cmsis-project.txt](query-cmsis-project.txt) | [4.2](../../P004_CMSIS选择与下载_Windows.md#section-4-2) | 只读查询 CMSIS 项目的仓库、修订和目录 |
| [resolve-west-manifest.txt](resolve-west-manifest.txt) | [4.2](../../P004_CMSIS选择与下载_Windows.md#section-4-2) | 只读展开当前清单的 imports |
| [download-cmsis.txt](download-cmsis.txt) | [4.3](../../P004_CMSIS选择与下载_Windows.md#section-4-3) | 按当前清单下载并检查 CMSIS 关键文件 |
| [verify-cmsis-revision.txt](verify-cmsis-revision.txt) | [4.3](../../P004_CMSIS选择与下载_Windows.md#section-4-3) | 核对已下载 CMSIS 的 HEAD 与 manifest-rev |
| [fetch-cmsis-if-missing.txt](fetch-cmsis-if-missing.txt) | [4.3.1](../../P004_CMSIS选择与下载_Windows.md#section-4-3-1) | 仅 CMSIS 缺失时获取源码的恢复块 |
| [diagnose-west-git.txt](diagnose-west-git.txt) | [4.4](../../P004_CMSIS选择与下载_Windows.md#section-4-4) | 只读复现 Windows Python 调用 Git 的解析检查 |
| [retry-cmsis-update.txt](retry-cmsis-update.txt) | [4.4](../../P004_CMSIS选择与下载_Windows.md#section-4-4) | Git 修正后重试更新并核对 revision |

两个 Git 选择分支按已有安装二选一；安装分支仅缺程序时执行。下载成功后做版本核验，故障诊断/重试仅失败时使用。清单查询不等于下载，源码在场不等于板支持完成。

补充 [查找真实 CMSIS 消费者](find-cmsis-consumer.txt)：先搜索 CPU 配置的读取位置，再比较两套 CMake 条件并核对模块绑定。正文见 [4.1.2](../../P004_CMSIS选择与下载_Windows.md#section-4-1-2)。

- [主仓必需头文件查询](prove-cmsis-required.txt)：4.1.3，在下载前确认选源、头文件引用与主仓文件边界。

- [可选迁移历史查询](inspect-cmsis-migration.txt)：4.1.6，对照清单收录、Cortex-M 迁移、官方说明与条件修正。
