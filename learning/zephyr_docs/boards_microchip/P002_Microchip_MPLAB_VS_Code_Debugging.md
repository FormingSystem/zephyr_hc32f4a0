---
id: learning.zephyr-docs.boards-microchip.page-2
title: Microchip MPLAB VS Code Debugging
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/microchip/common/mplab-core-da-debugging.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="microchip-mplab-vs-code-debugging"></a>

<a id="microchip-mplab-vscode-debugging"></a>

# 第2章\_Microchip MPLAB VS Code调试（Debugging）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/microchip/common/mplab-core-da-debugging.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

通过MPLAB Extension for Visual Studio Code扩展，可在VS Code中调试Microchip器件。该扩展集成Microchip调试工具，支持直接从VS Code启动和调试应用。（[用于Visual Studio Code的MPLAB扩展（Extension）](https://marketplace.visualstudio.com/items?itemName=microchip.mplab-core-da)）

本节介绍使用MPLAB调试扩展及launch.json，为Microchip目标配置VS Code调试的方法。

通常支持以下调试工具：


- MPLAB PICkit调试器／编程器
- MPLAB SNAP调试器
- MPLAB ICD调试器
- 部分Microchip开发板提供的板载调试器

具体器件及工具支持列表取决于所安装的MPLAB扩展、Microchip工具包及器件系列包。

<a id="requirements"></a>

## 前置要求（Requirements）

启动调试会话之前，安装并配置以下工具：


- [Visual Studio Code](https://code.visualstudio.com/)
- [用于Visual Studio Code的MPLAB扩展（Extension）](https://marketplace.visualstudio.com/items?itemName=microchip.mplab-core-da)
- 所需Microchip器件包（Device Packs）
- 受支持的Microchip调试探针或板载调试器
- 启用调试信息构建的固件镜像

构建系统生成的ELF文件用于源码级调试（Source-Level Debugging）。

```text
build/zephyr/zephyr.elf
```

<a id="installing-the-mplab-extension"></a>

## 安装MPLAB扩展（Installing the Extension）

安装步骤如下：


1. 打开Visual Studio Code。
2. 打开扩展（Extensions）视图。
3. 搜索MPLAB。
4. 安装Microchip官方MPLAB扩展。
5. 必要时重启VS Code。

安装后确认扩展能够检测所需Microchip调试工具及器件支持包。

<a id="building-a-zephyr-application"></a>

## 构建Zephyr应用（Building an Application）

启动调试会话前先构建Zephyr应用。

示例（Example）：

```text
# From the root of the zephyr repository
west build -b <board> samples/basic/blinky
```

构建成功后，Zephyr ELF文件位于：

```text
build/zephyr/zephyr.elf
```

`.vscode/launch.json`的program字段应引用此ELF文件。

<a id="vs-code-debug-configuration"></a>

## VS Code调试配置（Debug Configuration）

VS Code调试配置保存在以下文件中：

```text
.vscode/launch.json
```

MPLAB扩展使用mplab-core-da调试适配器类型（Debug Adapter Type）。

以下launch.json仅为示例，具体配置可能因开发板而异。应查阅目标开发板文档，使用对应launch.json。

```text
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "MPLAB Debug Zephyr : pic32cm_jh01_cpro",
      "type": "mplab-core-da",
      "request": "launch",
      "program": "${workspaceFolder}/zephyr/build/zephyr/zephyr.elf",
      "tool": "${command:pickTool}",
      "stopOnEntry": true,
      "device": "PIC32CM5164JH01100"
    }
  ]
}
```

tool字段使用以下命令：

```text
"tool": "${command:pickTool}"
```

这样MPLAB扩展就会在启动调试会话时，提示选择已连接的调试工具。

<a id="using-a-specific-debug-tool-serial-number"></a>

## 指定调试工具序列号（Serial Number）

连接多个兼容工具时，可在配置中增加serial字段，选择特定探针。

示例（Example）：

```text
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "MPLAB Debug Zephyr : pic32cm_jh01_cpro",
      "type": "mplab-core-da",
      "request": "launch",
      "program": "${workspaceFolder}/zephyr/build/zephyr/zephyr.elf",
      "tool": "${command:pickTool}",
      "stopOnEntry": true,
      "device": "PIC32CM5164JH01100",
      "serial": "020107402RYN000062"
    }
  ]
}
```

注意（Note）

serial必须匹配所连接Microchip调试探针的序列号。只连接一个工具时，通常无需此字段。可在VS Code命令面板执行“MPLAB: List connected tools”查找序列号。

<a id="configuration-fields"></a>

## 配置字段（Configuration Fields）

主要调试配置字段如下：

`name`

显示在VS Code运行和调试（Run and Debug）视图中的名称。

`type`

MPLAB扩展使用的调试适配器类型。MPLAB内核调试应使用mplab-core-da。

`request`

调试请求类型，使用launch启动新调试会话。

`program`

待调试ELF文件的路径，通常为`${workspaceFolder}/zephyr/build/zephyr/zephyr.elf`。原文也允许改用绝对路径；这里保留可随工作区移动的变量形式。

`device`

目标Microchip器件名称，例如PIC32CM5164JH01100。

`tool`

调试工具选择。`${command:pickTool}`让MPLAB扩展提示选择已连接工具。

`stopOnEntry`

设为true时，调试会话启动后会在程序入口点停止执行。

`serial`

可选的调试工具序列号，适用于连接多个探针的情况。

<a id="starting-a-debug-session"></a>

## 启动调试会话（Starting a Debug Session）

启动调试的步骤：


1. 将Microchip调试探针连接到目标板。
2. 给目标板供电。
3. 在VS Code中打开Zephyr工作区。
4. 构建应用。
5. 确认ELF文件存在。
6. 在菜单栏选择“运行（Run）→ 开始调试（Start Debugging）”，或按F5。
7. 随后可按需使用调试工具栏执行继续（Continue）、逐过程（Step Over）、逐语句（Step Into）等操作。

注意（Note）

若launch.json定义了多个调试配置，可在VS Code侧栏运行和调试视图的下拉菜单中选择。

会话启动时，MPLAB扩展提示选择已连接的调试工具。选中后，扩展连接工具、加载ELF文件并启动调试器。

调试时可在VS Code中执行以下操作：


- 设置及清除断点（Breakpoints）
- 单步执行源码（Step Through）
- 继续及暂停执行（Continue / Pause）
- 检查局部及全局变量（Variables）
- 查看调用栈（Call Stacks）
- 监视表达式（Watch Expressions）
- 检查寄存器（Registers），取决于扩展支持

<a id="troubleshooting"></a>

## 故障排查（Troubleshooting）

<a id="debugger-tool-is-not-detected"></a>

## 未检测到调试器（Debugger Tool Is Not Detected）

若未检测到调试工具：


- 检查USB连接。
- 确认MPLAB扩展支持该调试探针。
- 确认探针固件为最新版本。
- 断开并重新连接探针。
- 重启VS Code。
- 确认其他应用未占用调试工具。

<a id="device-is-not-recognized"></a>

## 无法识别器件（Device Is Not Recognized）

若无法识别器件：


- 确认device字段与Microchip器件的准确名称一致。
- 安装或更新所需Microchip器件包。
- 确认目标板已供电。
- 检查调试连接器及接线。
- 确认所选探针支持目标器件。

<a id="elf-file-is-not-found"></a>

## 找不到ELF文件（ELF File Is Not Found）

若调试会话找不到程序文件：


- 确认Zephyr应用已成功构建。
- 检查build/zephyr/zephyr.elf是否存在。
- 更新launch.json中的program路径。
- 可移植项目优先使用`${workspaceFolder}/zephyrproject/zephyr/build/zephyr/zephyr.elf`。

<a id="breakpoints-are-not-hit"></a>

## 未命中断点（Breakpoints Are Not Hit）

若断点没有命中：


- 确认应用构建时包含调试符号（Debug Symbols）。
- 修改源码后重新构建应用。
- 确认源码树与正在调试的ELF文件匹配。
- 若源码级调试不可靠，可降低编译器优化级别。
- 确认目标已编程为预期固件镜像。

<a id="debugger-mode"></a>

## 调试器模式（Debugger Mode）

Microchip调试工具，包括受支持开发板上的板载调试器，以及MPLAB SNAP、MPLAB ICD等外部探针，出厂默认处于MPLAB模式。如果使用pycmsisdapswitcher将调试器切换为CMSIS-DAP v2模式，MPLAB调试适配器将无法检测它。应恢复MPLAB模式并重新连接工具。

<a id="additional-documentation"></a>

## 其他文档（Additional Documentation）

更多信息见：


- [用于Visual Studio Code的MPLAB扩展（Extension）](https://marketplace.visualstudio.com/items?itemName=microchip.mplab-core-da)
- [Microchip开发者帮助（Developer Help）](https://developerhelp.microchip.com/)
- [Microchip软件包仓库（Packs Repository）](https://packs.download.microchip.com/)
- [`pycmsisdapswitcher`](https://pypi.org/project/pycmsisdapswitcher/)

## 译注

MPLAB源码级调试使用ELF。正文与故障排查分别给出${workspaceFolder}/zephyr和${workspaceFolder}/zephyrproject/zephyr两种布局，需按实际工作区选择。CMSIS-DAP v2模式不能被MPLAB调试适配器检测，需按对应工具流程恢复MPLAB模式。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [](https://developerhelp.microchip.com/)：The read operation timed out。

---

[上一章](P001_Flashing_with_Microchip_MPLAB_IPE.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P003_UPD301C_Basic_Sink_Application_Example.md)
