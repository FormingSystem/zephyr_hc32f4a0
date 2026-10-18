---
id: learning.zephyr-docs.audio-pdm-codec-binding-reference.page-15
title: renesas_ra-pdm
kind: reference
status: maintained
domains: [zephyr, devicetree, audio]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/audio/renesas,ra-pdm.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第15章\_renesas_ra-pdm

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/audio/renesas,ra-pdm.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="renesas-ra-pdm"></a>
<a id="dtbinding-renesas-ra-pdm"></a>
<a id="std-dtcompatible-renesas-ra-pdm"></a>

兼容字符串（Compatible String）：`renesas,ra-pdm`。厂商：[ Renesas Electronics Corporation ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-renesas)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=renesas,ra-pdm)。

驱动源码（Driver Source）：[drivers/audio/dmic_renesas_ra_pdm.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/dmic_renesas_ra_pdm.c)。

<a id="description"></a>

Renesas RA脉冲密度调制接口（Pulse Density Modulation Interface，PDM-IF）的一个通道。每通道具有自己的数据引脚、滤波链（Filter Chain）及数据缓冲区，使用独立节点描述。

滤波链依次为：sinc抽取滤波器；去除调制器直流偏置（DC Bias）的高通滤波器（High-pass Filter）；校正sinc通带下垂（Passband Droop）的补偿滤波器；半带低通滤波器（Half-band Low-pass Filter），用于抑制最终抽取会混叠进通带的成分。

