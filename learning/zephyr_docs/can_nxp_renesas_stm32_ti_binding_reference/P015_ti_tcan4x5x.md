---
id: learning.zephyr-docs.can-nxp-renesas-stm32-ti-binding-reference.page-15
title: ti_tcan4x5x
kind: reference
status: maintained
domains: [zephyr, devicetree, can]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/can/ti,tcan4x5x.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第15章\_ti_tcan4x5x

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/can/ti,tcan4x5x.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="ti-tcan4x5x-on-spi-bus"></a>
<a id="dtbinding-ti-tcan4x5x"></a>
<a id="std-dtcompatible-ti-tcan4x5x"></a>

兼容字符串（Compatible String）：`ti,tcan4x5x`。厂商：[ Texas Instruments ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-ti)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=ti,tcan4x5x)。

驱动源码（Driver Source）：[drivers/can/can_tcan4x5x.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/can_tcan4x5x.c)。

<a id="description"></a>

Texas Instruments TCAN4x5x SPI CAN FD控制器。

<a id="examples"></a>

官方设备树配置原例：

```dts
&spi0 {
  tcan4x5x: can@0 {
    compatible = ti,tcan4x5x";
    reg = <0>;
    spi-max-frequency = <18000000>;
    clock-frequency = <40000000>;
    device-state-gpios = <&gpio0 0 GPIO_ACTIVE_LOW>;
    device-wake-gpios = <&gpio0 1 GPIO_ACTIVE_HIGH>;
    reset-gpios = <&gpio0 2 GPIO_ACTIVE_HIGH>;
    int-gpios = <&gpio0 3 GPIO_ACTIVE_LOW>;
    bosch,mram-cfg = <0x0 15 15 10 0 0 10 10>;
    ti,nwkrq-voltage-vio;
    status = "okay";

    can-transceiver {
      max-bitrate = <8000000>;
    };
  };
};
```

译注：官方原例的 `compatible = ti,tcan4x5x";` 缺少起始双引号，此处按原文保留。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

<a id="top-level-properties"></a>

## 15.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `clock-frequency` | `int` | **必需**。TCAN4x5x振荡器时钟频率，单位为Hz，支持20 MHz或40 MHz。；合法值：`20000000, 40000000` |
| `device-state-gpios` | `phandle-array` | 连接到TCAN4x5x nWKRQ输出的GPIO；该信号低电平有效（Active Low）。 |
| `device-wake-gpios` | `phandle-array` | 连接到TCAN4x5x WAKE输入的GPIO；该信号为高电压信号，高电平有效（Active High）。 |
| `reset-gpios` | `phandle-array` | 连接到TCAN4x5x RST输入的GPIO；该信号高电平有效。 |
| `int-gpios` | `phandle-array` | **必需**。连接到TCAN4x5x nINT中断输出的GPIO；该信号为开漏（Open-drain）输出，低电平有效。 |
| `ti,nwkrq-voltage-vio` | `boolean` | nWKRQ引脚通用输出（General-Purpose Output，GPO）缓冲器的电源轨配置。设置本属性时，缓冲器配置为开漏，需要外部电阻上拉到VIO电源轨；未设置时，缓冲器以内部电源轨供电并配置为推挽（Push-pull）。 |
| `bosch,mram-cfg` | `array` | **必需**。Bosch M_CAN消息RAM（Message RAM）配置，单元按顺序为`offset`、`std-filter-elements`、`ext-filter-elements`、`rx-fifo0-elements`、`rx-fifo1-elements`、`rx-buffer-elements`、`tx-event-fifo-elements`、`tx-buffer-elements`。`offset`指定后续元素在消息RAM中的起始地址偏移；非共享RAM通常设`0x0`。其余单元指定每种过滤器／FIFO／缓冲区分配的元素数量。<br>IP支持范围：11位过滤器0至128元素／0至128字；29位过滤器0至64元素／0至128字；接收FIFO0、接收FIFO1、接收缓冲区各为0至64元素／0至1152字；发送事件FIFO为0至32元素／0至64字；发送缓冲区为0至32元素／0至576字。下方保留原始排列与容量表。；长度范围：`8 to 8` |
| `bosch,timestamp-counter-prescaler` | `int` | 内部时间戳计数器（Timestamp Counter）时间单位，以CAN位时间的倍数表示，有效范围1至16。默认预分频值1，即一个CAN位时间。；默认值：`1`；范围：`1 to 16` |
| `bitrate-data` | `int` | 数据阶段（Data Phase）初始位速率，单位为bit/s；未设置时使用`CONFIG_CAN_DEFAULT_BITRATE_DATA`。 |
| `sample-point-data` | `int` | 数据阶段初始采样点，以千分比表示，例如875代表87.5%。未设置或为0时，位速率大于800 kbit/s默认75.0%，大于500 kbit/s默认80.0%，其余默认87.5%。 |
| `bitrate` | `int` | 初始位速率（Bitrate），单位为bit/s。未设置时使用`CONFIG_CAN_DEFAULT_BITRATE`。 |
| `sample-point` | `int` | 初始采样点（Sample Point），单位为千分比，例如875代表87.5%。未设置或设为0时，位速率大于800 kbit/s默认75.0%，大于500 kbit/s默认80.0%，其余默认87.5%。 |
| `phys` | `phandle` | 可主动控制的CAN收发器（Transceiver），下方保留完整设备树原例。 |
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

本页没有已弃用的节点专用属性。

## 15.2\_基础属性

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

<a id="child-node-properties"></a>

## 子节点属性

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `min-bitrate` | `int` | CAN收发器支持的最低位速率，单位为bit/s。 |
| `max-bitrate` | `int` | **必需**。CAN收发器支持的最高位速率，单位为bit/s。 |

## 消息RAM数组与容量原表

数组单元顺序：

```text
<offset std-filter-elements ext-filter-elements rx-fifo0-elements rx-fifo1-elements
rx-buffer-elements tx-event-fifo-elements tx-buffer-elements>
```

容量原表；中文含义与单位见属性表：

```text
11-bit Filter    0-128 elements / 0-128 words
29-bit Filter     0-64 elements / 0-128 words
Rx FIFO 0                   0-64 elements / 0-1152 words
Rx FIFO 1                   0-64 elements / 0-1152 words
Rx Buffers          0-64 elements / 0-1152 words
Tx Event FIFO     0-32 elements / 0-64 words
Tx Buffers          0-32 elements / 0-576 words
```

## CAN收发器配置原例

```dts
  transceiver0: can-phy0 {
    compatible = "nxp,tja1040", "can-transceiver-gpio";
    standby-gpios = <gpioa 0 GPIO_ACTIVE_HIGH>;
    max-bitrate = <1000000>;
    #phy-cells = <0>;
  };

  &can0 {
    status = "okay";

    phys = <&transceiver0>;
  };
```

译注：原文 `standby-gpios` 的 `gpioa` 前未写 `&`；这里保留原例，实际配置须按设备树节点引用语法核对。

## SPI枚举原始对照 16

```text
  0    SPI_FULL_DUPLEX
  2048 SPI_HALF_DUPLEX
```

## SPI枚举原始对照 17

```text
  0     SPI_FRAME_FORMAT_MOTOROLA
  32768 SPI_FRAME_FORMAT_TI
```

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

[上一章](P014_ti_mspm0-canfd.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P016_zephyr_native-linux-can.md)
