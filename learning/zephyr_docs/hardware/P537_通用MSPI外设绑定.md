---
id: learning.zephyr-docs.hardware.emumembind-2
title: 通用MSPI外设绑定
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/mspi/zephyr,peripheral-device-mspi.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第537章\_通用MSPI外设绑定

<a id="dtbinding-zephyr-peripheral-device-mspi"></a>

原文：[zephyr,peripheral-device (on mspi bus)](https://docs.zephyrproject.org/latest/build/dts/api/bindings/mspi/zephyr,peripheral-device-mspi.html)。读取日期：2026-10-13，`latest`。

`zephyr,peripheral-device` 是通用 MSPI 外设绑定，描述 `mspi` 总线上的外设，例如处于外设模式的另一片芯片，或外部外设。本地 MSPI 控制器是主设备，这个节点表示与它通信的外设。适用于片上系统（System on Chip，SoC）之间的链路，或没有专用 Zephyr 驱动、由应用定义的外设。相关开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=zephyr,peripheral-device)。绑定文件名中的 `-mspi` 区分总线版本，不属于兼容字符串。

## 537.1\_频率、线路模式与数据速率

下面的属性配置**多线串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）**外设。`int` 为整数，`string` 为字符串，`boolean` 为布尔属性，`array` 为数值数组，`phandle` 为设备树节点引用，`phandle-array` 为节点引用及其说明单元数组。原页没有已弃用的专用属性；基础属性中的 `reg` 和 `compatible` 均必需。

必需属性 `mspi-max-frequency` 的类型为 `int`，设置设备的最大时钟频率，单位赫兹（Hertz，Hz）；设备树中通常填写初始化完成后的目标工作频率。

属性 `mspi-io-mode` 的类型为 `string`，设置**输入输出（Input/Output，I/O）**线路模式，通常表示初始化后的目标模式。完整合法值如下；模式标识保持原名，便于与驱动配置对照。

| 线路模式族 | 合法值 |
| --- | --- |
| 单线（Single） | `MSPI_IO_MODE_SINGLE` |
| 双线（Dual） | `MSPI_IO_MODE_DUAL`、`MSPI_IO_MODE_DUAL_1_1_2`、`MSPI_IO_MODE_DUAL_1_2_2` |
| 四线（Quad） | `MSPI_IO_MODE_QUAD`、`MSPI_IO_MODE_QUAD_1_1_4`、`MSPI_IO_MODE_QUAD_1_4_4` |
| 八线（Octal） | `MSPI_IO_MODE_OCTAL`、`MSPI_IO_MODE_OCTAL_1_1_8`、`MSPI_IO_MODE_OCTAL_1_8_8` |
| 十六线（Hex） | `MSPI_IO_MODE_HEX`、`MSPI_IO_MODE_HEX_8_8_16`、`MSPI_IO_MODE_HEX_8_16_16` |

属性 `mspi-data-rate` 的类型为 `string`，设置数据速率，通常也是初始化后的目标值。合法值为 `MSPI_DATA_RATE_SINGLE`、`MSPI_DATA_RATE_S_S_D`、`MSPI_DATA_RATE_S_D_D`、`MSPI_DATA_RATE_DUAL`，分别保留单速率、混合阶段速率和双速率的官方标识。

## 537.2\_时钟、芯片使能与事务阶段

**芯片使能（Chip Enable，CE）**用于选择外设；控制器可为同一 MSPI 实例上的多个外设分配专用 CE 编号。**时钟极性（Clock Polarity，CPOL）**和**时钟相位（Clock Phase，CPHA）**共同确定时钟模式。传输位序涉及**最高有效位（Most Significant Bit，MSB）**与**最低有效位（Least Significant Bit，LSB）**。

