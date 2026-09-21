<!-- SPDX-License-Identifier: Apache-2.0 -->

# 构建、板级配置与环境发布验收

## 2026-09-21 单元内实验重编后的实跑

本轮只在教学副本中修改源文件与配置，未改变板级驱动实现。以下是新版正文的实际观察；后面的 2026-09-19 记录仅保留历史。

| 单元 | 实际结果 |
| --- | --- |
| CMake 主机 | 起始程序 43；新增 limit.c 尚未登记时链接失败，登记后输出 40 且 CTest 通过；漏 calibrate 再次失败并恢复 |
| Zephyr 模块 | enabled 配置含源文件、disabled 不含；关闭模块却保留调用时链接缺 scale_sample；恢复条件编译后两种构建通过 |
| GDB | 原始 Debug 程序命中 calibrate，value=42，next 后 corrected=43，正常退出 |
| VS Code 材料 | 工作区移入 labs，根目录变量解析仍准确；正文 JSON 与实际材料一致，未操作图形界面 |
| Kconfig | 默认与附加 debug.conf 分目录配置，最终调试优化为 y；menuconfig 交互步骤未操作 |
| 设备树 | green/blue 最终 led0 分别对应 led-1/led-0，均构建通过；tx-pin=16 在 binding 阶段失败，明确切回合法 overlay 后同目录恢复构建 |
| Twister 正常与错误期望 | 两场景执行通过；期望改为 999 时日志仍为 42，按预期超时失败；恢复后两项通过 |
| Twister 源码变化练习 | 倍数 3、期望 42 时失败且输出 63；接受期望 63 后两项通过；恢复源码与场景后再得两项通过 |
| 工程回归 | project_env.py build 的 HC32 ELF 与源码来源审计通过；project_env.py test 的 QEMU 软件场景通过 |
| HC32 测试选择 | Twister 1 项 built (not run)，另一平台场景过滤，无运行或实板成功声明 |

实跑修复了递归搜索被 Git 忽略产物时漏读日志的问题：正文 rg 增加 --no-ignore 并解释作用。SDK 1.0.1、ARM GCC 14.3.0，主机编译器为 UCRT64 GCC。详细日志留在 .local/textbook-validation。未连接探针，未烧录，也未验证 PCB 上的灯与串口；源码观察与模拟器结果保持各自边界。

## 2026-09-19 初次补充记录

此记录覆盖当时新增的 CMake、VS Code、Kconfig/设备树、Twister/QEMU 教程，以及工程 .venv/west 配置。早期 venv/west 教学验收保留在 [VALIDATION.md](VALIDATION.md)，两者按各自范围阅读。

## 实际执行结果

| 验证 | 结果与边界 |
| --- | --- |
| setup_environment.py | 创建根 .venv，安装 requirements-dev.txt；pip check 通过，Python 3.12.10 |
| project_env.py doctor | 仓库 Python、SDK 1.0.1、ARM GCC 14.3.0、主机工具与源码边界通过 |
| project_env.py check | 48 项工具测试通过；pyOCD 0.45.1 离线检查通过，未打开探针 |
| west 配置 | 父目录工作区、project-west.yml；manifest validate/list、boards、空 projects 的 update 成功 |
| west build | HC32 bringup 成功；verify_hc32_image.py 对同一输出目录审计通过 |
| project_env.py build | HC32 构建及 ELF/源码审计通过；根 .venv 建立后做过 pristine 构建，最终 CMake 调整后再次构建 |
| project_env.py test | mps2/an386 实际运行 1 项通过；HC32 专用场景被过滤 |
| 主机 CMake/CTest | Debug 构建、value=43、1/1 通过 |
| 漏源文件反例 | 链接出现 calibrate 未定义；关闭故障选项后恢复并通过 CTest |
| 主机 GDB | 命令文件命中 calibrate；观察 value=42、单步后 corrected=43，正常退出 |
| Zephyr 模块场景 | QEMU 启用/关闭两个场景执行通过；.config 与编译数据库确认 scale.c 仅在启用时编译 |
| PCB overlay | led0 指向 green_led，DEBUG_OPTIMIZATIONS=y，HC32 构建成功；未观察实板灯 |
| 非法 UART 索引 | tx-pin=16 在 binding 枚举检查阶段按预期失败 |
| HC32 Twister | 1 项 built (not run)，另一平台场景过滤，无错误；没有模拟 HC32 |
| 原有 venv/west 实验 | 重新运行 check_labs.py，ALL CHECKS PASSED；新父工作区没有破坏独立教学工作区 |
| 原 T05 环境反例 | 按改为 Bash 的 Python 命令重新执行，三项子进程预期成立 |
| 文档与配置 | check_docs.py 通过；两个 code-workspace JSON 和新增 Python 语法检查通过 |

