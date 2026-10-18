---
id: learning.zephyr-docs.sensor-bosch-broadcom-espressif-binding-reference.page-30
title: espressif_esp32-pcnt
kind: reference
status: maintained
domains: [zephyr, devicetree, sensor]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/sensor/espressif,esp32-pcnt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第30章\_espressif_esp32-pcnt

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/sensor/espressif,esp32-pcnt.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="espressif-esp32-pcnt"></a>
<a id="dtbinding-espressif-esp32-pcnt"></a>
<a id="std-dtcompatible-espressif-esp32-pcnt"></a>

兼容字符串（Compatible String）：`espressif,esp32-pcnt`。厂商：[ Espressif Systems ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-espressif)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=espressif,esp32-pcnt)。

驱动源码（Driver Source）：[drivers/sensor/espressif/pcnt_esp32/pcnt_esp32.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/espressif/pcnt_esp32/pcnt_esp32.c)。

<a id="description"></a>

ESP32 脉冲计数器（Pulse Counter，PCNT）。

该模块统计输入信号上升沿和／或下降沿的数量。原始 ESP32 有 8 个独立计数单元（0 至 7）；ESP32-S2、ESP32-S3、ESP32-C5、ESP32-C6、ESP32-H2 和 ESP32-P4 各有 4 个（0 至 3）。

每个单元具有一个 16 位有符号计数寄存器和两个独立通道 `ch0`、`ch1`，通道可配置为递增或递减计数。每个通道包含接受待检测信号边沿的信号输入（Signal Input），以及可启用或禁用信号输入的控制输入（Control Input）。

每个计数单元的四个输入各有一个滤波器（Filter），可忽略短毛刺（Glitch）。结合信号输入与控制输入，PCNT 单元可以充当正交解码器（Quadrature Decoder）。

信号输入、控制输入与物理引脚之间通过引脚控制（Pinctrl）映射；完整说明见 `espressif,esp32-pinctrl.yaml`。后文原例使用 PCNT 读取旋转编码器（Rotary Encoder）。

<a id="examples"></a>

官方设备树配置原例：

```dts
/* Use PCNT to read a rotary-encoder */
&pinctrl {
    pcnt_default: pcnt_default {
        group1 {
            pinmux = <PCNT0_CH0SIG_GPIO14>,
                    <PCNT0_CH0CTRL_GPIO15>;
            bias-pull-up;
        };
    };
};
&pcnt {
  pinctrl-0 = <&pcnt_default>;
  pinctrl-names = "default";
  status = "okay";
  #address-cells = <1>;
  #size-cells = <0>;
  unit0@0 {
    reg = <0>;
    #address-cells = <1>;
    #size-cells = <0>;
    filter = <100>;
    channelA@0 {
        reg = <0>;
        sig-pos-mode = <2>;
        sig-neg-mode = <1>;
        ctrl-h-mode = <0>;
        ctrl-l-mode = <1>;
    };
  };
};
```

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

<a id="top-level-properties"></a>

## 30.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `friendly-name` | `string` | 描述传感器的可读字符串，可帮助主机操作系统区分同型号的多个实例，例如笔记本电脑上盖与底座的加速度计。此属性定义于[HID Usage Tables规范](https://usb.org/sites/default/files/hut1_3_0.pdf)第22.5节“通用传感器属性用途”（Generic Sensor Property Usages）。 |
| `pinctrl-0` | `phandles` | 第一个状态（State）的引脚配置（Pin Configuration），具体内容取决于所选引脚控制器驱动（Pin Controller Driver）的实现 |
| `pinctrl-1` | `phandles` | 第二个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-2` | `phandles` | 第三个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-3` | `phandles` | 第四个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-4` | `phandles` | 第五个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-names` | `string-array` | 所提供状态的名称，名称数量必须与状态数量一致 |

本页没有已弃用的节点专用属性。

## 30.2\_基础属性

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
| `reg` | `int` | **必需**。PCNT 单元索引（Unit Index）。ESP32 有 8 个 PCNT 单元，ESP32-S2/S3 有 4 个。；合法值：`0, 1, 2, 3, 4, 5, 6, 7` |
| `filter` | `int` | 毛刺滤波阈值（Glitch Filter Threshold），单位为 APB 时钟周期。典型 APB 时钟为 80 MHz，因此 1 周期为 12.5 ns。短于该值的脉冲被忽略。最大值为 1023，驱动会将更高值钳位到上限；省略或设为 0 可禁用滤波器。 |
| `counts-per-revolution` | `int` | 机械旋转一整圈对应的编码器计数（Encoder Counts）。非零时，`SENSOR_CHAN_ROTATION` 返回角度，范围为 [0, 360)；为零（默认）时返回原始计数（Raw Counts），保留这一旧行为以保持向后兼容。`SENSOR_CHAN_ENCODER_COUNT` 始终返回原始计数。 |
| `high-limit` | `int` | 上限观察点（Upper Watchpoint）。计数器达到该值时，PCNT 硬件自动清零并产生 `HIGH_LIMIT` 事件。数值必须可由 `int16_t` 表示，范围为 -32768 至 32767；省略本属性即禁用上限观察点。 |
| `low-limit` | `int` | 下限观察点（Lower Watchpoint）。计数器达到该值时，PCNT 硬件自动清零并产生 `LOW_LIMIT` 事件。数值必须可由 `int16_t` 表示，范围为 -32768 至 32767；省略本属性即禁用下限观察点。 |
| `zero-cross-event` | `boolean` | 存在本属性时，每次计数器跨越零点，PCNT 硬件都会产生 `ZERO_CROSS` 事件。该事件在此单元的计数器索引 0 上触发阈值触发器（Threshold Trigger）。 |

<a id="grandchild-node-properties"></a>

## 孙节点属性（Grandchild Properties）

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `int` | **必需**。PCNT 通道索引（Channel Index）。；合法值：`0, 1` |
| `sig-pos-mode` | `int` | 定义脉冲输入正向边沿（Positive Edge）的操作：0（默认）禁止计数，计数值保持不变；1 递增计数值；2 递减计数值。；合法值：`0, 1, 2` |
| `sig-neg-mode` | `int` | 定义脉冲输入负向边沿（Negative Edge）的操作：0（默认）禁止计数，计数值保持不变；1 递增计数值；2 递减计数值。；合法值：`0, 1, 2` |
| `ctrl-h-mode` | `int` | 定义控制输入为高电平时的操作：0（默认）不改变计数模式；1 反转计数模式（递增变为递减，递减变为递增）；2 为控制模式，禁止计数，计数值保持不变。；合法值：`0, 1, 2` |
| `ctrl-l-mode` | `int` | 定义控制输入为低电平时的操作：0（默认）不改变计数模式；1 反转计数模式（递增变为递减，递减变为递增）；2 为控制模式，禁止计数，计数值保持不变。；合法值：`0, 1, 2` |

## 30.3\_寄存器块命名原例

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

[上一章](P029_epcos_b57861s0103a039.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md)
