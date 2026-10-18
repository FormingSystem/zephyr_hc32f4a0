---
id: learning.zephyr-docs.lora-ieee802154-binding-reference.page-1
title: atmel_rf2xx
kind: reference
status: maintained
domains: [zephyr, devicetree, lora, ieee802154]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/ieee802154/atmel,rf2xx.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第1章\_atmel_rf2xx

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/ieee802154/atmel,rf2xx.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="atmel-rf2xx-on-spi-bus"></a>
<a id="dtbinding-atmel-rf2xx"></a>
<a id="std-dtcompatible-atmel-rf2xx"></a>

兼容字符串（Compatible String）：`atmel,rf2xx`。厂商：[ Atmel Corporation ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-atmel)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=atmel,rf2xx)。

驱动源码（Driver Source）：[drivers/ieee802154/ieee802154_rf2xx.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/ieee802154_rf2xx.c)。

<a id="description"></a>

ATMEL AT86RF2xx IEEE 802.15.4无线收发器（Wireless Transceiver）。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 1.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `irq-gpios` | `phandle-array` | **必需**。原文没有提供文字说明 |
| `reset-gpios` | `phandle-array` | **必需**。原文没有提供文字说明 |
| `slptr-gpios` | `phandle-array` | **必需**。多功能引脚（Multi-Functional Pin），控制睡眠、深度睡眠、发送启动和接收状态。 |
| `dig2-gpios` | `phandle-array` | 接收与发送帧时间戳（RX and TX Frame Time Stamping），对应TX_ARET。 |
| `clkm-gpios` | `phandle-array` | 主时钟信号输出（Master Clock Output）。 |
| `local-mac-address` | `uint8-array` | 分配给该网络设备的介质访问控制地址（Media Access Control Address，MAC Address）。 |
| `channel-page` | `int` | 按IEEE 802.15.4选择信道页（Channel Page）。页0同时用于Sub-GHz和2.4 GHz：Sub-GHz的信道0为BPSK-20、1～10为BPSK-40，2.4 GHz的11～26为O-QPSK-250。页2用于Sub-GHz：信道0为OQPSK-SIN-RC-100，1～10为OQPSK-SIN-250。页5用于日本Sub-GHz频段，信道0～3为OQPSK-RC-250。原始页号／模式对照表见后文；原文叙述中的“Channel 2／5”在对照表中标为Page 2／5。；合法值：`0, 2, 5` |
| `tx-pwr-table` | `uint8-array` | 发射功率映射表（Transmission Power Mapping Table）数组，用于满足当地规定。原文说明默认值使所有收发器输出高于0 dBm；正常使用时必须同时设置 `tx-pwr-min` 和 `tx-pwr-max`。条目数由数组长度决定，2.4 GHz的条目最大值为 `0x0f`，Sub-GHz为 `0xff`，详见器件数据手册的PHY_TX_PWR。<br><br>功率按后文原式计算：线性步长为最大与最小功率之差除以“表长减1”，表索引取“目标功率与最大功率之差除以步长”的绝对值，再从表中读取输出功率编码。<br><br>以不带外部功率放大器（Power Amplifier，PA）的AT86RF233为例，最小功率−17 dBm、最大功率+4 dBm，表有48项，按功率从高到低排列，完整数组见后文。表值依据数据手册表9-9的TX Output Power填写；线性步长约为 `(4 - (-17)) / (48 - 1) = 0.45 dBm`。目标为0 dBm时，索引为 `abs((0 - 4) / 0.45) = 8.95`，四舍五入为9，表值为 `0x07`，对应表9-9中的0 dBm。<br><br>原文特别说明：最小与最大功率均为 `[0x00, 0x00]` 时，步长为0，表索引固定使用首项；默认首项为 `0x00`。这是未配置任何 `tx-pwr-*` 时的一般情况，收发器始终使用高于0 dBm的输出功率。；默认值：`[0x0]` |
| `tx-pwr-min` | `uint8-array` | 收发器输出功率的最小归一化值（Minimum Normalized Power），单位dBm；定义 `tx-pwr-table` 时必须使用。采用两个元素表示：第一个表示符号，`0x00` 为正、`0x01` 为负；第二个表示最小功率数值。默认情况下，`tx-pwr-min` 与 `tx-pwr-max` 均为 `[0x00, 0x00]`，形成固定发射功率。；默认值：`[0x0, 0x0]` |
| `tx-pwr-max` | `uint8-array` | 收发器输出功率的最大归一化值（Maximum Normalized Power），单位dBm；定义 `tx-pwr-table` 时必须使用。采用两个元素表示：第一个表示符号，原文列出 `0x00` 为正；第二个表示最大功率数值。默认情况下，`tx-pwr-max` 与 `tx-pwr-min` 均为 `[0x00, 0x00]`，形成固定发射功率。；默认值：`[0x0, 0x0]` |
| `spi-max-frequency` | `int` | **必需**。设备SPI接口的最大时钟频率，单位Hz |
| `duplex` | `int` | 双工模式（Duplex Mode），可为全双工或半双工。默认全双工，对应0，这是最常见模式。应使用宏而非原始枚举值，`dt-bindings/spi/spi.h` 定义的对应关系为0对应SPI_FULL_DUPLEX，2048对应SPI_HALF_DUPLEX；原始对照表见下文；默认值：`0`；合法值：`0, 2048` |
| `frame-format` | `int` | Motorola或TI帧格式（Frame Format）。默认Motorola，对应0，这是最常见格式。应使用宏而非原始枚举值，`dt-bindings/spi/spi.h` 对应关系为0对应SPI_FRAME_FORMAT_MOTOROLA，32768对应SPI_FRAME_FORMAT_TI；原始对照表见下文；默认值：`0`；合法值：`0, 32768` |
| `spi-cpol` | `boolean` | SPI时钟极性（Clock Polarity），指示时钟空闲状态；设置时空闲为逻辑高电平，否则为低电平 |
| `spi-cpha` | `boolean` | SPI时钟相位（Clock Phase），决定采样边沿；设置时在第二个边沿采样，否则在第一个边沿采样 |
| `spi-lsb-first` | `boolean` | 设备要求最低有效位优先（Least Significant Bit First，LSB-first）的数据模式 |
| `spi-hold-cs` | `boolean` | 某些场景需由控制器通过软件管理SPI片选（Chip Select，CS），以连续执行多次SPI事务而不释放片选。典型情况为变长数据包：第一笔事务读取长度，第二笔读取该长度的字节数据 |
| `spi-cs-high` | `boolean` | 设备要求片选高电平有效（Active High） |
| `spi-interframe-delay-ns` | `int` | SPI字（Word）之间的延迟，单位纳秒。默认0是特殊值，表示SCK周期的一半；默认值：`0` |
| `spi-cs-setup-delay-ns` | `int` | 片选置有效之后，由控制器引入的延迟，单位纳秒，也称使能前置时间（Enable Lead Time） |
| `spi-cs-hold-delay-ns` | `int` | 片选释放之前，由控制器引入的延迟，单位纳秒，也称使能后置时间（Enable Lag Time） |
| `supply-gpios` | `phandle-array` | 控制设备供电的GPIO说明符（Specifier）。设备有专用供电开关时提供此属性，供电状态完全由设备驱动负责；与vin-supply的共享稳压器方式相区别 |
| `vin-supply` | `phandle` | 控制设备供电的稳压器引用，目标设备树节点必须使用稳压器兼容字符串。通过共享稳压器供电时应提供此属性，其供电状态取决于所有受电设备的请求状态。若同时提供supply-gpios，则必须先请求稳压器再将GPIO置为有效；释放稳压器前，必须先将GPIO置为无效 |

