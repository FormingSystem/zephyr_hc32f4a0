---
id: learning.zephyr-docs.lin-dali-mctp-sensor-bus-binding-reference.page-1
title: zephyr_dali-pwm
kind: reference
status: maintained
domains: [zephyr, devicetree, communication]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/dali/zephyr,dali-pwm.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第1章\_zephyr_dali-pwm

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/dali/zephyr,dali-pwm.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="zephyr-dali-pwm"></a>
<a id="dtbinding-zephyr-dali-pwm"></a>
<a id="std-dtcompatible-zephyr-dali-pwm"></a>

兼容字符串（Compatible String）：`zephyr,dali-pwm`。厂商：[ Zephyr Project ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-zephyr)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=zephyr,dali-pwm)。

驱动源码（Driver Source）：[drivers/dali/dali_pwm.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dali/dali_pwm.c)。

<a id="description"></a>

基于脉宽调制（Pulse Width Modulation，PWM）的数字可寻址照明接口（Digital Addressable Lighting Interface，DALI）。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 1.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `pwms` | `phandle-array` | **必需**。PWM单元控制DALI帧的发送。推荐时钟频率为1 MHz；为满足DALI标准，最低时钟频率为200 kHz。 |
| `counter` | `phandle` | **必需**。该计数器控制DALI收发中所有对时间敏感的操作。为满足DALI标准，最低时钟频率为1 MHz。 |
| `chan-id-rx` | `int` | **必需**。用于接收停止位（RX Stop Bit）与冲突超时（Collision Timeout）的计数器通道。 |
| `chan-id-tx` | `int` | **必需**。用于发送重配置（TX Re-programming）的计数器通道。 |
| `tx-prog-delay-us` | `int` | 不同控制器需要采用不同方式重新配置PWM单元。重配置由`rx-edge-event`同步，在PWM周期结束时间加上`tx-prog-delay-us`时执行；该延迟值可以为负。；默认值：`0` |
| `rx-gpios` | `phandle-array` | **必需**。连接到DALI RX引脚的GPIO。 |
| `tx-flank-shift-us` | `int` | **必需**。发送时下降沿与上升沿的传播延迟（Propagation Delay）差值，单位为微秒（µs）。例如高到低延迟8 µs、低到高延迟22 µs时，填写`(-14)`。应保持在较小的微秒范围；具体值取决于控制器及DALI物理接口的硬件实现。 |
| `rx-flank-shift-us` | `int` | **必需**。接收时下降沿与上升沿的传播延迟差值，单位为µs。例如高到低延迟47 µs、低到高延迟15 µs时，填写`(32)`。应保持在较小的微秒范围；具体值取决于控制器及DALI物理接口的硬件实现。 |
| `tx-rx-propagation-max-us` | `int` | **必需**。从发送端信号变化到读取并观察到该变化的最长时间，单位为µs。必须正确设置，才能实现正确的冲突检测；具体值取决于控制器及DALI物理接口的硬件实现。 |
| `rx-max-latency-us` | `int` | **必需**。从GPIO引脚状态变化到进入中断处理函数（IRQ Handler）的最长时间。必须调整此值，保证按标准要求读取位时序；具体值取决于控制器及DALI物理接口的硬件实现。 |
| `rx-grey-area-us` | `int` | **必需**。在帧间时序（Inter-frame Timing）上增加额外裕量，提高容差，以满足测试流程要求。 |

本页没有已弃用的节点专用属性。

## 1.2\_基础属性

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

[本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P002_renesas_ra-lin-sci-b.md)
