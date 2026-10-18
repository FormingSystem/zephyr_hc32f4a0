---
id: learning.zephyr-docs.sensor-invensense-6axis-pressure-binding-reference.page-10
title: invensense_icm45686s-i3c
kind: reference
status: maintained
domains: [zephyr, devicetree, sensor]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/sensor/invensense,icm45686s-i3c.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第10章\_invensense_icm45686s-i3c

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/sensor/invensense,icm45686s-i3c.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="invensense-icm45686s-on-i3c-bus"></a>
<a id="dtbinding-invensense-icm45686s-i3c"></a>

兼容字符串（Compatible String）：`invensense,icm45686s`。厂商：[ InvenSense Inc. ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-invensense)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=invensense,icm45686s)。

驱动源码（Driver Source）：[drivers/sensor/tdk/icm45686/icm45686.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/icm45686/icm45686.c)。

<a id="description"></a>

ICM45686S 高精度六轴运动跟踪器件（High-precision 6-axis Motion Tracking Device）。

在 `.dts` 或 `.dtsi` 文件中设置 `accel-pm`、`accel-range`、`accel-odr`、`gyro-pm`、`gyro-range` 和 `gyro-odr` 属性时，可以包含 `icm45686.h` 并使用其中定义的宏。完整官方示例见后文。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 10.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `assigned-address` | `int` | 将分配给设备的动态地址（Dynamic Address）。 |
| `supports-setaasa` | `boolean` | 标记设备是否支持公共命令码（Common Command Code，CCC）SETAASA；支持时用它优化总线初始化。 |
| `v1p0-support` | `boolean` | 标记设备是否符合I3C v1.0。 |
| `supply-gpios` | `phandle-array` | 控制设备供电的GPIO说明符（Specifier）。设备有专用供电开关时提供此属性，供电状态完全由设备驱动负责；与vin-supply的共享稳压器方式相区别 |
| `vin-supply` | `phandle` | 控制设备供电的稳压器引用，目标设备树节点必须使用稳压器兼容字符串。通过共享稳压器供电时应提供此属性，其供电状态取决于所有受电设备的请求状态。若同时提供supply-gpios，则必须先请求稳压器再将GPIO置为有效；释放稳压器前，必须先将GPIO置为无效 |
| `accel-fs` | `int` | 指定加速度计量程（Range），单位为 g，默认值为上电配置。；默认值：`0`；合法值：`0, 1, 2, 3, 4` |
| `gyro-fs` | `int` | 指定陀螺仪量程（Range），单位为度每秒，默认值为上电配置。；默认值：`0`；合法值：`0, 1, 2, 3, 4, 5, 6, 7, 8` |
| `int-gpios` | `phandle-array` | INT 信号默认高电平有效（Active High）。属性值中的标志必须正确描述驱动实际接收到的信号。 |
| `accel-pwr-mode` | `int` | 指定默认加速度计电源模式（Accelerometer Power Mode），默认值为上电配置。；默认值：`0`；合法值：`0, 2, 3` |
| `accel-odr` | `int` | 指定默认加速度计输出数据率（Output Data Rate），以每秒采样数（Hz）表示。默认值为上电配置。；默认值：`6`；合法值：`3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15` |
| `accel-lpf` | `int` | 指定加速度计低通滤波器（Low-pass Filter）的截止频率，以输出数据率（Output Data Rate）的比例表示。默认值为上电配置。；默认值：`0`；合法值：`0, 1, 2, 3, 4, 5, 6` |
| `gyro-pwr-mode` | `int` | 指定默认陀螺仪电源模式（Gyroscope Power Mode），默认值为上电配置。；默认值：`0`；合法值：`0, 1, 2, 3` |
| `gyro-odr` | `int` | 指定默认陀螺仪输出数据率（Output Data Rate），以每秒采样数（Hz）表示。默认值为上电配置。；默认值：`6`；合法值：`3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15` |
| `gyro-lpf` | `int` | 指定陀螺仪低通滤波器（Low-pass Filter）的截止频率，以输出数据率（Output Data Rate）的比例表示。默认值为上电配置。；默认值：`0`；合法值：`0, 1, 2, 3, 4, 5, 6` |
| `fifo-watermark` | `int` | 以帧数指定 FIFO 水位（Watermark），默认值为上电配置，即禁用。；默认值：`0`；范围：`0 to 104` |
| `fifo-watermark-equals` | `boolean` | 改变 FIFO 水位中断行为，使其仅在采样数恰好等于阈值时触发（`count = watermark`）。否则，采样数大于或等于 FIFO 水位阈值时均产生中断（`count >= watermark`）。 |
| `apex` | `string` | 高级计步与事件检测（Advanced Pedometer and Event Detection，APEX）功能包括：计步器（Pedometer）跟踪步数，并提供步频（Cadence）及估计的活动类型（步行 Walk、跑步 Run、未知 Unknown）；倾斜检测（Tilt Detection）在板子倾斜至少 30 度并保持 4 秒时检测倾斜；运动唤醒（Wake on Motion，WoM）检测各轴超过 195 mg 阈值的运动；显著运动检测器（Significant Motion Detector，SMD）检测用户是否发生明显移动。；默认值：`none`；合法值：`none, pedometer, tilt, smd, wom` |
| `friendly-name` | `string` | 描述传感器的可读字符串，可帮助主机操作系统区分同型号的多个实例，例如笔记本电脑上盖与底座的加速度计。此属性定义于[HID Usage Tables规范](https://usb.org/sites/default/files/hut1_3_0.pdf)第22.5节“通用传感器属性用途”（Generic Sensor Property Usages）。 |

本页没有已弃用的节点专用属性。

## 10.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `array` | **必需**。包含三个字段。<br>**I3C设备**：依次为静态地址（Static Address）、预置标识（Provisioned ID，PID）前半部分、PID后半部分。①在动态地址分配（Dynamic Address Assignment，DAA）开始前，可将静态地址用作目标设备动态地址；不使用静态地址、而通过DAA确定地址时，可填0。②PID前半部分为制造商标识左移1位；制造商标识位于48位PID的第33至47位，位号从0开始。③PID后半部分由器件标识（PID第16至31位）左移16位，与实例标识（PID第12至15位）左移12位组合；基本上就是PID的低32位。<br>I3C目标节点名称格式为`<node name>@<address + PID>`，例如`sensor@4200001234012345678`，PID部分扩展为64位整数。<br>**I²C设备**：依次为静态地址、`0x00`和传统虚拟寄存器（Legacy Virtual Register，LVR）值。①采用7位I²C地址，不支持10位寻址。②第二字段始终为`0x00`。③LVR中，bit[31:8]未使用；bit[7:5]为设备索引：0表示具有50 ns尖峰滤波器，SCL高频信号不会影响设备；1表示没有50 ns尖峰滤波器，但可在高频SCL下工作；2表示没有该滤波器，也不能在高频SCL下工作；其他值保留。bit[4]为I²C模式标志：0表示快速模式增强版（Fast-mode Plus，FM+），1表示快速模式（Fast Mode，FM）。bit[3:0]保留。<br>I²C节点名称格式为`<node name>@<address + 00000000 + LVR>`，例如`sensor@5000000000000000FF`，中间的`0x00`与LVR均扩展为32位整数。 |
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

属性说明中的“重要属性”参见[设备树语法与结构](../devicetree/P003_语法与结构.md#dt-important-props)。

## 六轴传感器总线配置原例

```dts
#include <zephyr/dt-bindings/sensor/icm45686.h>

&i3c1 {
  ...

  icm45686s: icm45686s@680000046a00000011 {
    ...

    accel-pwr-mode = <ICM45686_DT_ACCEL_LN>;
    accel-fs = <ICM45686_DT_ACCEL_FS_32>;
    accel-odr = <ICM45686_DT_ACCEL_ODR_800>;
    gyro-pwr-mode= <ICM45686_DT_GYRO_LN>;
    gyro-fs = <ICM45686_DT_GYRO_FS_4000>;
    gyro-odr = <ICM45686_DT_GYRO_ODR_800>;
  };
};
```

译注：介绍段落列出的 `accel-pm`、`accel-range`、`gyro-pm`、`gyro-range` 与属性表、示例使用的 `accel-pwr-mode`、`accel-fs`、`gyro-pwr-mode`、`gyro-fs` 名称不同；这里保留原文，实际配置应核对属性表及绑定定义。

## 10.3\_寄存器块命名原例

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

[上一章](P009_invensense_icm45686s-i2c.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P011_invensense_icm45686s-spi.md)
