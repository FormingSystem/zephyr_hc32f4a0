---
id: learning.zephyr-docs.arm-timing-ethosu-control-binding-reference.page-1
title: arm_axi-timing-adapter
kind: reference
status: maintained
domains: [zephyr, devicetree, arm]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/arm/arm,axi-timing-adapter.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第1章\_arm_axi-timing-adapter

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/arm/arm,axi-timing-adapter.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="arm-axi-timing-adapter"></a>
<a id="dtbinding-arm-axi-timing-adapter"></a>
<a id="std-dtcompatible-arm-axi-timing-adapter"></a>

兼容字符串（Compatible String）：`arm,axi-timing-adapter`。厂商：[ ARM Ltd. ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-arm)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=arm,axi-timing-adapter)。

<a id="description"></a>

时序适配器（Timing Adapter，TA）是AXI到AXI桥，通过提供明确定义的存储器时序来评估AXI主设备性能。桥根据运行时可配置参数延迟存储器响应；启用相应功能时，还会对被测设备（Device Under Test，DUT）进行时钟门控（Clock Gating），从DUT角度模拟更快的访问。可调参数包括读写响应延迟、未完成事务数量及干扰流量模型。

多数用户会调整的常用参数包括 `maxr`、`maxw`、`maxrw`、`rlatency`、`wlatency`、`pulse-on`、`pulse-off` 和 `bwcap`。其他参数用于完整性或专门用途，例如模式、性能计数器（Performance Counter）和直方图（Histogram），通常保留默认值。

在神经网络处理器（NPU）外部测量时，可用性能计数器统计DUT时钟关闭周期。枚举定义见官方驱动中的 `timing_adapter_perfctrl_settings`：[timing_adapter.h](https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-core-platform/-/blob/main/drivers/timing_adapter/include/timing_adapter.h)。

链接核验记录：2026-10-16，上方官方引用的Arm GitLab驱动页面连续返回HTTP 202，另一路网页读取也未成功；保留官方地址，暂不视为已确认可访问。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 1.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `version` | `int` | 可选时序适配器（TA）模块版本，仅作信息记录。 |
| `maxr` | `int` | 6位字段，允许挂起的最大读操作数（Maximum Pending Reads）。0解释为无限制。常用调节参数。 |
| `maxw` | `int` | 6位字段，允许挂起的最大写操作数（Maximum Pending Writes）。0解释为无限制。常用调节参数。 |
| `maxrw` | `int` | 6位字段，允许挂起的读写操作总数上限（Maximum Pending Reads and Writes）。0解释为无限制。常用调节参数。 |
| `rlatency` | `int` | 12位字段，读取操作的最小延迟（Minimum Read Latency），以周期计，表示ARVALID与RVALID信号之间的持续时间。常用调节参数。 |
| `wlatency` | `int` | 12位字段，写入操作的最小延迟（Minimum Write Latency），以周期计。原文定义为WVALID与WLAST之间、BVALID保持无效时的持续时间。常用调节参数。 |
| `pulse-on` | `int` | 脉冲窗口内允许地址通过的周期数（Pulse-On Cycles），范围0～65535。常用调节参数。 |
| `pulse-off` | `int` | 脉冲窗口内阻止地址通过的周期数（Pulse-Off Cycles），范围0～65535。常用调节参数。 |
| `bwcap` | `int` | 16位字段，每个脉冲周期最多传输的总线字数（Bus Words）。脉冲周期由 `pulse-on` 与 `pulse-off` 定义；0解释为无限制。Ethos-U55的总线字为64位，Ethos-U65／U85为128位。常用调节参数。 |
| `perfctrl` | `int` | 性能计数器的6位事件选择器（Event Selector），通常用于从NPU外部分析性能时统计DUT时钟开启／关闭周期。枚举值见官方驱动的 `timing_adapter_perfctrl_settings`。 |
| `perfcnt` | `int` | 32位性能计数器预加载／复位值（Preload/Reset Value）。可在测量前预加载；配置 `perfctrl` 后，在运行结束时回读，例如用于统计DUT时钟关闭周期。 |
| `mode` | `int` | 时序适配器工作模式（Operation Mode），使用位0～11。固定虚拟平台（Fixed Virtual Platform，FVP）仅实现位0，其他位忽略或保留。位0控制动态时钟：0为静态时钟，不动态调整；1启用动态时钟以避免欠载（Underrun），为推荐设置。位1为1时启用随机AR重排，位2为1时启用随机R重排，位3为1时启用随机B重排；这三位默认均为0。 |
| `histbin` | `int` | 直方图分箱选择器（Histogram Bin Selector），范围0～15。 |
| `histcnt` | `int` | 直方图分箱值（Histogram Bin Value），32位。 |

本页没有已弃用的节点专用属性。

## 1.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `array` | **必需**。时序适配器（TA）基地址。 |
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

[本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P002_arm_beetle-syscon.md)
