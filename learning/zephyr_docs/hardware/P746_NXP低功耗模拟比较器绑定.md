---
id: learning.zephyr-docs.hardware.compnxp-4
title: NXP低功耗模拟比较器绑定
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/comparator/nxp,lpacmp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第746章\_NXP低功耗模拟比较器绑定

<a id="dtbinding-nxp-lpacmp"></a>

原文：[nxp,lpacmp](https://docs.zephyrproject.org/latest/build/dts/api/bindings/comparator/nxp,lpacmp.html)。读取日期：2026-10-13，`latest`。

`nxp,lpacmp` 是NXP Semiconductors的设备树绑定（Devicetree Binding），描述低功耗模拟比较器（Low-Power Analog Comparator，LPACMP）。

驱动为 [`drivers/comparator/comparator_nxp_lpacmp.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/comparator/comparator_nxp_lpacmp.c)。

使用此兼容字符串的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=nxp,lpacmp)。

## 746.1\_节点专用属性

`int` 为整数，`string` 为字符串，`boolean` 为布尔属性，`phandles` 为节点引用（Phandle）列表，`phandle-array` 为节点引用与说明单元数组，`string-array` 为字符串数组。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `positive-input` | `string` | **必需**。通道0正输入选择，对应 `SEL0[INP_SEL]`。枚举按寄存器编码排列，**不能按输入编号排序**：硬件编码0对应 `comp_in4`，1对应 `comp_in5`，随后才是 `comp_in0` 至 `comp_in3`。驱动把枚举索引直接写入该字段，必须保持所列顺序；合法值：`comp_in4, comp_in5, comp_in0, comp_in1, comp_in2, comp_in3` |
| `negative-input` | `int` | **必需**。通道0负（参考）输入选择，对应 `SEL0[INN_SEL]`。数值0至13选择内部参考电压 `(value + 1) × AVDD / 15`，其中AVDD为模拟电源电压（Analog Supply Voltage）；14选择外部输入 `comp_in4`，15选择外部输入 `comp_in5`；范围：`0 to 15` |
| `sample-delay` | `int` | 通道0采样延迟计数器（Sample Delay Counter）值，对应 `DELAY0[DEL]`，以常开时钟（Always-On Clock，AON_CLK）周期为单位。计数器每次到0时采样比较器输出，所以该值决定采样周期，必须留出足够输出稳定时间。默认值等于寄存器复位值；本驱动使用的连续模式（Continuous Mode）使比较器始终上电，因而每个AON_CLK周期采样也可以工作，但非零值能增加采样之间的稳定裕量（Settling Margin）；默认值：`0`；范围：`0 to 65535` |

## 746.2\_采样时钟与条件必需的门控时钟

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `clocks` | `phandle-array` | **必需**。第0项为必需的采样计数器AON时钟，必须解析到带有 `clock-frequency` 属性的节点；驱动读取该频率，计算新样本所需时间，每次重新采样输出时等待这么久。第1项为经系统控制器（System Controller，syscon）访问的外设时钟门（Peripheral Clock Gate），一般可选；若片上系统（System on Chip，SoC）对该模块实施门控，就必须提供，否则模块内所有寄存器都不响应。例如MCXL255的CGU `PER_CLK_EN[COMP_CLK_EN]` 时钟门复位时禁用，CGU为原始时钟生成单元标识。模块没有独立时钟门时应省略第1项 |
| `clock-names` | `string-array` | 为提高可读性而提供的可选时钟项名称；提供时，采样时钟使用 `aon-clk`，外设时钟门使用 `gate`。驱动按索引访问两项，名称仅作说明 |

没有已弃用的节点专用属性。以下保留继承的基础属性，不保证全部适用于本绑定；`reg`、`interrupts`、`compatible` 为必需属性。

## 746.3\_状态、兼容字符串与寄存器

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

## 746.4\_地址映射与中断

`ranges` 的类型为 `compound`，定义总线子地址空间与总线节点父地址空间之间的映射或转换。它通常为空，或由“子总线地址、父总线地址、长度”三元组构成。**空属性表示两侧地址空间相同，不需要转换；总线节点没有此属性时，则认为子节点与父地址空间之间不存在映射。**详见规范 v0.4 第 2.3.8 节。

下列属性描述**中断（Interrupt）**，参见规范 v0.4 第 2.4 节“中断与中断映射”。

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `interrupts` | `array` | **必需**。设备产生的中断，编码为一个或多个中断说明符；格式由设备在中断树中的位置决定，具有相同 `interrupt-parent` 的设备使用相同格式 |
| `interrupts-extended` | `compound` | 扩展中断说明符，可替代 `interrupts` |
| `interrupt-names` | `string-array` | 设备各中断的可选名称；中断本身在 `interrupts` 或 `interrupts-extended` 中定义 |
| `interrupt-parent` | `phandle` | 若存在，引用负责处理此设备所产生中断的节点 |

## 746.5\_标签、时钟与地址单元

**时钟提供者（Clock Provider）**提供设备使用的时钟。下表同时保留标签和子节点地址编码相关属性。

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `label` | `string` | 描述设备的可读字符串；除逐案确有需要外，已不推荐使用此属性。参见规范 v0.4 第 4.1.2 节“其他属性” |
| `#address-cells` | `int` | 子节点 `reg` 地址字段所用的 `<u32>` 单元数量 |
| `#size-cells` | `int` | 子节点 `reg` 大小字段所用的 `<u32>` 单元数量 |

`<u32>` 是 32 位无符号单元，两个 cells 属性见规范 v0.4 第 2.3.5 节。时钟约定见 [dt-schema 的 clock.yaml](https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml)。`status`、`compatible`、`reg`、`interrupts` 和 `label` 另见官方[重要属性（Important Properties）](https://docs.zephyrproject.org/latest/build/dts/intro-syntax-structure.html#dt-important-props)。

## 746.6\_DMA、输入输出与邮箱通道

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

## 746.7\_电源域与硬件锁

**电源域（Power Domain）**描述设备所属供电域；**硬件自旋锁（Hardware Spinlock）**为硬件提供的锁资源。属性如下：

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `power-domains` | `phandle-array` | 与设备相关的电源域说明符 |
| `power-domain-names` | `string-array` | `power-domains` 中各电源域说明符的可选名称 |
| `#power-domain-cells` | `int` | `power-domains` 属性中的单元数量 |
| `hwlocks` | `phandle-array` | 与设备相关的硬件自旋锁标识 |
| `hwlock-names` | `string-array` | `hwlocks` 中各锁说明符的可选名称 |

## 746.8\_初始化、唤醒和运行时电源管理

`zephyr,deferred-init` 为 `boolean` 属性：启动时不自动初始化设备，应使用 `device_init()` 手动初始化。

`wakeup-source` 为 `boolean` 属性，标识设备可以作为**唤醒源（Wakeup Source）**。提供它后，设备会设置一个专门标志，告知系统该设备具备唤醒系统的能力。这类设备的唤醒功能默认禁用，即其中断不会唤醒系统，必要时可在运行期间启用。

`zephyr,pm-device-runtime-auto` 为 `boolean` 属性，在初始化函数执行后自动为设备配置**运行时电源管理（Runtime Power Management）**。

`zephyr,disabling-power-states` 的类型为 `phandles`，列出会关闭此设备电源的电源状态。

---

[上一章：NXPKinetis模拟比较器绑定](P745_NXPKinetis模拟比较器绑定.md) · [下一章：NXP低功耗比较器绑定](P747_NXP低功耗比较器绑定.md) · [返回大纲](大纲.md)
