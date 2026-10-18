---
id: learning.zephyr-docs.networking.page-98
title: zperf确定性回环吞吐量
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/samples/net/zperf/README-loopback-icount.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第98章\_zperf确定性回环吞吐量

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/zperf/README-loopback-icount.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 98.1\_概述

本页说明一种独立使用zperf示例检查网络吞吐量回归（Network Throughput Regression）的方法。它不依赖具体硬件，尤其不依赖运行模拟器的主机速度。

测量完全在`qemu_x86`客户机（Guest）内完成：

- 全部流量经过客户机内部的回环接口（Loopback Interface），测量路径不包含外部实时网络后端。
- QEMU以指令计数（Instruction Counting，icount）模式运行，客户机时间来自执行的指令数，而非主机挂钟时间（Host Wall-clock Time）。
- 示例自行驱动，无需交互式Shell：在回环接口上启动UDP、TCP接收端，向`127.0.0.1`上传数据，然后输出结果。

吞吐量为`bytes / elapsed_time`，即字节数除以经过时间。只有`elapsed_time`确定且与主机无关，这个指标才适合检测回归。icount模式下，虚拟CPU每执行一条指令，虚拟时间推进`2^shift`纳秒，因此报告的吞吐量成为每字节指令数（Instructions per Byte）的确定性函数：重复运行、换用主机时保持一致，而真实代码回归导致每字节指令数增加时，吞吐量数值下降。流量全部走回环接口，也排除了会破坏icount确定性的外部实时后端。

**注意**：绝对Mbps数值是虚拟时间代理指标（Virtual-time Proxy），代表每字节指令开销，不是真实线路速率（Line Rate）。只比较icount shift、数据包大小和系统节拍频率均相同的结果。

## 98.2\_工作原理

执行逻辑位于示例的`src/main.c`，受[`CONFIG_ZPERF_LOOPBACK_SELFTEST`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/zperf/Kconfig)控制。启用后，示例会自行启动网络；自动初始化被禁用，以免传输与网络启动发生竞争。

针对每个IP地址族（IP Family），示例依次执行一组传输。每项传输都先启动对应接收端，再执行阻塞上传（Blocking Upload），最后停止接收端，并输出一行`ZPERF-RESULT <marker>_mbps=<value>`。

| 标记（Marker） | 传输（Transfer） |
| --- | --- |
| `udp4`／`udp6` | 基准UDP测试，有效载荷接近最大传输单元（Maximum Transmission Unit，MTU），构成单个、不分片的数据报。 |
| `udp4_frag`／`udp6_frag` | 使用超过MTU的UDP有效载荷，迫使发送端IP分片（Fragmentation）、接收端重组（Reassembly）；仅在对应的[`CONFIG_NET_IPV4_FRAGMENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV4_FRAGMENT)／[`CONFIG_NET_IPV6_FRAGMENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6_FRAGMENT)启用时运行。 |
| `tcp4`／`tcp6` | 基准TCP测试，开启Nagle算法。 |
| `tcp4_nodelay`／`tcp6_nodelay` | 设置`TCP_NODELAY`、关闭Nagle算法，以覆盖另一条发送路径。 |

