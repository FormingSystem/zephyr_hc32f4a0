---
id: zephyr-vscode-validation
title: Zephyr IDE 教程验证记录
kind: reference
status: maintained
domains: [documentation, zephyr, tools]
---

<!-- SPDX-License-Identifier: Apache-2.0 -->

# 验证记录

## 2026-10-12：分类发布与Git对象核对

本次将IDE教材、61页正式PPT、命令附件、7张新增核验截图及原生重建源作为同一内容提交，验证记录与跨专题导航另行归档。正式PPT的286个ZIP部件、source清单和Git暂存对象逐项一致；补充 `slides/.gitattributes` 的原生源字节保留规则，防止新克隆时的换行转换影响重建。280份变更文本部件的常见凭据格式扫描未发现匹配；历史撤回的GUI证据保持下文边界，不恢复旧结论。

全仓107份文档的结构与本地链接检查通过，4项PPT结构回归通过。本轮只做发布与已有材料检查，没有重新渲染PPT、点击插件Build、下载安装组件或连接硬件；原生渲染和构建证据仍以各日期记录为准。

## 2026-10-11：按应用、硬件目标和组件来源补齐工程主线

本轮仍在用户指定的 `F:/git_storage/zephyr_hc32f4a0/learning/zephyr_vscode` 修改。以 49 页保存稿为基线，保留封面、设置页截图与已有操作入口，新增 12 页，形成 61 页。正文开篇先交代 MPS2 FPGA 平台、AN386 的 Cortex-M4F 目标，以及官方板文档使用 AN385 而本教程选择 AN386 的区别；再把应用的 `CMakeLists.txt`、`prj.conf`、源代码与 IDE 的 Project/Build 对应起来。

依据本机 Zephyr 提交 `25c8f4a23988dd3b2cfb463613622738298c2d6c` 和 IDE for Zephyr 4.1.1 源码，补全以下读取关系：主仓板/SoC/架构/驱动与外部 CMSIS Core；主仓 `modules/cmsis_6` 接入规则与工作区外部模块源码；west 活动项目发现、`EXTRA_ZEPHYR_MODULES` 追加及 `ZEPHYR_MODULES` 显式基础集合；HC32 设备头/DDL、通用 Core 头与 `hc32_port` 三类输入。Arm 存在独立 MPS2 BSP Pack 的事实与当前 Zephyr 构建是否使用该 Pack 分开说明。

新增 `commands/20-read-app-target.txt`、`21-hc32-build-fragment.json`、`22-check-hc32-inputs.txt`。JSON 片段用于合并新 Build，保留已有 MPS2 配置；命令文件先检查材料，缺失时停止。已有 `G:/zephyr_practice/hal_xhsc-zephyr` 无 `.git`，本次只核对关键文件，不把目录存在称为固定 Git SHA 已验证。G 盘 `hc32_port` 工作副本在本次核对时尚未建立，正文明确其准备步骤与检查入口。

只读 CLI 对照确认了树外新 SoC 的选板限制。IDE 4.1.1 的 `getBoardlistWest()` 只向 `west boards` 追加 `--board-root`，没有追加 `--soc-root`。对教材提供的 `learning/board/labs/hc32_port`，仅传板根时退出 1，提示找不到 `hc32f4a0pitb`；同时传入板根与 SoC 根时退出 0，得到 `uyup_rpi_a/hc32f4a0pitb`。这是目录发现验证，没有编译、下载或改写板/SoC。正文因此给出完整 Build JSON 与 CMake 模块三根发现链，不再要求读者只选 `boards` 文件夹就应出现该新 SoC。

`slides/content.json` 已同步原页修改与全部 12 张新增页；新增页逐字段与最终编排输入一致，61 页顺序与发布清单一致。Markdown 页码对照按实际页序重新计算，分散的小节分别列出范围。原正文的设置页图片引用保持不变；新增 JSON 与命令中的 Python 代码完成解析检查。正式发布后的 `learning/check_docs.py` 检查 107 份文档、36 章、19 份 Python 源、88 个标识，错误为 0。

61 页正式稿已通过最终文稿检查，并由 PowerPoint 原生打开和导出，文本框自动边界检查没有溢出项。23 张变化页逐页目检；第 7、11、16 页调整断行后复核最终图，未见行首孤立标点、裁切或重叠。正式稿同步到原生源并重建后，IDE 的 286 个 ZIP 部件逐项相同；本次 14 份正式 PPT 均完成同样的部件一致性核对。420 个 PPT 本地链接全部有效，其中 IDE 为 60 个；PPT 打包的 4 项结构回归测试通过。验证原件保存在忽略目录 `.local/engineering-guide-20261011`，包含发布渲染、链接审计和重建审计。

