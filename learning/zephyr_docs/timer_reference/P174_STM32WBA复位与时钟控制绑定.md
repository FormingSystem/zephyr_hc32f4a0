---
id: learning.zephyr-docs.timer_reference.stmrccw-174
title: STM32WBA复位与时钟控制绑定
kind: reference
status: maintained
domains: [zephyr, timer_reference]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/clock/st,stm32wba-rcc.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第174章\_STM32WBA复位与时钟控制绑定

<a id="dtbinding-st-stm32wba-rcc"></a>

原文：[st,stm32wba-rcc](https://docs.zephyrproject.org/latest/build/dts/api/bindings/clock/st,stm32wba-rcc.html)。读取日期：2026-10-13，`latest`。

`st,stm32wba-rcc`是 STMicroelectronics 的设备树绑定（Devicetree Binding），描述STM32WBA的复位与时钟控制器（Reset and Clock Controller，RCC）。

采用此兼容字符串的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=st,stm32wba-rcc)。

## 174.1\_时钟源与配置关系

总线名称中，AHB指高级高性能总线（Advanced High-performance Bus），APB指高级外设总线（Advanced Peripheral Bus）。CPU为中央处理器（Central Processing Unit），DMA为直接存储器访问（Direct Memory Access）；SRAM为静态随机存取存储器（Static Random-Access Memory），Flash为闪存。预分频器（Prescaler）从输入时钟产生分频输出；SYSCLK为系统时钟（System Clock），Hz为赫兹（Hertz），MHz为兆赫（Megahertz）。

高速外部时钟（High-speed External Clock，HSE）、高速内部时钟（High-speed Internal Clock，HSI）及锁相环（Phase-Locked Loop，PLL）是下文使用的时钟源术语。

此节点负责SYSCLK源选择，以及AHB与APB总线域（Bus Domain）的时钟控制。应从`clocks`节点中可用的时钟节点选择源，通常是`clk_hse`、`clk_hsi`或`pll`。用`clock-frequency`定义内核时钟频率（Core Clock Frequency），关系为`内核时钟频率 = SYSCLK / AHB预分频系数`。随后通过对应预分频属性配置外设总线时钟，通常为`PCLK1`、`PCLK2`、`PCLK7`。

官方RCC节点原例：

```dts
&rcc {
         clocks = <&pll>;                   /* Select pll as SYSCLK source */
         ahb-prescaler = <2>;
         clock-frequency = <DT_FREQ_M(40)>; /* = SYSCLK / AHB prescaler */
         apb1-presacler = <1>;
         apb2-presacler = <1>;
         apb7-presacler = <7>;
}
```

原注释说明选择PLL作为SYSCLK源，经AHB二分频得到40 MHz内核时钟；`DT_FREQ_M(40)`表示40 MHz。译注：原例把3项APB属性写成`apb1-presacler`、`apb2-presacler`、`apb7-presacler`，与下方正式属性名的`prescaler`拼写不同；原例的APB7值7也不在正式属性列出的合法值中，且节点结尾未写分号。这里保留原片段并指出差异，实际配置必须遵守正式属性名、合法取值及完整DTS语法，不能直接照抄该示意片段。

要指定门控时钟（Gated Clock），外设在`clocks`中按如下方式填写：

```dts
... {
         ...
         clocks = <&rcc STM32_CLOCK(APB2, 5)>;
         ...
}
```

在指向`rcc`的节点引用（Phandle）后使用`STM32_CLOCK()`宏：第一个参数指定外设所接总线，第二个参数指定RCC中该总线控制寄存器的时钟门控位编号（Gate Bit Number）。原例为`RCC_APB2ENR`第5位，并以STM32F401的`USART6EN`举例；USART是通用同步异步收发器（Universal Synchronous/Asynchronous Receiver/Transmitter）。该器件名按原页保留，不把此示例当成WBA专有位定义。

访问外设控制器时需要门控时钟，通常用于配置设备；若不使用双时钟域（Dual Clock Domain），门控时钟也用于外设运行。若需要多个门控位，可采用显式写法：