全部完成后输出`ZPERF-DONE`标记。两个地址族都会被测试，以便发现任一代码路径中的回归。IPv4传输使用`127.0.0.1`，IPv6传输使用`::1`；回环驱动为回环接口分配这两个地址。每个地址族的接收端绑定对应回环地址，而不仅是接口默认地址，以便客户端连接。禁用[`CONFIG_NET_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6)时跳过IPv6测试，IPv4同理。

每次上传都采用非默认套接字优先级[`NET_PRIORITY_VI`](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ggae87ef466e77ded673ed7e593d3eddffda7878127d03fb7d0a34b8d68b9461e792)。配合多个流量类别（Traffic Class）配置，流量会经过`net_tc.c`中各类别的专用线程，而非调用者上下文，从而每次都覆盖该调度路径。

完整配置由`overlay-loopback-icount.conf`提供，叠加在已有的`overlay-loopback.conf`之上。

## 98.3\_可配置参数

| Kconfig选项 | 含义 |
| --- | --- |
| [`CONFIG_ZPERF_LOOPBACK_SELFTEST`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/zperf/Kconfig) | 启用自行驱动的回环测试。 |
| [`CONFIG_ZPERF_LOOPBACK_SELFTEST_DURATION_MS`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/zperf/Kconfig) | 每次UDP、TCP上传运行的持续时间。 |
| [`CONFIG_ZPERF_LOOPBACK_SELFTEST_PACKET_SIZE`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/zperf/Kconfig) | 有效载荷大小，单位字节。默认值为MTU等于1280字节时的IPv6 TCP最大分段大小（Maximum Segment Size，MSS），使每次写入对应一个完整大小的分段，详见下节。 |
| [`CONFIG_ZPERF_LOOPBACK_SELFTEST_FRAG_PACKET_SIZE`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/zperf/Kconfig) | 额外UDP分片测试的有效载荷大小，单位字节；必须超过MTU才能触发分片，同时小于[`CONFIG_NET_ZPERF_MAX_PACKET_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_ZPERF_MAX_PACKET_SIZE)。 |
| [`CONFIG_ZPERF_LOOPBACK_SELFTEST_RATE_KBPS`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/zperf/Kconfig) | 目标速率；0表示按虚拟CPU允许的最快速度发送。 |
| [`CONFIG_ZPERF_LOOPBACK_SELFTEST_PORT`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/zperf/Kconfig) | 接收端与客户端共同使用的服务器端口。 |

译注：这些[`CONFIG_ZPERF_LOOPBACK_SELFTEST`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/zperf/Kconfig)系列配置来自[示例私有Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/zperf/Kconfig)，不是任意应用默认可用的全局配置。

## 98.4\_实现说明与注意事项

`overlay-loopback-icount.conf`内包含以下不易直接看出的配置考虑。

### 栈大小（Stack Sizes）

回环驱动在发送者上下文中同步交付每个包，因此整个接收路径和阻塞客户端上传都会嵌套使用调用者栈。配置增大了主线程和网络线程的栈，否则客户机在启动时就会栈溢出并发生故障。

### 节拍频率（Tick Rate）

节拍频率提高至10 kHz。在默认100 Hz下，`USECS_PER_TICK >= 1000`会使UDP上传器编译进时钟补偿路径，该路径按每包持续时间做除法。无限速（Unlimited Rate）时该持续时间为零，因此使用大于1 kHz的节拍频率既避免除零，也提供更细粒度的发送节奏控制（Pacing）。

### 接近MTU的数据包与MSS限制

叠加配置把回环MTU，即[`CONFIG_NET_LOOPBACK_MTU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_LOOPBACK_MTU)，提高到1280，并将zperf自身包长上限[`CONFIG_NET_ZPERF_MAX_PACKET_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_ZPERF_MAX_PACKET_SIZE)提高到有效载荷之上，因此默认1220字节有效载荷能形成接近MTU的帧。较大帧使每字节工作，例如校验和计算、缓冲区和片段遍历，相比每次调用的固定开销更占主导；吞吐量回归检查正应对这类工作敏感。

1220这个精确值关系到两个地址族之间的公平TCP比较。zperf TCP上传器每次`send()`提交整个有效载荷，再让TCP按MSS分段。MTU为1280字节时，IPv4 MSS为`1280 - 40 = 1240`，IPv6 MSS只有`1280 - 60 = 1220`，因为IPv6报头多20字节。假设载荷为1232字节，它能放入一个IPv4分段，却超过IPv6 MSS，使每次IPv6写入拆成一个1220字节完整分段和一个12字节短分段（Runt）。IPv6分段及确认包（ACK）数量因此约翻倍，TCP吞吐量接近减半。采用1220使每次写入在两个地址族中都保持为一个完整大小的分段。

基准UDP有效载荷在两个地址族中也都低于MTU，因此不会发生IP分片。不过，`net_buf`数据大小为1100，仍小于MTU，所以每帧横跨两个缓冲区片段（Buffer Fragments），有意覆盖片段链遍历（Fragment-chain Walk）。

### IP分片覆盖

