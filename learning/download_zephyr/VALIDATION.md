---
id: zephyr-sdk-mapping-validation
title: SDK 版本映射与工程接入验证记录
kind: reference
status: evolving
domains: [zephyr, tools]
---

<!-- SPDX-License-Identifier: Apache-2.0 -->

# 第1章\_SDK\_版本映射与工程接入验证记录

最新修订见 1.4：前一轮的工程锁定记录只描述本项目历史组合，已从上游规则的证据链移除；当前正文依据原生源码查版本和 CMake 行为。

## 1.1\_2026-10-03\_修订范围与源码基线

本轮按内容重写模式修复 [P05](P005_SDK和交叉编译器下载说明.md)。读者要求说明三条可查证关系：当前仓库版本与 SDK、SDK 与编译器版本、HC32 架构与工具链选择；原请求还要求从下载到工程接入和编译形成完整操作过程。主线使用当前 HC32 仓库，读者提供的上游解压源码用于对照。

原工作树快照在忽略目录 `.local/p05-sdk-20261003/P05-before.md`，没有用 Git HEAD 覆盖其他未提交修改。保留文档 ID、文件名、七个 section-5-N 锚点和上下章导航；重新组织版本依据、目标映射、下载、安装、应用、构建及恢复。原有主机/目标区分、工具职责、包选择、摘要校验、运行库和 SDK 发现知识保留其作用，移除重复的单句代码框和“下一节应该继续写”的未完成叙述。原稿 2273 行、208 个围栏块，修订稿约 640 行、30 个围栏块；操作和配置主要以完整单元呈现。

| 核对对象 | 版本与来源 |
| --- | --- |
| 当前 HC32 工程 | VERSION 为 4.4.99，dependencies.lock.json 记录上游 f19d03c78ba70a670e3dadc2121523d33984a5c7 |
| 当前工程 SDK | SDK_VERSION 与锁定记录均为 1.0.1；Windows arm-zephyr-eabi GCC 为 14.3.0 |
| 当前工程模块 | CMSIS_6 b2dfbe1a20bbd49c2d2c605073799671074bbb30；HAL a84e04900616f68097d80cda2e89eaa8af3afadd |
| 读者实际解压源码 | VERSION 为 4.5.0-rc1，SDK_VERSION 为 1.0.1；本地接回的 Git HEAD 为 3777ab91262f93c2c2da7e1ab8cff4e8ea5f4ce4；已核对 VERSION、SDK_VERSION、west.yml、FindHostTools 无本地差异 |
| 解压源码的模块 | 按其 west.yml 实际下载 CMSIS_6 1c1840af7a7e757d6e2fec3ddb0e5ce0dfcc93c8 ZIP，解压后用于编译 |

源码核对包括当前工程的 board.yml、SoC Kconfig、FindHostTools、FindZephyr-sdk、zephyr_module、ARM 编译参数生成，以及 SDK 1.0.1 的 GNU target.cmake、Windows setup 脚本。未修改外部解压源码或已安装 SDK。

## 1.2\_实际完成的检查

| 检查 | 实际结果及边界 |
| --- | --- |
| 官方下载依据 | 在线核对 sdk-ng v1.0.1 发布页、API 附件名和组件清单，取得该版 sha256.sum；确认 Minimal 与 Windows ARM 工具链直链 |
| 本机工具身份 | SDK 1.0.1、GNU 14.3.0、目标 arm-zephyr-eabi；核对对应安装脚本的 /t、/c 和 /h 行为 |
| 当前工程 HC32 编译 | 使用正文相同的最小应用、显式源码/模块/SDK/Python 参数，目标 uyup_rpi_a/hc32f4a0pitb，完整配置与编译成功 |
| 当前工程 Cortex-M4 对照 | 同一应用以 mps2/an386 配置和编译成功，仅使用当前工程 CMSIS_6 |
| 实际解压源码编译 | 读者提供的 4.5.0-rc1 源码，配上其清单要求的 CMSIS_6，以 mps2/an386 配置与编译成功 |
| 编译器与 CPU | 三个构建的 compile_commands.json 均核对 ARM GCC 路径及 -mcpu=cortex-m4；HC32 命令还核对 -mfpu=fpv4-sp-d16、-mfloat-abi=hard |
| 生成物 | 三个构建均生成 zephyr.elf；核对 ARM ELF 和最终板级配置 |
| HC32 镜像与来源 | 本次验证应用及输出置于仓库 build/learning-tools/sdk-p05-20261003 内，项目镜像审计通过；正文的用户主目录外部应用不适用该脚本的仓库来源限制，已就地说明 |
| 失败与恢复 | 把实际解压源码配置中的 SDK 根故意指到 gnu/arm-zephyr-eabi，新的构建目录按预期报告 Zephyr-sdk 查找失败；正确根的独立构建成功 |
| 命令静态检查 | 25 个 Bash 块通过已有 Git Bash 的 bash -n；嵌入 Python 查询通过语法检查 |
| 仓库检查 | check_docs.py 检查 60 份文档，0 错误；工程 55 项工具测试、pyOCD 离线检查及差异检查通过 |