本页没有已弃用的节点专用属性。

## 1.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `array` | **必需**。给出寻址设备所需的信息，具体含义随设备及 `compatible` 而变化。通常是一组地址与长度对，每对称为寄存器块（Register Block），数值通常写为十六进制。参见规范v0.4第2.3.6节及[重要属性](../devicetree/P003_语法与结构.md#dt-important-props) |
| `status` | `string` | 节点代表的硬件或其他资源的运行状态（Operational Status）。`okay` 表示资源可运行，例如可供驱动使用；`disabled` 表示资源不可运行，系统应将其视为不存在。参见《设备树规范》（Devicetree Specification）v0.4第2.3.4节；合法值：`okay, disabled, reserved, fail, fail-sss` |
| `compatible` | `string-array` | **必需**。字符串列表定义节点代表的硬件或其他资源类型。设备驱动通过特定兼容字符串（Compatible String）寻找应由自身管理的设备。推荐格式为 `vendor,device`：前者是厂商简称，后者通常来自数据手册。多个值从最具体到最通用排列，让具体设备匹配当前可用的最具体驱动。参见规范v0.4第2.3.1节 |
| `reg-names` | `string-array` | 为 `reg` 中每个寄存器块提供可选名称；原始例子及逐项说明见本层表后 |
| `ranges` | `compound` | 定义总线子地址空间与总线节点父地址空间之间的映射或转换。通常为空，或由子总线地址、父总线地址、长度三元组组成。**空属性表示两侧地址空间相同、不需要转换；总线节点没有此属性则认为子、父地址空间之间不存在映射**。参见规范v0.4第2.3.8节 |
| `interrupts` | `array` | 设备产生的中断，编码为一个或多个中断说明符；格式由设备在中断树中的位置决定，具有相同 `interrupt-parent` 的设备使用相同格式；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `interrupts-extended` | `compound` | 扩展中断说明符，可替代 `interrupts`；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `interrupt-names` | `string-array` | 设备各中断的可选名称；中断本身在 `interrupts` 或 `interrupts-extended` 中定义；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `interrupt-parent` | `phandle` | 若存在，引用负责处理此设备所产生中断的节点；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `label` | `string` | 描述设备的可读字符串；除逐案确有需要外，已不推荐使用此属性。参见规范 v0.4 第 4.1.2 节“其他属性” |
| `clocks` | `phandle-array` | 设备的时钟提供者（Clock Provider）信息，通常应遵守[dt-schema时钟绑定约定](https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml) |
| `clock-names` | `string-array` | `clocks` 中各时钟提供者的名称；通用说明称其为可选名称，是否必须填写以本层的必需标记为准 |
| `#address-cells` | `int` | 子节点 `reg` 地址字段所用的 `<u32>` 单元数量；`<u32>` 为32位无符号单元，参见《设备树规范》v0.4第2.3.5节 |
| `#size-cells` | `int` | 子节点 `reg` 大小字段所用的 `<u32>` 单元数量；`<u32>` 为32位无符号单元，参见《设备树规范》v0.4第2.3.5节 |
| `dma-coherent` | `boolean` | 表示设备支持一致性 DMA 操作，见规范 v0.4 第 2.3.10 节 |
| `dmas` | `phandle-array` | 与设备相关的 DMA 通道说明符 |
| `dma-names` | `string-array` | `dmas` 中各 DMA 通道说明符的可选名称 |
| `dma-ranges` | `compound` | 定义总线物理地址空间与其父总线物理地址空间之间的映射或转换，见规范 v0.4 第 2.3.9 节 |
| `io-channels` | `phandle-array` | 与设备相关的 I/O 通道说明符 |
| `io-channel-names` | `string-array` | `io-channels` 中各通道说明符的可选名称 |
| `mboxes` | `phandle-array` | 与设备相关的邮箱/IPM 通道说明符 |
| `mbox-names` | `string-array` | `mboxes` 中各邮箱说明符的可选名称 |
| `power-domains` | `phandle-array` | 与设备相关的电源域说明符 |
| `power-domain-names` | `string-array` | `power-domains` 中各电源域说明符的可选名称 |
| `#power-domain-cells` | `int` | `power-domains` 属性中的单元数量 |
| `hwlocks` | `phandle-array` | 与设备相关的硬件自旋锁（Hardware Spinlock）标识 |
| `hwlock-names` | `string-array` | `hwlocks` 中各锁说明符的可选名称 |
| `zephyr,deferred-init` | `boolean` | 延迟初始化（Deferred Initialization）：启动时不自动初始化设备，应由应用使用 `device_init()` 手动初始化 |
| `wakeup-source` | `boolean` | 标记设备可用作唤醒源（Wakeup Source）。设置该属性后，设备中会设置专门标志，通知系统此设备有唤醒能力。唤醒功能默认禁用，即中断不会唤醒系统；必要时可在运行期间启用 |
| `zephyr,pm-device-runtime-auto` | `boolean` | 初始化函数执行后，自动为设备配置运行时电源管理（Runtime Power Management） |
| `zephyr,disabling-power-states` | `phandles` | 会关闭该设备电源的电源状态（Power State）列表 |

