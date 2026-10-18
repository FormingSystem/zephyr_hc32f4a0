---
id: learning.zephyr-docs.sensor-st-lis-lps-binding-reference.page-6
title: st_lis2du12-i2c
kind: reference
status: maintained
domains: [zephyr, devicetree, sensor]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/sensor/st,lis2du12-i2c.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第6章\_st_lis2du12-i2c

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/sensor/st,lis2du12-i2c.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="st-lis2du12-on-i2c-bus"></a>
<a id="dtbinding-st-lis2du12-i2c"></a>

兼容字符串（Compatible String）：`st,lis2du12`。厂商：[ STMicroelectronics ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-st)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=st,lis2du12)。

驱动源码（Driver Source）：[drivers/sensor/st/lis2du12/lis2du12.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2du12/lis2du12.c)。

<a id="description"></a>

通过 I2C 总线访问的 STMicroelectronics LIS2DU12 三轴超低功耗加速度传感器（3-axis Ultra-low Power Accelerometer Sensor）。

<a id="examples"></a>

官方设备树配置原例：

```dts
#include <zephyr/dt-bindings/sensor/lis2du12.h>

lis2du12: lis2du12@0 {
  /* ... */

  accel-range = <LIS2DU12_DT_FS_16G>;
  accel-odr = <LIS2DU12_DT_ODR_AT_50Hz>;
};
```

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 6.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `supply-gpios` | `phandle-array` | 控制设备供电的GPIO说明符（Specifier）。设备有专用供电开关时提供此属性，供电状态完全由设备驱动负责；与vin-supply的共享稳压器方式相区别 |
| `vin-supply` | `phandle` | 控制设备供电的稳压器引用，目标设备树节点必须使用稳压器兼容字符串。通过共享稳压器供电时应提供此属性，其供电状态取决于所有受电设备的请求状态。若同时提供supply-gpios，则必须先请求稳压器再将GPIO置为有效；释放稳压器前，必须先将GPIO置为无效 |
| `int1-gpios` | `phandle-array` | INT1 引脚，传感器产生的信号默认高电平有效（Active High），属性标志必须正确描述驱动实际接收到的信号。 |
| `int2-gpios` | `phandle-array` | INT2 引脚，传感器产生的信号默认高电平有效（Active High），属性标志必须正确描述驱动实际接收到的信号。 |
| `drdy-pin` | `int` | 选择数据就绪（Data Ready，DRDY）引脚：1 从 INT1 产生，2 从 INT2 产生。本属性可选，省略时默认 1。默认将 DRDY 与 DELTA 唤醒功能分置于不同引脚，但也允许把二者配置到同一引脚。；默认值：`1`；合法值：`1, 2` |
| `delta-pin` | `int` | 选择 DELTA 唤醒（Wake-up）引脚：1 从 INT1 产生，2 从 INT2 产生。本属性可选，省略时默认 2。默认将 DELTA 与 DRDY 数据就绪功能分置于不同引脚，但也允许把二者配置到同一引脚。；默认值：`2`；合法值：`1, 2` |
| `accel-range` | `int` | 量程（Range），单位为 g，默认值为上电配置。编码 0、1、2、3 分别为 2、4、8、16 g，对应 0.061、0.122、0.244、0.488 mg/LSB；完整宏对照见后文。；默认值：`0`；合法值：`0, 1, 2, 3` |
| `accel-odr` | `int` | 默认加速度计输出数据率（ODR），以每秒采样数（Hz）表示，取值依据 `hal/st` 中 `lis2du12_md_t` 枚举，同时也启用或禁用高性能模式（High Performance Mode）。默认值为上电配置。编码 0x00 关闭；0x01–0x03 为超低功耗（ULP）1.6、3、6 Hz；0x04–0x0b 分别为 6、12、25、50、100、200、400、800 Hz；0x0e 为引脚触发，0x0f 为软件触发。完整宏对照见后文。；默认值：`0x0`；合法值：`0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0xa, 0xb, 0xe, 0xf` |
| `drdy-pulsed` | `boolean` | 启用时选择数据就绪中断的脉冲模式（Pulsed Mode），禁用时选择锁存模式（Latched Mode）。 |
| `friendly-name` | `string` | 描述传感器的可读字符串，可帮助主机操作系统区分同型号的多个实例，例如笔记本电脑上盖与底座的加速度计。此属性定义于[HID Usage Tables规范](https://usb.org/sites/default/files/hut1_3_0.pdf)第22.5节“通用传感器属性用途”（Generic Sensor Property Usages）。 |

本页没有已弃用的节点专用属性。

## 6.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `array` | **必需**。设备在I²C总线上的地址（Device Address） |
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

## 参数编码原始对照 8

```text
0 # LIS2DU12_DT_FS_2G  (0.061 mg/LSB)
1 # LIS2DU12_DT_FS_4G  (0.122 mg/LSB)
2 # LIS2DU12_DT_FS_8G  (0.244 mg/LSB)
3 # LIS2DU12_DT_FS_16G (0.488 mg/LSB)
```

## 参数编码原始对照 9

```text
0x00 # LIS2DU12_DT_ODR_OFF
0x01 # LIS2DU12_DT_ODR_AT_1Hz6_ULP
0x02 # LIS2DU12_DT_ODR_AT_3Hz_ULP
0x03 # LIS2DU12_DT_ODR_AT_6Hz_ULP
0x04 # LIS2DU12_DT_ODR_AT_6Hz
0x05 # LIS2DU12_DT_ODR_AT_12Hz
0x06 # LIS2DU12_DT_ODR_AT_25Hz
0x07 # LIS2DU12_DT_ODR_AT_50Hz
0x08 # LIS2DU12_DT_ODR_AT_100Hz
0x09 # LIS2DU12_DT_ODR_AT_200Hz
0x0a # LIS2DU12_DT_ODR_AT_400Hz
0x0b # LIS2DU12_DT_ODR_AT_800Hz
0x0e # LIS2DU12_DT_ODR_TRIG_PIN
0x0f # LIS2DU12_DT_ODR_TRIG_SW
```

## 6.3\_寄存器块命名原例

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

[上一章](P005_st_lis2ds12-spi.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P007_st_lis2du12-spi.md)
