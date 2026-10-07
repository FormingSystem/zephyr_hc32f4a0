---
id: zephyr-download-teaching-design
title: 下载与安装章节设计
kind: reference
status: evolving
domains: [zephyr, tools]
---

<!-- SPDX-License-Identifier: Apache-2.0 -->

# 第1章\_下载与安装章节设计

## 2026-10-07 P003 融合与范围收敛

当前 P003 为 26 页（含保留的系列封面），覆盖包关系、下载、安装、SDK 发现和交叉编译器选择；用户限制为不超过 30 页。融合用户提供的 18 页稿中的读取链和组装模型，保留当前保存稿的版本依据、主机架构页和手工截图。移除参考稿中的制作评语、占位 BOARD 命令和无条件 pristine 操作；不把注册写成 Minimal 组装的必做动作。MD 同步为 3.1—3.5，旧稳定锚点继续有效，详情与历史操作截图留在正文。后续章节仍为 P004—P011，不另拆本主题。下方记录描述各自日期的旧方案。


## 当前组织：2026-10-07

本条是当前组织依据；下面带日期的旧章号、页数仅记录当时设计，不作为当前导航。

下载准备按 P001—P005 排列。原来一册的 CMake 内容拆为 P006 原生 CMake 与目标模型（22 页）、P007 Zephyr 应用构建（17 页）、P009 输入与依赖发现（24 页）、P010 缓存与构建排错（20 页）。中间独立设置 P008 west 零基础与 Zephyr 构建（25 页），从核心命令/工作区/清单讲到 Zephyr 扩展与 CMake 调用，不在 CMSIS 下载中另建清单。新增板实验顺延 P011。

P006 用普通主机 C 程序建立 target 模型；P007 才解释 app 的创建和首次配置；P008 以同一个 hello_world 对照 west 与直接 CMake。P010 的预设示例在本章内创建，不要求先做 P011。完整入口见 [大纲](大纲.md)。所有旧构建目录标识保留；用户新增的包结构页保留在 P007。


## 当前交付：三种工具链准备与接入路线

2026-10-06 最新章号为 P001—P006。SDK 主题在 P003（45 页），完整 GNU SDK、Minimal SDK 加 ARM 组件、独立 ARM 工具链各自说明文件来源、参数输入、CMake 读取者及选择规则。独立包没有 SDK 的 cmake，由 Zephyr 源码的 cross-compile 规则接入；不要求读者补造配置文件。P006（51 页）6.2.3 承担独立工具链的官方 AN386 编译替代实验。页脚署名沿用最新母版规范。

以下为此前的设计演进记录，历史章号和页数不作为当前阅读导航；以大纲及本节为准。


当前 Python 入口以 2026-10-06 本次整改为准：检查已有安装，Windows 用 py -3.12、Linux 用 python3.12 创建项目 .venv，激活后用 python。基础解释器使用正常安装位置，历史记录中的工程内 python312 路线已退出正文，不再作为必做步骤。

当前 SDK 讲解以 2026-10-06 的体系整改为准：GNU SDK、Minimal SDK 和独立工具链归档分开，先讲目录与安装，再讲两种 SDK 包共同的 CMake 接口。作用范围按终端、构建缓存、应用用户预设和当前用户包地址记录说明；.venv 仅承担 Python。移除独立 sdk-check 练习，真实配置与编译在 P003 的 hello_world 完成。正式 P002 为 74 页、P003 为 48 页、Linux P001 为 21 页；Windows P001 保持原稿。

当前终端约定：默认使用 UCRT64 Bash，保持 Linux 命令习惯。只有 Zephyr 官方明确采用 PowerShell 的 Windows 下载/安装步骤，以及 setup.cmd 等 Windows 专用脚本和其 Windows 管理操作，才切换到 PowerShell。普通下载、摘要校验、解压、版本检查、Python/venv 与 CMake 工程操作仍用 UCRT64，不能仅因调用 Windows 可执行程序就整段改成 PowerShell。Ubuntu 22.04 使用原生 Linux Bash。每段标明终端和目录，切换时重新进入目录，临时变量不互相继承。

## 2026-10-06 CMSIS 获取与接入的当前主线

