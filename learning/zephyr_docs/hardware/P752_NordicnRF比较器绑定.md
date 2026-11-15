---
id: learning.zephyr-docs.hardware.comprennrf-4
title: NordicnRF比较器绑定
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/comparator/nordic,nrf-comp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第752章\_NordicnRF比较器绑定

<a id="dtbinding-nordic-nrf-comp"></a>

原文：[nordic,nrf-comp](https://docs.zephyrproject.org/latest/build/dts/api/bindings/comparator/nordic,nrf-comp.html)。读取日期：2026-10-13，`latest`。

`nordic,nrf-comp` 是设备树绑定（Devicetree Binding），描述Nordic nRF模拟比较器（Analog Comparator，COMP）。不同配置需要在设备树中设置不同属性；使能节点时，必须设置比较器的默认配置。

驱动为 [`drivers/comparator/comparator_nrf_comp.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/comparator/comparator_nrf_comp.c)。

使用此兼容字符串的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=nordic,nrf-comp)。

## 752.1\_节点布局与使能示例

以下保留官方设备树源码（Devicetree Source，DTS）示例。原代码中的地址、引脚及中断配置须结合具体芯片；带 `...` 的部分是原文省略内容。

`NRF_DEFAULT_IRQ_PRIORITY` 是默认中断请求（Interrupt Request，IRQ）优先级宏，`NRF_COMP_AIN0` 和 `NRF_COMP_AIN1` 是模拟输入（Analog Input，AIN）选择常量。`0xdeadbeef` 是原例占位地址。

最小节点布局：

```dts
/*
 * The following example displays the minimum node layout:
 */
comp: comp@deadbeef {
        compatible = "nordic,nrf-comp";
        reg = <0xdeadbeef 0x1000>;
        interrupts = <0 NRF_DEFAULT_IRQ_PRIORITY>;
        status = "disabled";
};
```

单端（Single-Ended，SE）模式，选择内部参考（Internal Reference）`INT_1V2`，使用正常模式NORMAL并关闭电流源DISABLED：

```dts
/*
 * The following example displays enabling the comparator in
 * single-ended mode, selecting an internal reference:
 */
&comp {
        status = "okay";
        main-mode = "SE";
        psel = <NRF_COMP_AIN0>;
        refsel = "INT_1V2";
        sp-mode = "NORMAL";
        th-up = <36>;
        th-down = <30>;
        isource = "DISABLED";
};
```

选择外部参考（External Reference）时，`refsel` 设为 `AREF`，同时提供 `extrefsel`：

```dts
/*
 * To select an external reference, select the "AREF"
 * reference and add the external reference:
 */
&comp {
        ...
        refsel = "AREF";
        extrefsel = <NRF_COMP_AIN1>;
        ...
};
```

差分（Differential，DIFF）模式，使用两个模拟输入并启用迟滞（Hysteresis）：

```dts
/*
 * The following example displays enabling the comparator
 * in differential mode:
 */
&comp {
        status = "okay";
        main-mode = "DIFF";
        psel = <NRF_COMP_AIN0>;
        extrefsel = <NRF_COMP_AIN1>;
        sp-mode = "NORMAL";
        enable-hyst;
        isource = "DISABLED";
};
```

原页的节点专用属性大多只列类型或枚举，没有逐项文字说明。下面仅补充名称释义及示例中能够确认的用途，不把示例数值当作默认值，也不补写未声明的范围或电气参数。

## 752.2\_节点专用属性

`int` 为整数，`string` 为字符串，`boolean` 为布尔属性，`phandles` 为节点引用（Phandle）列表，`string-array` 为字符串数组。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `main-mode` | `string` | 主工作模式（Main Mode），原页未给出单独说明；原示例中 `SE` 为单端（Single-Ended）模式，`DIFF` 为差分（Differential）模式；合法值：`SE, DIFF` |
| `psel` | `int` | 输入选择（Input Selection）配置；原页未给出单独说明，原示例使用 `NRF_COMP_AIN0` 输入常量 |
| `extrefsel` | `int` | 外部参考选择（External Reference Selection）配置；原页未给出单独说明，原示例使用 `NRF_COMP_AIN1` 作为外部参考输入常量 |
| `refsel` | `string` | 参考源选择（Reference Selection）；原页只列举合法值，原示例以 `AREF` 选择外部参考，并同时提供 `extrefsel`；合法值：`INT_1V2, INT_1V8, INT_2V4, AVDDAO1V8, VDD, AREF` |
| `enable-hyst` | `boolean` | 启用迟滞（Hysteresis）；原页未提供迟滞电压或其他独立说明 |
| `sp-mode` | `string` | 原始速度／功耗模式（Speed/Power Mode）选择标识；原页只列举LOW、NORMAL、HIGH，没有给出电流或响应时间参数；合法值：`LOW, NORMAL, HIGH` |
| `th-up` | `int` | 上阈值（Upper Threshold）配置；原页无独立说明，原例设置为36，不能将此例值视为默认值或电压单位 |
| `th-down` | `int` | 下阈值（Lower Threshold）配置；原页无独立说明，原例设置为30，不能将此例值视为默认值或电压单位 |
| `isource` | `string` | 电流源（Current Source）选择；原页只给出DISABLED、2UA5、5UA、10UA标识，保留其原始拼写，不补充未声明的硬件约束；合法值：`DISABLED, 2UA5, 5UA, 10UA` |

没有已弃用的节点专用属性。以下保留继承的基础属性，不保证全部适用于本绑定；`compatible` 为必需属性。

## 752.3\_状态、兼容字符串与寄存器

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

## 752.4\_地址映射与中断

`ranges` 的类型为 `compound`，定义总线子地址空间与总线节点父地址空间之间的映射或转换。它通常为空，或由“子总线地址、父总线地址、长度”三元组构成。**空属性表示两侧地址空间相同，不需要转换；总线节点没有此属性时，则认为子节点与父地址空间之间不存在映射。**详见规范 v0.4 第 2.3.8 节。

下列属性描述**中断（Interrupt）**，参见规范 v0.4 第 2.4 节“中断与中断映射”。

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `interrupts` | `array` | 设备产生的中断，编码为一个或多个中断说明符；格式由设备在中断树中的位置决定，具有相同 `interrupt-parent` 的设备使用相同格式 |
| `interrupts-extended` | `compound` | 扩展中断说明符，可替代 `interrupts` |
| `interrupt-names` | `string-array` | 设备各中断的可选名称；中断本身在 `interrupts` 或 `interrupts-extended` 中定义 |
| `interrupt-parent` | `phandle` | 若存在，引用负责处理此设备所产生中断的节点 |

## 752.5\_标签、时钟与地址单元

**时钟提供者（Clock Provider）**提供设备使用的时钟。下表同时保留标签和子节点地址编码相关属性。

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `label` | `string` | 描述设备的可读字符串；除逐案确有需要外，已不推荐使用此属性。参见规范 v0.4 第 4.1.2 节“其他属性” |
| `clocks` | `phandle-array` | 设备的时钟提供者信息，通常应遵守下述 dt-schema 时钟绑定约定 |
| `clock-names` | `string-array` | `clocks` 中各时钟提供者的可选名称 |
| `#address-cells` | `int` | 子节点 `reg` 地址字段所用的 `<u32>` 单元数量 |
| `#size-cells` | `int` | 子节点 `reg` 大小字段所用的 `<u32>` 单元数量 |

`<u32>` 是 32 位无符号单元，两个 cells 属性见规范 v0.4 第 2.3.5 节。时钟约定见 [dt-schema 的 clock.yaml](https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml)。`status`、`compatible`、`reg`、`interrupts` 和 `label` 另见官方[重要属性（Important Properties）](https://docs.zephyrproject.org/latest/build/dts/intro-syntax-structure.html#dt-important-props)。

## 752.6\_DMA、输入输出与邮箱通道

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

## 752.7\_电源域与硬件锁

**电源域（Power Domain）**描述设备所属供电域；**硬件自旋锁（Hardware Spinlock）**为硬件提供的锁资源。属性如下：

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `power-domains` | `phandle-array` | 与设备相关的电源域说明符 |
| `power-domain-names` | `string-array` | `power-domains` 中各电源域说明符的可选名称 |
| `#power-domain-cells` | `int` | `power-domains` 属性中的单元数量 |
| `hwlocks` | `phandle-array` | 与设备相关的硬件自旋锁标识 |
| `hwlock-names` | `string-array` | `hwlocks` 中各锁说明符的可选名称 |

## 752.8\_初始化、唤醒和运行时电源管理

`zephyr,deferred-init` 为 `boolean` 属性：启动时不自动初始化设备，应使用 `device_init()` 手动初始化。

`wakeup-source` 为 `boolean` 属性，标识设备可以作为**唤醒源（Wakeup Source）**。提供它后，设备会设置一个专门标志，告知系统该设备具备唤醒系统的能力。这类设备的唤醒功能默认禁用，即其中断不会唤醒系统，必要时可在运行期间启用。

`zephyr,pm-device-runtime-auto` 为 `boolean` 属性，在初始化函数执行后自动为设备配置**运行时电源管理（Runtime Power Management）**。

`zephyr,disabling-power-states` 的类型为 `phandles`，列出会关闭此设备电源的电源状态。

---

[上一章：RenesasRX电压检测器绑定](P751_RenesasRX电压检测器绑定.md) · [下一章：NordicnRF低功耗比较器绑定](P753_NordicnRF低功耗比较器绑定.md) · [返回大纲](大纲.md)
