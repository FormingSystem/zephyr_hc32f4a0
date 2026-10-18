---
id: learning.zephyr-docs.pwm-intel-microchip-nxp-binding-reference.page-20
title: nxp_emios-pwm
kind: reference
status: maintained
domains: [zephyr, devicetree, pwm]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/pwm/nxp,emios-pwm.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第20章\_nxp_emios-pwm

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/pwm/nxp,emios-pwm.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="nxp-emios-pwm"></a>
<a id="dtbinding-nxp-emios-pwm"></a>
<a id="std-dtcompatible-nxp-emios-pwm"></a>

兼容字符串（Compatible String）：`nxp,emios-pwm`。厂商：[ NXP Semiconductors ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-nxp)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=nxp,emios-pwm)。

驱动源码（Driver Source）：[drivers/pwm/pwm_nxp_emios.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/pwm_nxp_emios.c)。

<a id="description"></a>

NXP增强模块化I/O子系统（Enhanced Modular I/O Subsystem，eMIOS）PWM节点。每个统一通道（Unified Channel，UC）可配置为PWM或捕获操作。模块支持多种模式：部分仅适用于带内部计数器的通道，部分需要来自计数器总线的参考时基（Reference Timebase）。

OPWMB和OPWMCB采用参考时基，必须启用并配置对应计数器总线设备树节点；参见官方`nxp,emios`绑定。

<a id="examples"></a>

官方设备树示例（Devicetree Example）：

```dts
emios0_pwm: pwm {
  pwm0 {
    channel = <16>;
    mode = "OPWFMB";
    counter-bus-type = "BUS_INTERNAL";
    prescaler = <8>;
  };

  pwm1 {
    channel = <9>;
    mode = "OPWMB";
    counter-bus-type = "BUS_C";
    phase-shift = <100>;
  };

  pwm2 {
    channel = <2>;
    mode = "OPWMCB_LEAD_EDGE";
    counter-bus-type = "BUS_B";
    dead-time = <100>;
  };
};
```

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

<a id="top-level-properties"></a>

## 20.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `pinctrl-0` | `phandles` | **必需**。第一个状态（State）的引脚配置（Pin Configuration），具体内容取决于所选引脚控制器驱动（Pin Controller Driver）的实现 |
| `pinctrl-names` | `string-array` | **必需**。所提供状态的名称，名称数量必须与状态数量一致 |
| `#pwm-cells` | `int` | **必需**。PWM说明符（PWM Specifier）中预期的单元数量。；固定值：`3` |
| `channels` | `int` | 控制器支持的PWM通道（Channel）数量。 |
| `pinctrl-1` | `phandles` | 第二个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-2` | `phandles` | 第三个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-3` | `phandles` | 第四个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-4` | `phandles` | 第五个状态的引脚配置，参见pinctrl-0 |

本页没有已弃用的节点专用属性。

## 20.2\_基础属性

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

<a id="child-node-properties"></a>

## 子节点属性

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `channel` | `int` | **必需**。eMIOS PWM通道（Channel）。 |
| `mode` | `string` | **必需**。PWM模式选择：<br>`OPWFMB`：产生占空比和频率可变的波形，使用内部计数器。<br>`OPWMB`：产生前沿／后沿位置可编程的脉冲；周期由处于MCB向上计数模式的外部计数器周期决定。运行时修改PWM周期会影响共享该时基的所有通道，新周期和循环值在下一个周期边界生效。<br>`OPWMCB`：产生中心对齐PWM，在前沿或后沿插入死区；周期由处于MCB向上／向下计数模式的外部计数器决定。运行时修改周期同样影响共享时基的所有通道，新值在下一个周期边界生效。<br>`SAIC`：单动作输入捕获（Single Action Input Capture），事件发生即捕获，保存最近一次事件值供软件读取；使用内部计数器，范围`[0, 0xFFFF]`。；合法值：`OPWFMB, OPWMB, OPWMCB_TRAIL_EDGE, OPWMCB_LEAD_EDGE, SAIC` |
| `counter-bus-type` | `string` | **必需**。计数器总线（Counter Bus）为各通道提供时基。全局总线可供其他任意通道使用，局部总线只供指定通道使用；驱动总线的通道只能采用自身内部计数器作为时基。<br>`BUS_A`：全局总线，由通道23驱动，供其他所有通道使用。<br>`BUS_B`：局部总线，由通道0驱动，供通道1至7使用。<br>`BUS_C`：局部总线，由通道8驱动，供通道9至15使用。<br>`BUS_D`：局部总线，由通道16驱动，供通道17至23使用。<br>`BUS_F`：全局总线，由通道22驱动，供其他所有通道使用。<br>`BUS_INTERNAL`：通道自己的内部计数器，供OPWFMB及SAIC模式使用。；合法值：`BUS_A, BUS_B, BUS_C, BUS_D, BUS_F, BUS_INTERNAL` |
| `prescaler` | `int` | 内部计数器预分频器的时钟分频值。；默认值：`1`；范围：`1 to 16` |
| `dead-time` | `int` | OPWMCB模式下PWM通道的死区时间，以计数节拍（Tick）为单位。；默认值：`0` |
| `phase-shift` | `int` | OPWMB模式下PWM通道的相移（Phase Shift），以计数节拍为单位。；默认值：`0` |
| `input-filter` | `int` | 选择能通过输入滤波器（Input Filter）的最小输入脉冲宽度，以滤波时钟周期为单位。输入到响应的滤波延迟为三个时钟边沿。默认0表示旁路滤波器；可编程输入滤波器的时钟源为eMIOS时钟。；默认值：`0`；合法值：`0, 2, 4, 8, 16` |

## 20.3\_寄存器块命名原例

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

<a id="specifier-cell-names"></a>

## 20.4\_说明符单元名称

PWM说明符单元（PWM Specifier Cells）按原文顺序为：`channel`, `period`, `flags`。

名称对照：`channel` 为通道；`period` 为周期；`flags` 为标志。

---

[上一章](P019_nxp_ctimer-pwm.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md)
