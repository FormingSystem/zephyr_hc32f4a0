---
id: learning.zephyr-docs.usb-stm32-audio-binding-reference.page-11
title: usb-audio-hs
kind: reference
status: maintained
domains: [zephyr, devicetree, usb]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/usb/usb-audio-hs.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第11章\_usb-audio-hs

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/usb/usb-audio-hs.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="usb-audio-hs"></a>
<a id="dtbinding-usb-audio-hs"></a>
<a id="std-dtcompatible-usb-audio-hs"></a>

兼容字符串（Compatible String）：`usb-audio-hs`。厂商：[ 无厂商前缀 ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-no-vendor)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=usb-audio-hs)。

<a id="description"></a>

USB音频耳麦（USB Audio Headset）的专用字段。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 11.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `mic-resolution` | `int` | 原文没有提供文字说明；默认值：`16`；合法值：`8, 16, 24, 32` |
| `mic-sync-type` | `string` | IN设备的端点同步类型（Endpoint Synchronization Type），默认为同步（Synchronous）；不支持自适应（Adaptive）；默认值：`Synchronous`；合法值：`No Synchronization, Asynchronous, Adaptive, Synchronous` |
| `mic-sample-rate-hz` | `int` | 原文没有提供文字说明；默认值：`48000` |
| `mic-polling-interval` | `int` | 原文没有提供文字说明；默认值：`1` |
| `hp-resolution` | `int` | 原文没有提供文字说明；默认值：`16`；合法值：`8, 16, 24, 32` |
| `hp-sample-rate-hz` | `int` | 原文没有提供文字说明；默认值：`48000` |
| `hp-polling-interval` | `int` | 原文没有提供文字说明；默认值：`1` |
| `mic-channel-l` | `boolean` | 使能l声道（Channel）；保留原文的声道缩写 |
| `mic-channel-r` | `boolean` | 使能r声道（Channel）；保留原文的声道缩写 |
| `mic-channel-c` | `boolean` | 使能c声道（Channel）；保留原文的声道缩写 |
| `mic-channel-lfe` | `boolean` | 使能lfe声道（Channel）；保留原文的声道缩写 |
| `mic-channel-ls` | `boolean` | 使能ls声道（Channel）；保留原文的声道缩写 |
| `mic-channel-rs` | `boolean` | 使能rs声道（Channel）；保留原文的声道缩写 |
| `mic-channel-lc` | `boolean` | 使能lc声道（Channel）；保留原文的声道缩写 |
| `mic-channel-rc` | `boolean` | 使能rc声道（Channel）；保留原文的声道缩写 |
| `mic-channel-s` | `boolean` | 使能s声道（Channel）；保留原文的声道缩写 |
| `mic-channel-sl` | `boolean` | 使能sl声道（Channel）；保留原文的声道缩写 |
| `mic-channel-sr` | `boolean` | 使能sr声道（Channel）；保留原文的声道缩写 |
| `mic-channel-t` | `boolean` | 使能t声道（Channel）；保留原文的声道缩写 |
| `mic-channel-cfg` | `boolean` | 使能cfg声道（Channel）；保留原文的声道缩写 |
| `mic-feature-mute` | `boolean` | **必需**。使能静音（Mute）功能 |
| `mic-feature-volume` | `boolean` | 使能音量（Volume）功能，当前不支持 |
| `mic-feature-tone-control` | `boolean` | 使能音调控制（Tone Control），包括低音（Bass）、中音（Mid）和高音（Treble）；当前不支持 |
| `mic-feature-graphic-equalizer` | `boolean` | 使能图形均衡器（Graphic Equalizer）功能，当前不支持 |
| `mic-feature-automatic-gain-control` | `boolean` | 使能自动增益控制（Automatic Gain Control）功能，当前不支持 |
| `mic-feature-delay` | `boolean` | 使能延迟（Delay）功能，当前不支持 |
| `mic-feature-bass-boost` | `boolean` | 使能低音增强（Bass Boost）功能，当前不支持 |
| `mic-feature-loudness` | `boolean` | 使能响度（Loudness）功能，当前不支持 |
| `hp-channel-l` | `boolean` | 使能l声道（Channel）；保留原文的声道缩写 |
| `hp-channel-r` | `boolean` | 使能r声道（Channel）；保留原文的声道缩写 |
| `hp-channel-c` | `boolean` | 使能c声道（Channel）；保留原文的声道缩写 |
| `hp-channel-lfe` | `boolean` | 使能lfe声道（Channel）；保留原文的声道缩写 |
| `hp-channel-ls` | `boolean` | 使能ls声道（Channel）；保留原文的声道缩写 |
| `hp-channel-rs` | `boolean` | 使能rs声道（Channel）；保留原文的声道缩写 |
| `hp-channel-lc` | `boolean` | 使能lc声道（Channel）；保留原文的声道缩写 |
| `hp-channel-rc` | `boolean` | 使能rc声道（Channel）；保留原文的声道缩写 |
| `hp-channel-s` | `boolean` | 使能s声道（Channel）；保留原文的声道缩写 |
| `hp-channel-sl` | `boolean` | 使能sl声道（Channel）；保留原文的声道缩写 |
| `hp-channel-sr` | `boolean` | 使能sr声道（Channel）；保留原文的声道缩写 |
| `hp-channel-t` | `boolean` | 使能t声道（Channel）；保留原文的声道缩写 |
| `hp-channel-cfg` | `boolean` | 使能cfg声道（Channel）；保留原文的声道缩写 |
| `hp-feature-mute` | `boolean` | **必需**。使能静音（Mute）功能 |
| `hp-feature-volume` | `boolean` | 使能音量（Volume）功能 |
| `hp-feature-tone-control` | `boolean` | 使能音调控制（Tone Control），包括低音（Bass）、中音（Mid）和高音（Treble）；当前不支持 |
| `hp-feature-graphic-equalizer` | `boolean` | 使能图形均衡器（Graphic Equalizer）功能，当前不支持 |
| `hp-feature-automatic-gain-control` | `boolean` | 使能自动增益控制（Automatic Gain Control）功能，当前不支持 |
| `hp-feature-delay` | `boolean` | 使能延迟（Delay）功能，当前不支持 |
| `hp-feature-bass-boost` | `boolean` | 使能低音增强（Bass Boost）功能，当前不支持 |
| `hp-feature-loudness` | `boolean` | 使能响度（Loudness）功能，当前不支持 |
| `volume-max` | `int` | 注意：此属性为有符号值（Signed Value），表示最大音量（Maximum Volume）。范围从+127.9961 dB（0x7FFF）至−127.9961 dB（0x8001）；默认值：`0xa00`；范围：`0 to 0xffff` |
| `volume-min` | `int` | 注意：此属性为有符号值（Signed Value），表示最小音量（Minimum Volume）。范围从+127.9961 dB（0x7FFF）至−127.9961 dB（0x8001）；默认值：`0xba00`；范围：`0 to 0xffff` |
| `volume-res` | `int` | 注意：此属性只能为正值，表示音量分辨率／步进（Volume Resolution/Step）。1代表1/256 dB，即0.00390625 dB；0x100（256）代表1 dB；默认值：`0x100`；范围：`1 to 0x7fff` |

本页没有已弃用的节点专用属性。

## 11.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `status` | `string` | 节点代表的硬件或其他资源的运行状态（Operational Status）。`okay` 表示资源可运行，例如可供驱动使用；`disabled` 表示资源不可运行，系统应将其视为不存在。参见《设备树规范》（Devicetree Specification）v0.4第2.3.4节；合法值：`okay, disabled, reserved, fail, fail-sss` |
| `compatible` | `string-array` | **必需**。字符串列表定义节点代表的硬件或其他资源类型。设备驱动通过特定兼容字符串（Compatible String）寻找应由自身管理的设备。推荐格式为 `vendor,device`：前者是厂商简称，后者通常来自数据手册。多个值从最具体到最通用排列，让具体设备匹配当前可用的最具体驱动。参见规范v0.4第2.3.1节 |
| `reg` | `array` | 给出寻址设备所需的信息，具体含义随设备及 `compatible` 而变化。通常是一组地址与长度对，每对称为寄存器块（Register Block），数值通常写为十六进制。参见规范v0.4第2.3.6节及[重要属性](../devicetree/P003_语法与结构.md#dt-important-props) |
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

## 11.3\_寄存器块命名原例

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

[上一章](P010_usb-audio-hp.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P012_usb-audio-mic.md)
