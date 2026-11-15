---
id: learning.zephyr-docs.hardware.comprennrf-1
title: RenesasRA高速模拟比较器绑定
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/comparator/renesas,ra-acmphs.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第749章\_RenesasRA高速模拟比较器绑定

<a id="dtbinding-renesas-ra-acmphs"></a>

原文：[renesas,ra-acmphs](https://docs.zephyrproject.org/latest/build/dts/api/bindings/comparator/renesas,ra-acmphs.html)。读取日期：2026-10-13，`latest`。

`renesas,ra-acmphs` 是设备树绑定（Devicetree Binding），描述Renesas RA高速模拟比较器（High-Speed Analog Comparator，ACMPHS）控制器（Controller）。其全局父节点见[ACMPHS全局绑定](P748_RenesasRA高速模拟比较器全局绑定.md)。

驱动为 [`drivers/comparator/comparator_renesas_ra.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/comparator/comparator_renesas_ra.c)。

使用此兼容字符串的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=renesas,ra-acmphs)。

## 749.1\_节点布局与使能示例

以下保留官方设备树源码（Devicetree Source，DTS）示例。原代码中的地址、引脚及中断配置须结合具体芯片；带 `...` 的部分是原文省略内容。

最小节点布局：

```dts
  acmphs_global: acmphs_global@deadbeef {
          ...

          acmphs0: acmphs0 {
                  compatible = "renesas,ra-acmphs";
                  channel = <0>;
                  status = "disabled";
          };
  };
```

使能控制器需要最小默认配置，包括选择正、负输入并通过pinctrl路由。支持比较器的开发板已为默认控制器定义一组pinctrl，重新定义前应先检查。CH0表示通道0（Channel 0）。IVREF0为参考输入标识，IVCMP0为比较输入标识，`RA_PSEL` 与 `RA_PSEL_ACMPHS` 分别为引脚选择宏和比较器引脚功能标识。

```dts
&pinctrl {
        acmphs_ivref0: acmphs_ivref0 {
                group1 {
                        /* IVREF0 */
                        psels = <RA_PSEL(RA_PSEL_ACMPHS, ..., ...)>;
                        renesas,analog-enable;
                };
        };

        acmphs0_ivcmp0: acmphs0_ivcmp0 {
                group1 {
                        /* CH0 IVCMP0 */
                        psels = <RA_PSEL(RA_PSEL_ACMPHS, ..., ...)>;
                        renesas,analog-enable;
                };
        };
};

&acmphs_global {
        status = "okay";

        acmphs0 {
                pinctrl-0 = <&acmphs_ivref0 &acmphs0_ivcmp0>;
                pinctrl-names = "default";
                interrupts = <90 12>;
                interrupt-names = "hs";
                reference-input-source = "ivref0";
                compare-input-source = "ivcmp0";
                status = "okay";
        };
};
```

## 749.2\_节点专用属性

`int` 为整数，`string` 为字符串，`boolean` 为布尔属性，`phandles` 为节点引用（Phandle）列表，`string-array` 为字符串数组。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `channel` | `int` | **必需**。通道（Channel）编号；原页只标明类型与必需性，没有额外文字说明 |
| `reference-input-source` | `string` | **必需**。模拟参考电压源（Analog Reference Voltage Source）选择。`ivref2` 连接参考电压Vref，`ivref3` 连接数模转换器（Digital-to-Analog Converter，DAC）的DA0输出；选择这两者之一时，无须在pinctrl中配置引脚选择（Pin Selection，pinsel）；合法值：`ivref0, ivref1, ivref2, ivref3` |
| `compare-input-source` | `string` | **必需**。模拟比较电压源（Analog Compare Voltage Source）选择。`ivcmp1` 连接DAC的DA0输出，选择它时无须在pinctrl中配置pinsel；合法值：`ivcmp0, ivcmp1, ivcmp2, ivcmp3` |
| `noise-filter` | `int` | 硬件数字去抖滤波器（Digital Debounce Filter）的外设时钟（Peripheral Clock，PCLK）分频因子；因子越大，去抖时间越长，输出更新也越慢；默认值：`32`；合法值：`1, 8, 16, 32` |
| `output-invert-polarity` | `boolean` | 启用后将比较器输出反相（Invert） |
| `pin-output-enable` | `boolean` | 启用本通道的CMPOUTn输出信号；各通道CMPOUTn进行逻辑或（Logical OR），结果输出至共享的VCOUT引脚 |
| `pinctrl-0` | `phandles` | 第一个引脚控制（Pin Control）状态的配置引用；具体内容由选用的引脚控制器驱动实现决定 |
| `pinctrl-1` | `phandles` | 第二个引脚控制（Pin Control）状态的配置引用；具体内容由选用的引脚控制器驱动实现决定，参见 `pinctrl-0` |
| `pinctrl-2` | `phandles` | 第三个引脚控制（Pin Control）状态的配置引用；具体内容由选用的引脚控制器驱动实现决定，参见 `pinctrl-0` |
| `pinctrl-3` | `phandles` | 第四个引脚控制（Pin Control）状态的配置引用；具体内容由选用的引脚控制器驱动实现决定，参见 `pinctrl-0` |
| `pinctrl-4` | `phandles` | 第五个引脚控制（Pin Control）状态的配置引用；具体内容由选用的引脚控制器驱动实现决定，参见 `pinctrl-0` |
| `pinctrl-names` | `string-array` | 已提供的引脚状态名称；名称数量必须与状态数量一致 |

## 749.3\_比较结果中断

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `interrupts` | `array` | 比较器中断请求（Interrupt Request，IRQ）的编号与优先级。`hs` 表示由比较结果检测到有效边沿时产生的中断。**没有定义此属性时，不能使用任何触发应用程序接口（Application Programming Interface，API）**，包括 `set_trigger`、`set_trigger_callback` 和 `trigger_is_pending` |

没有已弃用的节点专用属性。以下保留继承的基础属性，不保证全部适用于本绑定；`compatible` 为必需属性。

## 749.4\_状态、兼容字符串与寄存器

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

## 749.5\_地址映射与中断

`ranges` 的类型为 `compound`，定义总线子地址空间与总线节点父地址空间之间的映射或转换。它通常为空，或由“子总线地址、父总线地址、长度”三元组构成。**空属性表示两侧地址空间相同，不需要转换；总线节点没有此属性时，则认为子节点与父地址空间之间不存在映射。**详见规范 v0.4 第 2.3.8 节。

下列属性描述**中断（Interrupt）**，参见规范 v0.4 第 2.4 节“中断与中断映射”。

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `interrupts-extended` | `compound` | 扩展中断说明符，可替代 `interrupts` |
| `interrupt-names` | `string-array` | 设备各中断的可选名称；中断本身在 `interrupts` 或 `interrupts-extended` 中定义 |
| `interrupt-parent` | `phandle` | 若存在，引用负责处理此设备所产生中断的节点 |

## 749.6\_标签、时钟与地址单元

**时钟提供者（Clock Provider）**提供设备使用的时钟。下表同时保留标签和子节点地址编码相关属性。

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `label` | `string` | 描述设备的可读字符串；除逐案确有需要外，已不推荐使用此属性。参见规范 v0.4 第 4.1.2 节“其他属性” |
| `clocks` | `phandle-array` | 设备的时钟提供者信息，通常应遵守下述 dt-schema 时钟绑定约定 |
| `clock-names` | `string-array` | `clocks` 中各时钟提供者的可选名称 |
| `#address-cells` | `int` | 子节点 `reg` 地址字段所用的 `<u32>` 单元数量 |
| `#size-cells` | `int` | 子节点 `reg` 大小字段所用的 `<u32>` 单元数量 |

`<u32>` 是 32 位无符号单元，两个 cells 属性见规范 v0.4 第 2.3.5 节。时钟约定见 [dt-schema 的 clock.yaml](https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml)。`status`、`compatible`、`reg`、`interrupts` 和 `label` 另见官方[重要属性（Important Properties）](https://docs.zephyrproject.org/latest/build/dts/intro-syntax-structure.html#dt-important-props)。

## 749.7\_DMA、输入输出与邮箱通道

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

## 749.8\_电源域与硬件锁

**电源域（Power Domain）**描述设备所属供电域；**硬件自旋锁（Hardware Spinlock）**为硬件提供的锁资源。属性如下：

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `power-domains` | `phandle-array` | 与设备相关的电源域说明符 |
| `power-domain-names` | `string-array` | `power-domains` 中各电源域说明符的可选名称 |
| `#power-domain-cells` | `int` | `power-domains` 属性中的单元数量 |
| `hwlocks` | `phandle-array` | 与设备相关的硬件自旋锁标识 |
| `hwlock-names` | `string-array` | `hwlocks` 中各锁说明符的可选名称 |

## 749.9\_初始化、唤醒和运行时电源管理

`zephyr,deferred-init` 为 `boolean` 属性：启动时不自动初始化设备，应使用 `device_init()` 手动初始化。

`wakeup-source` 为 `boolean` 属性，标识设备可以作为**唤醒源（Wakeup Source）**。提供它后，设备会设置一个专门标志，告知系统该设备具备唤醒系统的能力。这类设备的唤醒功能默认禁用，即其中断不会唤醒系统，必要时可在运行期间启用。

`zephyr,pm-device-runtime-auto` 为 `boolean` 属性，在初始化函数执行后自动为设备配置**运行时电源管理（Runtime Power Management）**。

`zephyr,disabling-power-states` 的类型为 `phandles`，列出会关闭此设备电源的电源状态。

---

[上一章：RenesasRA高速模拟比较器全局绑定](P748_RenesasRA高速模拟比较器全局绑定.md) · [下一章：RenesasRA电压检测器绑定](P750_RenesasRA电压检测器绑定.md) · [返回大纲](大纲.md)
