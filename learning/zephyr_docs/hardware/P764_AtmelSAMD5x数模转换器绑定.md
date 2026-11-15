---
id: learning.zephyr-docs.hardware.dacmcu-4
title: AtmelSAMD5x数模转换器绑定
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/dac/atmel,samd5x-dac.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第764章\_AtmelSAMD5x数模转换器绑定

<a id="dtbinding-atmel-samd5x-dac"></a>

原文：[atmel,samd5x-dac](https://docs.zephyrproject.org/latest/build/dts/api/bindings/dac/atmel,samd5x-dac.html)。读取日期：2026-10-13，`latest`。

`atmel,samd5x-dac` 是设备树绑定（Devicetree Binding），描述Atmel SAMD5x/E5x系列的数模转换器（Digital-to-Analog Converter，DAC）。

驱动为 [`drivers/dac/dac_samd5x.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/dac_samd5x.c)。使用此兼容字符串的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=atmel,samd5x-dac)。

## 764.1\_使能外设与原始节点示例

应在开发板设备树源码（Devicetree Source，DTS）或后续的覆盖文件（Overlay File）中使能DAC外设，并通过子节点绑定（Child Binding）属性配置每个通道。以下是官方原始示例：

```dts
&dac0 {
  status = "okay";
  reference = "intref";

  channel_0 {
    oversampling = <0>;
    refresh-period = <1>;
    current-control = <2>;
  };

  channel_1 {
    oversampling = <0>;
    refresh-period = <1>;
    current-control = <2>;
  };
};
```

**译注：原示例与同页属性表存在差异。** `oversampling` 和 `current-control` 的属性类型是 `string`，但示例使用整数；两个通道子节点还未列出下文要求的 `reg`。这里保留原代码以便对照，不将它当作已验证可直接构建的配置；编写实际节点时应按当前源码中的绑定类型、枚举与必需属性核对。

## 764.2\_控制器节点专用属性

以下属性用于控制器节点本身。`int` 为整数，`array` 为数值数组，`string` 为字符串，`boolean` 为布尔属性，`phandles` 为节点引用（Phandle）列表，`phandle-array` 为节点引用与说明单元数组，`string-array` 为字符串数组。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `atmel,assigned-clocks` | `phandle-array` | **必需**。分配的时钟（Assigned Clock）信息 |
| `atmel,assigned-clock-names` | `string-array` | **必需**。每个分配时钟的名称 |
| `reference` | `string` | 参考电压源（Reference Voltage Source）；原页列出可选源标识，未给出具体电压值；合法值：`vrefau, vddana, vrefab, intref` |
| `differential-mode` | `boolean` | 启用差分模式（Differential Mode），在VOUT0引脚输出通道0与通道1之差 |
| `#io-channel-cells` | `int` | **必需**。输入输出通道说明符（I/O Channel Specifier）中的单元数量（Cell Count）；固定值：`1` |
| `pinctrl-0` | `phandles` | 第一个引脚控制（Pin Control）状态的配置引用；具体内容由选用的引脚控制器驱动实现决定 |
| `pinctrl-1` | `phandles` | 第二个引脚控制（Pin Control）状态的配置引用；具体内容由选用的引脚控制器驱动实现决定，参见 `pinctrl-0` |
| `pinctrl-2` | `phandles` | 第三个引脚控制（Pin Control）状态的配置引用；具体内容由选用的引脚控制器驱动实现决定，参见 `pinctrl-0` |
| `pinctrl-3` | `phandles` | 第四个引脚控制（Pin Control）状态的配置引用；具体内容由选用的引脚控制器驱动实现决定，参见 `pinctrl-0` |
| `pinctrl-4` | `phandles` | 第五个引脚控制（Pin Control）状态的配置引用；具体内容由选用的引脚控制器驱动实现决定，参见 `pinctrl-0` |
| `pinctrl-names` | `string-array` | 已提供的引脚状态名称；名称数量必须与状态数量一致 |

通道说明单元名称（Specifier Cell Name）为 `output`，即输出；`io-channel` 说明符包含这一个单元。

## 764.3\_通道子节点属性

本节用于DAC通道子节点。这里的 `reg` 表示通道标识（Channel Identifier）；控制器自身的 `reg` 则表示设备寻址资源，二者所属节点不同。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `oversampling` | `string` | 过采样比（Oversampling Ratio）／插值深度（Interpolation Depth）。原文硬件字段编码0／1／2／3／4／5分别对应1／2／4／8／16／32倍过采样，1倍表示不插值。更高的过采样比可以更好地降低噪声，但会降低最大更新速率（Maximum Update Rate）；本属性使用下列字符串标识；合法值：`OSR_1, OSR_2, OSR_4, OSR_8, OSR_16, OSR_32` |
| `refresh-period` | `int` | DAC输出刷新周期（Refresh Period），**仅在输入数据不插值时有效**，原文称过采样速率为零，指前述编码0的情况。0禁用刷新模式；1至15对应 `Refresh period = REFRESH * 30µs`，即该数值乘以30微秒（Microsecond，µs） |
| `run-in-standby` | `boolean` | 使DAC通道在待机模式（Standby Mode）下继续工作 |
| `current-control` | `string` | 根据数据速率（Data Rate）选择输出缓冲器电流，按转换速率控制电流可降低功耗。原文硬件字段编码与时钟／采样率映射见后表；本属性使用下列字符串标识；合法值：`CC100K, CC1M, CC12M` |
| `reg` | `array` | **必需**。通道标识（Channel Identifier）；参见[设备树重要属性](https://docs.zephyrproject.org/latest/build/dts/intro-syntax-structure.html#important-properties) |
| `zephyr,resolution` | `int` | 此通道使用的DAC分辨率（Resolution） |
| `zephyr,buffered` | `boolean` | 为此通道启用输出缓冲器（Output Buffer） |
| `zephyr,internal` | `boolean` | 为此通道启用内部输出路径（Internal Output Path） |
| `zephyr,vref-mv` | `int` | 指定此通道所选参考源的电压，单位为毫伏（Millivolt，mV），使应用在需要计算时能够获取该值 |

`current-control` 的原文编码与时钟条件如下；GCLK_DAC为DAC时钟标识，kSPS／MSPS分别表示千／百万次每秒采样（Samples per Second）。属性字符串的合法值保留在上表，不根据名称推测额外映射。

| 原文编码 | 时钟条件 | 原文采样率 |
| --- | --- | --- |
| 0 | GCLK_DAC ≤ 1.2 MHz | 100 kSPS |
| 1 | 1.2 MHz < GCLK_DAC ≤ 6 MHz | 500 kSPS |
| 2 | 6 MHz < GCLK_DAC ≤ 12 MHz | 1 MSPS |

控制器的 `clock-names` 在本绑定中是**必需属性**；下文继承的通用描述虽使用“可选名称”，此处仍以必需性标记为准。

没有已弃用的控制器专用属性。以下是控制器继承的基础属性，不保证全部适用于本绑定；必需性以本页标记为准。

## 764.4\_状态、兼容字符串与寄存器

本页 `int` 为整数，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`boolean` 为布尔属性，`compound` 为复合类型。**节点引用（Phandle）**用来指向其他节点；`phandle-array` 表示节点引用及其说明单元，`phandles` 表示节点引用列表。

`status` 的类型为 `string`，描述节点所代表硬件或其他资源的运行状态。`okay` 表示资源可运行，例如可供驱动使用；`disabled` 表示资源不可运行，系统应将它视为不存在。合法值为 `okay`、`disabled`、`reserved`、`fail`、`fail-sss`。详见《设备树规范》（Devicetree Specification）v0.4 第 2.3.4 节。

`compatible` 的类型为 `string-array`，是**必需属性**。它用字符串列表定义节点代表的硬件或其他资源类型；设备驱动检查特定兼容字符串，以寻找应由自己管理的节点。推荐格式为 `vendor,device`，其中 `vendor` 是厂商简称，`device` 通常取自数据手册。多个值应按从最具体到最通用排列，使某一通用家族的具体设备能匹配当前可用的最具体驱动。详见规范 v0.4 第 2.3.1 节。

`reg` 的类型为 `array`，是**必需属性**，给出寻址设备所需的信息，其含义取决于设备及 `compatible`。通常是一组“地址、长度”对，每对称为**寄存器块（Register Block）**，数值惯常写成十六进制。详见规范 v0.4 第 2.3.6 节。

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

## 764.5\_地址映射与中断

`ranges` 的类型为 `compound`，定义总线子地址空间与总线节点父地址空间之间的映射或转换。它通常为空，或由“子总线地址、父总线地址、长度”三元组构成。**空属性表示两侧地址空间相同，不需要转换；总线节点没有此属性时，则认为子节点与父地址空间之间不存在映射。**详见规范 v0.4 第 2.3.8 节。

下列属性描述**中断（Interrupt）**，参见规范 v0.4 第 2.4 节“中断与中断映射”。

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `interrupts` | `array` | 设备产生的中断，编码为一个或多个中断说明符；格式由设备在中断树中的位置决定，具有相同 `interrupt-parent` 的设备使用相同格式 |
| `interrupts-extended` | `compound` | 扩展中断说明符，可替代 `interrupts` |
| `interrupt-names` | `string-array` | 设备各中断的可选名称；中断本身在 `interrupts` 或 `interrupts-extended` 中定义 |
| `interrupt-parent` | `phandle` | 若存在，引用负责处理此设备所产生中断的节点 |

## 764.6\_标签、时钟与地址单元

**时钟提供者（Clock Provider）**提供设备使用的时钟。下表同时保留标签和子节点地址编码相关属性。

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `label` | `string` | 描述设备的可读字符串；除逐案确有需要外，已不推荐使用此属性。参见规范 v0.4 第 4.1.2 节“其他属性” |
| `clocks` | `phandle-array` | **必需**。设备的时钟提供者信息，通常应遵守下述 dt-schema 时钟绑定约定 |
| `clock-names` | `string-array` | **必需**。`clocks` 中各时钟提供者的可选名称 |
| `#address-cells` | `int` | 子节点 `reg` 地址字段所用的 `<u32>` 单元数量 |
| `#size-cells` | `int` | 子节点 `reg` 大小字段所用的 `<u32>` 单元数量 |

`<u32>` 是 32 位无符号单元，两个 cells 属性见规范 v0.4 第 2.3.5 节。时钟约定见 [dt-schema 的 clock.yaml](https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml)。`status`、`compatible`、`reg`、`interrupts` 和 `label` 另见官方[重要属性（Important Properties）](https://docs.zephyrproject.org/latest/build/dts/intro-syntax-structure.html#dt-important-props)。

## 764.7\_DMA、输入输出与邮箱通道

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

## 764.8\_电源域与硬件锁

**电源域（Power Domain）**描述设备所属供电域；**硬件自旋锁（Hardware Spinlock）**为硬件提供的锁资源。属性如下：

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `power-domains` | `phandle-array` | 与设备相关的电源域说明符 |
| `power-domain-names` | `string-array` | `power-domains` 中各电源域说明符的可选名称 |
| `#power-domain-cells` | `int` | `power-domains` 属性中的单元数量 |
| `hwlocks` | `phandle-array` | 与设备相关的硬件自旋锁标识 |
| `hwlock-names` | `string-array` | `hwlocks` 中各锁说明符的可选名称 |

## 764.9\_初始化、唤醒和运行时电源管理

`zephyr,deferred-init` 为 `boolean` 属性：启动时不自动初始化设备，应使用 `device_init()` 手动初始化。

`wakeup-source` 为 `boolean` 属性，标识设备可以作为**唤醒源（Wakeup Source）**。提供它后，设备会设置一个专门标志，告知系统该设备具备唤醒系统的能力。这类设备的唤醒功能默认禁用，即其中断不会唤醒系统，必要时可在运行期间启用。

`zephyr,pm-device-runtime-auto` 为 `boolean` 属性，在初始化函数执行后自动为设备配置**运行时电源管理（Runtime Power Management）**。

`zephyr,disabling-power-states` 的类型为 `phandles`，列出会关闭此设备电源的电源状态。

---

[上一章：AtmelSAM0数模转换器绑定](P763_AtmelSAM0数模转换器绑定.md) · [下一章：NXPDAC12数模转换器绑定](P765_NXPDAC12数模转换器绑定.md) · [返回大纲](大纲.md)
