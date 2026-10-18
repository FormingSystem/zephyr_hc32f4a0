---
id: learning.zephyr-docs.spi-adi-atmel-esp-binding-reference.page-19
title: intel_penwell-spi
kind: reference
status: maintained
domains: [zephyr, devicetree, spi]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/spi/intel,penwell-spi.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第19章\_intel_penwell-spi

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/spi/intel,penwell-spi.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="intel-penwell-spi"></a>
<a id="dtbinding-intel-penwell-spi"></a>
<a id="std-dtcompatible-intel-penwell-spi"></a>

兼容字符串（Compatible String）：`intel,penwell-spi`。厂商：[ Intel ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-intel)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=intel,penwell-spi)。

驱动源码（Driver Source）：[drivers/spi/spi_pw.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/spi_pw.c)。

<a id="description"></a>

Intel Penwell SPI。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 19.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `cs-gpios` | `phandle-array` | **必需**。使用的片选GPIO数组（Chip Select GPIO Array）。每个元素指定一个GPIO，数组索引对应此片选GPIO控制的子节点。下方保留完整设备树示例。<br>原例中`spi-device@0`使用控制器`gpio0`的23号引脚，设备树GPIO标志为`GPIO_ACTIVE_LOW`；`spi-device@1`使用`gpio1`的10号引脚，同样为`GPIO_ACTIVE_LOW`。其他设备可按同样方式配置。<br>不确定标志单元时，对通常的低有效`CSn`引脚，一般可选择`GPIO_ACTIVE_LOW`。若中间硬件反转到外设的信号，或该线本身高有效，则可用`GPIO_ACTIVE_HIGH`。<br>未定义本属性时，不设置片选GPIO；具有专用CS引脚的SPI控制器无需定义`cs-gpios`。 |
| `pw,cs-mode` | `int` | **必需**。片选配置：0为硬件（Hardware），1为软件（Software），2为GPIO。 |
| `pw,cs-output` | `int` | **必需**。使用GSPI片选CS0或CS1；GSPI实例0、1、2均支持两种片选，可通过此DTS属性选择，默认CS0。输出取值：0为CS0，1为CS1。 |
| `pw,fifo-depth` | `int` | **必需**。带有内置发送及接收FIFO的SPI控制器。 |
| `clock-frequency` | `int` | 驱动SPI外设的时钟频率，单位为Hz。 |
| `overrun-character` | `int` | 当发送缓冲区（TX Buffer）的全部字节已发完，但因为仍需接收（RX）而继续传输时，使用溢出字符（Overrun Character，ORC）。 |
| `vendor-id` | `int` | 设备的厂商标识（Vendor ID）。 |
| `device-id` | `int` | 设备标识（Device ID）。 |
| `class-rev` | `int` | 可选的类别／修订版寄存器过滤器（Class/Revision Register Filter）。 |
| `class-rev-mask` | `int` | 类别／修订版寄存器掩码（Mask）。 |

本页没有已弃用的节点专用属性。

## 19.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `interrupts` | `array` | **必需**。设备产生的中断，编码为一个或多个中断说明符；格式由设备在中断树中的位置决定，具有相同 `interrupt-parent` 的设备使用相同格式；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `#address-cells` | `int` | **必需**。子节点 `reg` 地址字段所用的 `<u32>` 单元数量；`<u32>` 为32位无符号单元，参见《设备树规范》v0.4第2.3.5节；固定值：`1` |
| `#size-cells` | `int` | **必需**。子节点 `reg` 大小字段所用的 `<u32>` 单元数量；`<u32>` 为32位无符号单元，参见《设备树规范》v0.4第2.3.5节；固定值：`0` |
| `status` | `string` | 节点代表的硬件或其他资源的运行状态（Operational Status）。`okay` 表示资源可运行，例如可供驱动使用；`disabled` 表示资源不可运行，系统应将其视为不存在。参见《设备树规范》（Devicetree Specification）v0.4第2.3.4节；合法值：`okay, disabled, reserved, fail, fail-sss` |
| `compatible` | `string-array` | **必需**。字符串列表定义节点代表的硬件或其他资源类型。设备驱动通过特定兼容字符串（Compatible String）寻找应由自身管理的设备。推荐格式为 `vendor,device`：前者是厂商简称，后者通常来自数据手册。多个值从最具体到最通用排列，让具体设备匹配当前可用的最具体驱动。参见规范v0.4第2.3.1节 |
| `reg` | `array` | 给出寻址设备所需的信息，具体含义随设备及 `compatible` 而变化。通常是一组地址与长度对，每对称为寄存器块（Register Block），数值通常写为十六进制。参见规范v0.4第2.3.6节及[重要属性](../devicetree/P003_语法与结构.md#dt-important-props) |
| `reg-names` | `string-array` | 为 `reg` 中每个寄存器块提供可选名称；原始例子及逐项说明见本层表后 |
| `ranges` | `compound` | 定义总线子地址空间与总线节点父地址空间之间的映射或转换。通常为空，或由子总线地址、父总线地址、长度三元组组成。**空属性表示两侧地址空间相同、不需要转换；总线节点没有此属性则认为子、父地址空间之间不存在映射**。参见规范v0.4第2.3.8节 |
| `interrupts-extended` | `compound` | 扩展中断说明符，可替代 `interrupts`；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `interrupt-names` | `string-array` | 设备各中断的可选名称；中断本身在 `interrupts` 或 `interrupts-extended` 中定义；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `interrupt-parent` | `phandle` | 若存在，引用负责处理此设备所产生中断的节点；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `label` | `string` | 描述设备的可读字符串；除逐案确有需要外，已不推荐使用此属性。参见规范 v0.4 第 4.1.2 节“其他属性” |
| `clocks` | `phandle-array` | 设备的时钟提供者（Clock Provider）信息，通常应遵守[dt-schema时钟绑定约定](https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml) |
| `clock-names` | `string-array` | `clocks` 中各时钟提供者的名称；通用说明称其为可选名称，是否必须填写以本层的必需标记为准 |
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

## 片选GPIO数组原例

```dts
  spi@... {
          cs-gpios = <&gpio0 23 GPIO_ACTIVE_LOW>,
                        <&gpio1 10 GPIO_ACTIVE_LOW>,
                        ...;

          spi-device@0 {
                  reg = <0>;
                  ...
          };
          spi-device@1 {
                  reg = <1>;
                  ...
          };
          ...
  };
```

## 19.3\_寄存器块命名原例

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

[上一章](P018_infineon_xmc4xxx-spi.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P020_intel_sedi-spi.md)
