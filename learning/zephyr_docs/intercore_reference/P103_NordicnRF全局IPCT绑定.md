---
id: learning.zephyr-docs.intercore_reference.ipcbind-103
title: NordicnRF全局IPCT绑定
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/ipc/nordic,nrf-ipct-global.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第103章\_NordicnRF全局IPCT绑定

<a id="dtbinding-nordic-nrf-ipct-global"></a>

原文：[nordic,nrf-ipct-global](https://docs.zephyrproject.org/latest/build/dts/api/bindings/ipc/nordic,nrf-ipct-global.html)。读取日期：2026-10-13，`latest`。

`nordic,nrf-ipct-global`是 Nordic Semiconductor 的设备树绑定（Devicetree Binding），用于处理器间通信（Inter-Processor Communication，IPC）。

此绑定描述 Nordic 全局处理器间通信收发器（Global Interprocessor Communication Transceiver，Global IPCT）。

使用此兼容字符串的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=nordic,nrf-ipct-global)。

属性类型中，`int`为整数，`array`为数值数组，`string`为字符串，`string-array`为字符串数组，`boolean`为布尔属性，`compound`为复合类型；`phandle`为节点引用（Phandle），`phandles`为节点引用列表，`phandle-array`为节点引用与说明单元数组。必需性和数值约束仅适用于所在层节点。

基础属性可用于多种节点，不保证全部适用于当前硬件。通用术语包括中断（Interrupt）、时钟（Clock）、电源域（Power Domain）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）和处理器间消息（Inter-Processor Messaging，IPM）。

## 103.1\_节点属性

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `global-domain-id` | `int` | **必需**。全局 IPCT 实例位于全局域（Global Domain）内的特定总线，例如快速总线和慢速总线。这些总线具有不同标识（ID），并且与其地址所表示的标准全局域标识不一致 |
| `channels` | `int` | **必需**。IPCT 实例实现的通道数量 |
| `source-channel-links` | `array` | 跨不同域（Domain）的两个 IPCT 实例之间的通道映射，本节点的通道作为源端（Source）。数组中每个连续的三整数单元表示一条连接，格式为`<source_channel sink_domain_id sink_channel>`，依次表示源通道、接收端域标识和接收端通道。单元在数组中依次排列。原文长度措辞的译注见表后。原例将通道2映射到无线电核心（Radio Core，标识3）的 IPCT 通道4，可写为`<2 NRF_DOMAIN_ID_RADIOCORE 4>`或`<2 3 4>` |
| `sink-channel-links` | `array` | 跨不同域（Domain）的两个 IPCT 实例之间的通道映射，本节点的通道作为接收端（Sink）。数组中每个连续的三整数单元表示一条连接，格式为`<sink_channel source_domain_id source_channel>`，依次表示接收端通道、源端域标识和源端通道。单元在数组中依次排列。原文长度措辞的译注见表后。原例把本节点通道2与无线电核心（Radio Core，标识3）的 IPCT 通道4映射，可写为`<2 NRF_DOMAIN_ID_RADIOCORE 4>`或`<2 3 4>` |
| `owned-channels` | `array` | 在所有权分割外设（Split-ownership Peripheral）中，列出应归当前编译目标中央处理器（Central Processing Unit，CPU）所有并供其使用的通道 |
| `nonsecure-channels` | `array` | 在所有权分割、安全属性也分割的外设（Split-ownership, Split-security Peripheral）中，列出配置为非安全（Nonsecure）的通道。在 TrustZone 安全隔离系统中，本属性仅针对安全外设（Secure Peripheral）进行处理，因为非安全通道已通过`owned-channels`隐式指定；在非 TrustZone 系统中忽略本属性 |
| `child-owned-channels` | `array` | 在所有权分割外设中，列出名义上归当前编译目标 CPU 所有，但计划交由它的子处理器（Child Subprocessor）使用的通道 |
| `reg` | `array` | **必需**。给出寻址设备所需的信息，具体含义随设备及 `compatible` 而变化。通常是一组地址与长度对，每对称为寄存器块（Register Block），数值通常写为十六进制。参见规范v0.4第2.3.6节及[重要属性](../devicetree/P003_语法与结构.md) |
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

译注：原文两项通道映射都写长度为`a factor of 3`，直译是“3的因数”。按同段给出的连续三整数单元格式，元素个数应能被3整除，即3的整数倍；原格式和示例数值均已保留。接收端映射表中的`<2 3 4>`依格式表示本地接收通道2、源域3、源通道4。

`reg-names`的原例说明寄存器块（Register Block）命名；`uart`为通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）节点名。

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

`uart@1000`有两个寄存器块：名称为`foo`的块基址为`0x1000`、大小为`0x2000`；名称为`bar`的块基址为`0x3000`、大小为`0x4000`。

本页没有已弃用的顶层专用属性。

服务使用方式见 [IPC 服务使用指南](P092_IPC服务使用指南.md)。

---

[上一章：NordicnRF处理器间通信绑定](P102_NordicnRF处理器间通信绑定.md) · [下一章：NordicnRF本地IPCT绑定](P104_NordicnRF本地IPCT绑定.md) · [返回大纲](大纲.md)