主机 C 实验使用 UCRT64 GCC 16.1.0；底层工程命令在 UCRT64 Bash 中使用 Windows Python 和 Git for Windows。实验日志位于忽略的 build/learning-tools，不把机器绝对路径复制进公共正文。

关键日志包括 setup-project.log、check-environment-final.log、west-build-standard.log、west-build-audit.json、build-final.log、project-qemu-final.log、module-test.log、pcb-green.log、pcb-invalid.log、hc32-test.log、venv-west-regression.log、t05-regression.log。初始失败日志保留用于追踪，不作为最终通过证据。

## 验证中修正的问题

- 当前源码未定义 DEBUG_INFO，调试配置改用实际存在的 DEBUG_OPTIMIZATIONS。
- 模块追加使用 find_package 前的 EXTRA_ZEPHYR_MODULES，避免终端基础模块环境输入覆盖普通变量的追加。
- Windows 较长 Twister 实例路径造成归档工具找不到对象文件，使用 --short-build-path 后两个场景均通过。
- west 官方不支持工作区根同时作为 Git 仓库；最终配置改为仓库父目录的 .west，工程源码目录保持原位。脚本拒绝覆盖其他工作区，相关保护有测试。
- 普通 west 构建原先没有把 ZEPHYR_BASE 留在 CMake 缓存中，无法通过项目来源审计；应用现在明确缓存固定的本仓库源码根，两种构建入口均通过审计。

## 教学审阅

已运行技能的 audit_topic.py、audit_reader_continuity.py --strict、audit_terminology_onboarding.py --strict，覆盖新增 6 章。连续性严格检查均为零风险；CMake 和 VS Code 术语严格检查均为零风险。

board 术语检查剩余 8 条提示：CPU、PCB、LED、SPI 属于用户明确指定的嵌入式读者基础，PD10/PE15 是具体引脚标识而非待展开的缩写。正文已解释端口位号与物理封装脚号区别，因此采用人工确认，不把读者当成编程/硬件零基础。

通用 topic 审计剩余 12 条格式提示来自其要求的 H1 章号样式和固定“上一章/下一章”标签；本仓库沿用既有 `# 1. 标题` 与语义化导航，check_docs.py 已核对编号、实际相邻章节链接和目标存在。另有 8 条通用图表/C 代码块建议：本轮用真实 C 源文件、命令、配置表和生成产物完成证明，不为通过通用模板增加无必要的图。大纲元数据已补齐。

人工复核确认：先建立 target、模块发现、board/SoC、overlay/binding，再进入配置差异与错误实验；新增源文件、关闭模块、设备树合法但驱动不支持、QEMU 与实板边界分别有独立观察点。

## 尚未验证的范围

未新建或推送 GitHub 仓库，未用全新电脑完成网络下载/干净克隆安装；发布文档明确保留该发布前验收步骤。Python 依赖包含版本范围，未声称跨平台完整锁定。

未实际操作 VS Code 图形界面完成断点流程；主机 GDB 已执行，工作区配置作静态核对。未连接探针、烧录或测试真实 PCB。Linux/macOS 路径分支未在本轮实机验收。

Twister 期望字符串故意写错的挑战供读者练习，本轮未执行该变体。没有把所有练习建议都标记为已验证。
