---
id: learning.zephyr-docs.hardware.adcra-1
title: RenesasRAADCB扫描组绑定
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/adc/renesas,ra-adc-b-scan-group.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第866章\_RenesasRAADCB扫描组绑定

<a id="dtbinding-renesas-ra-adc-b-scan-group"></a>

原文：[renesas,ra-adc-b-scan-group](https://docs.zephyrproject.org/latest/build/dts/api/bindings/adc/renesas,ra-adc-b-scan-group.html)。读取日期：2026-10-13，`latest`。

`renesas,ra-adc-b-scan-group` 是Renesas Electronics Corporation模数转换器（Analog-to-Digital Converter，ADC）的设备树绑定（Devicetree Binding）。此节点配置Renesas RA ADC_B扫描组（Scan Group）。扫描组是触发和完成的硬件单元：每组有自己的扫描结束中断（Scan-End Interrupt），并且恰好由一个转换器（ADC0或ADC1）执行，通过 `renesas,converter-unit-id` 选择。

**本节点只携带配置，不绑定驱动。**位于 `adc-unit` 下的通道子节点通过 `renesas,scan-group` 节点引用（Phandle）加入扫描组。转换器及通道配置见[实例绑定](P867_RenesasRAADCB实例绑定.md)。

使用此兼容字符串的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=renesas,ra-adc-b-scan-group)。

以下严格区分各层节点，必需性、固定值及合法取值仅适用于所在层。`int` 为整数，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`string` 为字符串，`string-array` 为字符串数组，`boolean` 为布尔属性，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用及说明单元数组。Kconfig是Zephyr的配置系统。

基础属性可用于多种节点，不保证全部适用于当前硬件。电源域（Power Domain）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox）及处理器间消息（Inter-Processor Messaging，IPM）的通用属性也按原页保留。

原始设备树源码（Devicetree Source，DTS）示例：

```dts
  scan_group0: scan-group@0 {
      compatible = "renesas,ra-adc-b-scan-group";
      reg = <0>;
      interrupts = <60 12>;
      interrupt-names = "scanend";
      renesas,converter-unit-id = <0>;
  };
```

## 866.1\_扫描组节点属性

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `renesas,converter-unit-id` | `int` | **必需**。选择执行本扫描组的转换器：0为ADC0，1为ADC1。必须匹配引用此扫描组的通道所属 `adc-unit` 的 `unit-id`，驱动通过构建期断言（Build-Time Assertion） `BUILD_ASSERT` 强制检查。此处使用整数而非节点引用（Phandle），因为后者会形成 `adc-unit -> channel -> scan-group -> adc-unit` 的设备树循环依赖（Devicetree Cycle）；合法值：`0, 1` |
| `reg` | `array` | **必需**。硬件扫描组标识（Hardware Scan-Group ID），范围0至7；参见[重要属性](https://docs.zephyrproject.org/latest/build/dts/intro-syntax-structure.html#dt-important-props) |
| `interrupts` | `array` | 此扫描组的扫描结束中断（Scan-End Interrupt）；参见[重要属性](https://docs.zephyrproject.org/latest/build/dts/intro-syntax-structure.html#dt-important-props) |
| `interrupt-names` | `string-array` | **提供 `interrupts` 时，必须包含名称 `scanend`** |
| `status` | `string` | 节点代表的硬件或其他资源的运行状态（Operational Status）。`okay` 表示资源可运行，例如可供驱动使用；`disabled` 表示资源不可运行，系统应将其视为不存在。参见《设备树规范》（Devicetree Specification）v0.4第2.3.4节；合法值：`okay, disabled, reserved, fail, fail-sss` |
| `compatible` | `string-array` | **必需**。字符串列表定义节点代表的硬件或其他资源类型。设备驱动通过特定兼容字符串（Compatible String）寻找应由自身管理的设备。推荐格式为 `vendor,device`：前者是厂商简称，后者通常来自数据手册。多个值从最具体到最通用排列，让具体设备匹配当前可用的最具体驱动。参见规范v0.4第2.3.1节 |
| `reg-names` | `string-array` | 为 `reg` 中每个寄存器块提供可选名称；原始例子及逐项说明见本层表后 |
| `ranges` | `compound` | 定义总线子地址空间与总线节点父地址空间之间的映射或转换。通常为空，或由子总线地址、父总线地址、长度三元组组成。**空属性表示两侧地址空间相同、不需要转换；总线节点没有此属性则认为子、父地址空间之间不存在映射**。参见规范v0.4第2.3.8节 |
| `interrupts-extended` | `compound` | 扩展中断说明符，可替代 `interrupts`；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
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

本层 `reg-names` 的原始示例如下。设备树源码（Devicetree Source，DTS）中的 `uart` 是通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）节点名称，仅用于说明寄存器命名。

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

其中 `uart@1000` 有两个寄存器块：名称 `foo` 的基址为 `0x1000`、大小为 `0x2000`；名称 `bar` 的基址为 `0x3000`、大小为 `0x4000`。

本页没有已弃用的顶层专用属性。

---

[上一章：RenesasRAADCB控制器绑定](P865_RenesasRAADCB控制器绑定.md) · [下一章：RenesasRAADCB实例绑定](P867_RenesasRAADCB实例绑定.md) · [返回大纲](大纲.md)