本次 IDE 修订没有以文稿渲染、`west boards` 结果或编译数据库推断插件 Build、HC32 编译/实板、烧录或调试成功。`compile_commands.json` 记录生成的编译任务；本次执行是否完成仍须看本次构建日志与退出结果。其他章节实际运行的独立实验按该章验证记录判断。

## 2026-10-10：撤回旧 GUI 截图证据与操作结论

本轮在用户指定的 `F:/git_storage/zephyr_hc32f4a0/learning/zephyr_vscode` 核对材料，所属 Git 根为 `F:/git_storage/zephyr_hc32f4a0`。C 盘同名旧副本不是本轮编辑目标。

`assets/reset_demo` 共 91 张 JPG，其中 88 张具有完全相同的 SHA-256：`7b1914f04b1283ae58b6c0f9ee9c727005ba9ccdd6d428d1ae7a499ed1f70a0b`。对内容的检查发现，名为 `36-build-success.jpg` 的图片不能证明 Build 成功。文件名与文件存在性检查不足以支持逐步操作声明。

因此撤回此前“72 张本机实机操作截图”“完整 GUI 重置、导入和点击 Build 成功”“全部配置页面已逐项截图验证”等结论。旧文声称的 136/136、ELF 字节数和资源统计不能通过这批图片归因于 GUI 按钮操作。本轮没有以旧图片推断或补造任何 GUI 执行结果。

原始图片保留供追溯，现行正文不引用。12/13 两个文件名带 gui_verified 的 JSON 保留为历史配置副本，已在索引中撤回其验证含义。原始七份辅助文档已备份至仓库忽略目录 `.local/zephyr-ide-rewrite-20261010/baseline-docs`，便于核对撤回范围。

## 本轮已直接核对的内容

- 安装包路径：`C:/Users/Lizha/.vscode/extensions/mylonics.zephyr-ide-4.1.1`。package.json 定义 43 个设置，其中 35 个现行、8 个废弃兼容项。
- 插件自有设置页命令为 `Zephyr IDE: Open Settings`；原生 VS Code 设置按 `@ext:mylonics.zephyr-ide` 过滤。自有页 Virtual Environment Folder 与原生设置 Venv Folder 对应相同的 venvFolder 键。
- 外部目录命令路线的选择项为 Mark workspace as already set up；Workspace 配置页另有 Mark as Complete。这是两个不同入口，不能互换显示名称。
- 当前教程统一为 ide-mps2 与 `build/learning-tools/zephyr-vscode/hello_world`；单 CMSIS 完整列表从默认流程移至历史诊断。设置页、操作命令、Build 字段和 Zephyr 原生输入按读取者分开说明。

来源是本轮实际读取的 package.json、resources/zephyr-ide-schema.json 和 dist/extension.js，以及现有文件。实现说明证明命令和字段的含义，不等于已经在 GUI 中逐项执行。

## 2026-10-10：主线命令行构建与产物核对

本轮实际在Windows UCRT64激活现有venv，执行与教程Project/Build输入对应的命令：

```bash
cd /g/zephyr_practice/zephyr-main
source .venv/Scripts/activate
west build -b mps2/an386 \
  -d build/learning-tools/zephyr-vscode/hello_world \
  samples/hello_world -- \
  -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
```

执行日志保存在资料仓库忽略目录`.local/zephyr-ide-rewrite-20261010/native-build.log`。已直接读取日志，并独立读取G盘对应输出的CMakeCache.txt、zephyr_modules.txt、compile_commands.json和ELF文件信息，结果如下：

| 核对对象 | 本轮实际结果 |
| --- | --- |
| 应用与板 | samples/hello_world；BOARD=mps2/an386 |
| 构建工具与源码版本 | 日志为CMake 4.4.3、west 1.5.0、Zephyr 4.5.0-rc1 |
| SDK与编译器 | SDK 1.0.1；CMAKE_C_COMPILER为G:/zephyr_practice/zephyr-sdk-1.0.1/gnu/arm-zephyr-eabi/bin/arm-zephyr-eabi-gcc.exe |
| 模块发现 | zephyr_modules.txt列出acpica、cmsis、cmsis_6；没有hal_xhsc。本参考板不需要HC32 HAL |
| 编译数据库 | CMAKE_EXPORT_COMPILE_COMMANDS=TRUE；数据库109项，其中有hello_world/src/main.c |
| 最终构建日志 | 完成131/131，链接zephyr/zephyr.elf；FLASH 18488 B、RAM 6440 B |
| ELF | G:/zephyr_practice/zephyr-main/build/learning-tools/zephyr-vscode/hello_world/zephyr/zephyr.elf，382936字节 |

