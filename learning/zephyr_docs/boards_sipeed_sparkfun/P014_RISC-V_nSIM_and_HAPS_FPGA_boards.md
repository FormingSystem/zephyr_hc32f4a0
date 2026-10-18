---
id: learning.zephyr-docs.boards-sipeed-sparkfun.page-14
title: RISC-V nSIM and HAPS FPGA boards
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/snps/nsim/arc_v/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="nsim_arc_v"></a>

# 第14章\_RISC-V nSIM与HAPS FPGA平台

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/snps/nsim/arc_v/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

名称（Name）：

`nsim_arc_v`

厂商（Vendor）：

[Synopsys, Inc.](https://docs.zephyrproject.org/latest/boards/index.html#vendor=snps)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[riscv](https://docs.zephyrproject.org/latest/boards/index.html#arch=riscv)

片上系统（SoC）：

[rmx100](https://docs.zephyrproject.org/latest/boards/index.html#soc=rmx100)、[rhx100](https://docs.zephyrproject.org/latest/boards/index.html#soc=rhx100)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/snps/nsim/arc_v/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

<a id="id2"></a>

<a id="id7"></a>

此平台可通过[DesignWare ARC nSIM](https://www.synopsys.com/dw/ipdir.php?ds=sim_nsim) [注1](#id1)在广泛的Synopsys RISC-V处理器配置上仿真运行Zephyr，也可在[HAPS](https://www.synopsys.com/verification/prototyping/haps.html) FPGA原型平台[注3](#id6)运行相同镜像，包含：


- 实现riscv32指令集架构（ISA）的RISC-V处理器核
- 虚拟串口控制台，采用标准ns16550 UART模型

支持的板级目标如下：


- nsim_arc_v/rmx100：Synopsys RISC-V RMX100核
- nsim_arc_v/rhx100：Synopsys RISC-V RHX100核

<a id="board-nsim-arc-v-prop-files"></a>

建议查看[boards/snps/nsim/arc_v/support/](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/snps/nsim/arc_v/support/)中的.props文件，了解特定目标及启动仿真器时实际使用的选项。

警告（Warning）

全部nSIM目标均用于演示及测试，不代表实际系统，可能随时改名、删除或修改。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`nsim_arc_v`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
<th>调试服务器（debugserver）</th>
<th>连接调试会话（attach）</th>
</tr>
<tr>
<td><code>arc-nsim</code></td>
<td>✅（默认 / default）</td>
<td>✅（默认 / default）</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td><code>lldbac</code></td>
<td>✅</td>
<td>✅</td>
<td></td>
<td></td>
</tr>
<tr>
<td>mdb-hw</td>
<td>✅</td>
<td>✅</td>
<td></td>
<td></td>
</tr>
<tr>
<td>mdb-nsim</td>
<td>✅</td>
<td>✅</td>
<td></td>
<td></td>
</tr>
</table>

<a id="required-hardware-and-software"></a>

### 所需硬件及软件（Required Hardware and Software）

<a id="id3"></a>

<a id="id5"></a>

仿真运行单核Zephyr应用需要[DesignWare ARC nSIM](https://www.synopsys.com/dw/ipdir.php?ds=sim_nsim) [注1](#id1)或[DesignWare ARC Free nSIM](https://www.synopsys.com/cgi-bin/dwarcnsim/req1.cgi) [注2](#id4)。

<a id="building-running-sample-applications"></a>

### 构建及运行示例应用（Building and Running Sample Applications）

多数目标同时支持GNU及ARC MWDT工具链，但可能存在例外，尤其是新增目标。可在对应.yaml文件中检查支持的工具链。

例如，RMX100配置见[boards/snps/nsim/arc_v/nsim_arc_v_rmx100.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/snps/nsim/arc_v/nsim_arc_v_rmx100.yaml)，RHX100见同目录nsim_arc_v_rhx100.yaml。（[boards/snps/nsim/arc_v/nsim_arc_v_rhx100.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/snps/nsim/arc_v/nsim_arc_v_rhx100.yaml)）

受支持工具链列在.yaml文件的toolchain数组中，包括：


- zephyr：Zephyr SDK内的RISC-V GNU工具链，详情见所链接SDK说明。（[here](../toolchains/P002_ZephyrSDK.md#toolchain-zephyr-sdk)）
- cross-compile：独立于Zephyr SDK的RISC-V GNU交叉工具链。部分新目标可能只声明支持cross-compile而不支持zephyr，因为SDK尚未加入对应CPU；用法见所链接页面。（[here](https://docs.zephyrproject.org/latest/develop/toolchains/other_x_compilers.html#other-x-compilers)）
- arcmwdt：专有ARC MWDT工具链，用法见所链接页面。（[here](../toolchains/P013_ARC_MetaWare工具链.md#toolchain-designware-arc-mwdt)）

注意（Note）

即使目标同时声明支持GNU及MWDT，部分测试或示例仍可能因功能只在特定工具链提供而仅支持其中一种。

可使用此配置在nSIM运行基本Zephyr应用及内核测试，例如基本同步（[Basic Synchronization](../basic_samples/P029_基本同步示例.md#synchronization)）示例：

```text
# From the root of the zephyr repository
west build -b nsim_arc_v/rmx100 samples/synchronization
west flash
```

此命令构建同步示例镜像，通过nSIM启动并显示以下控制台输出：

```text
*** Booting Zephyr OS build zephyr-v3.2.0-3948-gd351a024dc87 ***
thread_a: Hello World from cpu 0 on nsim_arc_v!
thread_b: Hello World from cpu 0 on nsim_arc_v!
thread_a: Hello World from cpu 0 on nsim_arc_v!
thread_b: Hello World from cpu 0 on nsim_arc_v!
thread_a: Hello World from cpu 0 on nsim_arc_v!
```

注意（Note）

退出仿真器时先按Ctrl+]，再按Ctrl+C。

<a id="board-nsim-arc-v-verbose-build"></a>

尖端触点（Tip）

向west传入-v可显示详细构建信息，例如west -v build -b nsim_hs samples/synchronization；目标写法按原文保留。

<a id="debugging"></a>

### 调试（Debugging）

<a id="debugging-with-gdb"></a>

<a id="board-nsim-arc-v-debugging-gdb"></a>

#### 使用GDB调试（Debugging with GDB）

注意（Note）

通过GDB调试nSIM仅支持使用独立nSIM的单核目标。

注意（Note）

对nsim目标直接使用通常的west debug不能正常工作，因为仿真器与调试器共用控制台输入输出。使用GDB时应分别开终端运行GDB及nSIM，避免输出混杂。

构建后打开两个终端。在第一个终端启动nSIM的GDB服务器并等待远程连接：

```text
west debugserver --runner arc-nsim
```

在第二个终端使用Zephyr SDK内的RISC-V GDB连接服务器：


- 应使用riscv64-zephyr-elf-gdb

此命令从ELF二进制加载符号表，例如build/zephyr/zephyr.elf：

```text
riscv64-zephyr-elf-gdb  -ex 'target remote localhost:3333' -ex load build/zephyr/zephyr.elf
```

调试环境已准备好，可使用GDB命令调试应用。

<a id="debugging-with-lldbac"></a>

#### 使用lldbac调试（Debugging with lldbac）

lldbac运行工具随Synopsys ARC MWDT提供，使用run-lldbac统一调试仿真器及硬件目标。

注意（Note）

<a id="id9"></a>

确认[ARC MWDT](https://www.synopsys.com/dw/ipdir.php?ds=sw_metaware) [注4](#id8)的run-lldbac已安装并加入PATH。

lldbac运行工具支持：


1. debug：交互调试，并集成服务器管理
2. flash：在实体硬件上烧录及运行

<a id="debugging-with-simulator-nsim"></a>

## 调试仿真器nSIM

在nSIM进行交互调试时，向debug命令加入--simulator：

```text
west debug --runner lldbac --simulator
```

运行工具使用board.cmake内配置的nSIM属性，可通过--nsim-props覆盖，或通过--tcf指定目标配置文件（TCF）：

```text
west debug --runner lldbac --simulator --nsim-props=rmx100.props
west debug --runner lldbac --simulator --tcf=rmx100
```

注意（Note）

lldbac专用于交互调试。只需在仿真器运行而不调试时，应使用arc-nsim执行flash，提供高效非交互运行：

```text
west flash --runner arc-nsim
```

这种分工让lldbac负责调试，而arc-nsim负责常规运行。

<a id="debugging-with-hardware"></a>

## 调试硬件（Debugging with Hardware）

调试实体硬件时，通过命令行传入JTAG配置：

```text
west debug --runner lldbac
west flash --runner lldbac
```

可用硬件选项：


- --jtag：JTAG适配器类型，默认jtag-digilent
- --jtag-device：JTAG设备名，可选；不指定时自动检测，例如JtagHs2
- --jtag-frequency：JTAG时钟频率，默认500 kHz
- --postconnect-cmd：连接后执行的命令，可多次指定
- --postconnect-file：硬件初始化后执行的命令文件
- --board-json：复杂板级配置使用的board.json路径

使用postconnect命令初始化硬件的示例：

```text
west flash --runner lldbac --postconnect-cmd "reg write sp 0x1000"
west flash --runner lldbac --postconnect-file postconnect.cmd
west debug --runner lldbac --board-json board.json
```

<a id="gui-mode"></a>

## 图形界面模式（GUI Mode）

加入--gui标志，可启动支持VS Code图形界面的调试：

```text
west debug --runner lldbac --simulator --gui
west debug --runner lldbac --gui
```

<a id="modifying-the-configuration"></a>

## 修改配置（Modifying the Configuration）

修改现有nsim配置或创建新配置时，必须保持以下三部分一致：


- Zephyr操作系统配置
- nSIM配置（Configuration）
- GNU及MWDT工具链编译选项

注意（Note）

Zephyr不直接支持.tcf配置文件。它适合裸机单线程程序：将全部硬件选项传给编译器，便可充分使用硬件并生成优化代码。但功能丰富的多线程操作系统不同，照搬所有.tcf选项未必最优。例如，这可能要求对所有任务，甚至部分中断，保存及恢复完整寄存器上下文；启用DSP或FPU时，即使多数用户任务及内核任务并不使用它们，也会增加几十个寄存器的保存与恢复。因此Zephyr选择细调硬件功能的使用范围，这也要求将相关配置与.tcf分开维护。

<a id="zephyr-os-configuration"></a>

### Zephyr操作系统配置

Zephyr通过Kconfig及设备树定义操作系统配置。这些机制并非RISC-V专用，说明见[板级移植指南](https://docs.zephyrproject.org/latest/hardware/porting/board_porting.html#board-porting-guide)。

建议以<board_name>_defconfig、<board_name>.dts及<board_name>.yaml作为查找板级目标配置的入口。

<a id="nsim-configuration"></a>

### nSIM配置（Configuration）

nSIM配置由.props文件定义，通常与对应.tcf一致，但有以下例外：（[props配置文件](#board-nsim-arc-v-prop-files)）


- 加入UART模型
- 加入核内本地中断控制器（CLINT）模型

<a id="gnu-mwdt-toolchain-compiler-options"></a>

### GNU及MWDT工具链编译选项

硬件相关编译选项位于对应SoC的CMake文件；nsim_arc_v为[soc/snps/nsim/arc_v/CMakeLists.txt](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/snps/nsim/arc_v/CMakeLists.txt)。

GNU工具链的基本配置通过-march指定，由通用代码根据Kconfig选择的CPU模型设置，也可在SoC层强制覆盖。

注意（Note）

优化、库选择及C／C++语言选项等非硬件相关参数仍由Zephyr通用代码设置，可通过详细构建输出查看。（[以详细模式构建](#board-nsim-arc-v-verbose-build)）

<a id="references"></a>

## 参考资料（References）

<a id="id1"></a>

〔1〕 ([1](#id2),[2](#id3)) [https://www.synopsys.com/dw/ipdir.php?ds=sim_nsim](https://www.synopsys.com/dw/ipdir.php?ds=sim_nsim)

<a id="id4"></a>

〔[2](#id5)〕 [https://www.synopsys.com/cgi-bin/dwarcnsim/req1.cgi](https://www.synopsys.com/cgi-bin/dwarcnsim/req1.cgi)

<a id="id6"></a>

〔[3](#id7)〕 [https://www.synopsys.com/verification/prototyping/haps.html](https://www.synopsys.com/verification/prototyping/haps.html)

<a id="id8"></a>

〔[4](#id9)〕 [https://www.synopsys.com/dw/ipdir.php?ds=sw_metaware](https://www.synopsys.com/dw/ipdir.php?ds=sw_metaware)

## 译注

RISC-V nSIM采用RMX100／RHX100目标及riscv64-zephyr-elf-gdb。lldbac专注交互调试，非调试仿真运行使用arc-nsim；硬件调试可传JTAG及postconnect参数。Zephyr自身配置与调试器接收TCF的功能分别说明。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [ipdir.php?ds=sim_nsim](https://www.synopsys.com/dw/ipdir.php?ds=sim_nsim)：HTTP Error 403: Forbidden。
- [ipdir.php?ds=sw_metaware](https://www.synopsys.com/dw/ipdir.php?ds=sw_metaware)：HTTP Error 403: Forbidden。

---

[上一章](P013_ARC_nSIM_and_HAPS_FPGA_boards.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P015_Soldered_Electronics.md)