| 属性 | 类型 | 中文说明与合法值 |
| --- | --- | --- |
| `mspi-hardware-ce-num` | `int` | MSPI 硬件 CE 编号，供控制器原生管理同一实例上的多个外设 |
| `mspi-cpp-mode` | `string` | 时钟模式：`MSPI_CPP_MODE_0` 对应 CPOL=0、CPHA=0；`MSPI_CPP_MODE_1` 对应 0、1；`MSPI_CPP_MODE_2` 对应 1、0；`MSPI_CPP_MODE_3` 对应 1、1 |
| `mspi-endian` | `string` | 选择 MSB 或 LSB 优先传输，合法值 `MSPI_LITTLE_ENDIAN`、`MSPI_BIG_ENDIAN` |
| `mspi-ce-polarity` | `string` | CE 极性，大多数情况下为低有效；合法值 `MSPI_CE_ACTIVE_LOW`（低有效）、`MSPI_CE_ACTIVE_HIGH`（高有效） |
| `mspi-dqs-enable` | `boolean` | 为支持的设备启用数据选通模式；检查控制器的 `dqs-support` 能力后，在硬件支持时配置 MSPI 硬件 |
| `mspi-hold-ce` | `boolean` | 由控制器通过软件管理 CE，使多个 MSPI 事务之间不释放 CE |
| `rx-dummy` | `int` | 接收方向中，地址阶段与数据阶段之间的数据或时钟周期数；为 `0` 时禁用接收空周期阶段 |
| `tx-dummy` | `int` | 发送方向中，地址阶段与数据阶段之间的数据或时钟周期数；为 `0` 时禁用发送空周期阶段 |
| `read-command` | `int` | 接收方向使用的读命令 |
| `write-command` | `int` | 原文写作“在 RX 方向发送的写命令”，见下方译注 |
| `command-length` | `string` | 读写命令长度，单位字节；合法值 `INSTR_DISABLED`、`INSTR_1_BYTE`、`INSTR_2_BYTE`，分别为禁用、1 字节、2 字节 |
| `address-length` | `string` | 地址阶段发送的地址长度，单位字节；合法值 `ADDR_DISABLED`、`ADDR_1_BYTE`、`ADDR_2_BYTE`、`ADDR_3_BYTE`、`ADDR_4_BYTE`，分别为禁用和 1 至 4 字节 |

**数据选通（Data Strobe，DQS）**是此处的时序功能；`dqs-support` 是控制器绑定中的能力属性。**发送（Transmit，TX）**和**接收（Receive，RX）**分别表示两个传输方向。**空周期（Dummy Cycle）**出现在地址与数据阶段之间。

保持 CE 的典型用法是处理变长数据包：第一次 MSPI 事务读取长度，第二次事务读取该长度指定的字节数，两次事务之间不释放 CE。

译注：官方绑定对 `write-command` 的说明确实写为 RX。本译文保留这一表述并指出它与“写命令”的方向语义存在疑点，未擅自把原文改成 TX。

## 537.3\_内存映射、扰码与自动断开

**内存映射（Memory Mapping）**可在控制器支持时，将外设存储器映射到**片上系统（System on Chip，SoC）**的系统地址空间，使设备可作为外部**随机存取存储器（Random Access Memory，RAM）**使用并执行代码。

属性 `memmap-config` 的类型为 `array`，配置内存映射。各项含义如下：

| 数组项 | 中文说明 |
| --- | --- |
| `enable` | 是否启用内存映射 |
| `address_offset` | 相对平台专属内存映射地址区域起点的偏移，单位字节 |
| `size` | 要启用或禁用的内存映射区域大小，单位字节 |
| `permission` | 授予区域的权限：读写（Read/Write，RW）或只读（Read Only，RO） |

原说明中的默认参数示意保留如下：

```text
default =
<
  .enable         = false;
  .address_offset = 0;
  .size           = 0;
  .permission     = 0;
>
```

属性 `scramble-config` 的类型为 `array`，配置**扰码（Scrambling）**功能。支持硬件扰码的控制器可用它为外部设备存储的数据或代码提供额外保护。

| 数组项 | 中文说明 |
| --- | --- |
| `enable` | 是否启用扰码 |
| `address_offset` | 起始地址偏移，单位字节；可相对平台专属内存映射区域起点，也可相对物理设备地址 |
| `size` | 要启用或禁用的区域大小，单位字节 |

原说明中的默认参数示意为：

```text
default =
<
  .enable         = false;
  .address_offset = 0;
  .size           = 0;
>
```

属性 `ce-break-config` 的类型为 `array`，配置**自动断开芯片使能（Automatic CE Break）**。它通常用于具有存储边界或要求定期内部刷新的设备，例如**伪静态随机存取存储器（Pseudo-Static Random Access Memory，PSRAM）**。