这证明本轮命令行使用现有SDK、west自动模块发现和指定应用/板完成编译链接。没有以ZEPHYR_MODULES只列CMSIS的旧诊断替代主线。模块出现在发现记录中，不表示该模块的所有源码均参与编译。

此结果不是点击Zephyr IDE Build的实测，也不证明F12、QEMU、烧录或硬件运行通过；不能据此声称HC32 HAL或P011适配已经通过本轮验证。

## 2026-10-10：重新核对7张真实入口截图

本轮重新打开原生Settings、Zephyr IDE Settings、Workspace Information、Project Details和Modify Build Arguments两步输入框，保存到`assets/verified_20261010`。7张JPG逐张目检，SHA-256各不相同；摘要及每张图的证明范围见[图片记录](assets/README.md)与[来源清单](assets/sources.json)。

已确认点击CMake Args后，第1步是West build arguments，第2步才是CMake arguments。截图显示当前历史Build的原有值，仅供识别入口，不能照抄旧ZEPHYR_MODULES参数为主线。参数向导在第2步按Esc退出，未保存输入或修改G盘配置。上述截图不包含创建新Build或点击构建的成功证据。

## 历史结果如何使用

2026-10-07 的旧记录描述过命令行等价构建、PPT 渲染及结构检查；这些记录与 10-08 的 GUI 图片声明是不同证据。未在本轮重新执行的历史构建结果，不用于宣称当前 GUI、当前 SDK 路径或当前硬件已通过。其原文保留在本轮文档备份及仓库历史中。

原文将48页PPT保留、把操作内容追加到其他Markdown，导致PPT与三个指南分叉。本轮以49页PPT和同名主教程统一入口、配置名和输出；检查结果见下节。

## 2026-10-10：直接 CMake 分支与最终文稿

- 按 `commands/11-local-cmsis-build.txt` 在 UCRT64 执行直接 CMake/Ninja 分支，输出到 `build/learning-tools/zephyr-vscode/hello_world-native`。退出码0，136/136链接完成；ELF为382948字节，模块记录只有cmsis_6，SDK为1.0.1。日志在忽略目录 `.local/zephyr-ide-rewrite-20261010/native-cmake-build.log`。
- 本机仍装有west 1.5.0，CMake日志也检测到了它。上述结果只证明直接CMake入口和显式模块列表可用，不宣称在未安装west的新机器上完整验证。未修改 `.west`，也未覆盖IDE主线的hello_world输出。
- 49页正式PPT通过包完整性、Artifact Tool重新导入、标题/画布/字体与原生表格结构检查。几何估计对第40页表格给出一条警告；已用PowerPoint原生表格边界、单元格文字与正文边界复核，17张表均无相交或超过3pt的溢出，并目检对应页面。
- PowerPoint原生只读打开正式稿并导出49页，所有正文文本框无超过3pt的溢出。逐页看过渲染稿；保留原封面、主题、母版署名与自动页码。命令保持原生连续文本，正文段落120%行距。渲染只验证文稿，不代表IDE操作成功。
- `slides/content.json`、`author.mjs`、`finish_package.py`与原生`src/`已同步49页；正式稿从原生源重建后逐ZIP部件比较。包检查和渲染记录保存在忽略目录 `.local/zephyr-ide-rewrite-20261010`。
- 正式稿与重建稿逐部件相同，13段代码逐段与内容源一致；包内封面之外的正文段落均为120000多倍行距，原有母版、布局与主题字节保持不变。可移植作者入口和包装脚本也已实际生成49页候选稿。
- 当前2张Mermaid图通过default/dark主题渲染；第一图修正SDK附近连线布局后重新渲染并目检。其余文档结构/本地链接检查为104份文档、35章、0错误；9份Bash材料语法与10份JSON解析检查通过，`git diff --check`通过。

## 本轮未执行的动作

没有据截图声称已完成 GUI 重置/导入/构建、F12、Kconfig 保存或 Runner 动作。未运行 west update、pip/SDK 安装、QEMU、烧录、实板调试，也未因修订文档而覆盖 G 盘工作区的用户配置。hello_world/mps2 的说明不代表 HC32 移植验证。
