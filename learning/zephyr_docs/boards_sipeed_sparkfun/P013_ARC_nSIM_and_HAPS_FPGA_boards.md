---
id: learning.zephyr-docs.boards-sipeed-sparkfun.page-13
title: ARC nSIM and HAPS FPGA boards
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/snps/nsim/arc_classic/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="nsim"></a>

# 第13章\_ARC nSIM与HAPS FPGA平台

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/snps/nsim/arc_classic/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

名称（Name）：

`nsim`

厂商（Vendor）：

[Synopsys, Inc.](https://docs.zephyrproject.org/latest/boards/index.html#vendor=snps)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arc](https://docs.zephyrproject.org/latest/boards/index.html#arch=arc)

片上系统（SoC）：

[nsim_hs5x](https://docs.zephyrproject.org/latest/boards/index.html#soc=nsim_hs5x)、[nsim_vpx5](https://docs.zephyrproject.org/latest/boards/index.html#soc=nsim_vpx5)、[nsim_hs5x_smp](https://docs.zephyrproject.org/latest/boards/index.html#soc=nsim_hs5x_smp)、[nsim_em7d_v22](https://docs.zephyrproject.org/latest/boards/index.html#soc=nsim_em7d_v22)、[nsim_hs6x_smp](https://docs.zephyrproject.org/latest/boards/index.html#soc=nsim_hs6x_smp)、[nsim_em](https://docs.zephyrproject.org/latest/boards/index.html#soc=nsim_em)、[nsim_hs_smp](https://docs.zephyrproject.org/latest/boards/index.html#soc=nsim_hs_smp)、[nsim_hs](https://docs.zephyrproject.org/latest/boards/index.html#soc=nsim_hs)、[nsim_em11d](https://docs.zephyrproject.org/latest/boards/index.html#soc=nsim_em11d)、[nsim_sem](https://docs.zephyrproject.org/latest/boards/index.html#soc=nsim_sem)、[nsim_hs6x](https://docs.zephyrproject.org/latest/boards/index.html#soc=nsim_hs6x)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/snps/nsim/arc_classic/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

<a id="id2"></a>

<a id="id8"></a>

此平台可通过[DesignWare ARC nSIM](https://www.synopsys.com/dw/ipdir.php?ds=sim_nsim) [注1](#id1)在广泛的ARC处理器配置上仿真运行Zephyr，也可在[HAPS](https://www.synopsys.com/verification/prototyping/haps.html) FPGA原型平台[注3](#id7)运行相同镜像，包含：


- 实现ARCv2或ARCv3指令集架构（ISA）的ARC处理器核，当前支持的处理器系列完整列表见所链接页面（[here](https://docs.zephyrproject.org/latest/hardware/arch/arc-support-status.html#hardware-arch-arc-support-status)）
- 虚拟串口控制台，采用标准ns16550 UART模型

ARC处理器高度可定制，Zephyr当前支持其中部分配置，并非全部，支持功能完整列表见所链接页面。（[here](https://docs.zephyrproject.org/latest/hardware/arch/arc-support-status.html#hardware-arch-arc-support-status)）

平台支持多种子配置，以下只列出其中一部分：


- nsim/nsim_em：ARC EM v4.0核，两个寄存器组（Register Bank）、快速中断（FastIRQ）、MPUv2、DSP选项及XY存储器
- nsim/nsim_em7d_v22：ARC EM v3.0核，一个寄存器组及FastIRQ
- nsim/nsim_em11d：ARC EM v4.0核，一个寄存器组、无FastIRQ、MPUv2、DSP选项及XY存储器
- nsim/nsim_sem：ARC EM v4.0核，具有安全功能，SEM即Secure EM，并配MPUv4
- nsim/nsim_hs：ARCv2 HS v2.1核，两个寄存器组、FastIRQ及MPUv3
- nsim/nsim_hs_smp：双核ARCv2 HS v2.1，两个寄存器组、FastIRQ及MPUv3
- nsim/nsim_vpx5：ARCv2 VPX5核，接近vpx5_integer_full模板
- nsim/nsim_hs5x：32位ARCv3 HS核，包含丰富选项
- nsim/nsim_hs6x：64位ARCv3 HS核，包含丰富选项
- nsim/nsim_hs5x_smp/12cores：12核32位ARCv3 HS对称多处理（SMP）平台
- nsim/nsim_hs6x_smp/12cores：12核64位ARCv3 HS对称多处理（SMP）平台

<a id="board-arc-nsim-prop-args-files"></a>

建议查看[boards/snps/nsim/arc_classic/support/](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/snps/nsim/arc_classic/support/)中对应的.props或.args文件，了解特定子配置及启动仿真器时实际使用的选项。

单核配置的.props文件供nSIM使用，.args文件供MetaWare调试器（MDB）使用。二者应描述相同硬件配置，但分别适用于对应工具；MDB内部也通过nSIM仿真。

提示（Hint）

若运行与调试行为不同，尤其在新建或修改板级配置后，应检查.props与.args所定义功能在语义上是否一致。nSIM与MDB选项名称并不完全相同，需要仔细对应。

例如，单核nsim/nsim_hs5x对应[boards/snps/nsim/arc_classic/support/nsim_hs5x.props](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/snps/nsim/arc_classic/support/nsim_hs5x.props)及同目录mdb_hs5x.args。（[boards/snps/nsim/arc_classic/support/mdb_hs5x.args](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/snps/nsim/arc_classic/support/mdb_hs5x.args)）

多核配置只能借助MDB实例化，因此只有.args文件。

例如，多核nsim/nsim_hs5x_smp只有[boards/snps/nsim/arc_classic/support/mdb_hs5x_smp.args](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/snps/nsim/arc_classic/support/mdb_hs5x_smp.args)。

警告（Warning）

所有nSIM／MDB配置均用于演示及测试，不代表实际系统，可能随时改名、删除或修改。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`nsim`开发板支持下表所列的运行工具（Runners）及相关west命令。

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

<a id="id6"></a>

仿真运行单核Zephyr应用需要[DesignWare ARC nSIM](https://www.synopsys.com/dw/ipdir.php?ds=sim_nsim) [注1](#id1)或[DesignWare ARC Free nSIM](https://www.synopsys.com/cgi-bin/dwarcnsim/req1.cgi) [注2](#id5)。

<a id="id4"></a>

<a id="id15"></a>

仿真运行多核Zephyr应用需要[DesignWare ARC nSIM](https://www.synopsys.com/dw/ipdir.php?ds=sim_nsim) [注1](#id1)及[ARC MWDT](https://www.synopsys.com/dw/ipdir.php?ds=sw_metaware) [注4](#id14)中的MetaWare调试器。

<a id="id9"></a>

<a id="id16"></a>

在[HAPS](https://www.synopsys.com/verification/prototyping/haps.html) FPGA平台[注3](#id7)运行Zephyr时，除HAPS硬件外也需要[ARC MWDT](https://www.synopsys.com/dw/ipdir.php?ds=sw_metaware) [注4](#id14)中的MetaWare调试器。

<a id="building-running-sample-applications"></a>

### 构建及运行示例应用（Building and Running Sample Applications）

多数子配置同时支持GNU及ARC MWDT工具链，但可能存在例外，尤其是新增目标。可在对应.yaml文件中检查支持的工具链。

例如，nsim/nsim_hs5x的配置见[boards/snps/nsim/arc_classic/nsim_nsim_hs5x.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/snps/nsim/arc_classic/nsim_nsim_hs5x.yaml)。

受支持工具链列在.yaml文件的toolchain数组中，包括：


- zephyr：Zephyr SDK内的ARC GNU工具链，详情见所链接SDK说明。（[here](../toolchains/P002_ZephyrSDK.md#toolchain-zephyr-sdk)）
- cross-compile：独立于Zephyr SDK的ARC GNU交叉工具链。部分新子配置可能只声明支持cross-compile而不支持zephyr，因为SDK尚未加入对应CPU；用法见所链接页面。（[here](https://docs.zephyrproject.org/latest/develop/toolchains/other_x_compilers.html#other-x-compilers)）
- arcmwdt：专有ARC MWDT工具链，用法见所链接页面。（[here](../toolchains/P013_ARC_MetaWare工具链.md#toolchain-designware-arc-mwdt)）

注意（Note）

即使目标同时声明支持GNU及MWDT，部分测试或示例仍可能因功能只在特定工具链提供而仅支持其中一种。

可使用此配置在nSIM运行基本Zephyr应用及内核测试，例如基本同步（[Basic Synchronization](../basic_samples/P029_基本同步示例.md#synchronization)）示例：

```text
# From the root of the zephyr repository
west build -b nsim_em samples/synchronization
west flash
```

此命令构建同步示例镜像，通过nSIM启动并显示以下控制台输出：

```text
*** Booting Zephyr OS build zephyr-v3.2.0-3948-gd351a024dc87 ***
thread_a: Hello World from cpu 0 on nsim!
thread_b: Hello World from cpu 0 on nsim!
thread_a: Hello World from cpu 0 on nsim!
thread_b: Hello World from cpu 0 on nsim!
thread_a: Hello World from cpu 0 on nsim!
```

注意（Note）

退出仿真器时先按Ctrl+]，再按Ctrl+C。

<a id="board-arc-nsim-verbose-build"></a>

尖端触点（Tip）

向west传入-v可显示详细构建信息，例如west -v build -b nsim_hs samples/synchronization；目标写法按原文保留。

<a id="id10"></a>

为nsim构建的应用也可在[HAPS](https://www.synopsys.com/verification/prototyping/haps.html) FPGA硬件平台[注3](#id7)运行。运行已构建应用的方法如下：

```text
west flash --runner mdb-hw
```

注意（Note）

在HAPS运行还需设置HAPS本身并写入正确构建的FPGA镜像，即.bit文件。本说明不涵盖这些步骤，请遵循HAPS手册。

<a id="debugging"></a>

### 调试（Debugging）

<a id="debugging-with-mdb"></a>

<a id="board-arc-nsim-debugging-mwdt"></a>

#### 使用MDB调试（Debugging with MDB）

注意（Note）

原文强烈建议使用MetaWare调试器（MDB），原因如下：


- 支持更广泛的ARC硬件功能
- 支持单核及多核nsim目标调试
- <a id="id11"></a>

  支持[HAPS](https://www.synopsys.com/verification/prototyping/haps.html)平台[注3](#id7)调试

在nSIM仿真器运行应用时，无论单核还是多核，可使用以下命令启动图形界面调试：

```text
west debug --runner mdb-nsim
```

<a id="id12"></a>

在[HAPS](https://www.synopsys.com/verification/prototyping/haps.html)平台[注3](#id7)运行应用时，可使用以下命令启动图形界面调试：

```text
west debug --runner mdb-hw
```

尖端触点（Tip）

west debug及west flash均为封装命令（Wrapper），通过-v详细模式可提取实际调用的命令。例如执行：

```text
west -v debug --runner mdb-nsim
```

将产生以下输出，此例采用nsim/nsim_hs5x_smp配置：

```text
 < *snip* >
-- west debug: using runner mdb-nsim
runners.mdb-nsim: mdb -pset=1 -psetname=core0 -nooptions -nogoifmain -toggle=include_local_symbols=1 -nsim @/path/zephyr/boards/snps/nsim/support/mdb_hs5x_smp.args /path/zephyr/build/zephyr/zephyr.elf
runners.mdb-nsim: mdb -pset=2 -psetname=core1 -prop=download=2 -nooptions -nogoifmain -toggle=include_local_symbols=1 -nsim @/path/zephyr/boards/snps/nsim/support/mdb_hs5x_smp.args /path/zephyr/build/zephyr/zephyr.elf
runners.mdb-nsim: mdb -multifiles=core1,core0 -OKN
```

可从输出中提取用于建立图形调试会话的MDB命令：

```text
mdb -pset=1 -psetname=core0 -nooptions -nogoifmain -toggle=include_local_symbols=1 -nsim @/path/zephyr/boards/snps/nsim/support/mdb_hs5x_smp.args /path/zephyr/build/zephyr/zephyr.elf
mdb -pset=2 -psetname=core1 -prop=download=2 -nooptions -nogoifmain -toggle=include_local_symbols=1 -nsim @/path/zephyr/boards/snps/nsim/support/mdb_hs5x_smp.args /path/zephyr/build/zephyr/zephyr.elf
mdb -multifiles=core1,core0 -OKN
```

随后可直接执行这些命令，或按需集成到其他流程。

警告（Warning）

原文强烈建议从自己的配置中提取MDB命令，不要直接依赖上例列出的命令行选项。

注意（Note）

<a id="index-0"></a>

在nSIM多核配置上直接使用MDB运行或调试、而不经west flash／west debug时，必须将NSIM_MULTICORE环境变量设为1；使用west封装命令时会自动设置。

<a id="index-1"></a>

若NSIM_MULTICORE不为1，MDB会仿真两个互不共享内存的独立ARC核，启用SMP的代码将不能按预期工作。

<a id="debugging-with-gdb"></a>

#### 使用GDB调试（Debugging with GDB）

注意（Note）

通过GDB调试nSIM仅支持使用独立nSIM的单核配置；能够启动的多核nsim目标可改用MDB调试。这是nSIM与ARC GDB组合的限制，真实多核ARC硬件仍可用ARC GDB调试。（[使用MDB调试器调试](#board-arc-nsim-debugging-mwdt)）

注意（Note）

<a id="id13"></a>

原文说明当前不支持通过GDB调试[HAPS](https://www.synopsys.com/verification/prototyping/haps.html)平台[注3](#id7)。

注意（Note）

对nsim目标直接使用通常的west debug不能正常工作，因为仿真器与GDB或MDB共用控制台输入输出。使用GDB时，应分别开终端运行GDB及nSIM，避免输出混杂；MDB则使用图形界面模式。

构建后打开两个终端。在第一个终端启动nSIM的GDB服务器并等待远程连接：

```text
west debugserver --runner arc-nsim
```

在第二个终端使用Zephyr SDK内的ARC GDB连接服务器：


- ARCv2目标使用arc-zephyr-elf-gdb
- ARCv3目标使用arc64-zephyr-elf-gdb

此命令从ELF二进制加载符号表，例如build/zephyr/zephyr.elf：

```text
arc-zephyr-elf-gdb  -ex 'target remote localhost:3333' -ex load build/zephyr/zephyr.elf
```

调试环境已准备好，可使用GDB命令调试应用。

<a id="modifying-the-configuration"></a>

## 修改配置（Modifying the Configuration）

修改现有nsim配置或创建新配置时，必须保持以下三部分一致：


- Zephyr操作系统配置
- nSIM及MDB配置
- GNU及MWDT工具链编译选项

注意（Note）

Zephyr不直接支持.tcf配置文件。它适合裸机单线程程序：将全部硬件选项传给编译器，便可充分使用硬件并生成优化代码。但功能丰富的多线程操作系统不同，照搬所有.tcf选项未必最优。例如，这可能要求对所有任务，甚至部分中断，保存及恢复完整寄存器上下文；启用DSP或FPU时，即使多数用户任务及内核任务并不使用它们，也会增加几十个寄存器的保存与恢复。因此Zephyr选择细调硬件功能的使用范围，这也要求将相关配置与.tcf分开维护。

<a id="zephyr-os-configuration"></a>

### Zephyr操作系统配置

Zephyr通过Kconfig及设备树（Devicetree）定义操作系统配置。这些机制并非ARC专用，说明见[板级移植指南](https://docs.zephyrproject.org/latest/hardware/porting/board_porting.html#board-porting-guide)。

建议以<board_name>_defconfig、<board_name>.dts及<board_name>.yaml作为查找板级配置的入口。

<a id="nsim-configuration"></a>

### nSIM配置（Configuration）

nSIM配置由.props及.args文件定义，通常与对应.tcf一致，但有以下例外：（[props及args配置文件](#board-arc-nsim-prop-args-files)）


- 在.props及.args中加入UART模型
- 仅在.args中加入调整MDB行为的选项，用于关闭性能分析及细调多核系统行为

<a id="gnu-mwdt-toolchain-compiler-options"></a>

### GNU及MWDT工具链编译选项

硬件相关编译选项位于对应SoC的CMake文件；nsim为[soc/snps/nsim/arc_classic/CMakeLists.txt](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/snps/nsim/arc_classic/CMakeLists.txt)。

GNU工具链的基本配置通过-mcpu指定，由通用代码根据Kconfig选择的CPU模型设置，也可在SoC层强制覆盖。

MWDT的全部硬件相关编译选项直接设置于SoC的CMakeLists.txt。

注意（Note）

优化、库选择及C／C++语言选项等非硬件相关参数仍由Zephyr通用代码设置，可通过详细构建输出查看。（[以详细模式构建](#board-arc-nsim-verbose-build)）

<a id="references"></a>

## 参考资料（References）

<a id="id1"></a>

〔1〕 ([1](#id2),[2](#id3),[3](#id4)) [https://www.synopsys.com/dw/ipdir.php?ds=sim_nsim](https://www.synopsys.com/dw/ipdir.php?ds=sim_nsim)

<a id="id5"></a>

〔[2](#id6)〕 [https://www.synopsys.com/cgi-bin/dwarcnsim/req1.cgi](https://www.synopsys.com/cgi-bin/dwarcnsim/req1.cgi)

<a id="id7"></a>

〔3〕 ([1](#id8),[2](#id9),[3](#id10),[4](#id11),[5](#id12),[6](#id13)) [https://www.synopsys.com/verification/prototyping/haps.html](https://www.synopsys.com/verification/prototyping/haps.html)

<a id="id14"></a>

〔4〕 ([1](#id15),[2](#id16)) [https://www.synopsys.com/dw/ipdir.php?ds=sw_metaware](https://www.synopsys.com/dw/ipdir.php?ds=sw_metaware)

## 译注

ARC nSIM单核.props与MDB .args必须在硬件语义上匹配；多核仅使用MDB .args。直接调用MDB跑多核时需NSIM_MULTICORE=1，west封装命令自动设置。nSIM的GDB限制不代表真实多核ARC硬件无法使用GDB。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [ipdir.php?ds=sim_nsim](https://www.synopsys.com/dw/ipdir.php?ds=sim_nsim)：HTTP Error 403: Forbidden。
- [ipdir.php?ds=sw_metaware](https://www.synopsys.com/dw/ipdir.php?ds=sw_metaware)：HTTP Error 403: Forbidden。

---

[上一章](P012_ARC_IoT_Development_Kit.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P014_RISC-V_nSIM_and_HAPS_FPGA_boards.md)
