---
id: learning.zephyr-docs.driver_samples.page-24
title: MSPI吞吐量示例
kind: reference
status: maintained
domains: [zephyr, driver_samples, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/mspi/mspi_throughput/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="mspi-throughput"></a>

# 第24章\_MSPI吞吐量示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/drivers/mspi/mspi_throughput/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 24.1\_概览（Overview）

本例通过测量不同缓冲区（Buffer）大小、分组（Packet）配置下的传输速率，演示MSPI吞吐量（Throughput）性能测试。它执行一系列测试，以寻找能获得最高吞吐量和效率（Efficiency）的传输参数。

测试覆盖：

- 缓冲区大小：4、16、64、256、1024、1500和2304字节。
- 每次传输的分组数：1、4和16。
- 每个测试用例的总传输量：32 KB。
- 性能指标：吞吐量（MB/s）、效率（%）、CPU负载（%）和延迟（Latency）。

**注意：**延迟根据效率损失估算，是估计值；它不出现在汇总表中，而在每个测试用例的详细结果中打印。

本例支持直接存储器访问（Direct Memory Access，DMA）和CPU驱动的轮询（Polling）模式。启用`CONFIG_CPU_LOAD`时，通过[CPU负载（CPU Load）子系统](../observability/P007_CPU负载.md#cpu-load)报告负载百分比；该子系统支持Cortex-M、RISC-V和Cortex-A，且仅支持单核。

<a id="goals-and-future-work"></a>

## 24.2\_目标与后续工作（Goals and future work）

当前示例测量**控制器侧（Controller-side）**吞吐量和效率，用于观察驱动在不同分组大小、分组数下的表现，并比较DMA与先进先出队列（First In, First Out，FIFO）方式及CPU利用率。不论总线另一端是闪存、从设备还是主机，这种方式都可用于分析MSPI控制器的特性。

未来可能扩展为由两颗片上系统（System on Chip，SoC）分别运行控制器模式（Controller Mode）和外设模式（Peripheral Mode），通过简单协议测量完整链路吞吐量。这项扩展依赖明确的协议和MSPI外设支持。

> 译注——测量边界：这是原文对当前测量目标和未来计划的区分，不能把控制器侧发送结果解释为两端完整通信、接收校验或有效载荷吞吐量已验证。

<a id="configuration"></a>

## 24.3\_配置（Configuration）

MSPI设备参数——时钟频率、I/O模式、数据速率、字节序（Endianness）、命令和地址长度等——由`MSPI_DEVICE_CONFIG_DT()`从目标设备的设备树节点取得。具体数值见所用开发板的覆盖文件（Overlay）。

每个测试用例的总传输量通过Kconfig选项`CONFIG_SAMPLE_MSPI_THROUGHPUT_TOTAL_TRANSFER_SIZE`设置，默认32 KB。

> 译注——大小单位：所读[Kconfig](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/mspi/mspi_throughput/Kconfig)默认值为32768字节，取值范围1024—1048576字节。因此原文这里的32 KB实际对应32 KiB。

<a id="hardware-setup"></a>

## 24.4\_硬件设置（Hardware Setup）

需要在开发板覆盖文件中定义`dev0`别名，使其指向MSPI目标设备节点，例如控制器下具有`reg = <0>`的虚拟或外设节点。示例通过`dev0`的总线取得控制器，并用`MSPI_DEVICE_ID_DT(DT_ALIAS(dev0))`取得设备索引与片选（Chip Select）。

<a id="building-and-running"></a>

## 24.5\_构建与运行（Building and Running）

以下保留官方页面生成的命令：

```bash
west build -b nrf7120dk_nrf7120_cpuapp samples/drivers/mspi/mspi_throughput
west build -t Test
west build -t MSPI
west build -t throughput
```

> 译注——原命令生成问题：所读[README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/mspi/mspi_throughput/README.rst)把goals写为“Test MSPI throughput”，因此网页产生三个名为Test、MSPI、throughput的构建目标。所读[CMakeLists.txt](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/mspi/mspi_throughput/CMakeLists.txt)没有定义这些示例专用目标，不能把它们当作已核实的运行步骤。当前[tests.yaml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/mspi/mspi_throughput/tests.yaml)列出的板目标是nrf7120dk/nrf7120/cpuapp，也与原命令的下划线形式不同。实际构建须从所用版本的板目标、覆盖配置及运行方式重新核对，本文不将这段原命令标成可直接执行。

<a id="sample-output"></a>

### 24.5.1\_示例输出（Sample Output）

示例为每种测试配置输出详细性能指标。下面是原文给出的nRF7120在32 MHz时钟、每用例总传输量32 KB下的输出。

> 译注——原表排版恢复：原网页中的console代码块为空，性能数据因上游缩进问题落在块外。下面按同一官方README中的原始文本恢复等宽排版；21行测量值和汇总结果均保留，没有重新测量或替换数据。

```text
=== TEST RESULTS ===
BufSize  PktCnt   Time         Throughput   Efficiency   CPU Load
(bytes)           (us)         (MB/s)       (%)          (%)
-------------------------------------------------------------------
4        1        87432        0.536        3.51         100.00
4        4        79175        0.444        2.91         100.00
4        16       76135        0.423        2.77         100.00
16       1        31622        1.112        7.29         100.00
16       4        28646        1.125        7.37         100.00
16       16       28037        1.123        7.36         100.00
64       1        7910         4.074        26.70        99.99
64       4        7158         4.400        28.83        99.99
64       16       6956         4.501        29.50        99.99
256      1        3610         8.724        57.17        71.36
256      4        3460         9.049        59.31        69.28
256      16       3424         9.131        59.84        68.87
1024     1        2441         12.827       84.06        26.50
1024     4        2403         13.011       85.27        25.00
1024     16       2393         13.061       85.59        24.63
1500     1        2319         13.494       88.43        19.20
1500     4        2295         13.622       89.27        18.15
1500     16       2289         13.654       89.48        17.89
2304     1        2234         14.001       91.76        13.64
2304     4        2218         14.093       92.36        12.83
2304     16       2212         14.128       92.59        12.55


=== SUMMARY REPORT ===
Best TX Performance: 14.13 MB/s (buffer size=2304, packet count=16)
=== MSPI Throughput Test Complete ===
```

各字段含义如下：

| 字段 | 原文说明 |
| --- | --- |
| BufSize | 每次传输使用的缓冲区大小，单位字节 |
| PktCnt | 每次传输包含的分组数量 |
| Time | 总传输时间，原文称单位为微秒，并在括号中写CPU周期 |
| Throughput | 测得的吞吐量，原文单位为MB/s |
| Efficiency | 实际吞吐量占理想吞吐量的百分比 |
| CPU Load | 启用CONFIG_CPU_LOAD时的CPU利用率百分比 |

汇总报告指出获得最高吞吐量的配置。

> 译注——时间与速率单位：所读[main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/mspi/mspi_throughput/src/main.c)的print_test_results()直接打印transfer_cycles，尽管表头标为us；它没有在该列进行周期到微秒的换算。吞吐量计算则会用硬件周期频率换算秒，并除以MB(1)；[util.h](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/sys/util.h)将MB(1)定义为1048576字节，因此数值采用MiB/s。比较其他工具结果前应先统一时间和容量单位，不能凭原表头混用。

<a id="performance-analysis"></a>

### 24.5.2\_性能分析（Performance Analysis）

示例计算以下指标：

- **吞吐量（Throughput）**：实际数据传输速率，原文以MB/s表示；用总传输字节数（含命令和地址开销）除以传输时间。
- **效率（Efficiency）**：实际吞吐量相对理想吞吐量的百分比。原文给出的四线模式（Quad Mode）公式为`(clock_frequency * 4) / 8`，其中4表示数据线数量，8表示每字节位数。
- **CPU负载（CPU Load）**：启用`CONFIG_CPU_LOAD`后，通过CPU负载子系统测量传输期间的利用率；在受支持的架构上采用同一接口。
- **估算延迟（Estimated Latency）**：根据效率损失估算每个缓冲区的开销，用于寻找合适的缓冲区大小。

因此可用它分析最大吞吐量对应的缓冲区大小、分组批处理（Packet Batching）对性能的影响，以及不同传输配置的CPU开销。

> 译注——当前计算口径：上述main.c按I/O模式选择1、2、4、8或16根数据线来估算理想速率；四线公式是其中一个分支。其吞吐量分子实际按num_transfers累加命令和地址长度，而不是按total_buffers逐包累加，故不应直接把它称为外部仪器测得的总线字节率。代码还将传输描述的xfer_mode设为MSPI_DMA，启动提示则受CONFIG_MSPI_DMA影响；仅凭提示文字不足以证明已经完成两种底层方式的对比。以上为源码阅读结果，本批没有运行性能测试。

<a id="see-also"></a>

## 24.6\_相关接口（See also）

[MSPI接口参考](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html)。


对应官方文档源码：[samples/drivers/mspi/mspi_throughput/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/mspi/mspi_throughput/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/drivers/mspi/mspi_throughput/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/drivers/mspi/mspi_throughput/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P023_MSPI_NOR闪存示例.md) · [返回大纲](大纲.md) · [下一章](P025_Ambiq_MSPI时序扫描示例.md)