本条优先于下面的早期设计。P002 在已有源码上建立 west 工作区，以 west list 解释清单，再由 west update cmsis_6 获取配套源码，核对实际提交、目录和模块入口；网页仅用于来源查证，ZIP 仅为特殊环境补充。主线不创建 cmsis-source.json，不另写 YAML 下载器，不要求重命名模块。当前清单没有 hal_xhsc，因此固定 HAL 由 Git 单独获取，P003 通过 EXTRA_ZEPHYR_MODULES 追加 HAL 与适配模块；CMSIS 仍由 west 自动发现。P003 直接使用 CMake，仍能使用这种发现关系。

P002/P003 当前为 74/48 页；水印、自动页码、封面和用户图片保留。Windows Python/west 使用 Git for Windows，所有 Git/west 操作仍在 UCRT64；native Git 选择和 PATH 的作用范围在工具准备中解释。源码来自 ZIP 不等于模块必须手工下载，也不自动获得主源码的 Git 历史。

## 2026-10-06 当前章节结构

P002 从 Windows 官方主机工具开始，顺序为 Python 三种使用情况与根 `.venv`、SDK 选择与安装、芯片和源码依赖依据、CMSIS/HAL 下载与核验、交接检查。MPS2 和 HC32 仅用于解释依赖选择；不创建板文件或执行固件编译。

P003 先认识官方 MPS2/AN386 的硬件和源码入口，再编译 `hello_world` 建立基线；第二遍逐文件对照新增 `practice_mps2/an386`；第三遍为 HC32 分阶段加入身份、设备树/PCB、启动/HAL、驱动和完整性检查，最后构建并反查产物。CMake 的完整机制保留在正文 3.9，第一次实验前不要求先读完它。

MD 保存完整命令、前置状态和输出判断；PPT 保留关键步骤、对照表和 Mermaid 路线。Windows P001 41 页、Linux P001 20 页、P002 63 页、P003 45 页；具体页码已写进正文对照表。下面保留早期设计，发生冲突时以本节及当前正文为准。

## 1.1\_第二期的阅读契约

2026-10-03：按内容新增模式编写 P02，承接 P01 已安装 UCRT64、可下载源码的状态。读者有嵌入式 C 基础，尚不能区分源码、SDK、Python 包与主机工具。主线固定 Windows x64 + UCRT64 Bash + Windows Python；不扩大到 Linux、WSL、固件烧录或演示文稿制作。

贯穿任务：为上一期下载的源码准备外部工具，最终亲手调用 ARM 编译器并核对 Python 包环境。SDK 以实验源码 SDK_VERSION 指定的 1.0.1 演示；不同上游修订先读自己的版本要求，不宣称 1.0.1 适合所有 Zephyr。

## 1.2\_认识推进与术语顺序

| 顺序 | 读者已有认识与缺口 | 本章增加的判断能力 |
| --- | --- | --- |
| 1 | 源码已经在磁盘上，但不能因此编译 | 区分源码模块、主机程序、Python 包、目标工具链 |
| 2 | UCRT64 可以执行命令 | 分清 Bash 与 Windows 程序；核对工具路径和 Python 身份 |
| 3 | SDK 页面包含许多下载项 | 按版本、主机、工具链家族选择 GNU 包；解释 Minimal 不含工具链 |
| 4 | 已有压缩包 | 校验文件、解压到工具目录、执行 Windows 安装脚本并注册 |
| 5 | 编译器可执行，但项目仍缺 Python 库 | 在 Windows venv 中用 pip 安装对应源码要求的包 |
| 6 | 工具分别通过检查 | 分清工具验收、源码模块配套、完整构建、模拟与实板的边界 |

关键名称按上表引入：SDK 是工具集合；交叉编译器运行于主机、为目标生成机器码；GNU 是本期选择的编译工具家族；Minimal 是发行包裁剪方式；SHA-256 是文件摘要；PATH 是命令搜索目录列表；venv 是隔离 Python 包的环境；pip 是该解释器的包安装器。west 的工具安装与模块下载分别讲解，不以命令名称充当解释。

## 1.3\_证据与验证边界

依据实验源码的 SDK_VERSION、scripts/requirements-base.txt、doc/conf.py 和 CMake 查找规则，以及 SDK v1.0.1 发行页和 template_setup_win。主机包名核对 MSYS2 官方索引，Windows Python 安装入口核对 Python 官方发行页。

重点检查：1.0.1 的 gnu 子目录；Bash 调用 cmd.exe 时关闭参数路径转换；Windows setup 的 /h 仅打印跳过提示；源码 ZIP 不等同 SDK 二进制发行包；激活 Windows venv 使用 Scripts/activate。