下述每项系数默认采用对应寄存器复位值，合起来形成模块的语音频带设置：高通拐点100 Hz、低通拐点7 kHz，适合16 kHz采集。其他采样率需要设计对应的滤波链，硬件手册没有列出这些参数表。通道可在PDM_CLKn上升沿采样自身PDMDATn引脚，或在下降沿采样下一个较低通道的引脚，从而读取共享数据线的两个麦克风。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 15.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `channel` | `int` | **必需**。本节点描述的PDM-IF通道，用于选择其驱动的PDMDATn和PDMCLKn引脚；合法值：`0, 1, 2` |
| `pinctrl-0` | `phandles` | **必需**。第一个状态（State）的引脚配置（Pin Configuration），具体内容取决于所选引脚控制器驱动（Pin Controller Driver）的实现 |
| `pinctrl-names` | `string-array` | **必需**。所提供状态的名称，名称数量必须与状态数量一致 |
| `sinc-filter-order` | `int` | 对1位数据流进行抽取的sinc滤波器阶数（Order）。阶数越高，越能抑制调制器整形噪声（Shaped Noise），但滤波器自身增益会占用更多20位输出范围。默认模式设置寄存器的复位值；默认值：`4`；合法值：`1, 2, 3, 4` |
| `falling-edge` | `boolean` | 在时钟下降沿采样下一较低通道的数据引脚，而非在上升沿采样本通道引脚。选择输入接高的PDM麦克风在下降沿驱动数据线，因此共享数据线的一对麦克风作为本通道及上一较高通道读取；通道0读取通道2的引脚 |
| `lpf-shift` | `int` | 低通滤波器输入的右移位数。较响麦克风本可能使滤波器饱和时，可通过右移牺牲分辨率以换取幅度余量（Headroom）。默认复位值；默认值：`0`；合法值：`0, 1, 2, 3` |
| `compensation-shift` | `int` | 补偿滤波器输入的右移位数，默认复位值；默认值：`0`；合法值：`0, 1, 2, 3` |
| `hpf-shift` | `int` | 高通滤波器输入的右移位数，默认复位值；默认值：`0`；合法值：`0, 1, 2, 3` |
| `hpf-coefficient-s0` | `int` | 高通滤波器s(0)系数，采用16位有符号数据、14位小数格式。复位值使拐点频率为100 Hz；默认值：`0x3f61` |
| `hpf-coefficient-k1` | `int` | 高通滤波器k(1)系数，格式与s(0)相同；默认值：`0x3ec1` |
| `hpf-coefficients-h` | `array` | 高通滤波器的两个h系数，即h(0)与h(1)；默认值：`[0x4000, 0xc000]` |
| `compensation-coefficients` | `array` | 补偿滤波器的11个h系数，用于校平sinc滤波器在通带内留下的下垂；默认值：`[0x1fe8, 0x39, 0x3c, 0x1e56, 0x1dc, 0x6e1, 0x1dc, 0x1e56, 0x3c, 0x39, 0x1fe8]` |
| `lpf-coefficient-h0` | `int` | 半带低通滤波器的中心系数，该滤波器也执行最后的2倍抽取；复位值使拐点为7 kHz；默认值：`0x400` |
| `lpf-coefficients-h1` | `array` | 半带低通滤波器其余20个系数；默认值：`[0x1ff8, 0xa, 0x1ff0, 0x18, 0x1fdc, 0x34, 0x1fb3, 0x76, 0x1f2e, 0x289, 0x289, 0x1f2e, 0x76, 0x1fb3, 0x34, 0x1fdc, 0x18, 0x1ff0, 0xa, 0x1ff8]` |
| `pinctrl-1` | `phandles` | 第二个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-2` | `phandles` | 第三个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-3` | `phandles` | 第四个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-4` | `phandles` | 第五个状态的引脚配置，参见pinctrl-0 |

本页没有已弃用的节点专用属性。

## 15.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `array` | **必需**。给出寻址设备所需的信息，具体含义随设备及 `compatible` 而变化。通常是一组地址与长度对，每对称为寄存器块（Register Block），数值通常写为十六进制。参见规范v0.4第2.3.6节及[重要属性](../devicetree/P003_语法与结构.md#dt-important-props) |
| `clocks` | `phandle-array` | **必需**。设备的时钟提供者（Clock Provider）信息，通常应遵守[dt-schema时钟绑定约定](https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml) |
| `clock-names` | `string-array` | **必需**。必须先提供pclk，对应模块停止位所属的外设总线时钟，再提供pdmifclk，对应供应PDMIFCLK的节点。驱动将PDMIFCLK分频为麦克风时钟，因此第二项节点必须带有clock-frequency属性 |
| `interrupts` | `array` | **必需**。设备产生的中断，编码为一个或多个中断说明符；格式由设备在中断树中的位置决定，具有相同 `interrupt-parent` 的设备使用相同格式；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `interrupt-names` | `string-array` | **必需**。本通道的数据接收中断必须名为dat，错误检测中断必须名为err |
| `status` | `string` | 节点代表的硬件或其他资源的运行状态（Operational Status）。`okay` 表示资源可运行，例如可供驱动使用；`disabled` 表示资源不可运行，系统应将其视为不存在。参见《设备树规范》（Devicetree Specification）v0.4第2.3.4节；合法值：`okay, disabled, reserved, fail, fail-sss` |
| `compatible` | `string-array` | **必需**。字符串列表定义节点代表的硬件或其他资源类型。设备驱动通过特定兼容字符串（Compatible String）寻找应由自身管理的设备。推荐格式为 `vendor,device`：前者是厂商简称，后者通常来自数据手册。多个值从最具体到最通用排列，让具体设备匹配当前可用的最具体驱动。参见规范v0.4第2.3.1节 |
| `reg-names` | `string-array` | 为 `reg` 中每个寄存器块提供可选名称；原始例子及逐项说明见本层表后 |
| `ranges` | `compound` | 定义总线子地址空间与总线节点父地址空间之间的映射或转换。通常为空，或由子总线地址、父总线地址、长度三元组组成。**空属性表示两侧地址空间相同、不需要转换；总线节点没有此属性则认为子、父地址空间之间不存在映射**。参见规范v0.4第2.3.8节 |
| `interrupts-extended` | `compound` | 扩展中断说明符，可替代 `interrupts`；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `interrupt-parent` | `phandle` | 若存在，引用负责处理此设备所产生中断的节点；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `label` | `string` | 描述设备的可读字符串；除逐案确有需要外，已不推荐使用此属性。参见规范 v0.4 第 4.1.2 节“其他属性” |
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

## 15.3\_寄存器块命名原例

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

[上一章](P014_nxp_micfil.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P016_sifli_sf32lb-audcodec.md)
