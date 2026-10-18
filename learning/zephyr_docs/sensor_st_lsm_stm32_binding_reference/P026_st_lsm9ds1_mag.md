---
id: learning.zephyr-docs.sensor-st-lsm-stm32-binding-reference.page-26
title: st_lsm9ds1_mag
kind: reference
status: maintained
domains: [zephyr, devicetree, sensor]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/sensor/st,lsm9ds1_mag.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第26章\_st_lsm9ds1_mag

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/sensor/st,lsm9ds1_mag.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="st-lsm9ds1-mag-on-i2c-bus"></a>
<a id="dtbinding-st-lsm9ds1-mag"></a>
<a id="std-dtcompatible-st-lsm9ds1_mag"></a>

兼容字符串（Compatible String）：`st,lsm9ds1_mag`。厂商：[ STMicroelectronics ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-st)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=st,lsm9ds1_mag)。

驱动源码（Driver Source）：[drivers/sensor/st/lsm9ds1_mag/lsm9ds1_mag.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds1_mag/lsm9ds1_mag.c)。

<a id="description"></a>

通过 I2C 总线访问的 STMicroelectronics LSM9DS1-MAG 三轴磁力计（3-axis Magnetometer）。

本绑定只描述磁力计。在 `.dts` 或 `.dtsi` 文件中设置 `mag-range` 和 `mag-odr` 时，可以包含 `lsm9ds1.h` 并使用其中的宏。

<a id="examples"></a>

官方设备树配置原例：

```dts
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>

lsm9ds1_mag: lsm9ds1_mag@0 {
  /* ... */

  mag-range = <LSM9DS1_DT_FS_4Ga>;
  mag-odr = <LSM9DS1_MAG_MP_40Hz>;
};
```

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 26.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `mag-range` | `int` | 磁力计量程（Range），单位为高斯（Gauss），默认值为上电配置。编码 0、1、2、3 分别为 4、8、12、16 Gauss，对应 0.14、0.29、0.43、0.58 mgauss/LSB；完整宏对照见后文。；默认值：`0`；合法值：`0, 1, 2, 3` |
| `mag-odr` | `int` | 默认磁力计输出数据率（ODR），以每秒采样数表示，默认值为上电配置。后文保留全部编码和宏：POWER_DOWN 表示掉电，ONE_SHOT 表示单次测量；LP、MP、HP、UHP 四组模式分别列出 0.625–80 Hz 各档，还包括 UHP 155 Hz、HP 300 Hz、MP 560 Hz、LP 1000 Hz 的专用高速档。；默认值：`0`；合法值：`0xc0, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x20, 0x21, 0x22, 0x23, 0x24, 0x25, 0x26, 0x27, 0x30, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x28, 0x18, 0x8, 0x70` |
| `friendly-name` | `string` | 描述传感器的可读字符串，可帮助主机操作系统区分同型号的多个实例，例如笔记本电脑上盖与底座的加速度计。此属性定义于[HID Usage Tables规范](https://usb.org/sites/default/files/hut1_3_0.pdf)第22.5节“通用传感器属性用途”（Generic Sensor Property Usages）。 |
| `supply-gpios` | `phandle-array` | 控制设备供电的GPIO说明符（Specifier）。设备有专用供电开关时提供此属性，供电状态完全由设备驱动负责；与vin-supply的共享稳压器方式相区别 |
| `vin-supply` | `phandle` | 控制设备供电的稳压器引用，目标设备树节点必须使用稳压器兼容字符串。通过共享稳压器供电时应提供此属性，其供电状态取决于所有受电设备的请求状态。若同时提供supply-gpios，则必须先请求稳压器再将GPIO置为有效；释放稳压器前，必须先将GPIO置为无效 |

本页没有已弃用的节点专用属性。

## 26.2\_基础属性

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

## 参数编码原始对照 2

```text
- 0 # LSM9DS1_DT_FS_4Ga   (0.14  mgauss/LSB)
- 1 # LSM9DS1_DT_FS_8Ga   (0.29  mgauss/LSB)
- 2 # LSM9DS1_DT_FS_12Ga  (0.43  mgauss/LSB)
- 3 # LSM9DS1_DT_FS_16Ga  (0.58  mgauss/LSB)
```

## 参数编码原始对照 3

```text
- 0xC0 # LSM9DS1_MAG_POWER_DOWN
- 0x00 # LSM9DS1_MAG_LP_0Hz625
- 0x01 # LSM9DS1_MAG_LP_1Hz25
- 0x02 # LSM9DS1_MAG_LP_2Hz5
- 0x03 # LSM9DS1_MAG_LP_5Hz
- 0x04 # LSM9DS1_MAG_LP_10Hz
- 0x05 # LSM9DS1_MAG_LP_20Hz
- 0x06 # LSM9DS1_MAG_LP_40Hz
- 0x07 # LSM9DS1_MAG_LP_80Hz
- 0x10 # LSM9DS1_MAG_MP_0Hz625
- 0x11 # LSM9DS1_MAG_MP_1Hz25
- 0x12 # LSM9DS1_MAG_MP_2Hz5
- 0x13 # LSM9DS1_MAG_MP_5Hz
- 0x14 # LSM9DS1_MAG_MP_10Hz
- 0x15 # LSM9DS1_MAG_MP_20Hz
- 0x16 # LSM9DS1_MAG_MP_40Hz
- 0x17 # LSM9DS1_MAG_MP_80Hz
- 0x20 # LSM9DS1_MAG_HP_0Hz625
- 0x21 # LSM9DS1_MAG_HP_1Hz25
- 0x22 # LSM9DS1_MAG_HP_2Hz5
- 0x23 # LSM9DS1_MAG_HP_5Hz
- 0x24 # LSM9DS1_MAG_HP_10Hz
- 0x25 # LSM9DS1_MAG_HP_20Hz
- 0x26 # LSM9DS1_MAG_HP_40Hz
- 0x27 # LSM9DS1_MAG_HP_80Hz
- 0x30 # LSM9DS1_MAG_UHP_0Hz625
- 0x31 # LSM9DS1_MAG_UHP_1Hz25
- 0x32 # LSM9DS1_MAG_UHP_2Hz5
- 0x33 # LSM9DS1_MAG_UHP_5Hz
- 0x34 # LSM9DS1_MAG_UHP_10Hz
- 0x35 # LSM9DS1_MAG_UHP_20Hz
- 0x36 # LSM9DS1_MAG_UHP_40Hz
- 0x37 # LSM9DS1_MAG_UHP_80Hz
- 0x38 # LSM9DS1_MAG_UHP_155Hz
- 0x28 # LSM9DS1_MAG_HP_300Hz
- 0x18 # LSM9DS1_MAG_MP_560Hz
- 0x08 # LSM9DS1_MAG_LP_1000Hz
- 0x70 # LSM9DS1_MAG_ONE_SHOT
```

## 26.3\_寄存器块命名原例

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

[上一章](P025_st_lsm9ds1.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P027_st_stm32-digi-temp.md)
