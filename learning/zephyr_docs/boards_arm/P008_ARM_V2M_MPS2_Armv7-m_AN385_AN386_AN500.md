---
id: learning.zephyr-docs.boards-arm.page-8
title: ARM V2M MPS2 Armv7-m AN385 AN386 AN500
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/arm/mps2/doc/mps2_armv7m.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="arm-v2m-mps2-armv7-m-an385-an386-an500"></a>

<a id="mps2-armv7m-board"></a>

# 第8章\_ARM V2M MPS2 Armv7-m（AN385/AN386/AN500）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/arm/mps2/doc/mps2_armv7m.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

`mps2/an385`、`mps2/an386`及`mps2/an500`是Zephyr支持的三个基于Armv7-m的MPS2目标。本文介绍对AN385、AN386、AN500这三个目标及以下设备的支持：


- 嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）
- 系统滴答系统时钟（SYSTICK / System Tick System Clock）
- Cortex-M系统设计套件（CMSDK）UART

![官方原图：ARM V2M MPS2](images/mps21.jpg)

除实际硬件外，这些目标还可使用[FVP](https://developer.arm.com/downloads/view/FMFVP)模拟运行在MPS2+上的平台。

更多开发板信息见[V2M MPS2网站](https://developer.mbed.org/platforms/ARM-MPS2/)。

各开发板的应用说明如下：


- AN385见应用说明[Application Note AN385](https://documentation-service.arm.com/static/5ed107a5ca06a95ce53f89e3)
- AN386见应用说明[Application Note AN386](https://documentation-service.arm.com/static/5ed1094dca06a95ce53f8a9f)
- AN500见应用说明[Application Note AN500](https://documentation-service.arm.com/static/5ed112fcca06a95ce53f8eb3)

AN385还支持QEMU，并默认使用QEMU运行。

注意（Note）

这些目标不保证适用于实际MPS2硬件系统或其他硬件系统。

<a id="hardware"></a>

## 硬件（Hardware）

ARM V2M MPS2提供以下硬件组件：


- ARM Cortex-M芯片
- 面向Cortex-M的ARM物联网子系统（IoT Subsystem）
- 外形尺寸（Form Factor）：140 × 120 cm（单位依原文保留）
- 零总线周转SRAM（ZBTSRAM）：8 MB单周期SRAM及16 MB PSRAM
- 视频（Video）：QSVGA触摸屏面板、四位RGB VGA连接器
- 音频（Audio）：音频编解码器（Codec）
- Debug:


  - ARM JTAG20连接器
  - ARM并行跟踪连接器（Parallel Trace Connector，MICTOR38）
  - 20针Cortex调试连接器
  - 10针Cortex调试连接器
  - 用于FPGA调试的集成逻辑分析仪连接器（ILA Connector）
- 扩展（Expansion）


  - 通用输入输出（GPIO）
  - 串行外设接口（SPI）

注意（Note）

可使用4 MB闪存（位于ZBTSRAM 1，起始地址`0x00400000`）及4 MB RAM（位于ZBTSRAM 2和3，起始地址`0x20000000`）。

<a id="supported-features"></a>

### 支持的功能（Supported Features）


- 详情见[V2M MPS2](P005_V2M_MPS2.md#mps2)。

<a id="interrupt-controller"></a>

### 中断控制器（Interrupt Controller）

MPS2是基于Cortex-M的SoC，具有15个固定异常和45个IRQ。

基于Cortex-M3/4/7的开发板使用向量异常（Vectored Exceptions），每个异常直接通过向量表调用处理程序。

系统为异常1–6、11–12及14–15提供处理程序。下表列出各异常使用的处理程序。

<table>
<tr>
<th>异常编号（Exc#）</th>
<th>名称（Name）</th>
<th>备注（Remarks）</th>
<th>Zephyr内核中的用途（Used by Zephyr Kernel）</th>
</tr>
<tr>
<td>1</td>
<td>复位（Reset）</td>
<td></td>
<td>系统初始化（System Initialization）</td>
</tr>
<tr>
<td>2</td>
<td>不可屏蔽中断（NMI）</td>
<td></td>
<td>系统致命错误（System Fatal Error）</td>
</tr>
<tr>
<td>3</td>
<td>硬故障（Hard Fault）</td>
<td></td>
<td>系统致命错误（System Fatal Error）</td>
</tr>
<tr>
<td>4</td>
<td>存储器管理异常（MemManage）</td>
<td>内存保护单元故障（MPU Fault）</td>
<td>系统致命错误（System Fatal Error）</td>
</tr>
<tr>
<td>5</td>
<td>总线（Bus）</td>
<td></td>
<td>系统致命错误（System Fatal Error）</td>
</tr>
<tr>
<td>6</td>
<td>用法故障（Usage Fault）</td>
<td>未定义指令，或尝试切换到ARM模式</td>
<td>系统致命错误（System Fatal Error）</td>
</tr>
<tr>
<td>11</td>
<td>主管调用（SVC）</td>
<td></td>
<td>系统调用、内核运行时异常及中断卸载（IRQ Offloading）</td>
</tr>
<tr>
<td>12</td>
<td>调试监控（Debug Monitor）</td>
<td></td>
<td>系统致命错误（System Fatal Error）</td>
</tr>
<tr>
<td>14</td>
<td>可挂起系统调用（PendSV）</td>
<td></td>
<td>上下文切换（Context Switch）</td>
</tr>
<tr>
<td>15</td>
<td>系统节拍（SYSTICK）</td>
<td></td>
<td>系统时钟（System Clock）。</td>
</tr>
</table>

<a id="pin-mapping"></a>

### 引脚映射（Pin Mapping）

ARM V2M MPS2有四个GPIO控制器，负责引脚复用、输入／输出、上拉等功能。

GPIO控制器引脚按以下编号顺序引出：


- 引脚0–15属于GPIO 0
- 引脚16–31属于GPIO 1
- 引脚32–47属于GPIO 2
- 引脚48–51属于GPIO 3

ARM MPS2开发板引脚与GPIO控制器的映射：


- `D0 : EXT_0`
- `D1 : EXT_4`
- `D2 : EXT_2`
- `D3 : EXT_3`
- `D4 : EXT_1`
- `D5 : EXT_6`
- `D6 : EXT_7`
- `D7 : EXT_8`
- `D8 : EXT_9`
- `D9 : EXT_10`
- `D10 : EXT_12`
- `D11 : EXT_13`
- `D12 : EXT_14`
- `D13 : EXT_11`
- `D14 : EXT_15`
- `D15 : EXT_5`
- `D16 : EXT_16`
- `D17 : EXT_17`
- `D18 : EXT_18`
- `D19 : EXT_19`
- `D20 : EXT_20`
- `D21 : EXT_21`
- `D22 : EXT_22`
- `D23 : EXT_23`
- `D24 : EXT_24`
- `D25 : EXT_25`
- `D26 : EXT_26`
- `D27 : EXT_30`
- `D28 : EXT_28`
- `D29 : EXT_29`
- `D30 : EXT_27`
- `D31 : EXT_32`
- `D32 : EXT_33`
- `D33 : EXT_34`
- `D34 : EXT_35`
- `D35 : EXT_36`
- `D36 : EXT_38`
- `D37 : EXT_39`
- `D38 : EXT_40`
- `D39 : EXT_44`
- `D40 : EXT_41`
- `D41 : EXT_31`
- `D42 : EXT_37`
- `D43 : EXT_42`
- `D44 : EXT_43`
- `D45 : EXT_45`
- `D46 : EXT_46`
- `D47 : EXT_47`
- `D48 : EXT_48`
- `D49 : EXT_49`
- `D50 : EXT_50`
- `D51 : EXT_51`

外设映射（Peripheral Mapping）：


- `UART_3_RX : D0`
- `UART_3_TX : D1`
- `SPI_3_CS : D10`
- `SPI_3_MOSI : D11`
- `SPI_3_MISO : D12`
- `SPI_3_SCLK : D13`
- `I2C_3_SDA : D14`
- `I2C_3_SCL : D15`
- `UART_4_RX : D26`
- `UART_4_TX : D30`
- `SPI_4_CS : D36`
- `SPI_4_MOSI : D37`
- `SPI_4_MISO : D38`
- `SPI_4_SCK : D39`
- `I2C_4_SDA : D40`
- `I2C_4_SCL : D41`

更多细节见[MPS2技术参考手册（TRM）](https://developer.arm.com/documentation/100112/0200/)。

<a id="system-clock"></a>

### 系统时钟（System Clock）

V2M MPS2主时钟为24 MHz。

<a id="serial-port"></a>

### 串口（Serial Port）

V2M MPS2处理器有五路UART。原文随后称“两路UART”（Both the UARTs）都只有RX/TX两根线，不支持CTS/RTS流量控制或FIFO。Zephyr控制台默认使用UART0。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

<a id="flashing"></a>

### 烧录（Flashing）

V2M MPS2提供：


- 连接主机的USB接口，提供大容量存储设备（Mass Storage）和USB串口
- 串行闪存设备（Serial Flash Device），实现USB闪存盘文件存储
- 通过接口USB串口转接的物理UART连接

<a id="flashing-an-application-to-v2m-mps2"></a>

#### 向V2M MPS2烧录应用（Flashing an Application）

以下以AN385上的[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

```text
# From the root of the zephyr repository
west build -b mps2/an385 samples/hello_world
```

通过USB端口将V2M MPS2连接到主机，应出现大容量存储设备及USB串口。将生成的`zephyr.bin`复制到该存储设备，复位开发板后，对应串口应显示以下消息：

```text
Hello World! arm
```

<a id="running-an-applicatoin-with-fvp"></a>

#### 使用FVP运行应用（Running an Application）

以下是使用FVP运行同一示例的方法。将环境变量`ARMFVP_BIN_PATH`设为从此处下载的FVP所在位置。（[here](https://developer.arm.com/downloads/view/FMFVP)）

```text
export ARMFVP_BIN_PATH=/home/../FVP_MPS2/
```

随后使用通常的构建命令，再通过`west build -t run_armfvp`运行。

## 译注

原文外形尺寸使用cm，UART段落在写五路后又使用Both the UARTs；这些表述按原文保留。AN385默认QEMU与手动选择FVP的运行命令分别列出。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [](https://developer.arm.com/documentation/100112/0200/)：<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)>。
- [FMFVP](https://developer.arm.com/downloads/view/FMFVP)：<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)>。

---

[上一章](P007_ARM_V2M_MPS2_Armv6-m_AN383.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P009_MPS3_FPGA_Corstone_FVP.md)
