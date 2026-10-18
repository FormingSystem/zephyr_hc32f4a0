---
id: learning.zephyr-docs.hardware.mipi-1
title: MIPI显示总线接口
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第245章\_MIPI显示总线接口

原文：[group__mipi__dbi__interface](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html)。读取日期：2026-10-13，`latest`。

## 245.1\_范围与版本

本页提供 MIPI **显示总线接口（Display Bus Interface，DBI）**的驱动 **应用程序编程接口（Application Programming Interface，API）**，自 Zephyr 3.6 提供，本页版本为 1.0.0。主头文件为 `zephyr/drivers/mipi_dbi.h`；总线模式、颜色编码与同步边沿常量来自 `zephyr/dt-bindings/mipi_dbi/mipi_dbi.h`。

SPI 表示串行外设接口（Serial Peripheral Interface），DT 表示设备树（Devicetree），CS 表示片选（Chip Select），GPIO 表示通用输入输出（General-Purpose Input/Output）。本页原图中的 RESX 为复位信号，D/CX、D/C 或 CD 区分数据/命令（Data/Command），R/WX 区分读/写（Read/Write），E 为使能信号（Enable），WRX/RDX 为写/读控制，SCK 是串行时钟（Serial Clock），DOUT 是数据输出（Data Output），D[n:0] 表示数据线。

驱动实现者另见[MIPI DBI后端接口](P251_MIPI显示总线后端.md)。

## 245.2\_并行总线模式与原始时序图

Type A 基于 Motorola 6800 并行总线，模式宏为 `MIPI_DBI_MODE_6800_BUS_16_BIT = 0x3`、`MIPI_DBI_MODE_6800_BUS_9_BIT = 0x4`、`MIPI_DBI_MODE_6800_BUS_8_BIT = 0x5`，分别对应 16、9、8 位宽度。图中 COMMAND 为命令、DATA 为数据，信号名含义见开头。原图：

```text
         -.   .--------.      .------------------------
CS        '---'        '---'

         -------------------------------------------
RESX

                   .--------------------------------
D/CX     ----------'


R/WX     -------------------------------------------

         -------------------------------------------
E

          .--------.   .--------------------------.
D[15:0]/ -| COMMAND|---|  DATA                    |
D[8:0]/   '--------'   '--------------------------'
D[7:0]
```

Type B 基于 Intel 8080 并行总线，模式宏为 `MIPI_DBI_MODE_8080_BUS_16_BIT = 0x6`、`MIPI_DBI_MODE_8080_BUS_9_BIT = 0x7`、`MIPI_DBI_MODE_8080_BUS_8_BIT = 0x8`，分别对应 16、9、8 位宽度。原图：

```text
         -.                                       .-
CS        '---------------------------------------'

         -------------------------------------------
RESX

         --.           .----------------------------
D/CX       '-----------'

         ---.   .--------.   .----------------------
WRX         '---'        '---'

         -------------------------------------------
RDX

            .--------.   .--------------------------.
D[15:0]/ ---| COMMAND|---|  DATA                    |
D[8:0]/     '--------'   '--------------------------'
D[7:0]
```

这两种模式的详细周期图应参阅 MIPI DBI 规范。

## 245.3\_完整DBI配置宏

宏 `MIPI_DBI_CONFIG_DT(node_id, operation_, delay_)` 从设备树初始化 DBI 配置结构，设置模式、颜色编码及 SPI 配置字段。没有 `color-coding` 属性时，颜色编码保持 0，表示没有指定 Type A/B 编码。

