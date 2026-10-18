---
id: learning.zephyr-docs.i3c-smbus-binding-reference.page-5
title: microchip_xec-i3c
kind: reference
status: maintained
domains: [zephyr, devicetree, i3c, smbus]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/i3c/microchip,xec-i3c.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第5章\_microchip_xec-i3c

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/i3c/microchip,xec-i3c.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="microchip-xec-i3c"></a>
<a id="dtbinding-microchip-xec-i3c"></a>
<a id="std-dtcompatible-microchip-xec-i3c"></a>

兼容字符串（Compatible String）：`microchip,xec-i3c`。厂商：[ Microchip ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-microchip)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=microchip,xec-i3c)。

驱动源码（Driver Source）：[drivers/i3c/i3c_dw.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/i3c_dw.c)。

<a id="description"></a>

Microchip XEC I3C控制器。

MEC SoC通过XEC专用包装模块（Wrapper）集成Synopsys DesignWare `DWC_mipi_i3c` IP，所以本绑定与`snps,designware-i3c`共用`i3c_dw.c`驱动。包装模块增加了`HOST_CFG`端口选择寄存器，并经XEC中断汇聚器（EC Interrupt Aggregator，ECIA）路由中断。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 5.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `port-sel` | `int` | 写入`HOST_CFG[2:0]`的I3C端口选择值，选择控制器驱动的SoC焊盘组；必须与`pinctrl-0`引脚组一致。；默认值：`0` |
| `i3c-scl-hz` | `int` | I3C传输使用的SCL频率；未定义时使用控制器默认值或I3C规范规定的值。 |
| `i2c-scl-hz` | `int` | I²C传输使用的SCL频率。未定义且总线上连接了I²C设备时，读取所有已连接I²C设备的传统虚拟寄存器（Legacy Virtual Register，LVR），确定允许的最高频率。 |
| `primary-controller-da` | `int` | I3C控制器自行分配的动态地址（Dynamic Address），用于次控制器交接后与本控制器通信；仅当本控制器为主控制器（Primary Controller）时使用。 |
| `od-thigh-min-ns` | `int` | 纯I3C总线在开漏模式下的最小时钟高脉宽，单位为纳秒。默认值来自I3C Basic规范v1.2（2024-12-16）第4.3.11.2节及表49。；默认值：`24` |
| `od-tlow-min-ns` | `int` | 开漏模式下的最小时钟低脉宽，单位为纳秒。默认值来自I3C Basic规范v1.2（2024-12-16）第4.3.11.2节及表49。；默认值：`200` |
| `pp-thigh-min-ns` | `int` | 推挽模式（Push-pull Mode）下的最小时钟高脉宽，单位为纳秒。部分限速目标设备通过`GETMXDS`公共命令码（Common Command Code，CCC）声明需要高于总线最小值的脉宽。默认值来自I3C Basic规范v1.2（2024-12-16）第4.3.11.2节及表50。；默认值：`32` |
| `disable-bus-init` | `boolean` | 为真时，驱动初始化期间不执行I3C总线初始化函数`i3c_bus_init`，由应用稍后初始化总线。 |
| `disable-hj-at-init` | `boolean` | 为真时，总线初始化结束后不启用热加入应答（Hot-Join ACK）；应用显式启用之前，热加入事件均返回否定应答（NACK）。 |
| `pinctrl-0` | `phandles` | 第一个状态（State）的引脚配置（Pin Configuration），具体内容取决于所选引脚控制器驱动（Pin Controller Driver）的实现 |
| `pinctrl-1` | `phandles` | 第二个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-2` | `phandles` | 第三个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-3` | `phandles` | 第四个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-4` | `phandles` | 第五个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-names` | `string-array` | 所提供状态的名称，名称数量必须与状态数量一致 |
| `girqs` | `array` | **必需**。许多DEC／MEC外设中断支持直接路由（Direct Mode），信号接到GIRQ中的相应位。原文称每个GIRQ含5个32位寄存器，列出状态`status`（锁存或写1清除）、置位使能`set-enable`、清除使能`clr-enable`和只读结果`result`；原文数量与列举项数的差异在此保留。`result`各位为状态与使能按位与。直接模式把各结果位单独路由到NVIC输入；若在EC子系统中断控制寄存器将直接模式位置0，则对结果位求或，再按GIRQ编号接到NVIC输入。<br>驱动启用中断必须同时知道：`interrupts`中的NVIC输入号及优先级；`girqs`中的GIRQ编号与位位置。一个设备树节点内两项属性的条目数应相同。 |

