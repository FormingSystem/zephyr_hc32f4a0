---
id: learning.zephyr-docs.sensor-st-lsm-stm32-binding-reference.page-22
title: st_lsm6dsv80x-spi
kind: reference
status: maintained
domains: [zephyr, devicetree, sensor]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/sensor/st,lsm6dsv80x-spi.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第22章\_st_lsm6dsv80x-spi

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/sensor/st,lsm6dsv80x-spi.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="st-lsm6dsv80x-on-spi-bus"></a>
<a id="dtbinding-st-lsm6dsv80x-spi"></a>

兼容字符串（Compatible String）：`st,lsm6dsv80x`。厂商：[ STMicroelectronics ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-st)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=st,lsm6dsv80x)。

驱动源码（Driver Source）：[drivers/sensor/st/lsm6dsvxxx/lsm6dsvxxx.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dsvxxx/lsm6dsvxxx.c)。

<a id="description"></a>

通过 SPI 总线访问的 STMicroelectronics LSM6DSV80X 六轴惯性测量单元（6-axis Inertial Measurement Unit，IMU）。

<a id="examples"></a>

官方设备树配置原例：

```dts
#include <zephyr/dt-bindings/sensor/lsm6dsv80x.h>

lsm6dsv80x: lsm6dsv80x@0 {
  /* ... */

  accel-range = <LSM6DSV80X_DT_FS_8G>;
  accel-odr = <LSM6DSVXXX_DT_ODR_AT_60Hz>;
  gyro-range = <LSM6DSV80X_DT_FS_4000DPS>;
  gyro-odr = <LSM6DSVXXX_DT_ODR_AT_60Hz>;
};
```

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 22.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `spi-max-frequency` | `int` | **必需**。设备SPI接口的最大时钟频率，单位Hz |
| `duplex` | `int` | 双工模式（Duplex Mode），可为全双工或半双工。默认全双工，对应0，这是最常见模式。应使用宏而非原始枚举值，`dt-bindings/spi/spi.h` 定义的对应关系为0对应SPI_FULL_DUPLEX，2048对应SPI_HALF_DUPLEX；原始对照表见下文；默认值：`0`；合法值：`0, 2048` |
| `frame-format` | `int` | Motorola或TI帧格式（Frame Format）。默认Motorola，对应0，这是最常见格式。应使用宏而非原始枚举值，`dt-bindings/spi/spi.h` 对应关系为0对应SPI_FRAME_FORMAT_MOTOROLA，32768对应SPI_FRAME_FORMAT_TI；原始对照表见下文；默认值：`0`；合法值：`0, 32768` |
| `spi-cpol` | `boolean` | SPI时钟极性（Clock Polarity），指示时钟空闲状态；设置时空闲为逻辑高电平，否则为低电平 |
| `spi-cpha` | `boolean` | SPI时钟相位（Clock Phase），决定采样边沿；设置时在第二个边沿采样，否则在第一个边沿采样 |
| `spi-lsb-first` | `boolean` | 设备要求最低有效位优先（Least Significant Bit First，LSB-first）的数据模式 |
| `spi-hold-cs` | `boolean` | 某些场景需由控制器通过软件管理SPI片选（Chip Select，CS），以连续执行多次SPI事务而不释放片选。典型情况为变长数据包：第一笔事务读取长度，第二笔读取该长度的字节数据 |
| `spi-cs-high` | `boolean` | 设备要求片选高电平有效（Active High） |
| `spi-interframe-delay-ns` | `int` | SPI字（Word）之间的延迟，单位纳秒。默认0是特殊值，表示SCK周期的一半；默认值：`0` |
| `spi-cs-setup-delay-ns` | `int` | 片选置有效之后，由控制器引入的延迟，单位纳秒，也称使能前置时间（Enable Lead Time） |
| `spi-cs-hold-delay-ns` | `int` | 片选释放之前，由控制器引入的延迟，单位纳秒，也称使能后置时间（Enable Lag Time） |
| `supply-gpios` | `phandle-array` | 控制设备供电的GPIO说明符（Specifier）。设备有专用供电开关时提供此属性，供电状态完全由设备驱动负责；与vin-supply的共享稳压器方式相区别 |
| `vin-supply` | `phandle` | 控制设备供电的稳压器引用，目标设备树节点必须使用稳压器兼容字符串。通过共享稳压器供电时应提供此属性，其供电状态取决于所有受电设备的请求状态。若同时提供supply-gpios，则必须先请求稳压器再将GPIO置为有效；释放稳压器前，必须先将GPIO置为无效 |
| `accel-hg-odr` | `int` | 默认高加速度（High-g）加速度计输出数据率（ODR），以每秒采样数（Hz）表示。取值依据 `hal/st` 中 `lsm6dsv80x_hg_xl_data_rate_t` 枚举，不改变工作模式，器件保持默认高性能模式（High Performance）。默认值为上电配置。0x0 关闭，0x3–0x7 分别为 480、960、1920、3840、7680 Hz，完整宏对照见后文。；默认值：`0x0`；合法值：`0x0, 0x3, 0x4, 0x5, 0x6, 0x7` |
| `accel-range` | `int` | 加速度量程（Range），单位为 g，默认值为上电配置。32 g 及以上要求启用 High-g 传感器，参见 `accel-hg-odr`。2、4、8、16、32、64、80 g 分别对应 0.061、0.122、0.244、0.488、0.976、1.952、3.904 mg/LSB；完整宏对照见后文。；默认值：`2`；合法值：`2, 4, 8, 16, 32, 64, 80` |
| `gyro-range` | `int` | 陀螺仪量程（Range），单位为度每秒（dps），默认值为上电配置。0x0 使用上电配置；0x1–0x5 分别为 250、500、1000、2000、4000 dps，对应 8.75、17.50、35、70、140 mdps/LSB；完整宏对照见后文。；默认值：`0`；合法值：`0x0, 0x1, 0x2, 0x3, 0x4, 0x5` |
| `int1-gpios` | `phandle-array` | INT1 引脚，传感器产生的信号默认高电平有效（Active High），属性标志必须正确描述驱动实际接收到的信号。 |
| `int2-gpios` | `phandle-array` | INT2 引脚，传感器产生的信号默认高电平有效（Active High），属性标志必须正确描述驱动实际接收到的信号。 |
| `int-gpio-config` | `int` | INT2 GPIO 中断配置（Interrupt Configuration）。默认 0 为最常见配置，避免同一事件多次触发。0 对应有效边沿触发（`LSM6DSVXXX_DT_GPIO_INT_EDGE_TO_ACTIVE`），1 对应有效电平触发（`LSM6DSVXXX_DT_GPIO_INT_LEVEL_ACTIVE`）。；默认值：`0`；合法值：`0, 1` |
| `drdy-pin` | `int` | 选择数据就绪（DRDY）引脚编号：1 为 INT1，2 为 INT2。本属性可选，省略时默认 1，与上电配置一致。；默认值：`1`；合法值：`1, 2` |
| `self-test` | `boolean` | 启用器件自检（Self-test），向传感器施加静电力，模拟加速度与旋转，无需实际移动器件。 |
| `accel-odr` | `int` | 默认加速度计输出数据率（ODR），以每秒采样数（Hz）表示。取值依据 `hal/st` 中 `lsm6dsv16x_data_rate_t` 枚举，不改变工作模式，器件保持默认高性能模式（High Performance）。默认值为上电配置。后文完整保留普通数据率、HA01 与 HA02 精度系列的全部编码和宏，OFF 表示关闭。；默认值：`0x0`；合法值：`0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0xa, 0xb, 0xc, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18, 0x19, 0x1a, 0x1b, 0x1c, 0x23, 0x24, 0x25, 0x26, 0x27, 0x28, 0x29, 0x2a, 0x2b, 0x2c` |
| `gyro-odr` | `int` | 默认陀螺仪输出数据率（ODR），以每秒采样数（Hz）表示。取值依据 `hal/st` 中 `lsm6dsv16x_data_rate_t` 枚举，不改变工作模式，器件保持默认高性能模式（High Performance）。设备树中选择的值也是指定 ODR 精度的唯一方式，即使运行时使用 `SENSOR_ATTR_SAMPLING_FREQUENCY` 也仍由该选择决定精度。默认值为上电配置。后文完整保留普通数据率、HA01 与 HA02 系列的全部编码和宏。；默认值：`0x0`；合法值：`0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0xa, 0xb, 0xc, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18, 0x19, 0x1a, 0x1b, 0x1c, 0x23, 0x24, 0x25, 0x26, 0x27, 0x28, 0x29, 0x2a, 0x2b, 0x2c` |
| `drdy-pulsed` | `boolean` | 启用时选择数据就绪中断的脉冲模式（Pulsed Mode），禁用时选择锁存模式（Latched Mode）。 |
| `fifo-watermark` | `int` | 默认 FIFO 水位阈值（Watermark Threshold），每个单位表示一行 FIFO，即 1 字节标签（TAG）加 6 字节数据。范围为 0–255，典型值 32 被选为默认值。；默认值：`32` |
| `accel-fifo-batch-rate` | `int` | 默认加速度计 FIFO 批量存储数据率（FIFO Batch Data Rate），以每秒采样数（Hz）表示。取值依据 `hal/st` 中 `lsm6dsv16x_fifo_xl_batch_t` 枚举，默认值为上电配置。后文原表完整保留不批量存储（NOT_BATCHED）及 1.875–7680 Hz 各档编码和宏。；默认值：`0x0`；合法值：`0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0xa, 0xb, 0xc` |
| `gyro-fifo-batch-rate` | `int` | 默认陀螺仪 FIFO 批量存储数据率（FIFO Batch Data Rate），以每秒采样数（Hz）表示。取值依据 `hal/st` 中 `lsm6dsv16x_fifo_gy_batch_t` 枚举，默认值为上电配置。后文原表完整保留不批量存储（NOT_BATCHED）及 1.875–7680 Hz 各档编码和宏。；默认值：`0x0`；合法值：`0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0xa, 0xb, 0xc` |
| `temp-fifo-batch-rate` | `int` | 默认温度 FIFO 批量存储数据率（FIFO Batch Data Rate），以每秒采样数（Hz）表示。取值依据 `hal/st` 中 `lsm6dsv16x_fifo_temp_batch_t` 枚举，默认值为上电配置。编码 0x0 不批量存储，0x1 为 1.875 Hz，0x2 为 15 Hz，0x3 为 60 Hz；完整宏对照见后文。；默认值：`0x0`；合法值：`0x0, 0x1, 0x2, 0x3` |
| `sflp-odr` | `int` | 低功耗传感器融合（Sensor Fusion Low Power，SFLP）的输出数据率（ODR），以每秒采样数（Hz）表示。取值依据 `hal/st` 中 `lsm6dsv16x_sflp_data_rate_t` 枚举，默认值为上电配置。编码 0x0–0x5 分别为 15、30、60、120、240、480 Hz，完整宏对照见后文。；默认值：`0x3`；合法值：`0x0, 0x1, 0x2, 0x3, 0x4, 0x5` |
| `sflp-fifo-enable` | `int` | 指定哪些低功耗传感器融合（SFLP）分量批量写入 FIFO，取值依据 `hal/st` 中 `lsm6dsv16x_fifo_sflp_raw_t` 枚举，默认值为上电配置。编码 0x0 关闭；0x1 游戏旋转（Game Rotation）；0x2 重力（Gravity）；0x3 游戏旋转加重力；0x4 陀螺仪偏置（GBIAS）；0x5 游戏旋转加偏置；0x6 重力加偏置；0x7 三者全部。完整宏对照见后文。；默认值：`0x0`；合法值：`0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7` |
| `friendly-name` | `string` | 描述传感器的可读字符串，可帮助主机操作系统区分同型号的多个实例，例如笔记本电脑上盖与底座的加速度计。此属性定义于[HID Usage Tables规范](https://usb.org/sites/default/files/hut1_3_0.pdf)第22.5节“通用传感器属性用途”（Generic Sensor Property Usages）。 |

本页没有已弃用的节点专用属性。

## 22.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `array` | **必需**。给出寻址设备所需的信息，具体含义随设备及 `compatible` 而变化。通常是一组地址与长度对，每对称为寄存器块（Register Block），数值通常写为十六进制。参见规范v0.4第2.3.6节及[重要属性](../devicetree/P003_语法与结构.md#dt-important-props) |
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

## 参数编码原始对照 15

```text
- 0x0 # LSM6DSV80X_HG_XL_ODR_OFF
- 0x3 # LSM6DSV80X_HG_XL_ODR_AT_480Hz
- 0x4 # LSM6DSV80X_HG_XL_ODR_AT_960Hz
- 0x5 # LSM6DSV80X_HG_XL_ODR_AT_1920Hz
- 0x6 # LSM6DSV80X_HG_XL_ODR_AT_3840Hz
- 0x7 # LSM6DSV80X_HG_XL_ODR_AT_7680Hz
```

## 参数编码原始对照 16

```text
- 2   # LSM6DSV80X_DT_FS_2G  (0.061 mg/LSB)
- 4   # LSM6DSV80X_DT_FS_4G  (0.122 mg/LSB)
- 8   # LSM6DSV80X_DT_FS_8G  (0.244 mg/LSB)
- 16  # LSM6DSV80X_DT_FS_16G (0.488 mg/LSB)
- 32  # LSM6DSV80X_DT_FS_32G (0.976 mg/LSB)
- 64  # LSM6DSV80X_DT_FS_64G (1.952 mg/LSB)
- 80  # LSM6DSV80X_DT_FS_80G (3.904 mg/LSB)
```

## 参数编码原始对照 17

```text
- 0x0 # power-up configuration
- 0x1 # LSM6DSV80X_DT_FS_250DPS  (8.75 mdps/LSB)
- 0x2 # LSM6DSV80X_DT_FS_500DPS  (17.50 mdps/LSB)
- 0x3 # LSM6DSV80X_DT_FS_1000DPS (35 mdps/LSB)
- 0x4 # LSM6DSV80X_DT_FS_2000DPS (70 mdps/LSB)
- 0x5 # LSM6DSV80X_DT_FS_4000DPS (140 mdps/LSB)
```

## 参数编码原始对照 20

```text
- 0 # LSM6DSVXXX_DT_GPIO_INT_EDGE_TO_ACTIVE
- 1 # LSM6DSVXXX_DT_GPIO_INT_LEVEL_ACTIVE
```

## 参数编码原始对照 23

```text
- 0x00 # LSM6DSVXXX_DT_ODR_OFF
- 0x01 # LSM6DSVXXX_DT_ODR_AT_1Hz875
- 0x02 # LSM6DSVXXX_DT_ODR_AT_7Hz5
- 0x03 # LSM6DSVXXX_DT_ODR_AT_15Hz
- 0x04 # LSM6DSVXXX_DT_ODR_AT_30Hz
- 0x05 # LSM6DSVXXX_DT_ODR_AT_60Hz
- 0x06 # LSM6DSVXXX_DT_ODR_AT_120Hz
- 0x07 # LSM6DSVXXX_DT_ODR_AT_240Hz
- 0x08 # LSM6DSVXXX_DT_ODR_AT_480Hz
- 0x09 # LSM6DSVXXX_DT_ODR_AT_960Hz
- 0x0a # LSM6DSVXXX_DT_ODR_AT_1920Hz
- 0x0b # LSM6DSVXXX_DT_ODR_AT_3840Hz
- 0x0c # LSM6DSVXXX_DT_ODR_AT_7680Hz
- 0x13 # LSM6DSVXXX_DT_ODR_HA01_AT_15Hz625
- 0x14 # LSM6DSVXXX_DT_ODR_HA01_AT_31Hz25
- 0x15 # LSM6DSVXXX_DT_ODR_HA01_AT_62Hz5
- 0x16 # LSM6DSVXXX_DT_ODR_HA01_AT_125Hz
- 0x17 # LSM6DSVXXX_DT_ODR_HA01_AT_250Hz
- 0x18 # LSM6DSVXXX_DT_ODR_HA01_AT_500Hz
- 0x19 # LSM6DSVXXX_DT_ODR_HA01_AT_1000Hz
- 0x1a # LSM6DSVXXX_DT_ODR_HA01_AT_2000Hz
- 0x1b # LSM6DSVXXX_DT_ODR_HA01_AT_4000Hz
- 0x1c # LSM6DSVXXX_DT_ODR_HA01_AT_8000Hz
- 0x23 # LSM6DSVXXX_DT_ODR_HA02_AT_12Hz5
- 0x24 # LSM6DSVXXX_DT_ODR_HA02_AT_25Hz
- 0x25 # LSM6DSVXXX_DT_ODR_HA02_AT_50Hz
- 0x26 # LSM6DSVXXX_DT_ODR_HA02_AT_100Hz
- 0x27 # LSM6DSVXXX_DT_ODR_HA02_AT_200Hz
- 0x28 # LSM6DSVXXX_DT_ODR_HA02_AT_400Hz
- 0x29 # LSM6DSVXXX_DT_ODR_HA02_AT_800Hz
- 0x2a # LSM6DSVXXX_DT_ODR_HA02_AT_1600Hz
- 0x2b # LSM6DSVXXX_DT_ODR_HA02_AT_3200Hz
- 0x2c # LSM6DSVXXX_DT_ODR_HA02_AT_6400Hz
```

## 参数编码原始对照 24

```text
- 0x00 # LSM6DSVXXX_DT_ODR_OFF
- 0x01 # LSM6DSVXXX_DT_ODR_AT_1Hz875
- 0x02 # LSM6DSVXXX_DT_ODR_AT_7Hz5
- 0x03 # LSM6DSVXXX_DT_ODR_AT_15Hz
- 0x04 # LSM6DSVXXX_DT_ODR_AT_30Hz
- 0x05 # LSM6DSVXXX_DT_ODR_AT_60Hz
- 0x06 # LSM6DSVXXX_DT_ODR_AT_120Hz
- 0x07 # LSM6DSVXXX_DT_ODR_AT_240Hz
- 0x08 # LSM6DSVXXX_DT_ODR_AT_480Hz
- 0x09 # LSM6DSVXXX_DT_ODR_AT_960Hz
- 0x0a # LSM6DSVXXX_DT_ODR_AT_1920Hz
- 0x0b # LSM6DSVXXX_DT_ODR_AT_3840Hz
- 0x0c # LSM6DSVXXX_DT_ODR_AT_7680Hz
- 0x13 # LSM6DSVXXX_DT_ODR_HA01_AT_15Hz625
- 0x14 # LSM6DSVXXX_DT_ODR_HA01_AT_31Hz25
- 0x15 # LSM6DSVXXX_DT_ODR_HA01_AT_62Hz5
- 0x16 # LSM6DSVXXX_DT_ODR_HA01_AT_125Hz
- 0x17 # LSM6DSVXXX_DT_ODR_HA01_AT_250Hz
- 0x18 # LSM6DSVXXX_DT_ODR_HA01_AT_500Hz
- 0x19 # LSM6DSVXXX_DT_ODR_HA01_AT_1000Hz
- 0x1a # LSM6DSVXXX_DT_ODR_HA01_AT_2000Hz
- 0x1b # LSM6DSVXXX_DT_ODR_HA01_AT_4000Hz
- 0x1c # LSM6DSVXXX_DT_ODR_HA01_AT_8000Hz
- 0x23 # LSM6DSVXXX_DT_ODR_HA02_AT_12Hz5
- 0x24 # LSM6DSVXXX_DT_ODR_HA02_AT_25Hz
- 0x25 # LSM6DSVXXX_DT_ODR_HA02_AT_50Hz
- 0x26 # LSM6DSVXXX_DT_ODR_HA02_AT_100Hz
- 0x27 # LSM6DSVXXX_DT_ODR_HA02_AT_200Hz
- 0x28 # LSM6DSVXXX_DT_ODR_HA02_AT_400Hz
- 0x29 # LSM6DSVXXX_DT_ODR_HA02_AT_800Hz
- 0x2a # LSM6DSVXXX_DT_ODR_HA02_AT_1600Hz
- 0x2b # LSM6DSVXXX_DT_ODR_HA02_AT_3200Hz
- 0x2c # LSM6DSVXXX_DT_ODR_HA02_AT_6400Hz
```

## 参数编码原始对照 27

```text
- 0x0 # LSM6DSVXXX_DT_XL_NOT_BATCHED
- 0x1 # LSM6DSVXXX_DT_XL_BATCHED_AT_1Hz875
- 0x2 # LSM6DSVXXX_DT_XL_BATCHED_AT_7Hz5
- 0x3 # LSM6DSVXXX_DT_XL_BATCHED_AT_15Hz
- 0x4 # LSM6DSVXXX_DT_XL_BATCHED_AT_30Hz
- 0x5 # LSM6DSVXXX_DT_XL_BATCHED_AT_60Hz
- 0x6 # LSM6DSVXXX_DT_XL_BATCHED_AT_120Hz
- 0x7 # LSM6DSVXXX_DT_XL_BATCHED_AT_240Hz
- 0x8 # LSM6DSVXXX_DT_XL_BATCHED_AT_480Hz
- 0x9 # LSM6DSVXXX_DT_XL_BATCHED_AT_960Hz
- 0xa # LSM6DSVXXX_DT_XL_BATCHED_AT_1920Hz
- 0xb # LSM6DSVXXX_DT_XL_BATCHED_AT_3840Hz
- 0xc # LSM6DSVXXX_DT_XL_BATCHED_AT_7680Hz
```

## 参数编码原始对照 28

```text
- 0x0 # LSM6DSVXXX_DT_GY_NOT_BATCHED
- 0x1 # LSM6DSVXXX_DT_GY_BATCHED_AT_1Hz875
- 0x2 # LSM6DSVXXX_DT_GY_BATCHED_AT_7Hz5
- 0x3 # LSM6DSVXXX_DT_GY_BATCHED_AT_15Hz
- 0x4 # LSM6DSVXXX_DT_GY_BATCHED_AT_30Hz
- 0x5 # LSM6DSVXXX_DT_GY_BATCHED_AT_60Hz
- 0x6 # LSM6DSVXXX_DT_GY_BATCHED_AT_120Hz
- 0x7 # LSM6DSVXXX_DT_GY_BATCHED_AT_240Hz
- 0x8 # LSM6DSVXXX_DT_GY_BATCHED_AT_480Hz
- 0x9 # LSM6DSVXXX_DT_GY_BATCHED_AT_960Hz
- 0xa # LSM6DSVXXX_DT_GY_BATCHED_AT_1920Hz
- 0xb # LSM6DSVXXX_DT_GY_BATCHED_AT_3840Hz
- 0xc # LSM6DSVXXX_DT_GY_BATCHED_AT_7680Hz
```

## 参数编码原始对照 29

```text
- 0x0 # LSM6DSVXXX_DT_TEMP_NOT_BATCHED
- 0x1 # LSM6DSVXXX_DT_TEMP_BATCHED_AT_1Hz875
- 0x2 # LSM6DSVXXX_DT_TEMP_BATCHED_AT_15Hz
- 0x3 # LSM6DSVXXX_DT_TEMP_BATCHED_AT_60Hz
```

## 参数编码原始对照 30

```text
- 0x0 # LSM6DSVXXX_DT_SFLP_ODR_AT_15Hz
- 0x1 # LSM6DSVXXX_DT_SFLP_ODR_AT_30Hz
- 0x2 # LSM6DSVXXX_DT_SFLP_ODR_AT_60Hz
- 0x3 # LSM6DSVXXX_DT_SFLP_ODR_AT_120Hz
- 0x4 # LSM6DSVXXX_DT_SFLP_ODR_AT_240Hz
- 0x5 # LSM6DSVXXX_DT_SFLP_ODR_AT_480Hz
```

## 参数编码原始对照 31

```text
- 0x0 # LSM6DSVXXX_DT_SFLP_FIFO_OFF
- 0x1 # LSM6DSVXXX_DT_SFLP_FIFO_GAME_ROTATION
- 0x2 # LSM6DSVXXX_DT_SFLP_FIFO_GRAVITY
- 0x3 # LSM6DSVXXX_DT_SFLP_FIFO_GAME_ROTATION_GRAVITY
- 0x4 # LSM6DSVXXX_DT_SFLP_FIFO_GBIAS
- 0x5 # LSM6DSVXXX_DT_SFLP_FIFO_GAME_ROTATION_GBIAS
- 0x6 # LSM6DSVXXX_DT_SFLP_FIFO_GRAVITY_GBIAS
- 0x7 # LSM6DSVXXX_DT_SFLP_FIFO_GAME_ROTATION_GRAVITY_GBIAS
```

## SPI枚举原始对照 3

```text
  0    SPI_FULL_DUPLEX
  2048 SPI_HALF_DUPLEX
```

## SPI枚举原始对照 4

```text
  0     SPI_FRAME_FORMAT_MOTOROLA
  32768 SPI_FRAME_FORMAT_TI
```

## 22.3\_寄存器块命名原例

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

[上一章](P021_st_lsm6dsv80x-i3c.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P023_st_lsm9ds0-gyro-i2c.md)