```dts
... {
         ...
         clocks = <&rcc STM32_CLOCK_BUS_APB2 ((1 << 14) | (1 << 7))>;
         ...
}
```

`STM32_CLOCK_BUS_APB2`是显式APB2总线标识，第14位和第7位控制外设门控；可以使用两个以上的位，且各位无须连续。

要指定替代时钟源（Alternate Clock Source），可在时钟属性中增加一个时钟说明符（Clock Specifier）：

```dts
... {
         ...
         clocks = <&rcc STM32_CLOCK(APB2, 5)>,
                      <&rcc STM32_SRC_HSI I2C1_SEL(2)>;
         ...
}
```

原例中的 `STM32_SRC_HSI` 是HSI源标识，`I2C1_SEL(2)`是I2C1时钟源选择说明符；原例把I2C1设备的时钟源指定为HSI；I²C为集成电路间总线（Inter-Integrated Circuit）。设备驱动负责依照时钟控制应用程序编程接口（Clock Control Application Programming Interface，API）`clock_control`规范查询、使用时钟源信息。上述含`...`的片段是示意，须置于完整且有效的设备树源码（Devicetree Source，DTS）中。

## 174.2\_节点专用属性

属性类型：`int`为整数，`boolean`为布尔属性，`string`为字符串，`string-array`为字符串数组，`array`为数值数组，`compound`为复合类型；`phandle`为节点引用（Phandle），`phandles`为节点引用列表，`phandle-array`为节点引用与说明符单元数组。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `#clock-cells` | `int` | **必需**。时钟说明符（Clock Specifier）所需的单元数量；固定值：`2` |
| `clock-frequency` | `int` | **必需**。时钟输出`HCLK1`的默认频率，单位为Hz |
| `ahb-prescaler` | `int` | **必需**。AHB1、AHB2、AHB4共用预分频系数，亦称`HPRE`；根据系统频率输入确定实际内核时钟`HCLK`，HCLK为CPU、AHB1、AHB2、存储器及DMA供时钟；合法值：`1, 2, 4, 8, 16` |
| `ahb5-prescaler` | `int` | AHB5预分频系数，亦称`HPRE5`；根据系统频率输入确定`HCLK5`实际频率，用于将HCLK5限制在**32 MHz以下**。**仅在系统时钟源为PLL1时要求提供**；合法值：`1, 2, 3, 4, 6` |
| `apb1-prescaler` | `int` | **必需**。APB1预分频系数；原属性栏没有额外文字说明；合法值：`1, 2, 4, 8, 16` |
| `apb2-prescaler` | `int` | **必需**。APB2预分频系数；原属性栏没有额外文字说明；合法值：`1, 2, 4, 8, 16` |
| `apb7-prescaler` | `int` | **必需**。APB7预分频系数；原属性栏没有额外文字说明；合法值：`1, 2, 4, 8, 16` |
| `ahb5-div` | `boolean` | AHB5分频器。**仅适用于系统时钟源为HSI16（16 MHz内部时钟）或HSE32（32 MHz外部时钟）的情况**；启用时AHB5时钟等于系统时钟除以2，禁用时系统时钟不分频 |

本页没有已弃用的节点专用属性。

## 174.3\_基础属性

以下31项属性继承自基础绑定（Base Binding），**并非全部一定适用于本兼容字符串**。表中涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）和硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
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

## 174.4\_寄存器块命名原例

以下为`reg-names`的原设备树源码（Devicetree Source，DTS）示例；`uart`为通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）节点。

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

`uart@1000`包含两个寄存器块（Register Block）：`foo`基址`0x1000`、大小`0x2000`；`bar`基址`0x3000`、大小`0x4000`。

## 174.5\_说明符单元名称

时钟说明符依次包含`bus`和`bits`两个单元（Specifier Cells）。


---

[上一章：STM32WL复位与时钟控制绑定](P173_STM32WL复位与时钟控制绑定.md) · [下一章：STM32WB0复位与时钟控制绑定](P175_STM32WB0复位与时钟控制绑定.md) · [返回大纲](大纲.md)
