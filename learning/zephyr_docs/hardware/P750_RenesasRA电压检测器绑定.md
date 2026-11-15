---
id: learning.zephyr-docs.hardware.comprennrf-2
title: RenesasRA电压检测器绑定
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/comparator/renesas,ra-lvd.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第750章\_RenesasRA电压检测器绑定

<a id="dtbinding-renesas-ra-lvd"></a>

原文：[renesas,ra-lvd](https://docs.zephyrproject.org/latest/build/dts/api/bindings/comparator/renesas,ra-lvd.html)。读取日期：2026-10-13，`latest`。

`renesas,ra-lvd` 是设备树绑定（Devicetree Binding），描述Renesas RA低电压检测（Low-Voltage Detection，LVD）控制器。

驱动为 [`drivers/comparator/comparator_renesas_ra_lvd.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/comparator/comparator_renesas_ra_lvd.c)。

使用此兼容字符串的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=renesas,ra-lvd)。

## 750.1\_节点布局与使能示例

以下保留官方设备树源码（Devicetree Source，DTS）示例。原代码中的地址、引脚及中断配置须结合具体芯片；带 `...` 的部分是原文省略内容。

最小节点布局：

```dts
  lvd1: lvd@4001e0e0 {
          compatible = "renesas,ra-lvd";
          reg = <0x4001e0e0 0x02>;
          channel = <1>;
          status = "disabled";
  };
```

使能控制器需要设置最小默认配置，包括正、负输入。负输入通过具体电压阈值等级选择，正输入固定为电源电压（Supply Voltage，Vcc）。

```dts
  &lvd1 {
        lvd-action = "maskable-interrupt";
        voltage_level = <384>;
        lvd-trigger = "rising";
        reset-negation-timing = <0>;
        status = "okay";
  };
```

译注：示例写作 `voltage_level`，本绑定属性表实际为 `voltage-level`；示例值384也不能直接套用为本绑定的电压编码。RA属性按芯片硬件手册映射，不能套用RX按百分之一伏表达的规则。这里保留原代码，实际配置须使用正确属性名与对应芯片的合法编码。

## 750.2\_节点专用属性

`int` 为整数，`string` 为字符串，`boolean` 为布尔属性，`phandles` 为节点引用（Phandle）列表，`string-array` 为字符串数组。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `channel` | `int` | **必需**。通道（Channel）编号；原页只标明类型与必需性，没有额外文字说明 |
| `voltage-level` | `int` | **必需**。各通道电压检测等级（Voltage Detection Level）编码，须映射到硬件手册（Hardware Manual，HWM）列出的电压。例如RA8P1中，3.86 V使用 `0x03`，1.90 V使用 `0x0C`。**不得设置硬件手册禁止的值**；各RA微控制器（Microcontroller Unit，MCU）系列支持的具体等级以硬件手册为准 |
| `noise-filter` | `int` | 硬件数字去抖滤波器（Digital Debounce Filter）的低速片上振荡器（Low-Speed On-Chip Oscillator，LOCO）分频因子；因子越大，去抖时间越长、输出更新越慢。设为1时禁用滤波；硬件不支持滤波时也设为1；默认值：`16`；合法值：`1, 2, 4, 8, 16` |
| `lvd-trigger` | `string` | 指定电压检测条件（Voltage Detection Condition），并影响中断条件：`rising` 上升、`falling` 下降、`both` 两者；默认值：`falling`；合法值：`rising, falling, both` |
| `reset-only` | `boolean` | 表示此通道只支持复位动作（Reset Action），不支持中断与监测 |
| `lvd-action` | `string` | **必需**。检测到低电压时采取的动作：`non-maskable-interrupt` 为不可屏蔽中断（Non-Maskable Interrupt），`maskable-interrupt` 为可屏蔽中断（Maskable Interrupt），`reset` 为复位，`no-action` 为无动作。若 `reset-only` 为真，动作始终为 `reset`；合法值：`non-maskable-interrupt, maskable-interrupt, reset, no-action` |
| `reset-negation-timing` | `int` | 系统解除复位（Reset Negation）的时机；动作不为 `reset` 时忽略此属性。复位触发方向与0／1取值的具体条件见后文专节；默认值：`0`；合法值：`0, 1` |
| `pinctrl-0` | `phandles` | 第一个引脚控制（Pin Control）状态的配置引用；具体内容由选用的引脚控制器驱动实现决定 |
| `pinctrl-1` | `phandles` | 第二个引脚控制（Pin Control）状态的配置引用；具体内容由选用的引脚控制器驱动实现决定，参见 `pinctrl-0` |
| `pinctrl-2` | `phandles` | 第三个引脚控制（Pin Control）状态的配置引用；具体内容由选用的引脚控制器驱动实现决定，参见 `pinctrl-0` |
| `pinctrl-3` | `phandles` | 第四个引脚控制（Pin Control）状态的配置引用；具体内容由选用的引脚控制器驱动实现决定，参见 `pinctrl-0` |
| `pinctrl-4` | `phandles` | 第五个引脚控制（Pin Control）状态的配置引用；具体内容由选用的引脚控制器驱动实现决定，参见 `pinctrl-0` |
| `pinctrl-names` | `string-array` | 已提供的引脚状态名称；名称数量必须与状态数量一致 |

## 750.3\_解除复位时机及原文表述

Vcc表示电源电压，Vdet表示检测电压阈值（Detection Voltage Threshold），稳定时间（Stabilization Time）表示时序等待。

| 动作及触发 | 配置值 | 原文规定 |
| --- | --- | --- |
| `reset`，`falling`；Vcc低于Vdet时复位 | 0 | 原文写为在 `Vcc > Vdet + stabilization time` 后解除复位 |
| `reset`，`falling` | 1 | 复位断言后再经过稳定时间，解除复位 |
| `reset`，`rising`；Vcc高于Vdet时复位 | 0 | 原文写为在 `Vcc < Vdet - stabilization time` 后解除复位 |
| `reset`，`rising` | 1 | **禁止设置此值** |
| 非 `reset` 动作 | 0或1 | 忽略该属性 |

译注：上表保留原文将电压条件与稳定时间用加减号连接的表达，不能把电压与时间当作同量纲数值进行运算。实际解除复位的电压条件及等待时序应查对应芯片硬件手册；这里不替原文推定其未明确的时序。

没有已弃用的节点专用属性。以下保留继承的基础属性，不保证全部适用于本绑定；`compatible` 为必需属性。

## 750.4\_状态、兼容字符串与寄存器

本页 `int` 为整数，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`boolean` 为布尔属性，`compound` 为复合类型。**节点引用（Phandle）**用来指向其他节点；`phandle-array` 表示节点引用及其说明单元，`phandles` 表示节点引用列表。

`status` 的类型为 `string`，描述节点所代表硬件或其他资源的运行状态。`okay` 表示资源可运行，例如可供驱动使用；`disabled` 表示资源不可运行，系统应将它视为不存在。合法值为 `okay`、`disabled`、`reserved`、`fail`、`fail-sss`。详见《设备树规范》（Devicetree Specification）v0.4 第 2.3.4 节。

`compatible` 的类型为 `string-array`，是**必需属性**。它用字符串列表定义节点代表的硬件或其他资源类型；设备驱动检查特定兼容字符串，以寻找应由自己管理的节点。推荐格式为 `vendor,device`，其中 `vendor` 是厂商简称，`device` 通常取自数据手册。多个值应按从最具体到最通用排列，使某一通用家族的具体设备能匹配当前可用的最具体驱动。详见规范 v0.4 第 2.3.1 节。

`reg` 的类型为 `array`，是**必需属性**，给出寻址设备所需的信息，其含义取决于设备及 `compatible`。通常是一组“地址、长度”对，每对称为**寄存器块（Register Block）**，数值惯常写成十六进制。详见规范 v0.4 第 2.3.6 节。

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

## 750.5\_地址映射与中断

`ranges` 的类型为 `compound`，定义总线子地址空间与总线节点父地址空间之间的映射或转换。它通常为空，或由“子总线地址、父总线地址、长度”三元组构成。**空属性表示两侧地址空间相同，不需要转换；总线节点没有此属性时，则认为子节点与父地址空间之间不存在映射。**详见规范 v0.4 第 2.3.8 节。

下列属性描述**中断（Interrupt）**，参见规范 v0.4 第 2.4 节“中断与中断映射”。

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `interrupts` | `array` | 设备产生的中断，编码为一个或多个中断说明符；格式由设备在中断树中的位置决定，具有相同 `interrupt-parent` 的设备使用相同格式 |
| `interrupts-extended` | `compound` | 扩展中断说明符，可替代 `interrupts` |
| `interrupt-names` | `string-array` | 设备各中断的可选名称；中断本身在 `interrupts` 或 `interrupts-extended` 中定义 |
| `interrupt-parent` | `phandle` | 若存在，引用负责处理此设备所产生中断的节点 |

## 750.6\_标签、时钟与地址单元

**时钟提供者（Clock Provider）**提供设备使用的时钟。下表同时保留标签和子节点地址编码相关属性。

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `label` | `string` | 描述设备的可读字符串；除逐案确有需要外，已不推荐使用此属性。参见规范 v0.4 第 4.1.2 节“其他属性” |
| `clocks` | `phandle-array` | 设备的时钟提供者信息，通常应遵守下述 dt-schema 时钟绑定约定 |
| `clock-names` | `string-array` | `clocks` 中各时钟提供者的可选名称 |
| `#address-cells` | `int` | 子节点 `reg` 地址字段所用的 `<u32>` 单元数量 |
| `#size-cells` | `int` | 子节点 `reg` 大小字段所用的 `<u32>` 单元数量 |

`<u32>` 是 32 位无符号单元，两个 cells 属性见规范 v0.4 第 2.3.5 节。时钟约定见 [dt-schema 的 clock.yaml](https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml)。`status`、`compatible`、`reg`、`interrupts` 和 `label` 另见官方[重要属性（Important Properties）](https://docs.zephyrproject.org/latest/build/dts/intro-syntax-structure.html#dt-important-props)。

## 750.7\_DMA、输入输出与邮箱通道

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

## 750.8\_电源域与硬件锁

**电源域（Power Domain）**描述设备所属供电域；**硬件自旋锁（Hardware Spinlock）**为硬件提供的锁资源。属性如下：

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `power-domains` | `phandle-array` | 与设备相关的电源域说明符 |
| `power-domain-names` | `string-array` | `power-domains` 中各电源域说明符的可选名称 |
| `#power-domain-cells` | `int` | `power-domains` 属性中的单元数量 |
| `hwlocks` | `phandle-array` | 与设备相关的硬件自旋锁标识 |
| `hwlock-names` | `string-array` | `hwlocks` 中各锁说明符的可选名称 |

## 750.9\_初始化、唤醒和运行时电源管理

`zephyr,deferred-init` 为 `boolean` 属性：启动时不自动初始化设备，应使用 `device_init()` 手动初始化。

`wakeup-source` 为 `boolean` 属性，标识设备可以作为**唤醒源（Wakeup Source）**。提供它后，设备会设置一个专门标志，告知系统该设备具备唤醒系统的能力。这类设备的唤醒功能默认禁用，即其中断不会唤醒系统，必要时可在运行期间启用。

`zephyr,pm-device-runtime-auto` 为 `boolean` 属性，在初始化函数执行后自动为设备配置**运行时电源管理（Runtime Power Management）**。

`zephyr,disabling-power-states` 的类型为 `phandles`，列出会关闭此设备电源的电源状态。

---

[上一章：RenesasRA高速模拟比较器绑定](P749_RenesasRA高速模拟比较器绑定.md) · [下一章：RenesasRX电压检测器绑定](P751_RenesasRX电压检测器绑定.md) · [返回大纲](大纲.md)
