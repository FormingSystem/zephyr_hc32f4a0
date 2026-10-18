---
id: learning.zephyr-docs.uart-espressif-infineon-microchip-binding-reference.page-9
title: infineon_xmc4xxx-uart
kind: reference
status: maintained
domains: [zephyr, devicetree, uart]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/serial/infineon,xmc4xxx-uart.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第9章\_infineon_xmc4xxx-uart

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/serial/infineon,xmc4xxx-uart.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="infineon-xmc4xxx-uart"></a>
<a id="dtbinding-infineon-xmc4xxx-uart"></a>
<a id="std-dtcompatible-infineon-xmc4xxx-uart"></a>

兼容字符串（Compatible String）：`infineon,xmc4xxx-uart`。厂商：[ Infineon Technologies ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-infineon)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=infineon,xmc4xxx-uart)。

驱动源码（Driver Source）：[drivers/serial/uart_xmc4xxx.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/uart_xmc4xxx.c)。

<a id="description"></a>

Infineon XMC4XXX UART。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 9.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `input-src` | `string` | **必需**。将UART接收线，即通用串行接口通道（Universal Serial Interface Channel，USIC）的DX0输入，连接到指定GPIO。DX0是可接不同GPIO的多路复用器；引脚与复用映射须查XMC4XXX参考手册。DX0G为回环输入线。；合法值：`DX0A, DX0B, DX0C, DX0D, DX0E, DX0F, DX0G` |
| `pinctrl-0` | `phandles` | **必需**。第一个状态（State）的引脚配置（Pin Configuration），具体内容取决于所选引脚控制器驱动（Pin Controller Driver）的实现 |
| `pinctrl-names` | `string-array` | **必需**。所提供状态的名称，名称数量必须与状态数量一致 |
| `fifo-start-offset` | `int` | **必需**。USIC0至USIC2各有一个由两个通道共享的FIFO，例如`usic0ch0`和`usic0ch1`共用同一FIFO。本参数规定TX及RX FIFO起始偏移；共享时必须根据另一通道配置正确设置偏移。总容量64个条目，TX/RX FIFO需按对应`fifo-xx-size`大小对齐。 |
| `fifo-tx-size` | `int` | **必需**。发送字节缓冲FIFO的大小；0表示发送时不使用FIFO。UART采用异步模式（Asynchronous Mode）时，`fifo-tx-size`应设为0。；合法值：`0, 2, 4, 8, 16, 32, 64` |
| `fifo-rx-size` | `int` | **必需**。接收字节缓冲FIFO的大小；0表示接收时不使用FIFO。UART采用异步模式时，`fifo-rx-size`应设为0。；合法值：`0, 2, 4, 8, 16, 32, 64` |
| `clock-frequency` | `int` | UART工作所需的时钟频率信息。 |
| `current-speed` | `int` | UART初始波特率设置。 |
| `hw-flow-control` | `boolean` | 启动时启用请求发送／清除发送（Request to Send/Clear to Send，RTS/CTS）硬件流控（Hardware Flow Control）。 |
| `parity` | `string` | 适配器的奇偶校验（Parity）配置。枚举编号0为无校验（None），1为奇校验（Odd），2为偶校验（Even），3为标记校验（Mark），4为空格校验（Space）；未指定时默认无校验。；默认值：`none`；合法值：`none, odd, even, mark, space` |
| `stop-bits` | `string` | 停止位数量。；合法值：`0_5, 1, 1_5, 2` |
| `data-bits` | `int` | 数据位数量。；合法值：`5, 6, 7, 8, 9` |
| `pinctrl-1` | `phandles` | 第二个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-2` | `phandles` | 第三个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-3` | `phandles` | 第四个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-4` | `phandles` | 第五个状态的引脚配置，参见pinctrl-0 |

本页没有已弃用的节点专用属性。

## 9.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `array` | **必需**。给出寻址设备所需的信息，具体含义随设备及 `compatible` 而变化。通常是一组地址与长度对，每对称为寄存器块（Register Block），数值通常写为十六进制。参见规范v0.4第2.3.6节及[重要属性](../devicetree/P003_语法与结构.md#dt-important-props) |
| `interrupts` | `array` | 中断驱动UART使用的中断请求（Interrupt Request，IRQ）编号与优先级。USIC0、USIC1、USIC2的中断编号范围分别为[84, 89]、[90, 95]、[96, 101]。 |
| `dmas` | `phandle-array` | 异步UART可选的TX/RX DMA说明符（DMA Specifier），原例第一项为TX，第二项为RX。每项包含DMA设备节点引用、通道、优先级（0最低、7最高），以及由`XMC4XXX_SET_CONFIG(line, request_source)`编码的线路路由参数。<br>选择步骤：先选DMA设备及空闲通道；再选空闲线路，dma0仅能接线路[0, 7]，dma1可接[8, 11]；由中断求服务请求（Service Request，SR）编号，例如USIC0中84→SR0、85→SR1，USIC1中90→SR0、91→SR1，依次类推；最后按XMC4XXX参考手册的DMA Request Source Selection表选择`request_source`。<br>例如USIC0中断85、dma0通道3、优先级4、线路7，对应SR1，表中要求`request_source=10`。下方保留两段原例。译注：第二段原文使用单数`dma`并包含省略号，属于示意片段；正式属性为`dmas`。 |
| `dma-names` | `string-array` | 存在`dmas`属性时必需；应设为`"tx"`及`"rx"`并与`dmas`匹配。下方保留名称原例。 |
| `status` | `string` | 节点代表的硬件或其他资源的运行状态（Operational Status）。`okay` 表示资源可运行，例如可供驱动使用；`disabled` 表示资源不可运行，系统应将其视为不存在。参见《设备树规范》（Devicetree Specification）v0.4第2.3.4节；合法值：`okay, disabled, reserved, fail, fail-sss` |
| `compatible` | `string-array` | **必需**。字符串列表定义节点代表的硬件或其他资源类型。设备驱动通过特定兼容字符串（Compatible String）寻找应由自身管理的设备。推荐格式为 `vendor,device`：前者是厂商简称，后者通常来自数据手册。多个值从最具体到最通用排列，让具体设备匹配当前可用的最具体驱动。参见规范v0.4第2.3.1节 |
| `reg-names` | `string-array` | 为 `reg` 中每个寄存器块提供可选名称；原始例子及逐项说明见本层表后 |
| `ranges` | `compound` | 定义总线子地址空间与总线节点父地址空间之间的映射或转换。通常为空，或由子总线地址、父总线地址、长度三元组组成。**空属性表示两侧地址空间相同、不需要转换；总线节点没有此属性则认为子、父地址空间之间不存在映射**。参见规范v0.4第2.3.8节 |
| `interrupts-extended` | `compound` | 扩展中断说明符，可替代 `interrupts`；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `interrupt-names` | `string-array` | 设备各中断的可选名称；中断本身在 `interrupts` 或 `interrupts-extended` 中定义；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `interrupt-parent` | `phandle` | 若存在，引用负责处理此设备所产生中断的节点；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `label` | `string` | 描述设备的可读字符串；除逐案确有需要外，已不推荐使用此属性。参见规范 v0.4 第 4.1.2 节“其他属性” |
| `clocks` | `phandle-array` | 设备的时钟提供者（Clock Provider）信息，通常应遵守[dt-schema时钟绑定约定](https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml) |
| `clock-names` | `string-array` | `clocks` 中各时钟提供者的名称；通用说明称其为可选名称，是否必须填写以本层的必需标记为准 |
| `#address-cells` | `int` | 子节点 `reg` 地址字段所用的 `<u32>` 单元数量；`<u32>` 为32位无符号单元，参见《设备树规范》v0.4第2.3.5节 |
| `#size-cells` | `int` | 子节点 `reg` 大小字段所用的 `<u32>` 单元数量；`<u32>` 为32位无符号单元，参见《设备树规范》v0.4第2.3.5节 |
| `dma-coherent` | `boolean` | 表示设备支持一致性 DMA 操作，见规范 v0.4 第 2.3.10 节 |
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

## USIC服务请求路由原例

```dts
dma = <&dma0 3 4 XMC4XXX_SET_CONFIG(7,10) ...>;
```

## DMA配置原例 19

```dts
dmas = <&dma1 1 0 XMC4XXX_SET_CONFIG(10,6)>, <&dma1 2 0 XMC4XXX_SET_CONFIG(11,6)>;
```

## DMA配置原例 20

```dts
   dma-names = "tx", "rx";
```

## 9.3\_寄存器块命名原例

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

[上一章](P008_infineon_uart.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P010_intel_lw-uart.md)
