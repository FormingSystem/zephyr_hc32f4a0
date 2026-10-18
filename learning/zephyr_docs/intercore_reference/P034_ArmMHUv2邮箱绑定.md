---
id: learning.zephyr-docs.intercore_reference.mboxbind-34
title: ArmMHUv2邮箱绑定
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/mbox/arm,mhuv2.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第34章\_ArmMHUv2邮箱绑定

<a id="dtbinding-arm-mhuv2"></a>

原文：[arm,mhuv2](https://docs.zephyrproject.org/latest/build/dts/api/bindings/mbox/arm,mhuv2.html)。读取日期：2026-10-13，`latest`。

`arm,mhuv2`是 ARM Ltd. 的设备树绑定（Devicetree Binding），用于邮箱（Mailbox，MBOX）。

此绑定描述 Arm 消息处理单元第2版（Message Handling Unit v2，MHUv2）邮箱控制器，为处理器间提供门铃信号通知（Doorbell Signalling）。

驱动为 [`drivers/mbox/mbox_mhuv2.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mbox/mbox_mhuv2.c)。

使用此兼容字符串的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=arm,mhuv2)。

## 34.1\_原始设备树示例

```dts
mhu0: mbox@10000000 {
    compatible = "arm,mhuv2";
    reg = <0x10000000 0x10000>,
          <0x10010000 0x10000>;
    reg-names = "send", "recv";
    interrupts = <34 0>;
    #mbox-cells = <1>;
};
```

本页`int`为整数，`array`为数值数组，`string`为字符串，`string-array`为字符串数组，`boolean`为布尔属性，`compound`为复合类型；`phandle`为节点引用（Phandle），`phandles`为节点引用列表，`phandle-array`为节点引用与说明单元数组。必需性、默认值及合法值仅适用于所在层节点。

基础属性可用于多种节点，不保证全部适用于当前硬件。通用术语包括中断（Interrupt）、时钟（Clock）、电源域（Power Domain）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）和处理器间消息（Inter-Processor Messaging，IPM）。

## 34.2\_控制器节点属性

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `#mbox-cells` | `int` | **必需**。邮箱说明符（Mailbox Specifier）中应包含的说明单元数量 |
| `reg` | `array` | **必需**。两个寄存器区域：发送侧投递箱（Postbox，PBX）寄存器和接收侧邮箱（Mailbox，MBX）寄存器 |
| `reg-names` | `string-array` | **必需**。必须包含名称`send`和`recv`，分别标识PBX发送寄存器区域与MBX接收寄存器区域 |
| `interrupts` | `array` | **必需**。接收侧的单个中断（Interrupt） |
| `status` | `string` | 节点代表的硬件或其他资源的运行状态（Operational Status）。`okay` 表示资源可运行，例如可供驱动使用；`disabled` 表示资源不可运行，系统应将其视为不存在。参见《设备树规范》（Devicetree Specification）v0.4第2.3.4节；合法值：`okay, disabled, reserved, fail, fail-sss` |
| `compatible` | `string-array` | **必需**。字符串列表定义节点代表的硬件或其他资源类型。设备驱动通过特定兼容字符串（Compatible String）寻找应由自身管理的设备。推荐格式为 `vendor,device`：前者是厂商简称，后者通常来自数据手册。多个值从最具体到最通用排列，让具体设备匹配当前可用的最具体驱动。参见规范v0.4第2.3.1节 |
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

本页没有已弃用的顶层专用属性。

邮箱说明单元名称为`channel`，即原文`mbox cells: channel`。

通用接口见[邮箱公共接口](P014_邮箱驱动公共接口.md)。

---

[上一章：Andes软件中断邮箱绑定](P033_Andes软件中断邮箱绑定.md) · [下一章：ArmMHUv3邮箱绑定](P035_ArmMHUv3邮箱绑定.md) · [返回大纲](大纲.md)
