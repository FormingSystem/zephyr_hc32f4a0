---
id: learning.zephyr-docs.sensor-st-lsm-stm32-binding-reference.page-6
title: st_lsm6dso-spi
kind: reference
status: maintained
domains: [zephyr, devicetree, sensor]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/sensor/st,lsm6dso-spi.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第6章\_st_lsm6dso-spi

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/sensor/st,lsm6dso-spi.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="st-lsm6dso-on-spi-bus"></a>
<a id="dtbinding-st-lsm6dso-spi"></a>

兼容字符串（Compatible String）：`st,lsm6dso`。厂商：[ STMicroelectronics ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-st)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=st,lsm6dso)。

驱动源码（Driver Source）：[drivers/sensor/st/lsm6dso/lsm6dso.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dso/lsm6dso.c)。

<a id="description"></a>

通过 SPI 总线访问的 STMicroelectronics LSM6DSO 六轴惯性测量单元（6-axis Inertial Measurement Unit，IMU）。

<a id="examples"></a>

官方设备树配置原例：

```dts
#include <zephyr/dt-bindings/sensor/lsm6dso.h>

lsm6dso: lsm6dso@0 {
  /* ... */

  accel-pm = <LSM6DSO_DT_XL_ULP_MODE>;
  accel-range = <LSM6DSO_DT_FS_8G>;
  accel-odr = <LSM6DSO_DT_ODR_1Hz6>;
  gyro-pm = <LSM6DSO_DT_GY_NORMAL_MODE>;
  gyro-range = <LSM6DSO_DT_FS_2000DPS>;
  gyro-odr = <LSM6DSO_DT_ODR_6667Hz>;
};
```

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 6.1\_节点专用属性

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
| `irq-gpios` | `phandle-array` | 数据就绪引脚（Data Ready，DRDY）。传感器产生的信号默认高电平有效（Active High），属性标志必须正确描述驱动实际接收到的信号。 |
| `int-pin` | `int` | 选择数据就绪（DRDY）引脚编号：1 为 INT1，2 为 INT2。本属性可选，省略时默认 1，与上电配置一致。；默认值：`1`；合法值：`1, 2` |
| `accel-pm` | `int` | 加速度计电源模式（Power Mode），默认值为上电配置。编码 0 高性能（HP），1 低功耗／正常（LP Normal），2 超低功耗（ULP）；完整宏对照见后文。；默认值：`0`；合法值：`0, 1, 2` |
| `accel-range` | `int` | 量程（Range），单位为 g，默认值为上电配置。编码 0 为 2 g（0.061 mg/LSB），1 为 16 g（0.488 mg/LSB），2 为 4 g（0.122 mg/LSB），3 为 8 g（0.244 mg/LSB）。原文在第一项注明 LSM6DSO32 的这些值加倍，完整原表保留于后文。；默认值：`0`；合法值：`0, 1, 2, 3` |
| `accel-odr` | `int` | 默认加速度计输出数据率（ODR），以每秒采样数（Hz）表示，默认值为上电配置。编码 0 关闭，1–10 分别为 12.5、26、52、104、208、417、833、1667、3333、6667 Hz，11 为 1.6 Hz；宏名和数值按后文原表保留。；默认值：`0`；合法值：`0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11` |
| `accel-lp-filter` | `int` | 应用于加速度值的低通滤波强度（Low-pass Filtering），默认值为上电配置。通过 `CTRL1_XL` 的 `lpf2_xl_en` 位启用 LPF2。编码 0–7 分别为 ODR/2、/10、/20、/45、/100、/200、/400、/800；完整宏对照见后文。；默认值：`0`；合法值：`0, 1, 2, 3, 4, 5, 6, 7` |
| `gyro-pm` | `int` | 陀螺仪电源模式（Power Mode），默认值为上电配置。编码 0 高性能（HP），1 正常（Normal），完整宏对照见后文。；默认值：`0`；合法值：`0, 1` |
| `gyro-range` | `int` | 陀螺仪量程（Range），单位为度每秒（dps），默认值为上电配置。编码 0 → 250 dps（8.75 mdps/LSB）；1 → 125 dps（4.375 mdps/LSB）；2 → 500 dps（17.50 mdps/LSB）；4 → 1000 dps（35 mdps/LSB）；6 → 2000 dps（70 mdps/LSB）。；默认值：`0`；合法值：`0, 1, 2, 4, 6` |
| `gyro-odr` | `int` | 默认陀螺仪输出数据率（ODR），以每秒采样数（Hz）表示，默认值为上电配置。编码 0 关闭，1–10 分别为 12.5、26、52、104、208、417、833、1667、3333、6667 Hz；完整宏对照见后文。；默认值：`0`；合法值：`0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10` |
| `drdy-pulsed` | `boolean` | 启用时选择数据就绪中断的脉冲模式（Pulsed Mode），禁用时选择锁存模式（Latched Mode）。 |
| `tap-mode` | `int` | 敲击模式（Tap Mode），默认值为上电配置。编码 0 为单击（`LSM6DSO_DT_SINGLE_TAP`），1 为单击与双击（`LSM6DSO_DT_SINGLE_DOUBLE_TAP`）。；默认值：`0`；合法值：`0, 1` |
| `tap-threshold` | `array` | X/Y/Z 轴敲击阈值（Tap Threshold），默认值为上电配置，各轴值范围为 0x00–0x1F。用于启动对应轴敲击事件检测；每个阈值是对应 2 g 满量程的无符号 5 位数，零表示禁用该轴检测。例如 X 为 12、Z 为 14、Y 禁用时，设备树写作 `tap-threshold = <12>, <0>, <14>`；对应 X = 12 × 2g/32 = 750 mg，Z = 14 × 2g/32 = 875 mg。；默认值：`[0, 0, 0]` |
| `tap-shock` | `int` | 敲击冲击时间值（Tap Shock），默认值为上电配置，取值 0x0–0x3。表示超过阈值的信号可被识别为敲击事件的最长持续时间。0 对应 `4*1/ODR`，1 LSB 对应 `8*1/ODR`。；默认值：`0x0` |
| `tap-latency` | `int` | 敲击间隔（Tap Latency），默认值为上电配置，取值 0x0–0xF。启用双击识别时，表示连续两次敲击被判为双击的最大间隔。0 对应 `16*1/ODR`，1 LSB 对应 `32*1/ODR`。；默认值：`0x0` |
| `tap-quiet` | `int` | 敲击后的安静时间（Quiet Time），默认值为上电配置，取值 0x0–0x3。首次敲击后的这段时间内不能有任何超过阈值的事件。0 对应 `2*1/ODR`，1 LSB 对应 `4*1/ODR`。；默认值：`0x0` |
| `friendly-name` | `string` | 描述传感器的可读字符串，可帮助主机操作系统区分同型号的多个实例，例如笔记本电脑上盖与底座的加速度计。此属性定义于[HID Usage Tables规范](https://usb.org/sites/default/files/hut1_3_0.pdf)第22.5节“通用传感器属性用途”（Generic Sensor Property Usages）。 |

本页没有已弃用的节点专用属性。

## 6.2\_基础属性

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

## 参数编码原始对照 17

```text
- 0 # LSM6DSO_DT_XL_HP_MODE
- 1 # LSM6DSO_DT_XL_LP_NORMAL_MODE
- 2 # LSM6DSO_DT_XL_ULP_MODE
```

## 参数编码原始对照 18

```text
- 0 # LSM6DSO_DT_FS_2G  (0.061 mg/LSB) (LSM6DSO32 will be double these values)
- 1 # LSM6DSO_DT_FS_16G (0.488 mg/LSB)
- 2 # LSM6DSO_DT_FS_4G  (0.122 mg/LSB)
- 3 # LSM6DSO_DT_FS_8G  (0.244 mg/LSB)
```

## 参数编码原始对照 19

```text
- 0  # LSM6DSO_DT_ODR_OFF
- 1  # LSM6DSO_DT_ODR_12Hz5
- 2  # LSM6DSO_DT_ODR_26H
- 3  # LSM6DSO_DT_ODR_52Hz
- 4  # LSM6DSO_DT_ODR_104Hz
- 5  # LSM6DSO_DT_ODR_208Hz
- 6  # LSM6DSO_DT_ODR_417Hz
- 7  # LSM6DSO_DT_ODR_833Hz
- 8  # LSM6DSO_DT_ODR_1667Hz
- 9  # LSM6DSO_DT_ODR_3333Hz
- 10 # LSM6DSO_DT_ODR_6667Hz
- 11 # LSM6DSO_DT_ODR_1Hz6
```

## 参数编码原始对照 20

```text
- 0 # LSM6DSO_DT_LP_ODR_DIV_2
- 1 # LSM6DSO_DT_LP_ODR_DIV_10
- 2 # LSM6DSO_DT_LP_ODR_DIV_20
- 3 # LSM6DSO_DT_LP_ODR_DIV_45
- 4 # LSM6DSO_DT_LP_ODR_DIV_100
- 5 # LSM6DSO_DT_LP_ODR_DIV_200
- 6 # LSM6DSO_DT_LP_ODR_DIV_400
- 7 # LSM6DSO_DT_LP_ODR_DIV_800
```

## 参数编码原始对照 21

```text
- 0 # LSM6DSO_DT_GY_HP_MODE
- 1 # LSM6DSO_DT_GY_NORMAL_MODE
```

## 参数编码原始对照 22

```text
- 0 # LSM6DSO_DT_FS_250DPS  (8.75 mdps/LSB)
- 1 # LSM6DSO_DT_FS_125DPS  (4.375 mdps/LSB)
- 2 # LSM6DSO_DT_FS_500DPS  (17.50 mdps/LSB)
- 4 # LSM6DSO_DT_FS_1000DPS (35 mdps/LSB)
- 6 # LSM6DSO_DT_FS_2000DPS (70 mdps/LSB)
```

## 参数编码原始对照 23

```text
- 0  # LSM6DSO_DT_ODR_OFF
- 1  # LSM6DSO_DT_ODR_12Hz5
- 2  # LSM6DSO_DT_ODR_26H
- 3  # LSM6DSO_DT_ODR_52Hz
- 4  # LSM6DSO_DT_ODR_104Hz
- 5  # LSM6DSO_DT_ODR_208Hz
- 6  # LSM6DSO_DT_ODR_417Hz
- 7  # LSM6DSO_DT_ODR_833Hz
- 8  # LSM6DSO_DT_ODR_1667Hz
- 9  # LSM6DSO_DT_ODR_3333Hz
- 10 # LSM6DSO_DT_ODR_6667Hz
```

## 参数编码原始对照 25

```text
- 0 # LSM6DSO_DT_SINGLE_TAP
- 1 # LSM6DSO_DT_SINGLE_DOUBLE_TAP
```

## 敲击阈值原例

```dts
    tap-threshold = <12>, <0>, <14>
```

译注：敲击阈值原例未写末尾分号，此处按原文保留。

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

[上一章](P005_st_lsm6dso-i2c.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P007_st_lsm6dso16is-i2c.md)
