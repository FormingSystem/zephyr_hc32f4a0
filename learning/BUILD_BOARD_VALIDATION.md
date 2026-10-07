---
id: learning.build-board-validation
title: 构建、板级配置与环境发布验收
kind: reference
status: maintained
domains: [documentation]
---

<!-- SPDX-License-Identifier: Apache-2.0 -->

# 构建、板级配置与环境发布验收

## 2026-10-06 准备专题 P003 在 G 盘实跑

Windows UCRT64 下，当前 G 盘 Zephyr 4.5.0-rc1、SDK 1.0.1、Python 3.12.10 环境中，官方 mps2/an386、新建 practice_mps2/an386 和逐层接入的 uyup_rpi_a/hc32f4a0pitb 三个 hello_world 均编译链接成功。前两项配置为 25 MHz，HC32 教学模块为 12 MHz；未烧录开发板。

实跑修正新增练习板缺 CONFIG_GPIO=y 的问题：复用 MPS2 pinctrl 时需要 GPIO 设备。源码依赖改由 P002 统一下载与核验，构建目录为 build/learning-tools/p003。下载恢复、文件对照和 PPT 检查详情见[本轮完整记录](P01_zephyr_make_project/VALIDATION.md)。下方旧记录只描述对应日期。

## 2026-10-04 实验路径修订的验证边界

CMake、VS Code 和板级正文改以 G 盘实验源码为工作位置。模块材料明确读取实验源码与 CMSIS 路径；HC32 配置章节明确要求先在该源码树完成移植；Twister 直接使用原生入口。此轮完成静态核对，没有重跑构建、模拟或硬件实验，下方原有成功记录保留其历史适用范围。

## 2026-09-29 逐步教学重构后的正文重放

本轮覆盖公共准备章、CMake 两章、VS Code 一章、板级三章、三份大纲与配套材料。沿用原有实验与稳定文件身份，新增就地说明、源码/生成物关系和步骤定位。基线为 10f26bb93，实验使用新的 host-guided-0929、module-guided-0929、board-guided-0929、twister-guided-0929 与 cmake-host-guided-0929 目录，不覆盖旧练习。

| 验证对象 | 实际结果 |
| --- | --- |
| CMake P01 样章 | 从当前正文提取命令和完整 C 文件；原程序输出 43，漏 limit_value 链接失败，登记后输出 40 且 CTest 通过；遗漏 calibrate 再失败并恢复；最大值改为 50 后输出仍为 43 |
| CMake P02 | enabled/disabled 均构建；最终配置与编译数据库分别含/不含 scale.c；关闭库但留下调用时确实缺 scale_sample；恢复两配置通过，倍数 3 的构建练习及恢复也已执行 |
| VS Code 主机路线 | 主机 Debug 程序输出 43；批处理 GDB 命中 calibrate，value=42，next 后 corrected=43，进程正常退出；工作区 JSONC 去注释后与原配置语义相同 |
| Board P01 | 默认与追加 debug.conf 分目录配置，DEBUG_OPTIMIZATIONS=y；调试配置的 HC32 镜像构建成功 |
| Board P02 | green、blue 的 led0 分别对应绿灯与蓝灯；tx-pin=16 在属性枚举检查阶段失败，同目录切回合法 overlay 后构建恢复。最终蓝绿对照都保留 debug.conf，补跑 blue 配置与构建并检查最终优化值 |
| Board P03 正常与错误期望 | 首次两个场景执行通过；只改期望为 999 时 enabled 因 Timeout 失败、输出仍为 42；恢复后两项通过 |
| Board P03 源码变化 | 倍数改为 3、期望仍为 42 时失败，运行输出为 63；接受期望 63 后两项通过；恢复源码与期望后再次两项通过 |
| 工程检查、构建与运行 | UCRT64 环境中 project_env.py check 的 49 项测试、调试配置离线检查和差异检查通过；project_env.py build 的 HC32 镜像及源码来源审计通过；正文中的 project_env.py test 软件回归通过 |
| HC32 Twister | 1 项 built (not run)，1 项因平台过滤，0 项在实板执行；没有将生成 ELF 写成硬件运行通过 |
| 文档与图 | check_docs.py：42 文档、16 章节、22 ID、0 错误；7 章的 106 个 Bash 操作单元通过语法、顺序与位置注释检查，41 个小节步骤保持同一路线；61 张 Mermaid（含三份大纲）实际渲染，并抽看路线、构建关系与调试时序 |
| 材料一致性 | 18 个变动的 labs 文件去除注释后与基线语义一致；C、CMake、YAML、JSONC、GDB 注释与正文同步，保留原许可证。蓝色 overlay 的配置命令额外带上原有 debug.conf，以隔离本次比较变量 |

环境为 Windows、UCRT64 Bash、Python 3.12.10、west 1.5.0、CMake 4.4.3、SDK 1.0.1、ARM GCC 14.3.0。源码版本与硬件事实仍以项目记录为准。先在 PowerShell 启动的工程检查因测试调用 sh 而失败，未通过修改测试规避；改用学习资料约定的 UCRT64 环境后完整通过。蓝灯最终检查最初仅匹配解析后的节点路径，实际工具保留标签引用；已同时核对别名引用及节点身份，未把文本表现差异误判为构建失败。

本轮未操作 VS Code 图形界面、menuconfig 交互菜单、探针枚举、烧录或实板调试；准备章的网络安装和已有 west 配置没有为文档重写重复执行。Linux/macOS 仍是路径替换说明，没有本轮实机结果。命令行 GDB、离线配置检查和模拟器结果分别记录，不互相冒充。

证据保存在忽略目录 `.local/guided-build-20260929/`：before 快照、host/build/debug/twister 日志、blue-final.log、project-check-bash.log、project-build.log、render-final.log、审计候选与渲染图。命令顺序检查允许的唯一原有命令差量是 blue 构建补入相同 debug.conf。作者冷读与通用审计候选的处理见 REVIEW；未声称经过真实初学者试读。

下方按日期保留早期记录，其“未执行”与计数仅描述当时轮次。

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