本页没有已弃用的节点专用属性。

## 5.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `array` | **必需**。给出寻址设备所需的信息，具体含义随设备及 `compatible` 而变化。通常是一组地址与长度对，每对称为寄存器块（Register Block），数值通常写为十六进制。参见规范v0.4第2.3.6节及[重要属性](../devicetree/P003_语法与结构.md#dt-important-props) |
| `interrupts` | `array` | **必需**。设备产生的中断，编码为一个或多个中断说明符；格式由设备在中断树中的位置决定，具有相同 `interrupt-parent` 的设备使用相同格式；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `clocks` | `phandle-array` | **必需**。PCR时钟说明符：`<&pcr regidx bitpos MCHP_XEC_PCR_CLK_I3C>`。`regidx`及`bitpos`确定本控制器在PCR睡眠使能／时钟请求／复位使能寄存器中的位位置。时钟ID选择XEC时钟控制驱动报告的192 MHz I3C时钟域，要求SoC选择`HAS_MCHP_MEC_I3C`。 |
| `#address-cells` | `int` | **必需**。子节点 `reg` 地址字段所用的 `<u32>` 单元数量；`<u32>` 为32位无符号单元，参见《设备树规范》v0.4第2.3.5节；固定值：`3` |
| `#size-cells` | `int` | **必需**。子节点 `reg` 大小字段所用的 `<u32>` 单元数量；`<u32>` 为32位无符号单元，参见《设备树规范》v0.4第2.3.5节；固定值：`0` |
| `status` | `string` | 节点代表的硬件或其他资源的运行状态（Operational Status）。`okay` 表示资源可运行，例如可供驱动使用；`disabled` 表示资源不可运行，系统应将其视为不存在。参见《设备树规范》（Devicetree Specification）v0.4第2.3.4节；合法值：`okay, disabled, reserved, fail, fail-sss` |
| `compatible` | `string-array` | **必需**。字符串列表定义节点代表的硬件或其他资源类型。设备驱动通过特定兼容字符串（Compatible String）寻找应由自身管理的设备。推荐格式为 `vendor,device`：前者是厂商简称，后者通常来自数据手册。多个值从最具体到最通用排列，让具体设备匹配当前可用的最具体驱动。参见规范v0.4第2.3.1节 |
| `reg-names` | `string-array` | 为 `reg` 中每个寄存器块提供可选名称；原始例子及逐项说明见本层表后 |
| `ranges` | `compound` | 定义总线子地址空间与总线节点父地址空间之间的映射或转换。通常为空，或由子总线地址、父总线地址、长度三元组组成。**空属性表示两侧地址空间相同、不需要转换；总线节点没有此属性则认为子、父地址空间之间不存在映射**。参见规范v0.4第2.3.8节 |
| `interrupts-extended` | `compound` | 扩展中断说明符，可替代 `interrupts`；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `interrupt-names` | `string-array` | 设备各中断的可选名称；中断本身在 `interrupts` 或 `interrupts-extended` 中定义；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `interrupt-parent` | `phandle` | 若存在，引用负责处理此设备所产生中断的节点；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `label` | `string` | 描述设备的可读字符串；除逐案确有需要外，已不推荐使用此属性。参见规范 v0.4 第 4.1.2 节“其他属性” |
| `clock-names` | `string-array` | `clocks` 中各时钟提供者的名称；通用说明称其为可选名称，是否必须填写以本层的必需标记为准 |
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

## 5.3\_寄存器块命名原例

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

[上一章](P004_ite_it51xxx-i3cs.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P006_nuvoton_npcx-i3c.md)
