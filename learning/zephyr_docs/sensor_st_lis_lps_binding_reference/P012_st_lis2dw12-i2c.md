---
id: learning.zephyr-docs.sensor-st-lis-lps-binding-reference.page-12
title: st_lis2dw12-i2c
kind: reference
status: maintained
domains: [zephyr, devicetree, sensor]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/sensor/st,lis2dw12-i2c.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第12章\_st_lis2dw12-i2c

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/sensor/st,lis2dw12-i2c.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="st-lis2dw12-on-i2c-bus"></a>
<a id="dtbinding-st-lis2dw12-i2c"></a>

兼容字符串（Compatible String）：`st,lis2dw12`。厂商：[ STMicroelectronics ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-st)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=st,lis2dw12)。

驱动源码（Driver Source）：[drivers/sensor/st/lis2dw12/lis2dw12.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2dw12/lis2dw12.c)。

<a id="description"></a>

STMicroelectronics LIS2DW12 三轴加速度计（3-axis Accelerometer）。

<a id="examples"></a>

官方设备树配置原例：

```dts
#include <zephyr/dt-bindings/sensor/lis2dw12.h>

lis2dw12: lis2dw12@0 {
  /* ... */

  wakeup-duration = <LIS2DW12_DT_WAKEUP_4_ODR>;
  ff-threshold = <LIS2DW12_DT_FF_THRESHOLD_500_mg>;
  tap-mode = <LIS2DW12_DT_SINGLE_DOUBLE_TAP>;
  power-mode = <LIS2DW12_DT_HP_MODE>;
  bw-filt = <LIS2DW12_DT_FILTER_BW_ODR_DIV_2>;
};
```

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 12.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `supply-gpios` | `phandle-array` | 控制设备供电的GPIO说明符（Specifier）。设备有专用供电开关时提供此属性，供电状态完全由设备驱动负责；与vin-supply的共享稳压器方式相区别 |
| `vin-supply` | `phandle` | 控制设备供电的稳压器引用，目标设备树节点必须使用稳压器兼容字符串。通过共享稳压器供电时应提供此属性，其供电状态取决于所有受电设备的请求状态。若同时提供supply-gpios，则必须先请求稳压器再将GPIO置为有效；释放稳压器前，必须先将GPIO置为无效 |
| `irq-gpios` | `phandle-array` | 数据就绪引脚（Data Ready，DRDY）。传感器产生的信号默认高电平有效（Active High），属性标志必须正确描述驱动实际接收到的信号。 |
| `int-pin` | `int` | 选择数据就绪（DRDY）引脚编号：1 从 INT1 产生，2 从 INT2 产生。本属性可选，省略时默认 1，与上电配置一致。；默认值：`1`；合法值：`1, 2` |
| `range` | `int` | 量程（Range），单位为 g，默认值为上电配置。16 g → 1.952 mg/LSB，8 g → 0.976 mg/LSB，4 g → 0.488 mg/LSB，2 g → 0.244 mg/LSB。；默认值：`2`；合法值：`16, 8, 4, 2` |
| `odr` | `int` | 输出数据率（ODR），单位为 Hz，未设置时默认 12.5 Hz。带小数的数据率取整数部分表示，例如 1.65 Hz → 1，12.5 Hz → 12。ODR 选择 0 时，加速度计初始化为关闭状态（Power Off）。；合法值：`0, 1, 12, 25, 50, 100, 200, 400, 800, 1600` |
| `bw-filt` | `int` | 数字滤波截止带宽（Digital Filtering Cutoff Bandwidth），默认值为上电配置。编码 0、1、2、3 分别对应 ODR/2、ODR/4、ODR/10、ODR/20，完整宏对照见后文。；默认值：`0`；合法值：`0, 1, 2, 3` |
| `power-mode` | `int` | 传感器电源模式（Power Mode），默认值为上电配置。编码 0–3 分别对应低功耗模式 `LIS2DW12_DT_LP_M1` 至 `LIS2DW12_DT_LP_M4`，4 对应高性能模式 `LIS2DW12_DT_HP_MODE`。；默认值：`0`；合法值：`0, 1, 2, 3, 4` |
| `tap-mode` | `int` | 敲击模式（Tap Mode），默认值为上电配置。0 单击（`LIS2DW12_DT_SINGLE_TAP`），1 单击与双击（`LIS2DW12_DT_SINGLE_DOUBLE_TAP`）。；默认值：`0`；合法值：`0, 1` |
| `tap-threshold` | `array` | X/Y/Z 轴敲击阈值（Tap Threshold），默认值为上电配置，各轴值范围为 0x00–0x1F。用于启动对应轴敲击事件检测；每个阈值是对应 2 g 满量程的无符号 5 位数，零表示禁用该轴检测。例如 X 为 12、Z 为 14、Y 禁用时，设备树写作 `tap-threshold = <12>, <0>, <14>`；对应 X = 12 × 2g/32 = 750 mg，Z = 14 × 2g/32 = 875 mg。；默认值：`[0, 0, 0]` |
| `tap-shock` | `int` | 敲击冲击时间值（Tap Shock），默认值为上电配置。表示超过阈值的信号可被识别为敲击事件的最长持续时间。0 对应 `4*1/ODR`，1 LSB 对应 `8*1/ODR`。；默认值：`0x0`；范围：`0 to 3` |
| `tap-latency` | `int` | 敲击间隔（Tap Latency），默认值为上电配置。启用双击识别时，表示两个连续敲击能够被判为双击的最大时间间隔。0 对应 `16*1/ODR`，1 LSB 对应 `32*1/ODR`。；默认值：`0x0`；范围：`0 to 0xf` |
| `tap-quiet` | `int` | 检测到敲击后所需的安静时间（Quiet Time），默认值为上电配置。首次敲击之后，在此时间内不能有任何超过阈值的事件。0 对应 `2*1/ODR`，1 LSB 对应 `4*1/ODR`。；默认值：`0x0`；范围：`0 to 3` |
| `low-noise` | `boolean` | 启用 `CTRL6` 寄存器的 `LOW_NOISE` 标志，影响噪声密度（Noise Density）和电流消耗；详情参见数据手册。 |
| `hp-filter-path` | `boolean` | 设置 `CTRL6` 的滤波数据选择位（Filtered Data Selection）。启用时选择高通滤波器路径，禁用时选择低通滤波器路径。影响 `OUT_REG`／FIFO 值，但不影响唤醒功能（Wakeup）。 |
| `hp-ref-mode` | `boolean` | 启用 `CTRL7` 中的高通滤波器参考模式（High-pass Filter Reference Mode）。输出数据等于输入加速度与启用参考模式时捕获值之间的差，只计算差值，不进行 LIS2DW12 滤波。它同时影响 `OUT_REG`／FIFO 值及唤醒功能（Wakeup）。 |
| `drdy-pulsed` | `boolean` | 启用时选择数据就绪中断脉冲模式（Pulsed Mode），禁用时选择锁存模式（Latched Mode），设置 `CTRL7` 中对应的 `DRDY_PULSED` 位。 |
| `ff-duration` | `int` | 自由落体持续时间（Freefall Duration），单位为毫秒。所有轴的加速度读数持续低于自由落体阈值达到该时间时，产生自由落体触发。寄存器字段为 5 位，1 LSB = `1 * 1/ODR`，因此依赖输出数据率。代码用原文所称 `SENSOR ATTR SAMPLING FREQUENCY` 改变数据率后，必须通过原文写作 `SENSOR_ATT_FF_DUR` 的属性重新设置。ST DT0100 设计提示建议使用 100 Hz ODR 与 30 ms 的 `ff-duration` 检测自由落体。；默认值：`30` |
| `ff-threshold` | `int` | 自由落体阈值（Freefall Threshold），单位为 mg。所有轴的读数持续低于阈值达到自由落体持续时间时触发。字段为 3 位；根据 ST DT0100 设计提示，默认选择 3（312 mg）。编码 0–7 分别为 156、219、250、312、344、406、469、500 mg，完整宏对照见后文。；默认值：`3`；合法值：`0, 1, 2, 3, 4, 5, 6, 7` |
| `wakeup-duration` | `int` | 唤醒持续时间（Wakeup Duration），默认值为寄存器复位值。所有轴加速度读数持续高于唤醒阈值达到该时间时触发唤醒。字段为 2 位，1 LSB = `1 * 1/ODR`；编码 0–3 分别对应 `LIS2DW12_DT_WAKEUP_1_ODR` 至 `LIS2DW12_DT_WAKEUP_4_ODR`。；默认值：`0`；合法值：`0, 1, 2, 3` |
| `sleep-duration` | `int` | 休眠持续时间（Sleep Duration），默认寄存器复位值 `0000` 对应 `16*1/ODR`。所有轴加速度读数持续低于唤醒阈值达到该时间时，产生休眠触发或进入休眠模式。字段为 4 位，1 LSB = `512 * 1/ODR`，值为 0–15；原文列出的宏范围是 `LIS2DW12_DT_SLEEP_0_ODR` 至 `LIS2DW12_DT_SLEEP_15_ODR`。；默认值：`0`；合法值：`0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15` |
| `friendly-name` | `string` | 描述传感器的可读字符串，可帮助主机操作系统区分同型号的多个实例，例如笔记本电脑上盖与底座的加速度计。此属性定义于[HID Usage Tables规范](https://usb.org/sites/default/files/hut1_3_0.pdf)第22.5节“通用传感器属性用途”（Generic Sensor Property Usages）。 |

本页没有已弃用的节点专用属性。

## 12.2\_基础属性

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

## 参数编码原始对照 5

```text
   1 # drdy is generated from INT1
   2 # drdy is generated from INT2
```

## 参数编码原始对照 6

```text
  16 # 16g (1.952 mg/LSB)
   8 #  8g (0.976 mg/LSB)
   4 #  4g (0.488 mg/LSB)
   2 #  2g (0.244 mg/LSB)
```

## 参数编码原始对照 8

```text
- 0 # LIS2DW12_DT_FILTER_BW_ODR_DIV_2
- 1 # LIS2DW12_DT_FILTER_BW_ODR_DIV_4
- 2 # LIS2DW12_DT_FILTER_BW_ODR_DIV_10
- 3 # LIS2DW12_DT_FILTER_BW_ODR_DIV_20
```

## 参数编码原始对照 9

```text
- 0 # LIS2DW12_DT_LP_M1
- 1 # LIS2DW12_DT_LP_M2
- 2 # LIS2DW12_DT_LP_M3
- 3 # LIS2DW12_DT_LP_M4
- 4 # LIS2DW12_DT_HP_MODE
```

## 参数编码原始对照 10

```text
- 0 # LIS2DW12_DT_SINGLE_TAP
- 1 # LIS2DW12_DT_SINGLE_DOUBLE_TAP
```

## 敲击阈值原例

```dts
    tap-threshold = <12>, <0>, <14>
```

## 参数编码原始对照 20

```text
- 0 # LIS2DW12_DT_FF_THRESHOLD_156_mg
- 1 # LIS2DW12_DT_FF_THRESHOLD_219_mg
- 2 # LIS2DW12_DT_FF_THRESHOLD_250_mg
- 3 # LIS2DW12_DT_FF_THRESHOLD_312_mg
- 4 # LIS2DW12_DT_FF_THRESHOLD_344_mg
- 5 # LIS2DW12_DT_FF_THRESHOLD_406_mg
- 6 # LIS2DW12_DT_FF_THRESHOLD_469_mg
- 7 # LIS2DW12_DT_FF_THRESHOLD_500_mg
```

## 参数编码原始对照 21

```text
- 0 # LIS2DW12_DT_WAKEUP_1_ODR
- 1 # LIS2DW12_DT_WAKEUP_2_ODR
- 2 # LIS2DW12_DT_WAKEUP_3_ODR
- 3 # LIS2DW12_DT_WAKEUP_4_ODR
```

## 参数编码原始对照 22

```text
- 0 # LIS2DW12_DT_SLEEP_0_ODR
...
- 15 # LIS2DW12_DT_SLEEP_15_ODR
```

译注：敲击阈值原例未写末尾分号；自由落体说明将采样频率属性写作 `SENSOR ATTR SAMPLING FREQUENCY`，持续时间属性写作 `SENSOR_ATT_FF_DUR`。这里保留源文，实际调用应核对Zephyr传感器API定义。

## 12.3\_寄存器块命名原例

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

[上一章](P011_st_lis2duxs12-spi.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P013_st_lis2dw12-spi.md)
