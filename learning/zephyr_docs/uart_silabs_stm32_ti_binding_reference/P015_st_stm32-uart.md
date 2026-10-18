---
id: learning.zephyr-docs.uart-silabs-stm32-ti-binding-reference.page-15
title: st_stm32-uart
kind: reference
status: maintained
domains: [zephyr, devicetree, uart]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/serial/st,stm32-uart.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第15章\_st_stm32-uart

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/serial/st,stm32-uart.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="st-stm32-uart"></a>
<a id="dtbinding-st-stm32-uart"></a>
<a id="std-dtcompatible-st-stm32-uart"></a>

兼容字符串（Compatible String）：`st,stm32-uart`。厂商：[ STMicroelectronics ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-st)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=st,stm32-uart)。

驱动源码（Driver Source）：[drivers/serial/uart_stm32.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/uart_stm32.c)。

<a id="description"></a>

STM32 UART。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 15.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `resets` | `phandle-array` | **必需**。复位信息（Reset Information） |
| `current-speed` | `int` | UART初始波特率（Baud Rate）；未指定时采用标准波特率115200。；默认值：`115200` |
| `stop-bits` | `string` | 停止位（Stop Bits）数量；未指定时默认为1。；默认值：`1`；合法值：`0_5, 1, 1_5, 2` |
| `data-bits` | `int` | 数据位（Data Bits）数量；未指定时默认为8。；默认值：`8`；合法值：`5, 6, 7, 8, 9` |
| `single-wire` | `boolean` | 启用单线半双工通信（Single-wire Half-duplex Communication）。在此模式下，TX与RX在内部连接，之后仅使用TX引脚，也只需配置TX；用户必须自行处理收发冲突。 |
| `tx-rx-swap` | `boolean` | 交换TX和RX引脚，用于交叉接线（Cross-wired Connection）的情况。 |
| `pinctrl-0` | `phandles` | **必需**。第一个状态（State）的引脚配置（Pin Configuration），具体内容取决于所选引脚控制器驱动（Pin Controller Driver）的实现 |
| `pinctrl-names` | `string-array` | **必需**。所提供状态的名称，名称数量必须与状态数量一致 |
| `wakeup-line` | `int` | 与设备唤醒中断屏蔽寄存器对应的外部中断（External Interrupt，EXTI）线路编号。有些STM32器件的唤醒中断信号可能在启动时被配置为屏蔽，导致外设不能从停止模式（Stop Mode）唤醒处理器核，此时必须提供本属性。译注：原文举例器件拼写为`sm32wl55`，此处保留该拼写说明。；范围：`0 to 31` |
| `de-enable` | `boolean` | 通过驱动器使能（Driver Enable，DE）引脚激活外部收发器（Transceiver）；还必须使用pinctrl配置此DE引脚。 |
| `de-assert-time` | `int` | DE信号变为有效到起始位开始之间的时间，单位为一个位时间的1/16。；默认值：`0`；范围：`0 to 31` |
| `de-deassert-time` | `int` | 停止位结束到DE信号变为无效之间的时间，单位为一个位时间的1/16。；默认值：`0`；范围：`0 to 31` |
| `de-invert` | `boolean` | 反转DE引脚的二进制逻辑。启用后物理电平反相，使用1=低电平、0=高电平，取代1=高电平、0=低电平。 |
| `fifo-enable` | `boolean` | 按默认FIFO配置启用发送和接收FIFO，阈值通常为1/8。发送时，FIFO支持突发模式（Burst Mode），减轻高负载应用的调度压力，也使与帧间延迟变化敏感的UART设备通信更可靠；接收时，FIFO减少溢出（Overrun）。 |
| `st,sw-rts-gpios` | `phandle-array` | 对应硬件控制RTS引脚的GPIO，用于实现“协议违规后nRTS信号被异常拉低”（nRTS signal abnormally driven low after a protocol violation）勘误的规避方法：RTS改由软件控制，CTS仍由硬件控制。未设置`hw-flow-control`、即未启用硬件流控时，禁止提供本属性。硬件不受该勘误影响时也不得使用。 |
| `hw-flow-control` | `boolean` | 启动时启用请求发送／清除发送（Request to Send/Clear to Send，RTS/CTS）硬件流控（Hardware Flow Control）。 |
| `parity` | `string` | 适配器的奇偶校验（Parity）配置。枚举编号0为无校验（None），1为奇校验（Odd），2为偶校验（Even），3为标记校验（Mark），4为空格校验（Space）；未指定时默认无校验。；默认值：`none`；合法值：`none, odd, even, mark, space` |
| `pinctrl-1` | `phandles` | 第二个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-2` | `phandles` | 第三个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-3` | `phandles` | 第四个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-4` | `phandles` | 第五个状态的引脚配置，参见pinctrl-0 |
| `reset-names` | `string-array` | 各个复位的名称 |
| `tx-invert` | `boolean` | 反转TX引脚的二进制逻辑。启用后物理电平反相，采用1=低电平、0=高电平，取代1=高电平、0=低电平。 |
| `rx-invert` | `boolean` | 反转RX引脚的二进制逻辑。启用后物理电平反相，采用1=低电平、0=高电平，取代1=高电平、0=低电平。 |

本页没有已弃用的节点专用属性。

## 15.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `array` | **必需**。给出寻址设备所需的信息，具体含义随设备及 `compatible` 而变化。通常是一组地址与长度对，每对称为寄存器块（Register Block），数值通常写为十六进制。参见规范v0.4第2.3.6节及[重要属性](../devicetree/P003_语法与结构.md#dt-important-props) |
| `clocks` | `phandle-array` | **必需**。设备的时钟提供者（Clock Provider）信息，通常应遵守[dt-schema时钟绑定约定](https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml) |
| `interrupts` | `array` | **必需**。设备产生的中断，编码为一个或多个中断说明符；格式由设备在中断树中的位置决定，具有相同 `interrupt-parent` 的设备使用相同格式；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `status` | `string` | 节点代表的硬件或其他资源的运行状态（Operational Status）。`okay` 表示资源可运行，例如可供驱动使用；`disabled` 表示资源不可运行，系统应将其视为不存在。参见《设备树规范》（Devicetree Specification）v0.4第2.3.4节；合法值：`okay, disabled, reserved, fail, fail-sss` |
| `compatible` | `string-array` | **必需**。字符串列表定义节点代表的硬件或其他资源类型。设备驱动通过特定兼容字符串（Compatible String）寻找应由自身管理的设备。推荐格式为 `vendor,device`：前者是厂商简称，后者通常来自数据手册。多个值从最具体到最通用排列，让具体设备匹配当前可用的最具体驱动。参见规范v0.4第2.3.1节 |
| `reg-names` | `string-array` | 为 `reg` 中每个寄存器块提供可选名称；原始例子及逐项说明见本层表后 |
| `ranges` | `compound` | 定义总线子地址空间与总线节点父地址空间之间的映射或转换。通常为空，或由子总线地址、父总线地址、长度三元组组成。**空属性表示两侧地址空间相同、不需要转换；总线节点没有此属性则认为子、父地址空间之间不存在映射**。参见规范v0.4第2.3.8节 |
| `interrupts-extended` | `compound` | 扩展中断说明符，可替代 `interrupts`；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `interrupt-names` | `string-array` | 设备各中断的可选名称；中断本身在 `interrupts` 或 `interrupts-extended` 中定义；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `interrupt-parent` | `phandle` | 若存在，引用负责处理此设备所产生中断的节点；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `label` | `string` | 描述设备的可读字符串；除逐案确有需要外，已不推荐使用此属性。参见规范 v0.4 第 4.1.2 节“其他属性” |
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

## 15.3\_寄存器块命名原例

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

[上一章](P014_st_stm32-lpuart.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P016_st_stm32-usart.md)