验证记录放在同目录 VALIDATION.md。未实际执行全新 UCRT64 安装时，只记录链接、脚本语法及已安装工具的只读检查，不将 Git Bash 检查称为 UCRT64 安装验收。

## 1.4\_新增板与演示维护

2026-10-04：P02 以已有 mps2/an386 检查工具链；P03 先创建 practice_mps2/an386 理解板注册，再接入 UYUP HC32 所需的 board、SoC、设备树、驱动与外部 HAL。每条路线列出操作前不存在的内容和创建方式，不让目标名冒充实际目录。当前只验证板发现，编译等待 SDK 安装。

PPT 采用 P001/P002 三位编号；第二期追加八页实验说明，完整命令维护在 P03。PowerPoint 手工修改先同步到原生包源码，再生成候选，保留截图、备注和编辑对象。Windows 资源管理器路径与 UCRT64 命令路径分开标注，G 盘是实验现场；Git 更新原则继续待定。

## 1.5\_Python 安装与发现的阅读顺序

2026-10-04：先解释 Windows CPython 与 MSYS2 滚动包，再给图形安装、UCRT64 调用同一官方安装器两种入口。安装选择汇合到基础解释器定位，区分 Launcher 按版本选择与 Bash 按 PATH 搜索；最后统一到源码根 .venv 安装 west 1.5.0 及上游清单依赖。已有同版本安装、无 Launcher、PATH 缺失和旧 venv 分别处理，不让读者重复安装或给全局 Python 装项目包。命令安装的 build/learning-tools/python312 是持续依赖，明确不能随构建清理删除。

## 1.6\_环境准备与编译实验分期

2026-10-04：P002 的完成标志改为 SDK/Python/west 与 .venv 可检查、可恢复；P003 承接这些前提，先解释 CMake 输入与缓存，再编译官方已有板并反查结果，最后新增练习板与所选 HC32 支持。实际命令、路径契约与验证边界不变，移除跨期资料中的旧页码和“P002 已编译”说法。

2026-10-05：Windows 环境正文移至 windows/，正式 PPT 移至 slides/windows/。P002 增加官方来源与 UCRT64 衔接两页，现 35 页；Python 说明位于第 15—21 页，venv 位于第 32—35 页。Linux 环境另有独立正文和 8 页 PPT。P003 的知识共用，现有命令标注 Windows 实验。旧记录中的页码仅代表当时版本。

### 2026-10-05：统一目录与平台后缀

按用户最新决定，取消阅读材料的 windows/linux 目录分组。Markdown 统一放在专题根，PPT 统一放在 slides，文件名使用 _Windows 或 _Linux 后缀；P03/P003 按现有 Windows UCRT64 命令标记为 _Windows。页面内容、截图与批注保留，更新本地链接、页面内资料路径和重建入口。Linux 原生打包文件归入 p01_linux，仅供维护。此前分目录记录代表历史组织，当前以本条及大纲为准。

### 2026-10-05：芯片型号与 CMSIS/HAL 下载依据

P002 增至40页，补全丝印/BOM/数据手册→board/SoC→CMSIS/HAL选择依据；P003增至31页，补全west与ZIP下载分支、从当前清单读取CMSIS修订、HC32固定HAL快照及构建输入反查。Markdown、下载参考中的未解决批注、板级材料、阅读入口和页数同步，新增Mermaid阶段图。CMSIS依据核对到G盘25c8f4a23988dd3b2cfb463613622738298c2d6c；该清单没有hal_xhsc，HAL提交由配套移植指定。

验证：65篇文档本地链接与结构检查0错误；97段Bash、6段内嵌Python、12个Mermaid通过语法检查；实际只读清单查询得到CMSIS提交1c1840af7a7e757d6e2fec3ddb0e5ce0dfcc93c8与HAL缺项。两份PPT包结构、导入及全部71页渲染完成，新增/改动页逐页检查，原媒体与批注部件完整保留；P002仍只有原图两项连接线警告，P003无警告。未安装依赖、变更G盘源码、重新编译固件或做实板验证，未实现Git同步政策。

## 2026-10-05 正文与演示的职责整理

正文与 PPT 采用相同三位编号和主题名，以平台后缀区分。正文保留完整实验并补充起点、完成状态、视频对照、恢复与复习；PPT 保留关键命令、图表和讲解备注。Linux 根据用户实际环境明确为 Ubuntu 22.04，增加三页版本补齐与 Python 安装检查，完整命令放回 Markdown。当前页数为 Windows 28/40/31、Linux 11；历史页数不代表最新稿。
