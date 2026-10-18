---
id: learning.zephyr-docs.intercore_reference.mboxbind-38
title: Infineon邮箱绑定
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/mbox/infineon,mbox.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第38章\_Infineon邮箱绑定

<a id="dtbinding-infineon-mbox"></a>

原文：[infineon,mbox](https://docs.zephyrproject.org/latest/build/dts/api/bindings/mbox/infineon,mbox.html)。读取日期：2026-10-13，`latest`。

`infineon,mbox`是 Infineon Technologies 的设备树绑定（Devicetree Binding），用于邮箱（Mailbox，MBOX）。

此绑定将英飞凌处理器间通信（Inter-processor Communication，IPC）模块公开为 Zephyr 邮箱控制器。驱动通过直接寄存器访问，在该模块上实现多通道处理器间邮箱（Multi-Channel Inter-Processor Mailbox，MBOX）应用程序接口（Application Programming Interface，API）。每个通道携带一个或两个32位数据字，由各控制器的`msg-size-bytes`选择。

每个邮箱通道由索引相同的一项`ipc-configs`和一项`interrupts`共同描述：

| 条目或字段 | 含义 |
| --- | --- |
| `ipc-configs = <&ipcX channel interrupt>`中的`&ipcX` | 通道所属IPC实例的节点引用（Phandle） |
| `channel` | 该实例内部的IPC通道索引 |
| `interrupt` | 该实例内部、接收方为本通道监视的中断结构索引 |
| `interrupts` | 此中断结构在本核心上的嵌套向量中断控制器（Nested Vectored Interrupt Controller，NVIC）向量 |

使用方通过`#mbox-cells = <1>`传入的是**上述数组的索引，不是IPC硬件通道编号**。任意核心都可以使用任意IPC实例，没有固定的实例到核心映射。一个控制器可以引用任意实例，甚至为不同通道混用不同实例。只有`interrupts`条目与核心相关：必须填写所选中断结构在实际处理中断核心自身向量表中的NVIC向量。

原配置示例：

```dts
  &ipc0 {
      status = "okay";
  };

  mbox0: mbox {
      compatible = "infineon,mbox";
      #mbox-cells = <1>;
      ipc-configs = <&ipc0 3 3>, <&ipc0 4 4>;
      interrupts = <73 4>, <74 4>;
      status = "okay";
  };
```


驱动为 [`drivers/mbox/mbox_infineon.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mbox/mbox_infineon.c)。

使用此兼容字符串的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=infineon,mbox)。

本页`int`为整数，`array`为数值数组，`string`为字符串，`string-array`为字符串数组，`boolean`为布尔属性，`compound`为复合类型；`phandle`为节点引用（Phandle），`phandles`为节点引用列表，`phandle-array`为节点引用与说明单元数组。必需性、默认值及合法值仅适用于所在层节点。

基础属性可用于多种节点，不保证全部适用于当前硬件。通用术语包括中断（Interrupt）、时钟（Clock）、电源域（Power Domain）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）和处理器间消息（Inter-Processor Messaging，IPM）。

## 38.1\_控制器节点属性

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `ipc-configs` | `phandle-array` | **必需**。每个邮箱通道对应一项，选择所用IPC实例、通道与中断结构；条目数量必须与`interrupts`一致 |
| `msg-size-bytes` | `int` | 此控制器的每条通道承载的固定消息大小，单位为字节（Byte）。4字节仅使用IPC DATA0；8字节使用DATA0和DATA1，并要求IPC模块实现DATA1，例如M33SYSCPUSS、M7CPUSS或M4CPUSS v2（如PSE84、TRAVEO T2G）。只有DATA0的硬件模块（如M4CPUSS v1）应使用4字节。默认8字节以匹配PSE84系列；默认值：`8`；合法值：`4, 8` |
| `#mbox-cells` | `int` | **必需**。邮箱说明符（Mailbox Specifier）中应包含的说明单元数量 |
| `interrupts` | `array` | **必需**。设备产生的中断，编码为一个或多个中断说明符；格式由设备在中断树中的位置决定，具有相同 `interrupt-parent` 的设备使用相同格式；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `status` | `string` | 节点代表的硬件或其他资源的运行状态（Operational Status）。`okay` 表示资源可运行，例如可供驱动使用；`disabled` 表示资源不可运行，系统应将其视为不存在。参见《设备树规范》（Devicetree Specification）v0.4第2.3.4节；合法值：`okay, disabled, reserved, fail, fail-sss` |
| `compatible` | `string-array` | **必需**。字符串列表定义节点代表的硬件或其他资源类型。设备驱动通过特定兼容字符串（Compatible String）寻找应由自身管理的设备。推荐格式为 `vendor,device`：前者是厂商简称，后者通常来自数据手册。多个值从最具体到最通用排列，让具体设备匹配当前可用的最具体驱动。参见规范v0.4第2.3.1节 |
| `reg` | `array` | 给出寻址设备所需的信息，具体含义随设备及 `compatible` 而变化。通常是一组地址与长度对，每对称为寄存器块（Register Block），数值通常写为十六进制。参见规范v0.4第2.3.6节及[重要属性](../devicetree/P003_语法与结构.md) |
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

本层`reg-names`的原例用于说明寄存器块（Register Block）命名；`uart`为通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）节点名。

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

`uart@1000`有两个寄存器块：`foo`基址为`0x1000`、大小为`0x2000`；`bar`基址为`0x3000`、大小为`0x4000`。

本页没有已弃用的顶层专用属性。

邮箱说明单元名称为`channel`，即原文`mbox cells: channel`。

通用接口见[邮箱公共接口](P014_邮箱驱动公共接口.md)。

---

[上一章：ESP32邮箱绑定](P037_ESP32邮箱绑定.md) · [下一章：IVSHMEM邮箱绑定](P039_IVSHMEM邮箱绑定.md) · [返回大纲](大纲.md)