启用[`CONFIG_NET_IPV4_FRAGMENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV4_FRAGMENT)和[`CONFIG_NET_IPV6_FRAGMENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6_FRAGMENT)后，执行器针对每个地址族增加一项UDP测试。其有效载荷由[`CONFIG_ZPERF_LOOPBACK_SELFTEST_FRAG_PACKET_SIZE`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/zperf/Kconfig)指定，默认2000字节，超过MTU，从而覆盖发送侧`ipv4.c`／`ipv6.c`的分片路径和接收侧的重组路径，对应`*_frag`标记。[`CONFIG_NET_ZPERF_MAX_PACKET_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_ZPERF_MAX_PACKET_SIZE)也提高到该载荷之上。

### 流量类别与优先级

叠加配置将发送、接收流量类别数[`CONFIG_NET_TC_TX_COUNT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_TC_TX_COUNT)／[`CONFIG_NET_TC_RX_COUNT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_TC_RX_COUNT)都设为2，启用[`CONFIG_NET_CONTEXT_PRIORITY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CONTEXT_PRIORITY)以及[`CONFIG_NET_ALLOW_ANY_PRIORITY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_ALLOW_ANY_PRIORITY)。每次上传设置非默认`SO_PRIORITY`，使流量通过各流量类别专用线程分派，不在调用者上下文中直接处理。这样覆盖`net_tc.c`调度路径，同时也增加上下文切换，所以绝对数值低于单一流量类别配置。

### 无限速计算

在`rate = 0`的无限速模式下，执行器选择足够高的合成速率，使每包节奏延迟向下舍入为零。这个速率使用64位计算，避免中间结果溢出，因此支持现实可用的包大小，原文给出的范围上限约为500 kB。

> 译注：这里说的是速率计算的算术范围，不等于该示例配置允许500 kB的数据包；当前私有Kconfig对两项包大小设置了1～16384字节范围，还必须同时满足MTU、分片和zperf最大包长配置。

### 不使用SLIP／TAP

QEMU的SLIP主机联网后端被禁用，运行不需要主机侧的`slip.sock`。

### 日志缓冲区大小

结果行通过`printk()`输出，日志子系统再经延迟后端（Deferred Backend）转发。默认1024字节缓冲区在`qemu_x86_64`首次IPv4传输期间溢出，[`CONFIG_LOG_MODE_OVERFLOW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_MODE_OVERFLOW)会丢弃最早的三条消息，静默吞掉`udp4_frag`结果行，使该指标完全无法进入报告。叠加配置将[`CONFIG_LOG_BUFFER_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_BUFFER_SIZE)提高到4096。测量本身不受影响；在原文所述检查中，32位结果在增大缓冲区后逐位相同。

## 98.5\_使用方法

译注：本节保留官方命令，均从Zephyr源码根在Bash终端执行。示例源码、叠加配置、Twister及报告脚本必须存在于所用Zephyr版本中，且已安装支持该目标的工具链和QEMU。`../build/`为原例选择的、相对于源码根的同级构建目录，不依赖作者机器的仓库位置；输出和基线文件由后续命令生成。

### 构建并运行一次

```bash
west build -p -b qemu_x86 -d ../build/zperf_loop samples/net/zperf -- \
    -DEXTRA_CONF_FILE="overlay-loopback.conf;overlay-loopback-icount.conf"
west build -t run -d ../build/zperf_loop
```

预期输出如下。同一构建的数值具有确定性，重复运行时完全相同；精确数值取决于工具链、包大小、icount shift和节拍频率，因此下列数值仅为原文示例：

```text
ZPERF-RESULT udp4_mbps=13.099
ZPERF-RESULT udp4_frag_mbps=20.249
ZPERF-RESULT tcp4_mbps=5.970
ZPERF-RESULT tcp4_nodelay_mbps=5.876
ZPERF-RESULT udp6_mbps=13.310
ZPERF-RESULT udp6_frag_mbps=20.059
ZPERF-RESULT tcp6_mbps=5.979
ZPERF-RESULT tcp6_nodelay_mbps=5.910
ZPERF-DONE
```

IPv4与IPv6的TCP数值接近，是因为默认载荷等于IPv6 TCP MSS，原因见前面的MSS说明。分片UDP的`*_frag`结果高于基准UDP，是因为较大数据报将每个数据报的固定开销分摊到更多载荷字节上，即使计入分片工作仍然如此。

### 通过Twister运行

`tests.yaml`中的场景`sample.net.zperf.loopback_icount`使用控制台测试适配器（Console Harness，标识为`console`），将吞吐量值记录到Twister JSON报告中：

```bash
./scripts/twister -p qemu_x86 -s sample.net.zperf.loopback_icount \
    --outdir ../build/zperf_run
```

该场景允许在`qemu_x86`（32位）和`qemu_x86_64`（64位）运行；后者提供64位数据点，例如覆盖64位校验和快速路径。一次运行可以测量两个平台：

```bash
./scripts/twister -T samples/net/zperf -s sample.net.zperf.loopback_icount \
    -p qemu_x86 -p qemu_x86_64 --outdir ../build/zperf_run
```

`-T samples/net/zperf`将扫描范围限制到此示例，避免为了一个场景遍历整个源码树。

两个平台的绝对数值不同，不能彼此比较。`scripts/zperf_regression.py`因此以Twister平台名`qemu_x86/atom`、`qemu_x86_64/atom`作为指标键，分别报告。可用`--platform`把报告限制到其中一个平台，参数可写完整的开发板／SoC名称（`board/soc`），也可只写开发板名称。

译注：这里的`tests.yaml`和`scripts/zperf_regression.py`均位于`samples/net/zperf/`下；下方命令已使用脚本相对于源码根的完整路径。

## 98.6\_基线与回归门槛

辅助脚本`scripts/zperf_regression.py`读取Twister运行记录。先在参考提交（Reference Commit）上采集一次基线（Baseline）：

```bash
./scripts/twister -p qemu_x86 -s sample.net.zperf.loopback_icount \
    --outdir ../build/zperf_base
samples/net/zperf/scripts/zperf_regression.py --base-dir .. \
    --twister-json ../build/zperf_base/twister.json \
    --save baseline.json
```

在之后的提交上重新运行，并以允许的最大下降百分比作为门槛：

```bash
./scripts/twister -p qemu_x86 -s sample.net.zperf.loopback_icount \
    --outdir ../build/zperf_cur
samples/net/zperf/scripts/zperf_regression.py --base-dir .. \
    --twister-json ../build/zperf_cur/twister.json \
    --baseline baseline.json --tolerance 5
```

任一记录指标的下降幅度超过容差（Tolerance）时，脚本以非零状态退出，因此可用于持续集成（Continuous Integration，CI）回归检查。

也可以直接比较两次运行，不生成中间基线文件：

```bash
samples/net/zperf/scripts/zperf_regression.py --base-dir .. \
    --twister-json ../build/zperf_cur/twister.json \
    --baseline-twister-json ../build/zperf_base/twister.json
```

其余选项影响报告，而非测量本身：

| 选项 | 含义 |
| --- | --- |
| `--threshold PCT` | 报告噪声阈值（Reporting Noise Floor），默认1%。变化小于阈值时描述为“未变化”，不记为改善或回归。同一二进制文件的icount结果会精确重复，但两个源码树会生成不同二进制，即使完成的工作没变，代码布局也可能改变数值。原文给出一个相隔157次提交、仅涉及TCP改动的比较：所有UDP指标在`qemu_x86`上逐位相同，在`qemu_x86_64`上变化不超过0.02%，说明这种漂移实际较小。 |
| `--markdown PATH` | 将比较结果写成Markdown表格，每个平台一节，可用于GitHub Actions作业摘要或拉取请求评论。某平台全部指标不变时，折叠进`<details>`块，并在摘要行说明；存在变化的平台保持展开。 |
| `--annotate` | 每个平台输出一条`::notice::`工作流命令，总结发生变化的指标。 |
| `--exit-zero` | 始终成功退出；适用于只提供参考、不应使构建失败的比较。缺失或无法构建的基线同样报告为无法完成比较。 |

**注意**：为保证脚本由自动化调用时的路径边界，读取和写入的每个文件都必须解析到`--base-dir`之下，默认基准目录为当前目录。通过`..`或绝对路径逃出该目录的路径会被拒绝。示例指定`--base-dir ..`，是因为它们从同级的`../build`读取Twister报告，同时在仓库内写入输出。

> 译注：`--threshold`控制报告中“是否发生变化”的描述，`--tolerance`控制下降幅度是否导致失败；两个参数职责不同。上述源代码位置与路径行为已按[官方报告脚本](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/zperf/scripts/zperf_regression.py)核对。

## 98.7\_持续集成

官方`.github/workflows/net-perf.yml`会在拉取请求（Pull Request，PR）涉及`subsys/net/`、`include/zephyr/net/`、`lib/net_buf/`、回环驱动或本示例时运行此场景。它在同一个执行器（Runner）上、针对两个平台分别测量PR与目标分支，然后将比较结果写入作业摘要（Job Summary）。

以下两点保证比较反映应测的差异：

- 工作流在PR变基到目标分支之后运行，因此差异来自这组改动自身，不会混入目标分支上无关的变化。
- 测量目标分支时使用PR中的`samples/net/zperf/`副本，使测试执行器、叠加配置和有效载荷大小在两侧一致，只有被测代码不同。这样，修改示例的PR不会通过改变测量内容来改变结果。

配套工作流`.github/workflows/net-perf-comment.yml`把相同报告作为PR评论发布，以便在评审处看到结果。它被拆成单独工作流，是因为测量由`pull_request`事件触发，来自分叉仓库（Fork）的令牌只有读取权限，不能评论；配套工作流由`workflow_run`触发，从构件（Artifacts）读取报告和PR编号，且从不检出PR代码。

每个PR保留一条评论，每次推送后原地更新。某平台全部指标不变时折叠显示，使不变结果只占一行。

此检查仅提供参考（Advisory）：使用`--exit-zero`，每个测量步骤都设置`continue-on-error`，也不属于必需检查。红色或意外数值是供评审者判断的信息，不会阻止合并。如果无法产生结果，例如目标分支构建失败，则报告比较不可用，作业仍然通过。

这里只测量回环路径。报告没有变化，并不表示改动没有性能影响；驱动、二层（L2）和卸载（Offload）相关工作完全不会反映在这里。

译注：本节描述[官方测量工作流](https://github.com/zephyrproject-rtos/zephyr/blob/main/.github/workflows/net-perf.yml)及[官方评论工作流](https://github.com/zephyrproject-rtos/zephyr/blob/main/.github/workflows/net-perf-comment.yml)，不表示本次在当前仓库启用了自动化、发布评论或执行了性能测试。

## 98.8\_结果可视化

指定`--plot`可生成独立SVG柱状图（Bar Chart），无需额外Python依赖。没有基线时绘制当前指标；结合`--baseline`时绘制基线与当前值的分组柱状图：

```bash
samples/net/zperf/scripts/zperf_regression.py --base-dir .. \
    --twister-json ../build/zperf_cur/twister.json \
    --baseline baseline.json --plot throughput.svg
```

报告包含多个平台时，每个文件名会追加平台名。因此上述示例会输出`throughput-qemu_x86_atom.svg`和`throughput-qemu_x86_64_atom.svg`。

译注：原页未附带这些生成结果图片；此处保留官方生成命令和文件名，不自行生成未测量数据的图表。


<a id="zperf-deterministic-loopback-throughput-qemu-x86-icount"></a>
<a id="zperf-loopback-icount"></a>
<a id="overview"></a>
<a id="how-it-works"></a>
<a id="configuration-knobs"></a>
<a id="implementation-notes-gotchas"></a>
<a id="usage"></a>
<a id="build-and-run-once"></a>
<a id="run-through-twister"></a>
<a id="baseline-and-regression-gate"></a>
<a id="continuous-integration"></a>
<a id="visualize-the-results"></a>

[上一章](P097_zperf网络流量生成器示例.md) · [返回大纲](大纲.md) · [下一章](P099_Latmon完整API参考.md)
