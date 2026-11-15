---
id: learning.zephyr-docs.hardware.boardbasebind-0
title: GPIO按键绑定
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/input/gpio-keys.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="std-dtcompatible-gpio-keys"></a>

# 第563章\_GPIO按键绑定

<a id="dtbinding-gpio-keys"></a>

原文：[gpio-keys](https://docs.zephyrproject.org/latest/build/dts/api/bindings/input/gpio-keys.html)。读取日期：2026-10-13，`latest`。

`gpio-keys` 是通用、与厂商无关的**通用输入输出（General-Purpose Input/Output，GPIO）**按键组绑定。它定义一组能够产生输入事件（Input Event）的按钮；每个按钮用 `gpio-keys` 节点的一个子节点描述，并指定自己的键码（Key Code）。驱动为 [`drivers/input/input_gpio_keys.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/input_gpio_keys.c)，相关开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=gpio-keys)。

## 563.1\_按键定义示例

官方示例将按键连接到 GPIO 控制器节点 `gpio0` 的引脚 13，`GPIO_PULL_UP` 表示上拉，`GPIO_ACTIVE_LOW` 表示低电平有效。`INPUT_KEY_0` 是输入事件键码常量，来自示例引用的设备树头文件：

```dts
#include <zephyr/dt-bindings/input/input-event-codes.h>

/ {
       buttons {
               compatible = "gpio-keys";
               button_0 {
                       gpios = <&gpio0 13 (GPIO_PULL_UP | GPIO_ACTIVE_LOW)>;
                       zephyr,code = <INPUT_KEY_0>;
               };
       };
};
```

## 563.2\_消抖与轮询

**消抖（Debouncing）**的时间间隔由整数类型 `int` 属性 `debounce-interval-ms` 设置，单位毫秒（Millisecond，ms）；未指定时默认为 `30`。

布尔类型 `boolean` 属性 `polling-mode` 启用**轮询模式（Polling Mode）**：不使用按键 GPIO 中断，而是按 `debounce-interval-ms` 指定的间隔周期性读取引脚。

## 563.3\_挂起时的引脚处理

字符串类型 `string` 属性 `zephyr,suspend-action` 指定设备挂起（Suspend）时驱动如何处理按键 GPIO。合法值为 `none`、`disconnect-with-pupd`、`full-disconnect`；为保持向后兼容，默认值是 `disconnect-with-pupd`。

**上拉（Pull-Up，PU）**与**下拉（Pull-Down，PD）**分别对应 `GPIO_PULL_UP` 和 `GPIO_PULL_DOWN` 标志。`GPIO_DISCONNECTED` 表示 GPIO 断开状态。

| 属性值 | 挂起动作 |
| --- | --- |
| `none` | 不执行动作，不重新配置 GPIO；适合 GPIO 控制器不支持断开状态的情况 |
| `disconnect-with-pupd` | 主要用于向后兼容，原文建议通常选用 `full-disconnect`；通过 `gpio_pin_configure_dt()` 将引脚重新配置为断开状态，同时保留设备树中的上拉/下拉标志 |
| `full-disconnect` | 完全断开引脚，重新配置时去除上拉和下拉标志；通过 `gpio_pin_configure()` 将引脚置为断开状态，其余设备树标志保持不变，预期使引脚处于高阻抗/悬空（High-Impedance/Floating）状态 |

当设备树没有上拉或下拉标志时，`disconnect-with-pupd` 与 `full-disconnect` 行为相同。否则前者的行为由实现决定：请求的上拉/下拉电阻可能启用，也可能不启用；GPIO 控制器驱动还可能以 `-ENOTSUP`（不支持）拒绝请求。

## 563.4\_按键子节点属性

下面的属性属于每个按键子节点，`phandle-array` 为设备树节点引用及其说明单元数组，`string` 为字符串，`int` 为整数。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `gpios` | `phandle-array` | 按键使用的 GPIO，必需；原页未附额外描述 |
| `label` | `string` | 按键的描述性名称 |
| `zephyr,code` | `int` | 要产生的键码 |
| `wakeup-ctrls` | `phandle-array` | 对应唤醒控制器（Wakeup Controller）的节点引用和唤醒源标识 |

原页没有已弃用的顶层专用属性。以下完整保留顶层继承的基础属性，其中 `compatible` 必需；不保证每项都适用于此兼容字符串。

## 563.5\_状态、兼容字符串与寄存器

本页 `int` 为整数，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`boolean` 为布尔属性，`compound` 为复合类型。**节点引用（Phandle）**用来指向其他节点；`phandle-array` 表示节点引用及其说明单元，`phandles` 表示节点引用列表。

`status` 的类型为 `string`，描述节点所代表硬件或其他资源的运行状态。`okay` 表示资源可运行，例如可供驱动使用；`disabled` 表示资源不可运行，系统应将它视为不存在。合法值为 `okay`、`disabled`、`reserved`、`fail`、`fail-sss`。详见《设备树规范》（Devicetree Specification）v0.4 第 2.3.4 节。

`compatible` 的类型为 `string-array`，是**必需属性**。它用字符串列表定义节点代表的硬件或其他资源类型；设备驱动检查特定兼容字符串，以寻找应由自己管理的节点。推荐格式为 `vendor,device`，其中 `vendor` 是厂商简称，`device` 通常取自数据手册。多个值应按从最具体到最通用排列，使某一通用家族的具体设备能匹配当前可用的最具体驱动。详见规范 v0.4 第 2.3.1 节。

`reg` 的类型为 `array`，给出寻址设备所需的信息，其含义取决于设备及 `compatible`。通常是一组“地址、长度”对，每对称为**寄存器块（Register Block）**，数值惯常写成十六进制。详见规范 v0.4 第 2.3.6 节。

`reg-names` 的类型为 `string-array`，为 `reg` 中各寄存器块提供可选名称。以下保留官方示例；`#address-cells` 和 `#size-cells` 分别声明地址与长度使用的 32 位单元数。

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

`uart@1000` 节点有两个寄存器块：名称 `foo` 对应基址 `0x1000`、大小 `0x2000`；名称 `bar` 对应基址 `0x3000`、大小 `0x4000`。这里 uart 是**通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）**节点名称，示例只是演示寄存器块命名。

## 563.6\_地址映射与中断

`ranges` 的类型为 `compound`，定义总线子地址空间与总线节点父地址空间之间的映射或转换。它通常为空，或由“子总线地址、父总线地址、长度”三元组构成。**空属性表示两侧地址空间相同，不需要转换；总线节点没有此属性时，则认为子节点与父地址空间之间不存在映射。**详见规范 v0.4 第 2.3.8 节。

下列属性描述**中断（Interrupt）**，参见规范 v0.4 第 2.4 节“中断与中断映射”。

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `interrupts` | `array` | 设备产生的中断，编码为一个或多个中断说明符；格式由设备在中断树中的位置决定，具有相同 `interrupt-parent` 的设备使用相同格式 |
| `interrupts-extended` | `compound` | 扩展中断说明符，可替代 `interrupts` |
| `interrupt-names` | `string-array` | 设备各中断的可选名称；中断本身在 `interrupts` 或 `interrupts-extended` 中定义 |
| `interrupt-parent` | `phandle` | 若存在，引用负责处理此设备所产生中断的节点 |

## 563.7\_标签、时钟与地址单元

**时钟提供者（Clock Provider）**提供设备使用的时钟。下表同时保留标签和子节点地址编码相关属性。

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `label` | `string` | 描述设备的可读字符串；除逐案确有需要外，已不推荐使用此属性。参见规范 v0.4 第 4.1.2 节“其他属性” |
| `clocks` | `phandle-array` | 设备的时钟提供者信息，通常应遵守下述 dt-schema 时钟绑定约定 |
| `clock-names` | `string-array` | `clocks` 中各时钟提供者的可选名称 |
| `#address-cells` | `int` | 子节点 `reg` 地址字段所用的 `<u32>` 单元数量 |
| `#size-cells` | `int` | 子节点 `reg` 大小字段所用的 `<u32>` 单元数量 |

`<u32>` 是 32 位无符号单元，两个 cells 属性见规范 v0.4 第 2.3.5 节。时钟约定见 [dt-schema 的 clock.yaml](https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml)。`status`、`compatible`、`reg`、`interrupts` 和 `label` 另见官方[重要属性（Important Properties）](https://docs.zephyrproject.org/latest/build/dts/intro-syntax-structure.html#dt-important-props)。

## 563.8\_DMA、输入输出与邮箱通道

**直接存储器访问（Direct Memory Access，DMA）**属性描述设备的 DMA 能力、通道和地址映射；输入输出（Input/Output，I/O）及邮箱（Mailbox）属性描述关联通道。IPM 是**处理器间消息（Inter-Processor Messaging）**接口。

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `dma-coherent` | `boolean` | 表示设备支持一致性 DMA 操作，见规范 v0.4 第 2.3.10 节 |
| `dmas` | `phandle-array` | 与设备相关的 DMA 通道说明符 |
| `dma-names` | `string-array` | `dmas` 中各 DMA 通道说明符的可选名称 |
| `dma-ranges` | `compound` | 定义总线物理地址空间与其父总线物理地址空间之间的映射或转换，见规范 v0.4 第 2.3.9 节 |
| `io-channels` | `phandle-array` | 与设备相关的 I/O 通道说明符 |
| `io-channel-names` | `string-array` | `io-channels` 中各通道说明符的可选名称 |
| `mboxes` | `phandle-array` | 与设备相关的邮箱/IPM 通道说明符 |
| `mbox-names` | `string-array` | `mboxes` 中各邮箱说明符的可选名称 |

## 563.9\_电源域与硬件锁

**电源域（Power Domain）**描述设备所属供电域；**硬件自旋锁（Hardware Spinlock）**为硬件提供的锁资源。属性如下：

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `power-domains` | `phandle-array` | 与设备相关的电源域说明符 |
| `power-domain-names` | `string-array` | `power-domains` 中各电源域说明符的可选名称 |
| `#power-domain-cells` | `int` | `power-domains` 属性中的单元数量 |
| `hwlocks` | `phandle-array` | 与设备相关的硬件自旋锁标识 |
| `hwlock-names` | `string-array` | `hwlocks` 中各锁说明符的可选名称 |

## 563.10\_初始化、唤醒和运行时电源管理

`zephyr,deferred-init` 为 `boolean` 属性：启动时不自动初始化设备，应使用 `device_init()` 手动初始化。

`wakeup-source` 为 `boolean` 属性，标识设备可以作为**唤醒源（Wakeup Source）**。提供它后，设备会设置一个专门标志，告知系统该设备具备唤醒系统的能力。这类设备的唤醒功能默认禁用，即其中断不会唤醒系统，必要时可在运行期间启用。

`zephyr,pm-device-runtime-auto` 为 `boolean` 属性，在初始化函数执行后自动为设备配置**运行时电源管理（Runtime Power Management）**。

`zephyr,disabling-power-states` 的类型为 `phandles`，列出会关闭此设备电源的电源状态。

---

[上一章：核心转储绑定](P562_核心转储绑定.md) · [下一章：GPIO指示灯绑定](P564_GPIO指示灯绑定.md) · [返回大纲](大纲.md)