| 数组项 | 中文说明 |
| --- | --- |
| `mem_boundary` | 一次传输不应跨越的设备存储边界，单位字节 |
| `time_to_break` | 一次传输不应超过的最大时间，单位微秒（Microsecond，μs；原文记为 `us`） |

原说明中的默认参数示意为：

```text
default =
<
  .mem_boundary    = 0;
  .time_to_break   = 0;
>
```

译注：本页在描述中给出以上默认参数示意，但没有像仿真设备绑定那样另列这三个属性的“Default value”字段；此处保留这一差别。

## 537.4\_独立供电开关与共享稳压器

**通用输入输出（General-Purpose Input/Output，GPIO）**可控制独立的供电开关。属性 `supply-gpios` 的类型为 `phandle-array`，提供控制设备供电的 GPIO 说明符；设备存在专用供电开关时应提供此属性，供电状态完全由设备驱动负责。

属性 `vin-supply` 的类型为 `phandle`，引用控制设备供电的**稳压器（Regulator）**。被引用节点必须具有稳压器兼容字符串。设备由共享稳压器供电时应提供此属性，供电状态取决于该稳压器所供应的全部设备的请求状态。

若同时提供这两个属性，必须先请求稳压器，再把供电 GPIO 设为有效；关闭时必须先把供电 GPIO 设为无效，再释放稳压器。

## 537.5\_状态、兼容字符串与寄存器

本页 `int` 为整数，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`boolean` 为布尔属性，`compound` 为复合类型。**节点引用（Phandle）**用来指向其他节点；`phandle-array` 表示节点引用及其说明单元，`phandles` 表示节点引用列表。

`status` 的类型为 `string`，描述节点所代表硬件或其他资源的运行状态。`okay` 表示资源可运行，例如可供驱动使用；`disabled` 表示资源不可运行，系统应将它视为不存在。合法值为 `okay`、`disabled`、`reserved`、`fail`、`fail-sss`。详见《设备树规范》（Devicetree Specification）v0.4 第 2.3.4 节。

`compatible` 的类型为 `string-array`，是**必需属性**。它用字符串列表定义节点代表的硬件或其他资源类型；设备驱动检查特定兼容字符串，以寻找应由自己管理的节点。推荐格式为 `vendor,device`，其中 `vendor` 是厂商简称，`device` 通常取自数据手册。多个值应按从最具体到最通用排列，使某一通用家族的具体设备能匹配当前可用的最具体驱动。详见规范 v0.4 第 2.3.1 节。

`reg` 的类型为 `array`，给出寻址设备所需的信息，其含义取决于设备及 `compatible`。通常是一组“地址、长度”对，每对称为**寄存器块（Register Block）**，数值惯常写成十六进制。详见规范 v0.4 第 2.3.6 节。

`reg-names` 的类型为 `string-array`，为 `reg` 中各寄存器块提供可选名称。以下保留官方示例；`#address-cells` 和 `#size-cells` 分别声明地址与长度使用的 32 位单元数。

```dts
  / {
       soc {
           #address-cells = <1>;
           #size-cells = <1>;

           uart@1000 {
               reg = <0x1000 0x2000>, <0x3000 0x4000>;
               reg-names = "foo", "bar";
           };
       };
  };
```

`uart@1000` 节点有两个寄存器块：名称 `foo` 对应基址 `0x1000`、大小 `0x2000`；名称 `bar` 对应基址 `0x3000`、大小 `0x4000`。这里 uart 是**通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）**节点名称，示例只是演示寄存器块命名。

## 537.6\_地址映射与中断

`ranges` 的类型为 `compound`，定义总线子地址空间与总线节点父地址空间之间的映射或转换。它通常为空，或由“子总线地址、父总线地址、长度”三元组构成。**空属性表示两侧地址空间相同，不需要转换；总线节点没有此属性时，则认为子节点与父地址空间之间不存在映射。**详见规范 v0.4 第 2.3.8 节。

下列属性描述**中断（Interrupt）**，参见规范 v0.4 第 2.4 节“中断与中断映射”。

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `interrupts` | `array` | 设备产生的中断，编码为一个或多个中断说明符；格式由设备在中断树中的位置决定，具有相同 `interrupt-parent` 的设备使用相同格式 |
| `interrupts-extended` | `compound` | 扩展中断说明符，可替代 `interrupts` |
| `interrupt-names` | `string-array` | 设备各中断的可选名称；中断本身在 `interrupts` 或 `interrupts-extended` 中定义 |
| `interrupt-parent` | `phandle` | 若存在，引用负责处理此设备所产生中断的节点 |