属性说明中的“重要属性”参见[设备树语法与结构](../devicetree/P003_语法与结构.md#dt-important-props)。

## 信道页原始模式表

```text
  0: Page 0 - BPSK-20 [0], BPSK-40 [1-10], O-QPSK-250 [11-26].
  2: Page 2 - OQPSK-SIN-RC-100 [0], OQPSK-SIN-250 [1-10].
  5: Page 5 - OQPSK-RC-250 [0-3].
```

## 发射功率原始公式与映射数组

```text
  linear_step = (tx-pwr-max - tx-pwr-min)
              / (sizeof(tx-pwr-table) - 1.0);
  table_index = abs((value_in_dbm - tx-pwr-max) / linear_step);
  output_power = tx-pwr-table[table_index];
```

```text
  tx-pwr-min = [01 11]; /* -17.0 dBm */
  tx-pwr-max = [00 04]; /*   4.0 dBm */
  tx-pwr-table = [00 01 03 04 05 05 06 06
                  07 07 07 08 08 09 09 0a
                  0a 0a 0b 0b 0b 0b 0c 0c
                  0c 0c 0d 0d 0d 0d 0d 0d
                  0d 0d 0e 0e 0e 0e 0e 0e
                  0e 0e 0e 0e 0e 0e 0f 0f];
```

```text
  linear_step = (4 - (-17)) / (48 - 1) => ~0.45 dBm
```

```text
  table_index = abs((0 - 4) / 0.45) => 8.95 ( round to 9 )
  output_power = tx-pwr-table[9] => 0x07 ( 0 dBm as table 9-9 )
```

## SPI枚举原始对照 10

```text
  0    SPI_FULL_DUPLEX
  2048 SPI_HALF_DUPLEX
```

## SPI枚举原始对照 11

```text
  0     SPI_FRAME_FORMAT_MOTOROLA
  32768 SPI_FRAME_FORMAT_TI
```

## 1.3\_寄存器块命名原例

以下设备树源码（Devicetree Source，DTS）演示 `reg-names` 命名；`uart` 指通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）。

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

`uart@1000` 节点有两个寄存器块（Register Block）：一个基址为 `0x1000`、大小为 `0x2000`、名称为 `foo`；另一个基址为 `0x3000`、大小为 `0x4000`、名称为 `bar`。

---

[本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P002_bflb_ieee802154.md)
