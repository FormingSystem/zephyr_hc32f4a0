---
id: learning.zephyr-docs.sensor-liteon-maxim-temperature-binding-reference.page-25
title: maxim_max32664c
kind: reference
status: maintained
domains: [zephyr, devicetree, sensor]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/sensor/maxim,max32664c.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第25章\_maxim_max32664c

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/sensor/maxim,max32664c.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="maxim-max32664c-on-i2c-bus"></a>
<a id="dtbinding-maxim-max32664c"></a>
<a id="std-dtcompatible-maxim-max32664c"></a>

兼容字符串（Compatible String）：`maxim,max32664c`。厂商：[ Maxim Integrated Products ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-maxim)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=maxim,max32664c)。

驱动源码（Driver Source）：[drivers/sensor/adi/max32664c/max32664c.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/max32664c/max32664c.c)。

<a id="description"></a>

MAX32664 超低功耗生物识别传感器集线器（Ultra-low Power Biometric Sensor Hub）。

注意：驱动主要为 MAX86141 编写，其他传感器可以使用但未经测试。驱动最多支持两个光电探测器（Photodetector，PD），以及固定的三个 LED；MAX86141 需要特定配置：LED1 → 绿光，LED2 → 红外，LED3 → 红光。可以手动改变 LED，但可能需要修改驱动。

驱动使用 Sensor Hub 固件 30.13.31 和外部加速度计（例如 LIS2DH12）测试。参见[数据手册](https://www.analog.com/media/en/technical-documentation/data-sheets/MAX32664.pdf)。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 25.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reset-gpios` | `phandle-array` | **必需**。外部系统复位输入（External System Reset Input），低电平有效。 |
| `mfio-gpios` | `phandle-array` | **必需**。传感器集线器需要与主机通信时，MFIO 作为输出拉低；复位期间 MFIO 作为输入，若保持低电平，传感器集线器进入引导加载程序模式（Bootloader Mode）。 |
| `use-max86141` | `boolean` | 将 MAX86141 用作 MAX32664C 的模拟前端（Analog Front End，AFE）。这是默认且推荐的配置，驱动已针对该传感器优化。 |
| `use-max86161` | `boolean` | 将 MAX86161 用作 MAX32664C 的模拟前端（Analog Front End，AFE）。 |
| `motion-time` | `int` | 传感器集线器配置：运动激活时间（Motion Activation Time），单位为毫秒。默认值对应 HR 与 SpO₂ 用户指南表 12。；默认值：`200` |
| `motion-threshold` | `int` | 传感器集线器配置：运动激活参数，原文称为时间（Motion Activation Time），但单位给出为毫重力加速度（milli-g）。默认值对应 HR 与 SpO₂ 用户指南表 12。；默认值：`500` |
| `report-period` | `int` | 传感器集线器配置：采样报告周期（Samples Report Period），例如 25 表示每 25 个采样生成一次报告。默认值对应 HR 与 SpO₂ 用户指南表 16。；默认值：`1` |
| `spo2-calib` | `array` | 算法配置：血氧饱和度（SpO₂）校准系数（Calibration Coefficients）。默认值对应 HR 与 SpO₂ 用户指南表 12。；默认值：`[0xffe69196, 0xcb735, 0x989680]` |
| `min-integration-time` | `int` | 算法配置：最短积分时间（Minimum Integration Time），单位为微秒。默认值对应 HR 与 SpO₂ 用户指南表 11。；默认值：`14`；合法值：`14, 29, 58, 117` |
| `min-sampling-rate` | `int` | 算法配置：最低采样率（每秒采样数）及平均采样数（Averaging）。默认值对应 HR 与 SpO₂ 用户指南表 11。；默认值：`50`；合法值：`25, 50, 100, 200, 400` |
| `max-integration-time` | `int` | 算法配置：最长积分时间（Maximum Integration Time），单位为微秒。默认值对应 HR 与 SpO₂ 用户指南表 11。；默认值：`117`；合法值：`14, 29, 58, 117` |
| `max-sampling-rate` | `int` | 算法配置：最高采样率（每秒采样数）及平均采样数（Averaging）。默认值对应 HR 与 SpO₂ 用户指南表 11。；默认值：`100`；合法值：`25, 50, 100, 200, 400` |
| `led-current` | `uint8-array` | 初始 LED 电流的位编码配置。应查阅所连接模拟前端（AFE）的数据手册以确定合适值，固件以后也可改变电流。索引 0、1、2 分别对应 LED1、LED2、LED3。默认值对应 HR 与 SpO₂ 用户指南表 5。；默认值：`[0x7f, 0x7f, 0x7f]` |
| `hr-config` | `uint8-array` | 算法配置：心率测量（Heart Rate Measurement）的 LED 与光电探测器（PD）配置。第一个条目配置通道 1，第二个配置通道 2。默认值对应 HR 与 SpO₂ 用户指南表 15。；默认值：`[0x0, 0x1]` |
| `spo2-config` | `uint8-array` | 算法配置：血氧饱和度测量（SpO₂ Measurement）的 LED 与光电探测器（PD）配置。第一个条目配置红外通道，第二个配置红光通道。默认值对应 HR 与 SpO₂ 用户指南表 15。；默认值：`[0x10, 0x20]` |
| `friendly-name` | `string` | 描述传感器的可读字符串，可帮助主机操作系统区分同型号的多个实例，例如笔记本电脑上盖与底座的加速度计。此属性定义于[HID Usage Tables规范](https://usb.org/sites/default/files/hut1_3_0.pdf)第22.5节“通用传感器属性用途”（Generic Sensor Property Usages）。 |
| `supply-gpios` | `phandle-array` | 控制设备供电的GPIO说明符（Specifier）。设备有专用供电开关时提供此属性，供电状态完全由设备驱动负责；与vin-supply的共享稳压器方式相区别 |
| `vin-supply` | `phandle` | 控制设备供电的稳压器引用，目标设备树节点必须使用稳压器兼容字符串。通过共享稳压器供电时应提供此属性，其供电状态取决于所有受电设备的请求状态。若同时提供supply-gpios，则必须先请求稳压器再将GPIO置为有效；释放稳压器前，必须先将GPIO置为无效 |

本页没有已弃用的节点专用属性。

## 25.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `status` | `string` | 节点代表的硬件或其他资源的运行状态（Operational Status）。`okay` 表示资源可运行，例如可供驱动使用；`disabled` 表示资源不可运行，系统应将其视为不存在。参见《设备树规范》（Devicetree Specification）v0.4第2.3.4节；合法值：`okay, disabled, reserved, fail, fail-sss` |
| `compatible` | `string-array` | **必需**。字符串列表定义节点代表的硬件或其他资源类型。设备驱动通过特定兼容字符串（Compatible String）寻找应由自身管理的设备。推荐格式为 `vendor,device`：前者是厂商简称，后者通常来自数据手册。多个值从最具体到最通用排列，让具体设备匹配当前可用的最具体驱动。参见规范v0.4第2.3.1节 |
| `reg` | `array` | **必需**。给出寻址设备所需的信息，具体含义随设备及 `compatible` 而变化。通常是一组地址与长度对，每对称为寄存器块（Register Block），数值通常写为十六进制。参见规范v0.4第2.3.6节及[重要属性](../devicetree/P003_语法与结构.md#dt-important-props) |
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

译注：运动激活参数中有一项原文称为时间，单位却为milli-g；译文保留这一差异，配置时应核对传感器集线器协议与对应属性。

## 25.3\_寄存器块命名原例

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

[上一章](P024_maxim_max31875.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P026_maxim_max44009.md)
