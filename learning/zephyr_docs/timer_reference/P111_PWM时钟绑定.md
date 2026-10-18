---
id: learning.zephyr-docs.timer_reference.clockbind-111
title: PWM时钟绑定
kind: reference
status: maintained
domains: [zephyr, timer_reference]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/clock/pwm-clock.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第111章\_PWM时钟绑定

<a id="dtbinding-pwm-clock"></a>

原文：[pwm-clock](https://docs.zephyrproject.org/latest/build/dts/api/bindings/clock/pwm-clock.html)。读取日期：2026-10-13，`latest`。

`pwm-clock`是通用或厂商无关（Generic or Vendor-independent）的设备树绑定（Devicetree Binding）。

它描述由脉宽调制（Pulse Width Modulation，PWM）引脚驱动的外部时钟信号。设备树必须定义时钟节点。原例中`PWM_HZ()`是频率转周期宏，`PWM_POLARITY_NORMAL`是正常极性（Normal Polarity）标志：

```dts
pwmclock: pwmclock {
    status = "okay";
    compatible = "pwm-clock";
    #clock-cells = <1>;
    pwms = <&pwm_ccu40 2 PWM_HZ(1000000) PWM_POLARITY_NORMAL>;
};
```

这会创建提供时钟控制器（Clock Controller）应用程序编程接口（Application Programming Interface，API）的设备节点；设备内部使用 PWM API 启动1 MHz时钟信号。宏`PWM_HZ()`将频率换算为以纳秒（Nanosecond，ns）为单位的时间。原文称“时钟频率不是整数纳秒时”会产生舍入误差。

译注：该句混用了频率与时间单位；这里实际涉及对应周期不能以整数纳秒精确表示的情况。原例保持不变。可用`clock-frequency`显式指定时钟频率。

PWM 节点可能需要适当配置，例如设置预分频器（Prescaler）选项，才能生成目标周期；应参阅所用 PWM 驱动的文档。

驱动源码：[`drivers/clock_control/clock_control_pwm.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/clock_control_pwm.c)。

采用此兼容字符串的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=pwm-clock)。

属性类型：`int`为整数，`boolean`为布尔属性，`string`为字符串，`string-array`为字符串数组，`array`为数值数组，`compound`为复合类型；`phandle`为节点引用（Phandle），`phandles`为节点引用列表，`phandle-array`为节点引用与说明符单元数组。

## 111.1\_节点专用属性

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `pwms` | `phandle-array` | **必需**。PWM 说明符数组；原页没有额外文字说明 |
| `clock-frequency` | `int` | 精确输出频率：用于 PWM 周期不精确、已舍入到纳秒的情况。此属性可选 |
| `pwm-on-delay` | `int` | 可选的阻塞延时（Blocking Delay），单位为微秒（Microsecond，µs），确保时钟开启接口（Clock Enable API）函数`clock_control_on()`返回后 PWM 时钟已启动；默认值：`0` |
| `#clock-cells` | `int` | **必需**。时钟说明符（Clock Specifier）所需的单元数量；固定值：`1` |

本页没有已弃用的节点专用属性。

## 111.2\_基础属性

以下属性继承自基础绑定（Base Binding），是可用于许多节点的通用定义，**并非全部一定适用于本兼容字符串**。

表中涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `status` | `string` | 节点代表的硬件或其他资源的运行状态（Operational Status）。`okay` 表示资源可运行，例如可供驱动使用；`disabled` 表示资源不可运行，系统应将其视为不存在。参见《设备树规范》（Devicetree Specification）v0.4第2.3.4节；合法值：`okay, disabled, reserved, fail, fail-sss` |
| `compatible` | `string-array` | **必需**。字符串列表定义节点代表的硬件或其他资源类型。设备驱动通过特定兼容字符串（Compatible String）寻找应由自身管理的设备。推荐格式为 `vendor,device`：前者是厂商简称，后者通常来自数据手册。多个值从最具体到最通用排列，让具体设备匹配当前可用的最具体驱动。参见规范v0.4第2.3.1节 |
| `reg` | `array` | 给出寻址设备所需的信息，具体含义随设备及 `compatible` 而变化。通常是一组地址与长度对，每对称为寄存器块（Register Block），数值通常写为十六进制。参见规范v0.4第2.3.6节及[重要属性](../devicetree/P003_语法与结构.md) |
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

## 111.3\_寄存器块命名原例

以下设备树源码（Devicetree Source，DTS）仅演示`reg-names`命名；`uart`指通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）。

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

`uart@1000`有两个寄存器块（Register Block）：`foo`的基址为`0x1000`、大小为`0x2000`；`bar`的基址为`0x3000`、大小为`0x4000`。

## 111.4\_说明符单元名称

时钟说明符（Clock Specifier）的单元名称为`id`。


---

[上一章：固定比例时钟绑定](P110_固定比例时钟绑定.md) · [下一章：Infineon固定时钟绑定](P112_Infineon固定时钟绑定.md) · [返回大纲](大纲.md)
