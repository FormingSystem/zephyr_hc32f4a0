---
id: learning.zephyr-docs.hardware.spiapi-0
title: SPI公共接口
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第318章\_SPI公共接口

原文：[group__spi__interface](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html)。读取日期：2026-10-13，`latest`。

## 318.1\_接口范围与传输模型

**串行外设接口（Serial Peripheral Interface，SPI）**通过时钟和数据线交换数据；本页为控制器提供公共接口，声明位于 `zephyr/drivers/spi.h`，自 Zephyr 1.0 提供，接口版本为 1.1.0。

**控制器（Controller）**控制时钟、**片选（Chip Select，CS）**和通信时序；**外设（Peripheral）**等待控制器提供时钟并选中自己。同步（Synchronous）调用在传输完成后返回；异步（Asynchronous）调用启动传输后返回，用回调（Callback）或信号（Signal）报告完成。异步调用仍可能阻塞：总线已被占用时，它会等待总线可用，才能启动此次传输。

SPI 数据字（Data Word）是移入或移出控制器硬件先进先出队列（First In, First Out，FIFO）的值，也是总线通信的原子单位。本接口也称它为数据帧（Data Frame）；一次传输可以包含任意数量的数据字。

相关分组为 [SPI 设备树接口](P329_SPI设备树宏.md)、[SPI 驱动后端](P324_SPI驱动后端接口.md)和 [SPI 模拟接口](P326_SPI模拟接口.md)。设备树（Devicetree）描述硬件连接及参数。[`spi_cs_control`](P319_SPI片选控制结构.md) 保存片选控制信息，[`spi_config`](P320_SPI控制器配置结构.md) 保存通信配置，[`spi_dt_spec`](P321_SPI设备树描述结构.md) 保存来自设备树的完整 SPI 信息，[`spi_buf`](P322_SPI缓冲区结构.md) 描述一个缓冲区，[`spi_buf_set`](P323_SPI缓冲区集合结构.md) 描述缓冲区集合。

## 318.2\_操作模式、时钟、数据字和片选

<a id="ga398a8ae1c4799e77fb6c067b6d47294a"></a>

操作类型 [`spi_operation_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#ga398a8ae1c4799e77fb6c067b6d47294a) 是不透明的 SPI 操作配置类型。原页声明如下：

```c
typedef uint16_t spi_operation_t;
```

下列常量组合到操作字段中；`BIT(n)` 表示第 n 位的掩码。控制器和外设模式由最低位选择，旧名称保留为弃用别名。

| 宏 | 原定义 | 含义 |
| --- | --- | --- |
| <a id="gace0f0d954c2bd7d603c4003289c11102"></a>[`SPI_OP_MODE_CONTROLLER`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#gace0f0d954c2bd7d603c4003289c11102) | `0U` | 控制器模式 |
| <a id="gaa1f42ffeac36380f4d1d8f84bda2990b"></a>[`SPI_OP_MODE_PERIPHERAL`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#gaa1f42ffeac36380f4d1d8f84bda2990b) | `BIT(0)` | 外设模式 |
| <a id="ga5b9d40fa0f455b1e63f8040b3316b0da"></a>[`SPI_OP_MODE_MASTER`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#ga5b9d40fa0f455b1e63f8040b3316b0da) | `SPI_OP_MODE_CONTROLLER __DEPRECATED_MACRO` | 已弃用，使用控制器名称 |
| <a id="ga1c3310d3711cb99cdb78fa9d1c970779"></a>[`SPI_OP_MODE_SLAVE`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#ga1c3310d3711cb99cdb78fa9d1c970779) | `SPI_OP_MODE_PERIPHERAL __DEPRECATED_MACRO` | 已弃用，使用外设名称 |
| <a id="ga5a2be1003873beaa0ade10e7218d67d5"></a>[`SPI_MODE_CPOL`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#ga5a2be1003873beaa0ade10e7218d67d5) | `BIT(1)` | 时钟极性（Clock Polarity，CPOL） |
| <a id="ga35e98b37e3ec4889a90100abe884590f"></a>[`SPI_MODE_CPHA`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#ga35e98b37e3ec4889a90100abe884590f) | `BIT(2)` | 时钟相位（Clock Phase，CPHA） |
| <a id="ga8619b297de563eca6852af34c79daa62"></a>[`SPI_MODE_LOOP`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#ga8619b297de563eca6852af34c79daa62) | `BIT(3)` | 控制器回环（Loopback）模式 |
| <a id="ga7761f42c6241cf396fc02d0de8617e46"></a>[`SPI_TRANSFER_MSB`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#ga7761f42c6241cf396fc02d0de8617e46) | `(0U)` | 最高有效位（Most Significant Bit，MSB）先传 |
| <a id="ga93504a76a265bedbe781c107beebc9dc"></a>[`SPI_TRANSFER_LSB`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#ga93504a76a265bedbe781c107beebc9dc) | `BIT(4)` | 最低有效位（Least Significant Bit，LSB）先传 |
| <a id="gae917312adef283b4bf67cdb53566e4bb"></a>[`SPI_HOLD_ON_CS`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#gae917312adef283b4bf67cdb53566e4bb) | `BIT(12)` | 事务结束后尝试保持片选有效 |
| <a id="gafe8dc164d6fc0a0f93f2ff9d5381af14"></a>[`SPI_LOCK_ON`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#gafe8dc164d6fc0a0f93f2ff9d5381af14) | `BIT(13)` | 保留 SPI 设备所有权 |
| <a id="ga44076fa14703997f7e3aefb2bfccd801"></a>[`SPI_CS_ACTIVE_HIGH`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#ga44076fa14703997f7e3aefb2bfccd801) | `BIT(14)` | 片选高电平有效 |

CPOL 置位时，时钟空闲状态为 1、活动状态为 0；清零时反之，后者为默认值。CPHA 置位时，在时钟从活动状态返回空闲状态的边沿采样；清零时，在空闲状态进入活动状态的边沿采样，后者为默认值。回环模式将发送数据反馈到接收端，用于测试，并非所有控制器都支持。

片选默认低电平有效；[`SPI_CS_ACTIVE_HIGH`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#ga44076fa14703997f7e3aefb2bfccd801) 将其改为高电平有效。若控制器不支持这种极性，可通过通用输入输出（General-Purpose Input/Output，GPIO）软件控制片选。[`SPI_HOLD_ON_CS`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#gae917312adef283b4bf67cdb53566e4bb) 要求在事务完成后尽可能保持片选有效，取决于硬件或驱动支持。

`SPI_LOCK_ON` 保留设备所有权，阻止其他调用方访问。后续传输及释放操作必须使用同一个 [`spi_config`](P320_SPI控制器配置结构.md) 指针，因为驱动可用指针比较识别所有者。需要连续安排异步传输时，应使用实时输入输出（Real-Time Input/Output，RTIO）接口 [`spi_iodev_submit`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#ga8b23855bdc7dab7d02b8f7daa7db651b)；不要从完成回调重新进入收发接口，回调可能处于中断服务程序（Interrupt Service Routine，ISR）上下文。

## 318.3\_线数、双工和帧格式

部分控制器支持双线、四线或八线的串行数据输入（Serial Data Input，SDI）连接。默认单线；未启用 Kconfig 配置项 [`CONFIG_SPI_EXTENDED_MODES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_EXTENDED_MODES) 时只支持单线。

