---
id: learning.zephyr-docs.boards-arm.page-6
title: ARM MPS2 AN521
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/arm/mps2/doc/mps2_an521.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="arm-mps2-an521"></a>

<a id="mps2-an521-board"></a>

# 第6章\_ARM MPS2+ AN521

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/arm/mps2/doc/mps2_an521.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

`mps2/an521`开发板配置用于运行在MPS2+ AN521上的Zephyr应用，支持MPS2+ AN521 ARM Cortex-M33 CPU及以下设备：


- 嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）
- 系统滴答系统时钟（SYSTICK / System Tick System Clock）
- Cortex-M系统设计套件（CMSDK）GPIO
- Cortex-M系统设计套件（CMSDK）UART

![官方原图：ARM MPS2+ AN521](images/mps21.jpg)

除支持实际硬件外，此配置还可通过QEMU模拟运行在MPS2+上的AN521平台。

更多开发板信息见[MPS2 FPGA网站](https://developer.arm.com/tools-and-software/development-boards/fpga-prototyping-boards/mps2)。

注意（Note）

此配置不保证适用于采用AN521的实际MPS2硬件系统或其他硬件。虽然已在实际硬件上测试，但主要用途是配合QEMU及ARM Cortex-M33单元测试。

<a id="zephyr-board-options"></a>

### Zephyr开发板选项（Board Options）

MPS2+ AN521是双核片上系统（SoC），CPU0和CPU1均采用Cortex-M33架构。Zephyr支持为两个CPU构建固件镜像；CPU0支持ARM安全扩展（Security Extensions），可以构建安全（Secure）及非安全（Non-Secure）固件。

`BOARD`选项汇总如下：

<table>
<tr>
<th>开发板目标（BOARD）</th>
<th>说明（Description）</th>
</tr>
<tr>
<td><code>mps2/an521/cpu0</code></td>
<td>为CPU0构建安全固件，或仅安全态固件（Secure-Only）</td>
</tr>
<tr>
<td><code>mps2/an521/cpu0/ns</code></td>
<td>为CPU0构建非安全固件（Non-Secure）</td>
</tr>
<tr>
<td><code>mps2/an521/cpu1</code></td>
<td>为CPU1构建固件</td>
</tr>
</table>

<a id="memory-partitioning"></a>

### 存储器分区（Memory Partitioning）

AN521为代码空间分配4 MB，为SRAM分配4 MB。这些存储区域由两个内核共享，在安全和非安全区域中均存在地址别名（Alias）；安全别名地址相对非安全地址偏移`0x10000000`。

默认采用以下内存映射及分区方案。偏移值相对于4 MB代码块或SRAM块的基址，不计安全／非安全（S/NS）别名差异。

<table>
<tr>
<th>开发板（Board）</th>
<th>中央处理器（CPU）</th>
<th>代码空间（偏移量 / Offset）</th>
<th>SRAM（偏移量 / Offset）</th>
<th>安全／非安全别名（S/NS Alias）</th>
</tr>
<tr>
<td><code>mps2/an521/cpu0</code></td>
<td>0</td>
<td>4 MB（偏移0）</td>
<td>4 MB（偏移0）</td>
<td>安全态（S）</td>
</tr>
<tr>
<td><code>mps2/an521/cpu0/ns</code></td>
<td>0</td>
<td>512 KB（偏移1 MB）</td>
<td>512 KB（偏移1 MB）</td>
<td>非安全态（NS）</td>
</tr>
<tr>
<td><code>mps2/an521/cpu1</code></td>
<td>1</td>
<td>468 KB（偏移3628 KB）</td>
<td>512 KB（偏移1.5 MB）</td>
<td>非安全态（NS）</td>
</tr>
</table>

`mps2/an521/cpu0/ns`目标用于配合TF-M，Zephyr内存映射与TF-M上游定义的AN521映射一致。TF-M先启动安全处理环境（SPE），再初始化非安全处理环境（NSPE）中的Zephyr。非安全Zephyr镜像为安全引导加载程序和安全固件（TF-M）预留偏移空间，起始地址为`0x00100000`；SRAM偏移1 MB，从`0x28100000`开始。

`mps2/an521/cpu1`目标用于AN521的第二个内核，使用4 MB代码块的最后468 KB。此值用于兼容TF-M，因为TF-M将这最后468 KB标为未使用（Unused）。代码空间从偏移3628 KB（地址`0x0038B000`）开始，SRAM从偏移1.5 MB（地址`0x28180000`）开始。

此内存映射允许按需同时使用这两个替代目标，代价是第二内核的可用代码空间按TF-M最坏情况缩减。

使用`mps2/an521/cpu0/ns`或`mps2/an521/cpu1`时，需注意主目标`mps2/an521`占用的代码或SRAM容量，因为内存映射存在重叠。

<a id="hardware"></a>

## 硬件（Hardware）

ARM MPS2+ AN521提供以下硬件组件：


- 双核ARM Cortex-M33
- SSE-200子系统的软宏模型（SMM / Soft Macro Model）实现
- 存储器（Memory）


  - 4 MB代码存储器（SSRAM1）
  - 4 MB SRAM（SSRAM2及SSRAM3）
  - 16 MB并行SRAM（PSRAM），仅供非安全态使用
  - 8 KB非易失性代码存储器（NVM Code）
- 调试（Debug）


  - P-JTAG、串行线调试（SWD）及16位跟踪（TRACE）
  - UART串口
- 接口（Interface）


  - 连接到EXP扩展端口的高级高性能总线GPIO（AHB GPIO）
  - 通用异步收发器（UART）
  - 串行外设接口（SPI）
  - 集成电路间总线（I2C）
  - 集成电路间音频总线（I2S）
  - 彩色液晶显示器串行接口（LCD Serial Interface）
  - 以太网（Ethernet）
  - 视频图形阵列接口（VGA）
- 板载外设（On-Board Peripherals）


  - 彩色液晶显示器（LCD）
  - 八个LED
  - 八个开关
  - 外部SSRAM1、SSRAM2及SSRAM3
  - SMSC9220
  - CS42L52

<a id="user-push-buttons"></a>

### 用户按键（User Push Buttons）

`mps2/an521`提供以下用户按键：


- ON：上电
- nSRST：Cortex-M33系统复位及CoreSight调试复位
- USERPB0和USERPB1：用户自定义按键

<a id="supported-features"></a>

### 支持的功能（Supported Features）


- 详情见[V2M MPS2](P005_V2M_MPS2.md#mps2)。

<a id="interrupt-controller"></a>

### 中断控制器（Interrupt Controller）

MPS2+ AN521是基于Cortex-M33的SoC，具有15个固定异常（Exceptions）和77个中断请求（IRQ）。

基于Cortex-M33的开发板使用向量异常（Vectored Exceptions），每个异常直接通过向量表调用处理程序。

Zephyr为异常1–7、11、12、14和15提供处理程序，如下表所示：

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
<td>7</td>
<td>安全故障（SecureFault）</td>
<td>从非安全空间（NS Space）未经授权访问安全区域</td>
<td>系统致命错误（System Fatal Error）</td>
</tr>
<tr>
<td>8</td>
<td>保留（Reserved）</td>
<td></td>
<td>未处理（Not Handled）</td>
</tr>
<tr>
<td>9</td>
<td>保留（Reserved）</td>
<td></td>
<td>未处理（Not Handled）</td>
</tr>
<tr>
<td>10</td>
<td>保留（Reserved）</td>
<td></td>
<td>未处理（Not Handled）</td>
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
<td>13</td>
<td>保留（Reserved）</td>
<td></td>
<td>未处理（Not Handled）</td>
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
<tr>
<td>16</td>
<td>保留（Reserved）</td>
<td></td>
<td>未处理（Not Handled）</td>
</tr>
<tr>
<td>17</td>
<td>保留（Reserved）</td>
<td></td>
<td>未处理（Not Handled）</td>
</tr>
<tr>
<td>18</td>
<td>保留（Reserved）</td>
<td></td>
<td>未处理（Not Handled）</td>
</tr>
</table>

<a id="pin-mapping"></a>

### 引脚映射（Pin Mapping）

ARM MPS2+ AN521有四个CMSDK AHB GPIO控制器，每个提供16位I/O，负责引脚复用（Pin Muxing）、输入／输出、上拉等功能。

GPIO控制器引脚按以下编号顺序引出：


- 引脚0–15属于GPIO0
- 引脚16–31属于GPIO1
- 引脚32–47属于GPIO2
- 引脚48–51属于GPIO3

ARM MPS2+ AN521开发板引脚与GPIO控制器的映射：


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

更多细节见[MPS2+ AN521技术参考手册（TRM）](https://developer.arm.com/documentation/dai0521/latest/)。

<a id="led"></a>

### 发光二极管（LED）

MPS2+有八个板载LED，连接到串行配置控制器（SCC / Serial Configuration Controller）。

注意（Note）

SCC寄存器`CFG_REG1`的位`[7:0]`控制LEDa，0表示熄灭（OFF），1表示点亮（ON）。

<a id="system-clock"></a>

### 系统时钟（System Clock）

MPS2+ AN521连接了以下时钟：


- `MAINCLK : 20MHz`
- `SYSCLK : 20MHz`
- `S32KCLK : 32kHz`
- `TRACECLK : 20MHz`
- `SWCLKTCK : 20MHz`
- `TRACECLKIN : 20MHz`

<a id="serial-port"></a>

### 串口（Serial Port）

MPS2+ AN521有五路UART。Zephyr控制台默认使用UART0，对应板上的J10。

UART2为保留接口；UART1、UART3及UART4是EXP端口上的复用功能（Alternate Functions）。

<a id="security-components"></a>

### 安全组件（Security Components）


- 实现定义归属单元（[IDAU](https://developer.arm.com/documentation/100690/latest/Attribution-units--SAU-and-IDAU-) / Implementation Defined Attribution Unit）用于定义安全及非安全内存映射。默认所有存储空间均仅允许安全态访问。
- 通过外设保护控制器（PPC / Peripheral Protection Controller）设置安全及非安全外设，可将外设分配为允许安全态或非安全态访问。
- 安全启动（Secure Boot）
- 安全[AMBA®](https://developer.arm.com/products/architecture/system-architectures/amba)互连（Secure AMBA Interconnect）

<a id="serial-configuration-controller-scc"></a>

### 串行配置控制器（SCC / Serial Configuration Controller）

MPS2+ AN521实现了串行配置控制（SCC）寄存器，用于分别控制外设时钟、复位信号、中断、引脚复用，以及LED和开关。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

MPS2+ AN521的CPU0支持Armv8-M安全扩展（Security Extension）。为`mps2/an521`构建的应用默认从安全态启动。

MPS2+ AN521的CPU1不支持Armv8-M安全扩展。

<a id="building-secure-non-secure-zephyr-applications-with-arm-trustzone"></a>

### 使用Arm® TrustZone®构建安全／非安全Zephyr应用

MPS2+ AN521 CPU0上的应用可包含安全与非安全固件镜像。安全镜像可使用Zephyr或可信固件M（TF-M）构建；非安全镜像始终使用Zephyr构建。两种方案如下。（[可信固件M（TF-M / Trusted Firmware M）](https://tf-m.docs.trustedfirmware.org/en/latest/building/tfm_build_instruction.html)）

注意（Note）

默认使用TF-M构建MPS2+ AN521 CPU0的安全镜像。

<a id="building-the-secure-firmware-with-tf-m"></a>

#### 使用TF-M构建安全固件（Secure Firmware）

用TF-M构建安全镜像、用Zephyr构建非安全镜像，需要以下步骤：


1. 使用`-DBOARD=mps2/an521/cpu0/ns`为MPS2+ AN521 CPU0构建非安全Zephyr应用。要触发TF-M构建，需启用Kconfig选项`BUILD_WITH_TFM`；构建非安全Zephyr应用时默认已启用。Zephyr构建系统会自动完成以下步骤：

  > - 按常规Zephyr应用构建非安全固件镜像
  > - 构建TF-M安全固件镜像（Secure Firmware Image）
  > - 合并生成的二进制镜像
  > - 按需构建引导加载程序镜像（MCUboot）

注意（Note）

根据TF-M配置，可能需要应用设备树覆盖文件（DTS Overlay）来调整非安全镜像的闪存及SRAM起始地址与大小。

<a id="building-the-secure-firmware-using-zephyr"></a>

#### 使用Zephyr构建安全固件

使用Zephyr同时构建安全及非安全固件镜像，需要以下步骤：


1. 为MPS2+ AN521 CPU0构建安全Zephyr应用，使用`-DBOARD=mps2/an521`，并在应用项目配置文件中设置`CONFIG_TRUSTED_EXECUTION_SECURE=y`及`CONFIG_BUILD_WITH_TFM=n`。
2. 使用`-DBOARD=mps2/an521/cpu0/ns`为MPS2+ AN521 CPU0构建非安全Zephyr应用。
3. 将两个二进制文件合并。

<a id="building-a-secure-only-application-on-mps2-an521-cpu0"></a>

### 在MPS2+ AN521 CPU0上构建仅安全态应用（Secure-Only）

按通常方式构建Zephyr应用，参见[构建应用（Building an Application）](../application/P001_应用开发.md#build-an-application)及[运行应用（Run an Application）](https://docs.zephyrproject.org/latest/develop/application/index.html#application-run)；运行于MPS2+ AN521 CPU0的固件使用`-DBOARD=mps2/an521`。

为MPS2+ AN521 CPU0构建安全／非安全应用时，安全应用必须配置安全归属单元／实现定义归属单元（SAU/IDAU），允许非安全固件访问它使用的全部CPU资源。这些配置必须在跳转到非安全应用之前完成。

安全固件阶段必须正确配置以下系统组件：


- AHB5 TrustZone内存保护控制器（MPC）
- AHB5 TrustZone外设保护控制器（PPC）
- 实现定义归属单元（IDAU / Implementation-Defined Attribution Unit）

更多细节见[Corelink SSE-200子系统（Subsystem）](https://developer.arm.com/documentation/dto0051/latest/subsystem-overview/about-the-sse-200)。

<a id="building-standalone-applications-on-mps2-an521-cpu1"></a>

### 在MPS2+ AN521 CPU1上构建独立应用（Standalone Applications）

可为MPS2+ AN521的第二个Cortex-M33远端内核（Remote Core）构建应用，该内核称为CPU1。

按通常方式构建Zephyr应用，参见[构建应用（Building an Application）](../application/P001_应用开发.md#build-an-application)及[运行应用（Run an Application）](https://docs.zephyrproject.org/latest/develop/application/index.html#application-run)；运行于MPS2+ AN521 CPU1的固件使用`-DBOARD=mps2/an521/cpu1`。

Zephyr构建过程会自动为CPU0构建最小的空安全态固件，用于启动远端内核CPU1。

<a id="flashing"></a>

### 烧录（Flashing）

MPS2+ AN521提供：


- 连接主机的USB接口，提供大容量存储设备（Mass Storage）
- 串口，对应MPS2+板上的J10

按上述说明构建应用。以下以CPU0上仅安全态的[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

```text
# From the root of the zephyr repository
west build -b mps2/an521 samples/hello_world
```

打开串口终端（如minicom或PuTTY），设置如下：


- 速率（Speed）：115200波特率
- 数据位（Data）：8位
- 奇偶校验（Parity）：无（None）
- 停止位（Stop Bits）：1位

复位开发板后，对应串口应显示以下消息：

```text
Hello World! mps2_an521
```

<a id="uploading-an-application-to-mps2-an521"></a>

#### 向MPS2+ AN521上传应用（Uploading an Application）

应用可使用ELF、HEX或BIN格式。开发板启动时，从板载Micro SD卡读取文件并烧录二进制程序。主板配置控制器（MCC / Motherboard Configuration Controller）负责加载FPGA镜像及二进制程序。

通过USB端口将MPS2+连接到主机，应出现USB大容量存储设备，默认名称为`V2M_MPS2`。

更新需要三个步骤：


1. 将应用文件复制到`<MPS2 device name>/SOFTWARE/`。
2. 打开`<MPS2 device name>/MB/HBI0263C/AN521/images.txt`。
3. 按以下方式更新`AN521/images.txt`：

```text
TITLE: Versatile Express Images Configuration File

[IMAGES]
TOTALIMAGES: 1 ;Number of Images (Max: 32)

IMAGE0ADDRESS: 0x10000000 ;Please select the required executable program

IMAGE0FILE: \SOFTWARE\zephyr.bin
```

复位开发板后，对应串口应显示以下消息：

```text
Hello World! mps2_an521
```

注意（Note）

TF-M集成及多镜像场景的更多细节见`tfm_integration`示例。

## 译注

原文主目标部分段落使用mps2/an521，功能表与其他命令则使用包含cpu0或cpu1的目标，均保留原始写法。CPU0和CPU1的代码／SRAM地址、与TF-M的重叠条件及启动CPU1所需的CPU0固件均未合并省略。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [Attribution-units--SAU-and-IDAU-](https://developer.arm.com/documentation/100690/latest/Attribution-units--SAU-and-IDAU-)：<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)>。
- [](https://developer.arm.com/documentation/dai0521/latest/)：<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)>。
- [about-the-sse-200](https://developer.arm.com/documentation/dto0051/latest/subsystem-overview/about-the-sse-200)：<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)>。
- [amba](https://developer.arm.com/products/architecture/system-architectures/amba)：<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)>。
- [mps2](https://developer.arm.com/tools-and-software/development-boards/fpga-prototyping-boards/mps2)：<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)>。

---

[上一章](P005_V2M_MPS2.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P007_ARM_V2M_MPS2_Armv6-m_AN383.md)