构建使用本机已有 Windows 工具和当前工程 Python 环境，通过直接 CMake/Ninja 调用验证。输出均放在本仓库忽略的 `build/learning-tools/sdk-p05-20261003/`；日志、下载元数据及逐项核对保存在 `.local/p05-sdk-20261003/`。正文使用用户主目录作为独立应用位置，本次构建输出选择不等于读者必须采用相同盘符。

未执行：全新 UCRT64 安装、整套 SDK 附件重新下载与解压安装、新虚拟环境联网安装全量依赖、CMake 用户注册表修改、QEMU 运行、烧录和实板测试。Git Bash 的静态检查不冒充实际 UCRT64 软件安装验收；软件编译不冒充硬件运行。

## 1.3\_阅读审查与自动审计候选

按读者问题重新连读：版本文件与发布页先建立选择依据，芯片配置再建立目标家族，实际下载先于解压，创建 app 和依赖先于 CMake，产生构建结果后再观察缓存和编译命令。官方 ZIP 单独建环境，并从它自己的 west.yml 取模块版本，避免把两个源码基线混合。

通用连续阅读脚本报告一项链接密度候选：30 个内部链接。保留理由是读者明确要求“从哪里查到”，开篇提供可点击证据，后文仍在本地完整解释关系和操作；隐藏链接后不影响执行主线。没有空小节或超长 H2 模块风险。未宣称已经进行外部读者试读。

通用结构脚本不识别本仓库已使用的 HTML section 锚点和行尾上下章格式，将其报告为错误；本轮保留稳定链接，使用仓库 check_docs.py 复核真实锚点和导航。脚本也无法从 Bash here-document 中识别完整 C 应用，因此“缺少 C 场景”是形式识别限制。本文讲解线性配置操作，采用七步路线和就地文字说明，不额外加入重复的 Mermaid 状态/时序图。

术语脚本的剩余候选逐项按下表处理，不为窗口匹配将章节改成大术语表：

| 候选名称 | 处理与保留依据 |
| --- | --- |
| SDK_VERSION、sdk_version | 分别为源码要求文件和 SDK 自身版本文件，5.1/5.3 明确身份、读取方法与结果；开篇表是问题导航 |
| SOURCE_ROOT/SDK_VERSION、ZIP_SOURCE/SDK_VERSION、ZIP_SOURCE/VERSION | 已解释变量与文件组合成路径，不是另一个待展开术语 |
| SDK_URL、MODULE_DIRS、PYTHON_EXE | 自定 Bash 变量，赋值及邻近文字/表格说明下载基址、模块列表、解释器路径 |
| CMSIS_REV、CMSIS_DIR、SDK_INPUT | 自定 Bash 变量，分别保存从清单查询的提交、模块根、交互输入的安装位置，5.7 已解释其消费位置 |
| CMSIS_6、cmsis_6 | 前章已建立模块背景，5.4 补充 CMSIS 全称和用途；大小写分别用于仓库名称和清单项目名，5.7 对照其真实条目 |
| MSYS2_ARG_CONV_EXCL | 5.3 在调用块之后就地解释其作用域及为何保护 cmd 斜杠参数 |
| DZEPHYR_BASE、DCMAKE_EXPORT_COMPILE_COMMANDS、ON | 前两项是审计将 -D 与变量名粘合，不是独立标识；5.5 解释 -D 与编译数据库开关，ON 为 CMake 开启值 |
| PY | Python here-document 的结束标记，与已解释的 EOF 同类，不是模块或变量 |
| pwd、venv、win32 | 命令/标准库模块/平台输出值，命令和解释紧邻；win32 包括 64 位 Windows，正文已说明 |
| GPIO、PCB、SRAM、ICG | GPIO、PCB、SRAM 属于既定嵌入式读者背景，分别指通用输入输出、印制电路板、静态随机存储器；ICG 在镜像检查段说明为本芯片启动配置区域，并连接硬件记录，非本章选 SDK 的前置条件 |

返回 [P05 正文](P005_SDK和交叉编译器下载说明.md)或[阅读大纲](大纲.md)。

## 1.4\_2026-10-03\_原生依据、CMake\_变量与演示同步