| 宏 | 原定义 | 含义 |
| --- | --- | --- |
| <a id="ga7a183f157e8cb8b437857a0babbd923b"></a>[`SPI_LINES_SINGLE`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#ga7a183f157e8cb8b437857a0babbd923b) | `(0U << 16)` | 单线 |
| <a id="ga120ab60329d664d5d6e828f90251a98a"></a>[`SPI_LINES_DUAL`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#ga120ab60329d664d5d6e828f90251a98a) | `(1U << 16)` | 双线 |
| <a id="ga30866b948e995224de854e10a428bda5"></a>[`SPI_LINES_QUAD`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#ga30866b948e995224de854e10a428bda5) | `(2U << 16)` | 四线 |
| <a id="ga512d76085e600886654b8541aab31cf7"></a>[`SPI_LINES_OCTAL`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#ga512d76085e600886654b8541aab31cf7) | `(3U << 16)` | 八线 |
| <a id="gadc79f986c4b30fe5b263841cd8bb5676"></a>[`SPI_LINES_MASK`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#gadc79f986c4b30fe5b263841cd8bb5676) | `(0x3U << 16)` | 线数位掩码 |
| <a id="ga5585d5e81dec606b605f31b6745c35d3"></a>[`SPI_FULL_DUPLEX`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#ga5585d5e81dec606b605f31b6745c35d3) | `(0U << 11)` | 全双工（Full Duplex），默认 |
| <a id="ga602a7804b7434d7ebc1ebe6cb9b47a2f"></a>[`SPI_HALF_DUPLEX`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#ga602a7804b7434d7ebc1ebe6cb9b47a2f) | `(1U << 11)` | 半双工（Half Duplex），使用三线连接 |
| <a id="ga6a1b4ba33900165b6e09706903a6e6ee"></a>[`SPI_FRAME_FORMAT_MOTOROLA`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#ga6a1b4ba33900165b6e09706903a6e6ee) | `(0U << 15)` | Motorola 帧格式，默认 |
| <a id="ga22801357a9682371e3d8a10e522de388"></a>[`SPI_FRAME_FORMAT_TI`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#ga22801357a9682371e3d8a10e522de388) | `(1U << 15)` | TI 帧格式 |

双工和帧格式常量来自 `zephyr/dt-bindings/spi/spi.h`。全双工支持同时发送和接收，半双工由两个方向分时使用数据线。Motorola 与 Texas Instruments（TI）是此处帧格式使用的厂商名称。在 Motorola 格式中，整个传输期间片选保持有效；TI 格式只在实际传输前的一个串行时钟周期内使片选有效，传输期间反而无效，传输随时钟结束。最常用的 Motorola 格式为默认格式。

> 译注：原生成页面同时展示 16 位的 [`spi_operation_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#ga398a8ae1c4799e77fb6c067b6d47294a) 和位于第 16–17 位的扩展线数常量。本译文保留两者；使用扩展模式时须核对实际构建配置下的头文件类型，不能据此页面把高位配置截断到 16 位。

## 318.4\_设备树配置与片选初始化宏

以下宏从硬件描述生成 C 结构初始化器。展开代码中的 `DT_PROP` 读取节点属性，`DT_PROP_OR` 在属性缺失时使用默认值，`DT_REG_ADDR` 读取地址，`DT_DRV_INST` 按驱动实例取得节点；`COND_CODE_1` 依据值是否为 1 选择展开分支。`SPI_CS_CONTROL_INIT` 是下文说明的片选结构初始化宏。`node_id` 或 `spi_dev` 指 SPI 外设节点标识符，不是总线控制器节点；`inst` 是设备树实例编号，`operation_` 是所需操作字段。

<a id="gaf7d4888063e5b739f2a3bee295962bfe"></a>

`SPI_CONFIG_DT(node_id, operation_)` 为 [`spi_config`](P320_SPI控制器配置结构.md) 生成静态初始化器，读取频率、外设编号及片选等属性。展开式保留如下：

```c
{                                                               \
        .frequency = DT_PROP(node_id, spi_max_frequency),       \
        .operation = (operation_) |                             \
                DT_PROP(node_id, duplex) |                      \
                DT_PROP(node_id, frame_format) |                        \
                COND_CODE_1(DT_PROP(node_id, spi_cpol), SPI_MODE_CPOL, (0)) |   \
                COND_CODE_1(DT_PROP(node_id, spi_cpha), SPI_MODE_CPHA, (0)) |   \
                COND_CODE_1(DT_PROP(node_id, spi_hold_cs), SPI_HOLD_ON_CS, (0)) | \
                COND_CODE_1(DT_PROP(node_id, spi_lsb_first), SPI_TRANSFER_LSB, (0)) |   \
                COND_CODE_1(DT_PROP(node_id, spi_cs_high), SPI_CS_ACTIVE_HIGH, (0)),    \
        .peripheral = DT_REG_ADDR(node_id),                     \
        .cs = SPI_CS_CONTROL_INIT(node_id),                     \
        .word_delay = DT_PROP(node_id, spi_interframe_delay_ns),\
}
```

<a id="ga67837cbae6f29c5f8ad9a05dbc9b05f8"></a>

`SPI_CONFIG_DT_INST(inst, operation_)` 使用驱动实例节点，等价于：

```c
SPI_CONFIG_DT(DT_DRV_INST(inst), operation_)
```

<a id="ga81308d27cd78e65f0a3ddaa918f2a74a"></a>

`SPI_CS_CONTROL_INIT(node_id)` 初始化 [`spi_cs_control`](P319_SPI片选控制结构.md)，根据设备树选择 GPIO 或原生片选控制，并设置 `cs_is_gpio`：

```c
{                                                                               \
        COND_CODE_1(DT_SPI_DEV_HAS_CS_GPIOS(node_id),                           \
                        (SPI_CS_CONTROL_INIT_GPIO(node_id)),                    \
                        (SPI_CS_CONTROL_INIT_NATIVE(node_id)))                  \
        .cs_is_gpio = DT_SPI_DEV_HAS_CS_GPIOS(node_id),                         \
}
```

`DT_SPI_DEV_HAS_CS_GPIOS` 判断节点是否使用 GPIO 片选，`SPI_CS_CONTROL_INIT_GPIO` 和 `SPI_CS_CONTROL_INIT_NATIVE` 分别生成 GPIO 与原生片选初始化内容，`cs_is_gpio` 字段记录结果。原文给定以下设备树片段，其中 `GPIO_ACTIVE_LOW` 是低电平有效标志，后续 `DT_NODELABEL` 根据节点标签取得节点：

```dts
spi@abcd0001 {
        cs-gpios = <&gpio0 1 GPIO_ACTIVE_LOW>;
        spidev: spi-device@0 { ... };
};
```

对应初始化代码为：

```c
struct spi_cs_control ctrl =
        SPI_CS_CONTROL_INIT(DT_NODELABEL(spidev));
```

大致展开如下：`SPI_CS_GPIOS_DT_SPEC_GET` 取得片选 GPIO 描述，`MAX` 选择较大延时，`DIV_ROUND_UP` 将纳秒除以 1000 并向上取整为微秒。

```c
struct spi_cs_control ctrl = {
        .gpio = SPI_CS_GPIOS_DT_SPEC_GET(DT_NODELABEL(spidev)),
        .delay = DIV_ROUND_UP(MAX(DT_PROP_OR(node_id, spi_cs_setup_delay_ns, 0),
                                  DT_PROP_OR(node_id, spi_cs_hold_delay_ns, 0)),
                              1000),
        .cs_is_gpio = true,
};
```

> 译注：原说明称该宏“取得指针”，但所列展开式和示例实际是结构初始化器，不能将其直接当作返回指针的函数。原展开示例还保留了 `node_id`，而调用使用 `DT_NODELABEL(spidev)`；这里保留原例的写法，不把这个未替换标识符解释为已定义变量。

<a id="ga92195f45dac561b19204f6be21f62b55"></a>

`SPI_CS_CONTROL_INIT_INST(inst)` 使用当前驱动实例；使用前须定义 `DT_DRV_COMPAT`。原文同样称其取得指针，实际委托给上述初始化宏：

```c
SPI_CS_CONTROL_INIT(DT_DRV_INST(inst))
```

<a id="ga48aa19f45413d56b03596d10b72c732e"></a>

`SPI_CS_GPIOS_DT_SPEC_GET(spi_dev)` 取得 SPI 设备片选引脚的 [`gpio_dt_spec`](https://docs.zephyrproject.org/latest/doxygen/html/structgpio__dt__spec.html)，用设备的寄存器地址选择总线节点 `cs-gpios` 中的条目：

```c
GPIO_DT_SPEC_GET_BY_IDX_OR(DT_BUS(spi_dev), cs_gpios,   \
                           DT_REG_ADDR_RAW(spi_dev), {})
```

例如，原设备树为：

```dts
gpio1: gpio@abcd0001 { ... };

gpio2: gpio@abcd0002 { ... };

spi@abcd0003 {
        compatible = "vnd,spi";
        cs-gpios = <&gpio1 10 GPIO_ACTIVE_LOW>,
                   <&gpio2 20 GPIO_ACTIVE_LOW>;

        a: spi-dev-a@0 {
                reg = <0>;
        };

        b: spi-dev-b@1 {
                reg = <1>;
        };
};
```

两次取值分别生成对应 GPIO 控制器、引脚号和低电平有效标志：

```c
SPI_CS_GPIOS_DT_SPEC_GET(DT_NODELABEL(a)) \
      // { DEVICE_DT_GET(DT_NODELABEL(gpio1)), 10, GPIO_ACTIVE_LOW }
SPI_CS_GPIOS_DT_SPEC_GET(DT_NODELABEL(b)) \
      // { DEVICE_DT_GET(DT_NODELABEL(gpio2)), 20, GPIO_ACTIVE_LOW }
```

<a id="ga88fefbfadb8184806123e1f935a4ff7c"></a>

`SPI_CS_GPIOS_DT_SPEC_INST_GET(inst)` 是实例版本：

```c
SPI_CS_GPIOS_DT_SPEC_GET(DT_DRV_INST(inst))
```

## 318.5\_SPI 设备定义与 RTIO 设备宏

<a id="ga27af5f053c5fd4e9eef0900406fbf854"></a>

`SPI_DEVICE_DT_DEFINE(node_id, init_fn, pm, data, config, level, prio, api, ...)` 类似 `DEVICE_DT_DEINIT_DEFINE` 但不设置反初始化函数，增加 SPI 专用处理；启用 Kconfig 配置项 [`CONFIG_SPI_STATS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_STATS) 时可以使用专用设备状态及初始化包装。此宏不设置反初始化函数：

```c
SPI_DEVICE_DT_DEINIT_DEFINE(node_id, init_fn, NULL, pm, data, config,   \
                            level, prio, api, __VA_ARGS__)
```

<a id="gaf98b0cb38cb316b9fe05146bba34126d"></a>

`SPI_DEVICE_DT_DEINIT_DEFINE(node_id, init_fn, deinit_fn, pm, data, config, level, prio, api, ...)` 类似 `DEVICE_DT_DEINIT_DEFINE`，同时支持反初始化（Deinitialization）：

```c
Z_DEVICE_STATE_DEFINE(Z_DEVICE_DT_DEV_ID(node_id));                     \
Z_DEVICE_DEFINE(node_id, Z_DEVICE_DT_DEV_ID(node_id),                   \
                DEVICE_DT_NAME(node_id), init_fn, deinit_fn,            \
                Z_DEVICE_DT_FLAGS(node_id), pm, data, config,           \
                level, prio, api,                                       \
                &Z_DEVICE_STATE_NAME(Z_DEVICE_DT_DEV_ID(node_id)),      \
                __VA_ARGS__)
```

这些参数依次指定设备树节点、初始化函数、可选的反初始化函数、电源管理（Power Management，PM）信息、运行时数据指针、配置数据地址、初始化级别、优先级及应用程序编程接口（Application Programming Interface，API）函数表。没有 PM 信息时 `pm` 为 `NULL`；没有 API 表时 `api` 可为 `NULL`。初始化级别和优先级沿用 `SYS_INIT` 的定义。

<a id="ga84811e0fdd574477c8569d559f773dae"></a>

`SPI_DEVICE_DT_INST_DEFINE(inst, ...)` 将当前驱动实例和其余参数传给节点版本：

```c
SPI_DEVICE_DT_DEFINE(DT_DRV_INST(inst), __VA_ARGS__)
```

<a id="ga50cbb6845d230033f192f1e716fd9f2b"></a>

`SPI_DEVICE_DT_INST_DEINIT_DEFINE(inst, ...)` 是带反初始化的实例版本：

```c
SPI_DEVICE_DT_DEINIT_DEFINE(DT_DRV_INST(inst), __VA_ARGS__)
```

<a id="ga4e5633f6e8da22f4c00a723a669b2d9a"></a>

RTIO 的输入输出设备（I/O Device，iodev）把总线节点和操作配置绑定为提交请求的对象。`SPI_DT_INST_IODEV_DEFINE(name, inst, operation_)` 用实例编号定义该对象：

```c
SPI_DT_IODEV_DEFINE(name, DT_DRV_INST(inst), operation_)
```

<a id="ga1eec8a77be8a512e8b0fa74d270877e5"></a>

`SPI_DT_IODEV_DEFINE(name, node_id, operation_)` 用节点标识符定义对象，`name` 为对象名称。多个使用者可以共享同一个对象；共享并非必需，但能节省少量随机存取存储器（Random Access Memory，RAM）：

```c
const struct spi_dt_spec _spi_dt_spec_##name =                          \
        SPI_DT_SPEC_GET(node_id, operation_);                           \
RTIO_IODEV_DEFINE(name, &spi_iodev_api, (void *)&_spi_dt_spec_##name)
```

<a id="ga43857c934651c4bfb3823a5080a4a294"></a>

`SPI_DT_SPEC_GET(node_id, operation_)` 生成完整 [`spi_dt_spec`](P321_SPI设备树描述结构.md) 静态初始化器，包括总线设备和通信配置：

```c
{                                                                       \
        .bus = DEVICE_DT_GET(DT_BUS(node_id)),                          \
        .config = SPI_CONFIG_DT(node_id, operation_),                   \
}
```

<a id="gac9537325ca3188121d0f8c382c798ca1"></a>

使用前仍须检查设备就绪状态，可调用 [`spi_is_ready_dt`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#ga37b4e5079ed18b70b0c5a260f4c36403)；原文也提示参考 [`device_is_ready`](../device_reference/P001_设备模型公共接口.md#gaa4944bd850e90cbd52b0489f9b12edfb)。`SPI_DT_SPEC_INST_GET(inst, operation_)` 使用实例节点：

```c
SPI_DT_SPEC_GET(DT_DRV_INST(inst), operation_)
```

## 318.6\_位域提取、发送耗尽字节与统计宏

<a id="gaa3582b96ff42dba0b0ad815c727d5e42"></a>

`SPI_MODE_GET(_mode_)` 从操作值提取时钟极性和相位模式位：

```c
((_mode_) & SPI_MODE_MASK)
```

<a id="gaa9621b033dfaf128602b1432927a67fe"></a>

`SPI_MOSI_OVERRUN_DT(node_id)` 已弃用，改用 [`SPI_SDO_OVERRUN_DT`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#gaf66331d56f20e0c37f2a3cff998c6bce)；旧名称中的 MOSI 为主机输出、从机输入（Master Out, Slave In），是历史线名：

```c
SPI_SDO_OVERRUN_DT(node_id) __DEPRECATED_MACRO
```

<a id="ga24c7416a98421e353a8892151f34122c"></a>

`SPI_MOSI_OVERRUN_DT_INST(inst)` 同样已弃用，使用 [`SPI_SDO_OVERRUN_DT_INST`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#ga0e05910cd0be7211389514b7b4edc0cc)：

```c
SPI_SDO_OVERRUN_DT_INST(inst) __DEPRECATED_MACRO
```

<a id="ga6dd4395e027407a7b3b92cff2abcc8b3"></a>

`SPI_OP_MODE_GET(_operation_)` 提取控制器/外设操作模式位：

```c
((_operation_) & SPI_OP_MODE_MASK)
```

<a id="gaf66331d56f20e0c37f2a3cff998c6bce"></a>

当全部发送数据已耗尽、接收仍在继续时，控制器会在串行数据输出（Serial Data Output，SDO）线上输出一个替代字节。`SPI_SDO_OVERRUN_DT(node_id)` 在编译期查询这个字节，以便判断是否需要另备常量发送数组。若控制器没有公布该值，则返回 [`SPI_SDO_OVERRUN_UNKNOWN`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#ga1dbef324b98a8921507de0da1c4e4fa6)：

```c
DT_PROP_OR(node_id, overrun_character, SPI_SDO_OVERRUN_UNKNOWN)
```

<a id="ga0e05910cd0be7211389514b7b4edc0cc"></a>

`SPI_SDO_OVERRUN_DT_INST(inst)` 是对应实例版本，等价于对 `DT_DRV_INST(inst)` 调用节点版本：

```c
DT_INST_PROP_OR(inst, overrun_character, SPI_SDO_OVERRUN_UNKNOWN)
```

| 宏 | 原定义 | 含义 |
| --- | --- | --- |
| <a id="ga1dbef324b98a8921507de0da1c4e4fa6"></a>[`SPI_SDO_OVERRUN_UNKNOWN`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#ga1dbef324b98a8921507de0da1c4e4fa6) | `0x100` | 未知替代字节的哨兵值，不是有效字节 |
| <a id="ga15b5fa509a3b7dc87bfd451af5a11917"></a>[`SPI_MOSI_OVERRUN_UNKNOWN`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#ga15b5fa509a3b7dc87bfd451af5a11917) | `SPI_SDO_OVERRUN_UNKNOWN __DEPRECATED_MACRO` | 已弃用的历史名称 |

<a id="ga83fa04d1e9f281cd566ee32cf807325e"></a>

<a id="gadd3b82af2396b91930ece09fa79fc4e2"></a>

<a id="ga6f69e68a79afbbe016aecc515f14de3a"></a>

<a id="gad7d1058f600d6aef4fc4e2bdff5d55f3"></a>

原页列出下列统计宏，但没有进一步的参数或展开说明，原声明保留如下：

```c
SPI_STATS_RX_BYTES_INC(dev_)
SPI_STATS_TRANSFER_ERROR_INC(dev_)
SPI_STATS_TX_BYTES_INC(dev_)
spi_transceive_stats(dev, error, tx_bufs, rx_bufs)
```

<a id="gac1115bf80134efd38d88161e3f5e3e1a"></a>

`SPI_WORD_SET(word_size)` 将以位计的数据字长度编码为操作字段的位掩码：

```c
((word_size) << SPI_WORD_SIZE_SHIFT)
```

<a id="gacd7edd9ce02bd8351f8eebe5b5c07c7a"></a>

`SPI_WORD_SIZE_GET(operation)` 从操作字段提取以位计的数据字长度：

```c
(((operation) & SPI_WORD_SIZE_MASK) >> SPI_WORD_SIZE_SHIFT)
```

## 318.7\_就绪检查与 RTIO 提交

以下辅助函数均为 `static inline`，声明来自 `zephyr/drivers/spi.h`。

```c
bool spi_cs_is_gpio(const struct spi_config *config);
bool spi_cs_is_gpio_dt(const struct spi_dt_spec *spec);
void spi_iodev_submit(struct rtio_iodev_sqe *iodev_sqe);
bool spi_is_ready_dt(const struct spi_dt_spec *spec);
bool spi_is_ready_iodev(const struct rtio_iodev *spi_iodev);
```

<a id="gae1156a4ee1b5909c321811045566d888"></a>

<a id="gaa13f0da1f28cffa0da4677987db0c9c5"></a>

[`spi_cs_is_gpio`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#gae1156a4ee1b5909c321811045566d888) 检查 `config` 的片选控制方式；GPIO 控制时返回 [`true`](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#a41f9c5fb8b08eb5dc3edce4dcb37fee7)，硬件或其他方式控制时返回 [`false`](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#a65e9886d74aaee76545e83dd09011727)。[`spi_cs_is_gpio_dt`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#gaa13f0da1f28cffa0da4677987db0c9c5) 对设备树规格 `spec` 执行同一检查。

<a id="ga8b23855bdc7dab7d02b8f7daa7db651b"></a>

[`spi_iodev_submit`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#ga8b23855bdc7dab7d02b8f7daa7db651b) 提交 SPI 请求。`iodev_sqe` 是已经准备好、关联到 iodev 的提交队列条目（Submission Queue Entry，SQE）；只要请求还在进行，它就必须保持有效。原参数说明将设备定义宏写作 `SPI_IODEV_DEFINE`；本页实际列出的设备树定义宏是 [`SPI_DT_IODEV_DEFINE`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#ga1eec8a77be8a512e8b0fa74d270877e5)。

<a id="ga37b4e5079ed18b70b0c5a260f4c36403"></a>

<a id="gafea78af1fe1fa49fdc5459ab3a2d5f73"></a>

[`spi_is_ready_dt`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#ga37b4e5079ed18b70b0c5a260f4c36403) 检查 `spec` 的 SPI 总线以及配置了的片选 GPIO 是否就绪；均可用时返回 [`true`](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#a41f9c5fb8b08eb5dc3edce4dcb37fee7)，总线或片选 GPIO 未就绪时返回 [`false`](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#a65e9886d74aaee76545e83dd09011727)。[`spi_is_ready_iodev`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#gafea78af1fe1fa49fdc5459ab3a2d5f73) 对通过 [`SPI_DT_IODEV_DEFINE`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#ga1eec8a77be8a512e8b0fa74d270877e5) 定义的 `spi_iodev` 作相同检查。

## 318.8\_同步读取与信号式异步读取

读取函数使用 `rx_bufs` 指定接收缓冲区数组。`dev` 指向驱动实例设备结构，`config` 指向有效的 [`spi_config`](P320_SPI控制器配置结构.md)；驱动可能通过指针比较判断配置是否相对上次操作发生变化。

```c
int spi_read(const struct device *dev, const struct spi_config *config,
             const struct spi_buf_set *rx_bufs);
int spi_read_dt(const struct spi_dt_spec *spec,
                const struct spi_buf_set *rx_bufs);
```

<a id="ga41f771785a4fa9ca0954125d1e97959e"></a>

两者均为 `static inline`。[`spi_read`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#ga41f771785a4fa9ca0954125d1e97959e) 是调用 [`spi_transceive`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#gad51054c1ba259db5a64619788506a6f5) 的同步辅助函数，读取指定数量的数据。控制器模式成功返回 0，外设模式返回收到的数据帧数；失败返回负的错误码。`-ENOTSUP` 表示硬件或驱动不支持该 SPI 配置，`-EINVAL` 表示 [`spi_config`](P320_SPI控制器配置结构.md) 中某个参数无效。

<a id="ga7a1d7ebd37d2861b169c265cb90015bf"></a>

[`spi_read_dt`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#ga7a1d7ebd37d2861b169c265cb90015bf) 从设备树规格 `spec` 指定的总线读取数据，返回 `spi_read` 的结果，等价于：

```c
spi_read(spec->bus, &spec->config, rx_bufs);
```

<a id="ga9a1ceadb217368232af5b688c12169c5"></a>

异步读取使用轮询信号（Poll Signal）报告完成：

```c
int spi_read_signal(const struct device *dev, const struct spi_config *config,
                    const struct spi_buf_set *rx_bufs,
                    struct k_poll_signal *sig);
```

此 `static inline` 辅助函数调用 [`spi_transceive_signal`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#ga41b8a541257c0d45575fdc4593417edc)，仅在同时启用 [`CONFIG_SPI_ASYNC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_ASYNC) 和 [`CONFIG_POLL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POLL) 时可用。`sig` 指向有效且可被触发的 [`k_poll_signal`](../eventpoll_reference/P005_轮询信号结构.md)；若为 `NULL`，不会通知事务结束，也不会通知事务是否成功。其余参数含义同同步读取。原页返回值约定同样写为外设模式返回接收帧数、控制器模式成功返回 0、失败返回负错误码，并列出上述 `-ENOTSUP` 和 `-EINVAL`。

> 译注：异步函数的“返回帧数”措辞按原页保留；不能据此将异步函数返回误认为传输已经完成，完成仍依赖其通知机制。

## 318.9\_释放总线所有权与片选

<a id="ga0c4f4f0a93bb83a4f58d551a7491164e"></a>

[`spi_release`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#ga0c4f4f0a93bb83a4f58d551a7491164e) 是同步函数，用于释放当前配置持有的 SPI 设备锁和/或保持有效的片选：

```c
int spi_release(const struct device *dev, const struct spi_config *config);
int spi_release_dt(const struct spi_dt_spec *spec);
```

只有当传入 `config` 正是前述操作最后使用的配置，且其操作字段设置了 `SPI_LOCK_ON` 和/或 [`SPI_HOLD_ON_CS`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#gae917312adef283b4bf67cdb53566e4bb) 时，才适用这种释放行为。调用者可借此连续占用设备或连续选中外设；通常两位一起使用，使设备保持锁定及选中，直到下一次必要操作或显式释放。`dev` 是设备结构指针，`config` 必须指向有效配置。成功返回 0，失败返回负错误码。

<a id="ga829b59767c51b20b546eee8a9cc84b69"></a>

[`spi_release_dt`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#ga829b59767c51b20b546eee8a9cc84b69) 是 `static inline` 包装，使用设备树规格并返回 [`spi_release`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#ga0c4f4f0a93bb83a4f58d551a7491164e) 的结果，等价于：

```c
spi_release(spec->bus, &spec->config);
```

## 318.10\_同步与异步收发

同步收发接口如下；`tx_bufs` 是发送数据来源的缓冲区数组，无发送数据时可为 `NULL`；`rx_bufs` 是接收数据写入的缓冲区数组，无接收数据时可为 `NULL`。

```c
int spi_transceive(const struct device *dev, const struct spi_config *config,
                   const struct spi_buf_set *tx_bufs,
                   const struct spi_buf_set *rx_bufs);
int spi_transceive_cb(const struct device *dev, const struct spi_config *config,
                      const struct spi_buf_set *tx_bufs,
                      const struct spi_buf_set *rx_bufs,
                      spi_callback_t callback, void *userdata);
int spi_transceive_dt(const struct spi_dt_spec *spec,
                      const struct spi_buf_set *tx_bufs,
                      const struct spi_buf_set *rx_bufs);
```

<a id="gad51054c1ba259db5a64619788506a6f5"></a>

[`spi_transceive`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#gad51054c1ba259db5a64619788506a6f5) 读写指定数量的数据。控制器模式下，给定缓冲区集合的全部缓冲区传完之前，片选持续有效；全部传完后才解除。外设模式下，只有控制器使片选有效并提供时钟，数据才会传输；函数等待控制器完成后返回。此时片选由控制器控制，所以它不一定在整个传输过程中始终有效。

`dev` 为驱动实例设备指针，`config` 为有效配置指针；驱动可通过指针比较检测相对前次操作的变化。控制器模式成功返回 0，外设模式返回接收帧数，失败返回负错误码。`-ENOTSUP` 表示设备硬件或驱动不支持配置，`-EINVAL` 表示配置中的参数无效。

<a id="ga6114e63ca23b82f9be0ac70e372b878b"></a>

[`spi_transceive_cb`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#ga6114e63ca23b82f9be0ac70e372b878b) 为 `static inline` 异步收发函数，仅启用 [`CONFIG_SPI_ASYNC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_ASYNC) 时可用。片选行为及控制器/外设模式与 [`spi_transceive`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#gad51054c1ba259db5a64619788506a6f5) 相同；设备、配置及缓冲区参数也相同。`callback` 为完成回调指针，`userdata` 为传给该回调的用户数据。回调为 `NULL` 时不通知事务结束和成功与否。原文给出与同步收发相同的返回值及 `-ENOTSUP`、`-EINVAL` 说明；仍须按异步完成机制使用。

<a id="ga52c017066736414b31ff709ddc67c4ff"></a>

[`spi_transceive_dt`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#ga52c017066736414b31ff709ddc67c4ff) 是 `static inline` 设备树包装，参数为设备树规格及上述两个缓冲区集合，返回 `spi_transceive` 的结果，等价于：

```c
spi_transceive(spec->bus, &spec->config, tx_bufs, rx_bufs);
```

<a id="ga41b8a541257c0d45575fdc4593417edc"></a>

使用信号通知的异步收发声明如下：

```c
int spi_transceive_signal(const struct device *dev,
                          const struct spi_config *config,
                          const struct spi_buf_set *tx_bufs,
                          const struct spi_buf_set *rx_bufs,
                          struct k_poll_signal *sig);
```

此 `static inline` 函数仅在同时启用 [`CONFIG_SPI_ASYNC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_ASYNC)、[`CONFIG_POLL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POLL) 时可用。片选行为和控制器/外设模式同 `spi_transceive`；设备、配置指针比较及可为空的收发缓冲区约定也相同。`sig` 须指向有效且可被触发的轮询信号，为 `NULL` 时不通知结束和成功与否。原文返回值写为外设模式接收帧数、控制器模式成功 0、失败负错误码；`-ENOTSUP` 和 `-EINVAL` 含义同上。

## 318.11\_同步与异步写入

以下三个函数均为 `static inline`，`tx_bufs` 提供待发送数据的缓冲区数组，`dev` 为驱动实例设备指针，`config` 为有效配置指针。驱动可使用配置指针比较来判断相对前次操作的变化。

```c
int spi_write(const struct device *dev, const struct spi_config *config,
              const struct spi_buf_set *tx_bufs);
int spi_write_dt(const struct spi_dt_spec *spec,
                 const struct spi_buf_set *tx_bufs);
int spi_write_signal(const struct device *dev, const struct spi_config *config,
                     const struct spi_buf_set *tx_bufs,
                     struct k_poll_signal *sig);
```

<a id="ga7e7c4460670ec1c0433ba19accd97796"></a>

[`spi_write`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#ga7e7c4460670ec1c0433ba19accd97796) 为调用 `spi_transceive` 的同步辅助函数，写入指定数量的数据。成功返回 0，失败返回负错误码；`-ENOTSUP` 表示设备硬件或驱动不支持配置，`-EINVAL` 表示 [`spi_config`](P320_SPI控制器配置结构.md) 中有无效参数。

<a id="ga292d6d1fe82f3f1ce0d9a2aa5437201b"></a>

[`spi_write_dt`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#ga292d6d1fe82f3f1ce0d9a2aa5437201b) 使用设备树规格 `spec` 指定的总线，返回 `spi_write` 的结果，等价于：

```c
spi_write(spec->bus, &spec->config, tx_bufs);
```

<a id="gadcb19d43461ef88e31f6b382cc87fd0b"></a>

[`spi_write_signal`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#gadcb19d43461ef88e31f6b382cc87fd0b) 为调用 `spi_transceive_signal` 的异步辅助函数；仅在同时启用 [`CONFIG_SPI_ASYNC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_ASYNC) 和 [`CONFIG_POLL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POLL) 时可用。`sig` 必须指向有效且可被触发的 [`k_poll_signal`](../eventpoll_reference/P005_轮询信号结构.md)；若为 `NULL`，不会报告事务结束和成功与否。成功返回 0，失败返回负错误码；`-ENOTSUP` 和 `-EINVAL` 的含义与同步写入一致。

---

[上一章：I2C模拟函数表](P317_I2C模拟函数表.md) · [下一章：SPI片选控制结构](P319_SPI片选控制结构.md) · [返回大纲](大纲.md)