## 537.7\_标签、时钟与地址单元

**时钟提供者（Clock Provider）**提供设备使用的时钟。下表同时保留标签和子节点地址编码相关属性。

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `label` | `string` | 描述设备的可读字符串；除逐案确有需要外，已不推荐使用此属性。参见规范 v0.4 第 4.1.2 节“其他属性” |
| `clocks` | `phandle-array` | 设备的时钟提供者信息，通常应遵守下述 dt-schema 时钟绑定约定 |
| `clock-names` | `string-array` | `clocks` 中各时钟提供者的可选名称 |
| `#address-cells` | `int` | 子节点 `reg` 地址字段所用的 `<u32>` 单元数量 |
| `#size-cells` | `int` | 子节点 `reg` 大小字段所用的 `<u32>` 单元数量 |

`<u32>` 是 32 位无符号单元，两个 cells 属性见规范 v0.4 第 2.3.5 节。时钟约定见 [dt-schema 的 clock.yaml](https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml)。`status`、`compatible`、`reg`、`interrupts` 和 `label` 另见官方[重要属性（Important Properties）](https://docs.zephyrproject.org/latest/build/dts/intro-syntax-structure.html#dt-important-props)。

## 537.8\_DMA、输入输出与邮箱通道

**直接存储器访问（Direct Memory Access，DMA）**属性描述设备的 DMA 能力、通道和地址映射；输入输出（Input/Output，I/O）及邮箱（Mailbox）属性描述关联通道。IPM 是**处理器间消息（Inter-Processor Messaging）**接口。

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `dma-coherent` | `boolean` | 表示设备支持一致性 DMA 操作，见规范 v0.4 第 2.3.10 节 |
| `dmas` | `phandle-array` | 与设备相关的 DMA 通道说明符 |
| `dma-names` | `string-array` | `dmas` 中各 DMA 通道说明符的可选名称 |
| `dma-ranges` | `compound` | 定义总线物理地址空间与其父总线物理地址空间之间的映射或转换，见规范 v0.4 第 2.3.9 节 |
| `io-channels` | `phandle-array` | 与设备相关的 I/O 通道说明符 |
| `io-channel-names` | `string-array` | `io-channels` 中各通道说明符的可选名称 |
| `mboxes` | `phandle-array` | 与设备相关的邮箱/IPM 通道说明符 |
| `mbox-names` | `string-array` | `mboxes` 中各邮箱说明符的可选名称 |

## 537.9\_电源域与硬件锁

**电源域（Power Domain）**描述设备所属供电域；**硬件自旋锁（Hardware Spinlock）**为硬件提供的锁资源。属性如下：

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `power-domains` | `phandle-array` | 与设备相关的电源域说明符 |
| `power-domain-names` | `string-array` | `power-domains` 中各电源域说明符的可选名称 |
| `#power-domain-cells` | `int` | `power-domains` 属性中的单元数量 |
| `hwlocks` | `phandle-array` | 与设备相关的硬件自旋锁标识 |
| `hwlock-names` | `string-array` | `hwlocks` 中各锁说明符的可选名称 |

## 537.10\_初始化、唤醒和运行时电源管理

`zephyr,deferred-init` 为 `boolean` 属性：启动时不自动初始化设备，应使用 `device_init()` 手动初始化。

`wakeup-source` 为 `boolean` 属性，标识设备可以作为**唤醒源（Wakeup Source）**。提供它后，设备会设置一个专门标志，告知系统该设备具备唤醒系统的能力。这类设备的唤醒功能默认禁用，即其中断不会唤醒系统，必要时可在运行期间启用。

`zephyr,pm-device-runtime-auto` 为 `boolean` 属性，在初始化函数执行后自动为设备配置**运行时电源管理（Runtime Power Management）**。

`zephyr,disabling-power-states` 的类型为 `phandles`，列出会关闭此设备电源的电源状态。

---

[上一章：MSPI仿真Flash绑定](P536_MSPI仿真Flash绑定.md) · [下一章：模拟Flash绑定](P538_模拟Flash绑定.md) · [返回大纲](大纲.md)