参数 `node_id` 是待初始化设备的 DT 节点标识；`operation_` 是所需 [`spi_config`](P320_SPI控制器配置结构.md) 结构操作字段；`delay_` 是其片选控制结构 [`spi_cs_control`](P319_SPI片选控制结构.md) 的延时字段值（存在该控制结构时）。原展开式的 [`DT_STRING_UPPER_TOKEN`](../dt_property_reference/P001_设备树属性读取宏.md#gae0b5e2b6633a98ead17ec20d3494658f) 把属性字符串转换为大写标识，[`DT_STRING_UPPER_TOKEN_OR`](../dt_property_reference/P001_设备树属性读取宏.md#gab79f5274c82d025d805ec94d2935c9b9) 在属性不存在时使用默认值；嵌套 SPI 配置宏见后文。

```c
{                                                               \
        .mode = DT_STRING_UPPER_TOKEN(node_id, mipi_mode),      \
        .color_coding = DT_STRING_UPPER_TOKEN_OR(node_id, color_coding, 0), \
        .config = MIPI_DBI_SPI_CONFIG_DT(node_id, operation_, delay_), \
}
```

宏 `MIPI_DBI_CONFIG_DT_INST(inst, operation_, delay_)` 从设备实例初始化相同配置。`inst` 是设备实例编号，其余参数含义同上；[`DT_DRV_INST`](../dt_instance_reference/P001_设备树驱动实例宏.md#ga219f413efba2f4c0151468b9a25a8dc1) 将实例编号转换成节点标识。完整展开式：

```c
MIPI_DBI_CONFIG_DT(DT_DRV_INST(inst), operation_, delay_)
```

## 245.4\_SPI三线与四线模式

宏 `MIPI_DBI_MODE_SPI_3WIRE = 0x1` 对应三线 SPI，即 Type C1。每发送一个数据字节使用 9 个写时钟，额外的一位标识该字节是命令还是数据。原文称“第9个时钟发送的位”，原图按一个字开头的 D/C 位绘制，以下原样保留：

```text
      .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-
SCK  -' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-'

     -.---.---.---.---.---.---.---.---.---.---.---.---.---.---.---.-
DOUT  |D/C| D7| D6| D5| D4| D3| D2| D1| D0|D/C| D7| D6| D5| D4|...|
     -'---'---'---'---'---'---'---'---'---'---'---'---'---'---'---'-
      | Word 1                            | Word n

     -.                                                           .-
CS    '-----------------------------------------------------------'
```

宏 `MIPI_DBI_MODE_SPI_4WIRE = 0x2` 对应四线 SPI，即 Type C3。每字节使用 8 个写时钟，并使用额外 C/D（Command/Data，命令/数据）引脚表示命令或数据：

```text
      .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-.
SCK  -' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '---

     -.---.---.---.---.---.---.---.---.---.---.---.---.---.---.---.---.-
DOUT  | D7| D6| D5| D4| D3| D2| D1| D0| D7| D6| D5| D4| D3| D2| D1| D0|
     -'---'---'---'---'---'---'---'---'---'---'---'---'---'---'---'---'-
      | Word 1                        | Word n

     -.                                                               .-
CS    '---------------------------------------------------------------'

     -.-------------------------------.-------------------------------.-
CD    |             D/C               |             D/C               |
     -'-------------------------------'-------------------------------'-
```

## 245.5\_SPI配置与片选判断宏

宏 `MIPI_DBI_SPI_CONFIG_DT(node_id, operation_, delay_)` 从设备树生成 [`spi_config`](P320_SPI控制器配置结构.md) 初始化器。参数 `node_id` 为设备节点标识；`operation_` 为期望操作字段；`delay_` 为存在片选控制结构时的延时字段值。

原展开式中的属性读取宏包括 [`DT_PROP`](../dt_property_reference/P001_设备树属性读取宏.md#ga8e1fd9ebacd85d2013df027d041d506b)、带默认值的 [`DT_PROP_OR`](../dt_property_reference/P001_设备树属性读取宏.md#ga5e5bfc9b1a6627b3f73014329e96340f)、寄存器地址宏 [`DT_REG_ADDR`](../dt_reg_reference/P001_设备树寄存器属性宏.md#gac6d8279c32351ced4c0ac7f32270974e)；`COND_CODE_1` 为条件展开宏。[`SPI_MODE_CPOL`](P318_SPI公共接口.md)、[`SPI_MODE_CPHA`](P318_SPI公共接口.md) 分别表示时钟极性（Clock Polarity，CPOL）与时钟相位（Clock Phase，CPHA）；[`SPI_HOLD_ON_CS`](P318_SPI公共接口.md) 表示保持片选。宏 `MIPI_DBI_SPI_DEV_HAS_CS_GPIOS` 判断是否配置 GPIO 片选，详见本节后半。GPIO 片选与原生片选分别经 `MIPI_DBI_SPI_CS_CONTROL_INIT_GPIO`、`SPI_CS_CONTROL_INIT_NATIVE` 初始化。

```c
{                                                               \
        .frequency = DT_PROP(node_id, mipi_max_frequency),      \
        .operation = (operation_) |                             \
                DT_PROP_OR(node_id, duplex, 0) |                        \
                COND_CODE_1(DT_PROP(node_id, mipi_cpol), SPI_MODE_CPOL, (0)) |  \
                COND_CODE_1(DT_PROP(node_id, mipi_cpha), SPI_MODE_CPHA, (0)) |  \
                COND_CODE_1(DT_PROP(node_id, mipi_hold_cs), SPI_HOLD_ON_CS, (0)),       \
        .peripheral = DT_REG_ADDR(node_id),                             \
        .cs = {                                                                 \
                COND_CODE_1(MIPI_DBI_SPI_DEV_HAS_CS_GPIOS(node_id),                     \
                (MIPI_DBI_SPI_CS_CONTROL_INIT_GPIO(node_id, delay_)),           \
                (SPI_CS_CONTROL_INIT_NATIVE(node_id)))                          \
                .cs_is_gpio = MIPI_DBI_SPI_DEV_HAS_CS_GPIOS(node_id),           \
        },                                                                      \
}
```

宏 `MIPI_DBI_SPI_CONFIG_DT_INST(inst, operation_, delay_)` 根据设备实例编号 `inst` 初始化 SPI 配置，其他参数同上：

```c
MIPI_DBI_SPI_CONFIG_DT(DT_DRV_INST(inst), operation_, delay_)
```

> 译注：原文等价表达式的说明文字省略了 `operation_`、`delay_`，但宏定义保留这两个参数；这里保留完整定义。

宏 `MIPI_DBI_SPI_DEV_HAS_CS_GPIOS(node_id)` 检查 DBI SPI 设备是否配置片选线，是宏 [`DT_SPI_DEV_HAS_CS_GPIOS()`](P329_SPI设备树宏.md) 在 DBI 场景下的对应形式。区别在于通过父节点的 `spi-dev` 引用句柄（phandle）找到 SPI 控制器，而不是使用 [`DT_BUS()`](../dt_node_reference/P001_设备树总线查询宏.md#ga1082d31ac2dafdf9e085d4c23f2169dc)。

如果该控制器在索引 `DT_REG_ADDR(node_id)` 处有片选引脚，返回 1，否则返回 0。原展开式中的 `MIPI_DBI_DT_SPI_DEV` 取得 SPI 控制器节点，[`DT_PROP_HAS_IDX`](../dt_property_reference/P001_设备树属性读取宏.md#ga479dfc704087eea7e7c5af42ae98576c) 检查属性索引，[`DT_REG_ADDR_RAW`](../dt_reg_reference/P001_设备树寄存器属性宏.md#ga14ebfb75548e45279f3954a75a5f9ac1) 取得原始地址索引：

```c
DT_PROP_HAS_IDX(MIPI_DBI_DT_SPI_DEV(node_id), cs_gpios,         \
                DT_REG_ADDR_RAW(node_id))
```

## 245.6\_命令传输块宽度

宏 `MIPI_DBI_SPI_XFR_16BIT = 16` 表示以 16 位块传输 DBI 命令，是 Type C3 四线模式中的少见用法。时序与通常的 Type C3 略有不同，原图保留填充（Stuffing）部分与有效字节（Byte）：

```text
      .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-.
SCK  -' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '---

     -.---.---.---.---.---.---.---.---.---.---.---.---.---.---.---.---.-
DOUT  |D15|D14|D13|D12|D11|D10| D9| D8| D7| D6| D5| D4| D3| D2| D1| D0|
     -'---'---'---'---'---'---'---'---'---'---'---'---'---'---'---'---'-
      | Word 1             (stuffing) :                        (byte) |

     -.                                                               .-
CS    '---------------------------------------------------------------'

     -.---------------------------------------------------------------.-
CD    |                              D/C                              |
     -'---------------------------------------------------------------'-
```

宏 `MIPI_DBI_SPI_XFR_8BIT = 8` 表示以 8 位块传输，是 Type C3 的默认行为，时序与前面的 Type C3 原图完全一致。

## 245.7\_撕裂同步边沿及设备树宏

TE 表示撕裂效应同步信号（Tearing Effect）；RAM 表示随机存取存储器（Random Access Memory）。宏 `MIPI_DBI_TE_NO_EDGE = 0x0` 禁用 TE 同步。

宏 `MIPI_DBI_TE_FALLING_EDGE = 0x2` 在 TE 下降沿同步。控制器只在下降沿开始发送显示数据，适合写入一帧比面板从 RAM 读取一帧更慢的情况。控制器必须在面板完成两个读取周期之前完成写入，否则读指针会追上写指针。原图：

```text
              .------.                        .------.
TE       -----'      '------------------------'      '-------------
         ------------.                                       .-----
CS                   '---------------------------------------'
```

宏 `MIPI_DBI_TE_MODE_DT(node_id, edge_prop)` 从设备树属性取得 TE 模式；`node_id` 是具有该属性的设备节点标识，`edge_prop` 是要读取的属性名：

```c
DT_STRING_UPPER_TOKEN(node_id, edge_prop)
```

宏 `MIPI_DBI_TE_MODE_DT_INST(inst, edge_prop)` 为设备实例 `inst` 取得 TE 模式，`edge_prop` 含义同上：

```c
DT_STRING_UPPER_TOKEN(DT_DRV_INST(inst), edge_prop)
```

> 译注：原文等价说明把第二参数写成 `edge_mode`，实际参数和展开式为 `edge_prop`，这里按定义保留。

宏 `MIPI_DBI_TE_RISING_EDGE = 0x1` 在 TE 上升沿同步。控制器只在上升沿开始发送显示数据，适合控制器写入一帧比面板从 RAM 读取一帧更快的情况。原图：

```text
              .------.                        .------.
TE       -----'      '------------------------'      '-------------
         -----.        .----------------------.
CS            '--------'                      '--------------------
```

## 245.8\_Type A与Type B颜色编码

RGB 表示红、绿、蓝（Red, Green, Blue）；每像素位数写作 bpp（Bits per Pixel）。RGB332、RGB444、RGB565、RGB666、RGB888 的数字依次表示红、绿、蓝分量位数；后缀 `_1`、`_2` 区分打包方案。以下都是颜色编码宏：

| 宏 | 值 | 编码 |
| --- | --- | --- |
| [`MIPI_DBI_MODE_RGB332`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#ga11d68e3a9a449ec8fce4bbae637af08c) | `(0x1 << 4U)` | RGB332，8 bpp。 |
| [`MIPI_DBI_MODE_RGB444`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#gac18f3926b86551908300f055ebe9212a) | `(0x2 << 4U)` | RGB444，12 bpp。 |
| [`MIPI_DBI_MODE_RGB565`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#ga53bbca5860b8845e892d3605c44877b4) | `(0x3 << 4U)` | RGB565，16 bpp。 |
| [`MIPI_DBI_MODE_RGB666_1`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#gaa264bb127fbbece867bf444c8168b6f4) | `(0x4 << 4U)` | RGB666，18 bpp，方案1。 |
| [`MIPI_DBI_MODE_RGB666_2`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#gafb1d7ae963a9cfedadaa4c4299ad7f99) | `(0x5 << 4U)` | RGB666，18 bpp，方案2。 |
| [`MIPI_DBI_MODE_RGB888_1`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#gad7195e4b6aad08002b4b61a3052bf8e7) | `(0x6 << 4U)` | RGB888，24 bpp，方案1。 |
| [`MIPI_DBI_MODE_RGB888_2`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#ga0edb36a8b62a252bff686f0463bd83fc) | `(0x7 << 4U)` | RGB888，24 bpp，方案2。 |

RGB332：8 位总线每周期发送 1 像素；16 位总线每周期发送 2 像素。

RGB444：8 位总线用 3 周期发送 2 像素；16 位总线每周期发送 1 像素，高 4 位未使用。

RGB565：8 位总线用 2 周期发送 1 像素；16 位总线每周期发送 1 像素。

RGB666：8 位总线上两方案相同，每像素 3 周期，R 分量先发，低 2 位未使用；9 位总线上两方案也相同，每像素 2 周期。16 位总线上的排列如下：

| 方案 | 传输量 | 像素 | R分量 | G分量 | B分量 |
| --- | --- | --- | --- | --- | --- |
| RGB666_1 | 3周期/2像素 | 第1像素 | 周期1位10～15 | 周期1位2～7 | 周期2位10～15 |
| RGB666_1 | 3周期/2像素 | 第2像素 | 周期2位2～7 | 周期3位10～15 | 周期3位2～7 |
| RGB666_2 | 2周期/1像素 | 单像素 | 周期1位2～7 | 周期2位10～15 | 周期2位2～7 |

RGB888：8 位总线上两方案相同，每像素 3 周期，R 分量先发。16 位总线上的排列按原文列出：

| 方案 | 传输量 | 像素 | R分量 | G分量 | B分量 |
| --- | --- | --- | --- | --- | --- |
| RGB888_1 | 3周期/2像素 | 第1像素 | 周期1位8～15 | 周期1位0～7 | 周期2位0～15 |
| RGB888_1 | 3周期/2像素 | 第2像素 | 周期2位0～7 | 周期3位8～15 | 周期3位0～7 |
| RGB888_2 | 2周期/1像素 | 单像素 | 周期1位0～7 | 周期2位8～15 | 周期2位0～7 |

> 译注：RGB888_1 第一像素 B 分量原文写“周期2位0～15”，与单分量8位以及第二像素R占用位0～7的说明冲突。本表保留原值，不自行猜改。

## 245.9\_写命令与读响应

以下函数的 `dev` 为 MIPI DBI 控制器，`config` 指向 DBI 配置结构。

```c
static inline int mipi_dbi_command_write(const struct device *dev,
    const struct mipi_dbi_config *config, uint8_t cmd, const uint8_t *data, size_t len);
static inline int mipi_dbi_command_read(const struct device *dev,
    const struct mipi_dbi_config *config, uint8_t *cmds, size_t num_cmd,
    uint8_t *response, size_t len);
```

函数 [`mipi_dbi_command_write()`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#gad36e3d57fd931236c4ed4e58dfef1cca) 写入命令 [`cmd`](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)，并可选地发送其后的 `data` 缓冲区；`len` 为数据字节数。数据指针为空 `NULL`、长度为 0 时只发命令；`len=0` 跳过数据发送。若 SPI 配置锁定总线，调用者负责调用 [`mipi_dbi_release()`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#gade0b635bcd4f16fb3ec5d122d1b09161) 释放。

函数 [`mipi_dbi_command_read()`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#gafac64feca9fdee3803154bacb58e8e47) 读取命令响应：`cmds` 是要发送的单字节命令数组，`num_cmd` 是命令数，`response` 是接收响应的缓冲区，`len` 为响应缓冲区字节数。

两者成功返回 0；`-EIO` 为输入输出错误（Input/Output Error）；`-ETIMEDOUT` 为传输超时（Transfer Timed Out）；`-EBUSY` 为控制器忙（Controller Busy）；`-ENOSYS` 为未实现（Not Implemented）。

## 245.10\_写显示缓冲区

```c
static inline int mipi_dbi_write_display(const struct device *dev,
    const struct mipi_dbi_config *config, const uint8_t *framebuf,
    struct display_buffer_descriptor *desc, enum display_pixel_format pixfmt);
```

函数 [`mipi_dbi_write_display()`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#ga62aa7b9677da010a678580d956f7d0e3) 写入显示缓冲区。若显示控制器要求先发送“写存储器”命令，应先通过 [`mipi_dbi_command_write()`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#gad36e3d57fd931236c4ed4e58dfef1cca) 发送。

`framebuf` 是要写入的帧缓冲区（Framebuffer）；`desc` 是其[缓冲区描述符](P215_显示缓冲区描述符.md)，**行跨度 `pitch` 必须等于宽度 `width`，`buf_size` 决定写入字节数**；`pixfmt` 是像素格式。

成功返回 0；可能错误为 `-EIO`、`-ETIMEDOUT`、`-EBUSY`、`-ENOSYS`，含义同前节。

## 245.11\_复位与释放锁定

```c
static inline int mipi_dbi_reset(const struct device *dev, uint32_t delay_ms);
static inline int mipi_dbi_release(const struct device *dev,
                                  const struct mipi_dbi_config *config);
```

函数 [`mipi_dbi_reset()`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#ga1c1a117ae5db5f7508f302d48dc72013) 复位所连接的显示控制器，`delay_ms` 为复位信号保持时长，单位毫秒（Millisecond）。成功返回 0；`-EIO` 为输入输出错误，`-ENOSYS` 为未实现，`-ENOTSUP` 为不支持（Not Supported）。

函数 [`mipi_dbi_release()`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#gade0b635bcd4f16fb3ec5d122d1b09161) 释放锁定的 DBI 设备和/或片选线。条件是：给定 `config` 必须是最后一次用于上述操作的配置，且操作位中设置了 `SPI_LOCK_ON` 和/或 [`SPI_HOLD_ON_CS`](P318_SPI公共接口.md)。锁的行为与 SPI 锁相同，可用于跨多个事务保持片选有效，或锁住 DBI 设备。

返回值为 0、`-EIO`、`-ENOSYS`、`-ENOTSUP`。原文把 0 的描述写成“复位成功（reset succeeded）”；译注：本函数是释放操作，此处保留该原文措辞差异。

## 245.12\_配置撕裂同步信号

```c
static inline int mipi_dbi_configure_te(const struct device *dev,
                                       uint8_t edge, uint32_t delay_us);
```

函数 [`mipi_dbi_configure_te()`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#gab74f96d99f9702f29b51cc2fe0b48d95) 配置 TE 信号。许多显示器可让它在每次垂直同步（Vertical Synchronization，VSync）或水平同步（Horizontal Synchronization，HSync）间隔脉冲。微控制器（Microcontroller Unit，MCU）可据此选择新帧传输时机，避免面板读指针与 MCU 写指针重叠。

函数使 DBI 控制器等待选定 TE 边沿后再传输显示帧。`edge` 选择边沿；`delay_us` 为边沿之后再等待的微秒（Microsecond）数。

原文说明：当**前一次**调用提供的描述符设置了 `frame_incomplete` 标志时，本次 [`mipi_dbi_write_display()`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#ga62aa7b9677da010a678580d956f7d0e3) 会执行这一等待，因为本次缓冲区被视为新帧的第一个缓冲区。

> 译注：这段条件表述与[描述符页](P215_显示缓冲区描述符.md)将 `frame_incomplete` 定义为“不是本帧最后一个缓冲区”存在歧义。这里保留原说法，实际帧边界判定需要核对所用驱动实现。

大多数显示控制器需要先用厂商专用命令启用 TE 输出，DBI 控制器才能响应。原页列出错误返回：`-EIO`、`-ENOSYS`、`-ENOTSUP`；没有单独列出成功返回项。

---

[上一章：MIPI显示接口定义](P244_MIPI显示接口定义.md) · [下一章：MIPI显示串行接口](P246_MIPI显示串行接口.md) · [返回大纲](大纲.md)