2026-10-03 同步修订 P02、P05 与第二期 PPT，原生证据固定为 Zephyr 4.5.0-rc1 / 3777ab91262f93c2c2da7e1ab8cff4e8ea5f4ce4。依据原生 VERSION、SDK_VERSION、doc/conf.py、scripts/west_commands/sdk.py、工具链文档、FindHostTools/FindZephyr-sdk、extensions 的 zephyr_get、modules/boards/Kconfig/arch 及 SDK 1.0.1 自带 CMake 配置。自建锁文件不再承担上游规则证明，HC32/UYUP 明确属于项目移植。

使用原生 samples/hello_world 与其 west.yml 对应的 CMSIS_6（1c1840af7a7e757d6e2fec3ddb0e5ce0dfcc93c8），显式配置 mps2/an386，完成编译。核对 compile_commands.json 中 SDK 内 ARM GCC、Cortex-M4 参数与 ELF32/ARM 文件头；错误环境配合正确 -D 可以成功，随后仅改变环境而复用缓存仍使用原 SDK。本轮测试脚本未导入 project_env；既有 Python 环境仅提供工具依赖。复用已安装 SDK 与此前按原生清单下载的模块，没有重新安装全套环境。

两篇正文合计 50 个 Bash 块通过 bash -n，内嵌 Python 通过语法解析，文档结构与本地链接检查通过；55 项工程工具测试、pyOCD 离线检查和差异检查通过。两篇连续阅读严格审计均为 0 风险。术语审计候选已人工复核：ENV/CACHE/MERGE 是原生语法名而非待翻译缩写，-D 与变量拼接被识别成新名字，变量和路径的意义已在附近正文与表格解释；不为消除启发式提示改写有效接口。

PPT 保留原设计并扩展为 46 页，含 46 页备注、45 个自动页码和 15 张原生可编辑表格。正式文件与上次输出一致，重建前未发现额外手工修改；全页渲染、结构/字体/几何检查通过，逐页视觉检查后调整一处表格间距。最终重建的其余 43 页渲染与前次逐字节一致，3 个变化页重新目检。原稿快照、生成报告、逐页图片及构建日志保存在忽略目录 `.local/p02-cmake-20261003/`。

没有修改原生源码或已安装 SDK；没有运行新机 pacman/pip 安装、SDK 注册、QEMU、烧录或实板验证。未暂存、提交或推送。
# 2026-10-04 SDK 示例的实验现场修订

P05 改为在 G 盘原生源码上使用 MPS2 目标，保留 SDK 版本推导、变量解释、自建应用、反查与恢复步骤。模块版本从实验源码的 west.yml 取得，Python 环境使用源码根 .venv。其他参考草稿明确其示意布局与可执行主线的边界。

本轮完成静态文档核对，未重新运行下载、构建与缓存反例；下面旧日志的路径、版本和结果仍表示当时环境，不视为本轮 G 盘全流程实测。

## 2026-10-06 Windows SDK 原生终端修正

P005 的 Windows SDK 下载、摘要、解压、setup 与工具核验统一改为 PowerShell，共同环境说明同步；此前 MSYS2_ARG_CONV_EXCL 包装 setup 的记录属于历史。后续应用构建仍使用 UCRT64，切换时重新确认目录。已完成语法与文档链接检查，未执行新一轮下载或重新安装；实际 PowerShell 调用验证见 P01_zephyr_make_project/VALIDATION.md 最新记录。


## 2026-10-06 恢复默认 UCRT64 的终端原则

本条取代上一条“Windows SDK 原生终端修正”的过宽表述。P005 普通下载、摘要核验、解压及编译器检查恢复 UCRT64；setup.cmd 由 PowerShell 执行，Zephyr 官方明确采用 PowerShell 的 Windows 工具安装步骤仍用 PowerShell。公共环境约定同步，切换处重新进入目录。两篇相关正文共 59 段 Bash、8 段 PowerShell 通过语法检查；70 篇文档检查 0 错误，G 盘实际 SDK 的 UCRT64 版本和目标检查通过。未重新下载安装或编译，PPT 和详细验证见 P01_zephyr_make_project/VALIDATION.md 的终端规则纠正记录。


## 2026-10-06 SDK 专题复用 west 模块

P005 的两个 CMSIS ZIP 下载段改为复用 P002 已建立的 west 工作区；普通 CMake 配置不再传入显式 CMSIS 列表。P003 下载加速与 P004 清单专题的交叉说明同步，P000 的专门显式输入练习通过 west list 取得现有模块。语法、链接检查通过。G 盘本轮已完成官方 hello_world、练习板、HC32 与用户预设构建，验证 west 模块发现及额外模块追加；未重新执行 P005 自建应用和所有 SDK 失败反例。详细证据见准备专题 VALIDATION.md 的 CMSIS 主线记录。
