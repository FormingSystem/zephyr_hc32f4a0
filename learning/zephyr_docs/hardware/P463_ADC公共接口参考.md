---
id: learning.zephyr-docs.hardware.adcapi-0
title: ADC公共接口参考
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第463章\_ADC公共接口参考

原文：[group__adc__interface](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html)。读取日期：2026-10-13，`latest`。

## 463.1\_范围、头文件与相关类型

本页提供**模数转换器（Analog-to-Digital Converter，ADC）**的应用程序接口（Application Programming Interface，API）。官方注明此接口自 1.0 引入，接口版本为 1.0.0。

```c
#include <zephyr/drivers/adc.h>
```

以下术语用于本页：设备树（Devicetree，DT）、增益（Gain）、参考电压（Reference Voltage）、采样序列（Sampling Sequence）、分辨率（Resolution）、过采样（Oversampling）、解码器（Decoder）、实时输入输出（Real-Time Input/Output，RTIO）、先进先出缓冲区（First In, First Out，FIFO）。

本页错误码包括：`-EINVAL` 无效参数（Invalid Argument）、`-ENOTSUP` 不支持（Not Supported）、`-ENOMEM` 无法取得所需内存/队列项或缓冲区不足（No Memory）、`-EBUSY` 忙（Busy）、`-ENODATA` 暂无数据（No Data）。具体触发条件以各函数的返回值说明为准。

相关数据结构：

| 结构 | 用途 |
| --- | --- |
| [adc_channel_cfg](P443_ADC通道配置结构.md) | 通道配置 |
| [adc_dt_spec](P444_ADC设备树规格.md) | 设备树通道信息 |
| [adc_sequence_options](P446_ADC采样序列选项.md) | 采样序列附加选项 |
| [adc_sequence](P445_ADC采样序列结构.md) | 采样序列 |
| [adc_data_header](P450_ADC数据头.md) | 数据头 |
| [adc_data](P452_ADC解码数据.md) | ADC 通道数据 |
| [adc_stream_trigger](P449_ADC流触发配置.md) | 流触发配置 |
| [adc_chan_spec](P447_ADC通道规格.md) | 通道规格 |
| [adc_read_config](P448_ADC读取配置.md) | 读取配置 |
| [adc_decoder_api](P455_ADC解码器API结构.md) | 单个原始缓冲区的解码接口 |
| [adc_data_generic_header](P451_ADC通用数据头.md) | 编码后流式帧的通用头 |

本组还包含 ADC 驱动后端、ADS126X 驱动接口、设备专用扩展、模拟 ADC 后端以及 Renesas RA ADC_B 物理模拟输入通道选择器；对应专题保留在官方本页的子组导航中。[驱动后端译文](P456_ADC驱动后端.md)可直接查阅。

## 463.2\_设备树宏与解码器宏

宏中的 `node_id` 表示设备树节点标识符，`inst` 为 `DT_DRV_COMPAT` 对应的驱动兼容实例编号，`idx` 为通道索引，`name` 为通道名称，`default_value` 为后备值（Fallback Value）。流设备定义宏中的同名 `name` 则是生成的设备变量名，下文单独说明。

设备树宏返回静态初始化器（Static Initializer），用于初始化通道配置或通道规格结构。原始展开和示例按官方顺序保留。展开式中的辅助宏含义如下，便于对应原代码。

| 辅助名称 | 含义 |
| --- | --- |
| `DT_STRING_TOKEN`、`DT_STRING_TOKEN_BY_IDX` | 取得字符串属性对应的代码标记，后者按索引选择 |
| `DT_PROP`、`DT_PROP_OR` | 读取设备树属性；后者提供后备值 |
| `DT_REG_ADDR` | 取得节点的寄存器地址值，本例作为通道编号 |
| `DT_NODE_HAS_PROP` | 检查节点是否具有某属性 |
| `DT_CHILD`、`DT_NODELABEL`、`DT_PATH`、`DT_ALIAS` | 按子节点、节点标签、路径或别名取得节点标识符 |
| `DT_DRV_INST` | 取得当前驱动的指定实例节点 |
| `DT_HAS_COMPAT_STATUS_OKAY` | 检查指定兼容字符串是否有状态为 okay 的节点 |
| `DEVICE_DT_GET` | 取得设备树节点对应的设备对象指针 |
| `DT_IO_CHANNELS_CTLR_BY_IDX`、`DT_IO_CHANNELS_CTLR_BY_NAME` | 按索引或名称取得输入输出通道的控制器节点 |
| `DT_IO_CHANNELS_INPUT_BY_IDX`、`DT_IO_CHANNELS_INPUT_BY_NAME` | 按索引或名称取得输入输出通道的输入编号 |
| `ADC_DT_SPEC_STRUCT` | 组合 ADC 设备树规格的内部辅助宏 |
| `COND_CODE_1`、`IF_ENABLED` | 条件展开代码 |
| `UTIL_OR`、`UTIL_AND` | 预处理逻辑组合 |
| `UTIL_CAT`、`_CONCAT` | 拼接代码标识符 |
| `STRUCT_SECTION_ITERABLE` | 定义可迭代段中的结构体对象 |
| `ARRAY_SIZE` | 取得数组元素个数 |
| `RTIO_IODEV_DEFINE` | 定义 RTIO 输入输出设备 |
| `ADC_ACQ_TIME` | 组合采集时间；`ADC_ACQ_TIME_MICROSECONDS` 选择微秒单位，`ADC_ACQ_TIME_DEFAULT` 使用默认采集时间 |

Kconfig 选项 `CONFIG_ADC_CONFIGURABLE_INPUTS` 控制可配置模拟输入字段，`CONFIG_ADC_CONFIGURABLE_EXCITATION_CURRENT_SOURCE_PIN` 控制可配置激励电流源引脚字段，`CONFIG_ADC_CONFIGURABLE_VBIAS_PIN` 控制可配置偏置电压引脚字段。后文 `CONFIG_ADC_STREAM` 启用流式接口，`CONFIG_ADC_ASYNC` 启用异步接口。

### ADC_CHANNEL_CFG_DT

从给定设备树节点获取 ADC 通道配置，返回填入节点数据的 `struct adc_channel_cfg` 静态初始化器。参数 `node_id` 为节点标识符。下面依次保留宏展开、设备树片段和使用示例。

译注：示例使用 Nordic SAADC 模拟输入标识 `NRF_SAADC_AIN6`、`NRF_SAADC_AIN7`、`NRF_SAADC_AIN0`；注释中的 `.input-negative` 是原文拼写，实际字段名为 `input_negative`。输入、激励电流源引脚（Excitation Current Source Pin）和偏置电压引脚（Bias Voltage Pin）的条件配置也保留在展开式中。

```c
#define ADC_CHANNEL_CFG_DT(node_id)
```

```c
        { \
        .gain             = DT_STRING_TOKEN(node_id, zephyr_gain), \
        .reference        = DT_STRING_TOKEN(node_id, zephyr_reference), \
        .acquisition_time = DT_PROP(node_id, zephyr_acquisition_time), \
        .channel_id       = DT_REG_ADDR(node_id), \
COND_CODE_1(UTIL_OR(DT_PROP(node_id, zephyr_differential), \
                   UTIL_AND(CONFIG_ADC_CONFIGURABLE_INPUTS, \
                            DT_NODE_HAS_PROP(node_id, zephyr_input_negative))), \
        (.differential    = true,), \
        (.differential    = false,)) \
IF_ENABLED(CONFIG_ADC_CONFIGURABLE_INPUTS, \
        (.input_positive  = DT_PROP_OR(node_id, zephyr_input_positive, 0), \
         .input_negative  = DT_PROP_OR(node_id, zephyr_input_negative, 0),)) \
IF_ENABLED(CONFIG_ADC_CONFIGURABLE_EXCITATION_CURRENT_SOURCE_PIN, \
        (.current_source_pin_set = DT_NODE_HAS_PROP(node_id, zephyr_current_source_pin), \
         .current_source_pin = DT_PROP_OR(node_id, zephyr_current_source_pin, {0}),)) \
IF_ENABLED(CONFIG_ADC_CONFIGURABLE_VBIAS_PIN, \
        (.vbias_pins = DT_PROP_OR(node_id, zephyr_vbias_pins, 0),)) \
}
```

```dts
&adc {
   #address-cells = <1>;
   #size-cells = <0>;

   channel@0 {
       reg = <0>;
       zephyr,gain = "ADC_GAIN_1_6";
       zephyr,reference = "ADC_REF_INTERNAL";
       zephyr,acquisition-time = <ADC_ACQ_TIME(ADC_ACQ_TIME_MICROSECONDS, 20)>;
       zephyr,input-positive = <NRF_SAADC_AIN6>;
       zephyr,input-negative = <NRF_SAADC_AIN7>;
   };

   channel@1 {
       reg = <1>;
       zephyr,gain = "ADC_GAIN_1_6";
       zephyr,reference = "ADC_REF_INTERNAL";
       zephyr,acquisition-time = <ADC_ACQ_TIME_DEFAULT>;
       zephyr,input-positive = <NRF_SAADC_AIN0>;
   };
};
```

```c
static const struct adc_channel_cfg ch0_cfg_dt =
    ADC_CHANNEL_CFG_DT(DT_CHILD(DT_NODELABEL(adc), channel_0));
static const struct adc_channel_cfg ch1_cfg_dt =
    ADC_CHANNEL_CFG_DT(DT_CHILD(DT_NODELABEL(adc), channel_1));

// Initializes 'ch0_cfg_dt' to:
// {
//     .channel_id = 0,
//     .gain = ADC_GAIN_1_6,
//     .reference = ADC_REF_INTERNAL,
//     .acquisition_time = ADC_ACQ_TIME(ADC_ACQ_TIME_MICROSECONDS, 20),
//     .differential = true,
//     .input_positive = NRF_SAADC_AIN6,
//     .input-negative = NRF_SAADC_AIN7,
// }
// and 'ch1_cfg_dt' to:
// {
//     .channel_id = 1,
//     .gain = ADC_GAIN_1_6,
//     .reference = ADC_REF_INTERNAL,
//     .acquisition_time = ADC_ACQ_TIME_DEFAULT,
//     .input_positive = NRF_SAADC_AIN0,
// }
```

### ADC_DECODER_API_DT_DEFINE

定义解码器 API。对 ADC 的每个兼容字符串（Compatible String）应定义一次，从而创建可静态引用的解码接口。下面为原展开和使用示例。

译注：原示例列出 `get_timestamp`、`get_shift`，但当前 [`adc_decoder_api`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__decoder__api.html) 结构没有这两个成员，见前面的解码器结构页；保留示例，不将它标作可直接编译的当前定义。

```c
#define ADC_DECODER_API_DT_DEFINE()
```

```c
COND_CODE_1(DT_HAS_COMPAT_STATUS_OKAY(DT_DRV_COMPAT), (), (static))                     \
const STRUCT_SECTION_ITERABLE(adc_decoder_api, ADC_DECODER_NAME())
```

```c
ADC_DECODER_API_DT_DEFINE() = {
  .get_frame_count = my_driver_get_frame_count,
  .get_timestamp = my_driver_get_timestamp,
  .get_shift = my_driver_get_shift,
  .decode = my_driver_decode,
};
```

### ADC_DECODER_DT_GET

静态取得给定 `node_id` 节点的解码器。下面保留原展开和使用示例。译注：原示例把 [`adc_decoder_api`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__decoder__api.html) 直接作为类型名，当前文档结构名称为 `struct adc_decoder_api`；示例原样保留。

```c
#define ADC_DECODER_DT_GET(node_id)
```

```c
&UTIL_CAT(DT_STRING_TOKEN_BY_IDX(node_id, compatible, 0), __adc_decoder_api)
```

```c
static const adc_decoder_api *decoder = ADC_DECODER_DT_GET(DT_ALIAS(adc));
```

### ADC_DECODER_NAME

取得当前驱动的解码器名称，依赖预先定义 `DT_DRV_COMPAT`。

```c
#define ADC_DECODER_NAME()
```

```c
UTIL_CAT(DT_DRV_COMPAT, __adc_decoder_api)
```

### ADC_DT_SPEC_GET

等价于 `ADC_DT_SPEC_GET_BY_IDX(node_id, 0)`，取索引 0。返回 `struct adc_dt_spec` 静态初始化器。

```c
#define ADC_DT_SPEC_GET(node_id)
```

```c
ADC_DT_SPEC_GET_BY_IDX(node_id, 0)
```

### ADC_DT_SPEC_GET_BY_IDX

根据设备树节点 `node_id` 和通道索引 `idx` 获取 ADC 输入输出通道（I/O Channel）信息。节点必须定义 `io-channels` 属性。返回 `struct adc_dt_spec` 静态初始化器；另见 [`ADC_DT_SPEC_GET()`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#gad05df3d329ba785c094ea4c32e2913b7)。下面保留展开式、设备树片段和使用示例。

```c
#define ADC_DT_SPEC_GET_BY_IDX(node_id, idx)
```

```c
ADC_DT_SPEC_STRUCT(DT_IO_CHANNELS_CTLR_BY_IDX(node_id, idx), \
                   DT_IO_CHANNELS_INPUT_BY_IDX(node_id, idx))
```

```dts
/ {
    zephyr,user {
        io-channels = <&adc0 1>, <&adc0 3>;
    };
};

&adc0 {
   #address-cells = <1>;
   #size-cells = <0>;

   channel@3 {
       reg = <3>;
       zephyr,gain = "ADC_GAIN_1_5";
       zephyr,reference = "ADC_REF_VDD_1_4";
       zephyr,vref-mv = <750>;
       zephyr,acquisition-time = <ADC_ACQ_TIME_DEFAULT>;
       zephyr,resolution = <12>;
       zephyr,oversampling = <4>;
   };
};
```

```c
static const struct adc_dt_spec adc_chan0 =
    ADC_DT_SPEC_GET_BY_IDX(DT_PATH(zephyr_user), 0);
static const struct adc_dt_spec adc_chan1 =
    ADC_DT_SPEC_GET_BY_IDX(DT_PATH(zephyr_user), 1);

// Initializes 'adc_chan0' to:
// {
//     .dev = DEVICE_DT_GET(DT_NODELABEL(adc0)),
//     .channel_id = 1,
// }
// and 'adc_chan1' to:
// {
//     .dev = DEVICE_DT_GET(DT_NODELABEL(adc0)),
//     .channel_id = 3,
//     .channel_cfg_dt_node_exists = true,
//     .channel_cfg = {
//         .channel_id = 3,
//         .gain = ADC_GAIN_1_5,
//         .reference = ADC_REF_VDD_1_4,
//         .acquisition_time = ADC_ACQ_TIME_DEFAULT,
//     },
//     .vref_mv = 750,
//     .resolution = 12,
//     .oversampling = 4,
// }
```

### ADC_DT_SPEC_GET_BY_IDX_OR

与 [`ADC_DT_SPEC_GET_BY_IDX()`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#gae9867df7a034d45ed3d3c58c69c246ed) 相同，但支持通过 `default_value` 指定后备值。另见 [`ADC_DT_SPEC_INST_GET_BY_IDX_OR`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#gae1504135e99a163d10fbe10a545c9a4a)。 返回对应属性的 `struct adc_dt_spec` 静态初始化器；节点或属性不存在时返回 `default_value`。具体索引/名称存在性测试保留在展开式中。

```c
#define ADC_DT_SPEC_GET_BY_IDX_OR(node_id, idx, default_value)
```

```c
COND_CODE_1(DT_PROP_HAS_IDX(node_id, io_channels, idx), \
            (ADC_DT_SPEC_GET_BY_IDX(node_id, idx)), (default_value))
```

### ADC_DT_SPEC_GET_BY_NAME

根据设备树节点 `node_id` 和通道名称 `name` 获取 ADC 输入输出通道信息。节点必须定义 `io-channels` 属性。返回 `struct adc_dt_spec` 静态初始化器。下面保留展开式、含 `io-channel-names` 的设备树片段和使用示例。

```c
#define ADC_DT_SPEC_GET_BY_NAME(node_id, name)
```

```c
ADC_DT_SPEC_STRUCT(DT_IO_CHANNELS_CTLR_BY_NAME(node_id, name), \
                   DT_IO_CHANNELS_INPUT_BY_NAME(node_id, name))
```

```dts
/ {
    zephyr,user {
        io-channels = <&adc0 1>, <&adc0 3>;
        io-channel-names = "A0", "A1";
    };
};

&adc0 {
   #address-cells = <1>;
   #size-cells = <0>;

   channel@3 {
       reg = <3>;
       zephyr,gain = "ADC_GAIN_1_5";
       zephyr,reference = "ADC_REF_VDD_1_4";
       zephyr,vref-mv = <750>;
       zephyr,acquisition-time = <ADC_ACQ_TIME_DEFAULT>;
       zephyr,resolution = <12>;
       zephyr,oversampling = <4>;
   };
};
```

```c
static const struct adc_dt_spec adc_chan0 =
    ADC_DT_SPEC_GET_BY_NAME(DT_PATH(zephyr_user), a0);
static const struct adc_dt_spec adc_chan1 =
    ADC_DT_SPEC_GET_BY_NAME(DT_PATH(zephyr_user), a1);

// Initializes 'adc_chan0' to:
// {
//     .dev = DEVICE_DT_GET(DT_NODELABEL(adc0)),
//     .channel_id = 1,
// }
// and 'adc_chan1' to:
// {
//     .dev = DEVICE_DT_GET(DT_NODELABEL(adc0)),
//     .channel_id = 3,
//     .channel_cfg_dt_node_exists = true,
//     .channel_cfg = {
//         .channel_id = 3,
//         .gain = ADC_GAIN_1_5,
//         .reference = ADC_REF_VDD_1_4,
//         .acquisition_time = ADC_ACQ_TIME_DEFAULT,
//     },
//     .vref_mv = 750,
//     .resolution = 12,
//     .oversampling = 4,
// }
```

### ADC_DT_SPEC_GET_BY_NAME_OR

与 [`ADC_DT_SPEC_GET_BY_NAME()`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#ga058dbc619b7bbf624cd48518b429bb58) 相同，但支持通过 `default_value` 指定后备值。另见 [`ADC_DT_SPEC_INST_GET_BY_NAME_OR`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#gab6f02234d4eaf62e9c47694978cdae92)。 返回对应属性的 `struct adc_dt_spec` 静态初始化器；节点或属性不存在时返回 `default_value`。具体索引/名称存在性测试保留在展开式中。

```c
#define ADC_DT_SPEC_GET_BY_NAME_OR(node_id, name, default_value)
```

```c
COND_CODE_1(DT_PROP_HAS_NAME(node_id, io_channels, name), \
            (ADC_DT_SPEC_GET_BY_NAME(node_id, name)), (default_value))
```

### ADC_DT_SPEC_GET_OR

等价于 `ADC_DT_SPEC_GET_BY_IDX_OR(node_id, 0, default_value)`，取索引 0 并提供后备值。 返回对应属性的 `struct adc_dt_spec` 静态初始化器；节点或属性不存在时返回 `default_value`。具体索引/名称存在性测试保留在展开式中。

```c
#define ADC_DT_SPEC_GET_OR(node_id, default_value)
```

```c
ADC_DT_SPEC_GET_BY_IDX_OR(node_id, 0, default_value)
```

### ADC_DT_SPEC_INST_GET

等价于 `ADC_DT_SPEC_INST_GET_BY_IDX(inst, 0)`；参见 [`ADC_DT_SPEC_GET()`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#gad05df3d329ba785c094ea4c32e2913b7)，返回 `struct adc_dt_spec` 静态初始化器。

```c
#define ADC_DT_SPEC_INST_GET(inst)
```

```c
ADC_DT_SPEC_GET(DT_DRV_INST(inst))
```

### ADC_DT_SPEC_INST_GET_BY_IDX

根据 `DT_DRV_COMPAT` 的实例编号 `inst` 和通道索引 `idx` 获取 ADC 通道信息，返回 `struct adc_dt_spec` 静态初始化器。参见 [`ADC_DT_SPEC_GET_BY_IDX()`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#gae9867df7a034d45ed3d3c58c69c246ed)。

```c
#define ADC_DT_SPEC_INST_GET_BY_IDX(inst, idx)
```

```c
ADC_DT_SPEC_GET_BY_IDX(DT_DRV_INST(inst), idx)
```

### ADC_DT_SPEC_INST_GET_BY_IDX_OR

与 [`ADC_DT_SPEC_INST_GET_BY_IDX()`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#ga4705a1e2cc22fe73b7e967e8ba220584) 相同，但支持通过 `default_value` 指定后备值。另见 [`ADC_DT_SPEC_GET_BY_IDX_OR`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#ga8bc36476f0362513f9257c658e0ef8c1)。 返回对应属性的 `struct adc_dt_spec` 静态初始化器；节点或属性不存在时返回 `default_value`。具体索引/名称存在性测试保留在展开式中。

```c
#define ADC_DT_SPEC_INST_GET_BY_IDX_OR(inst, idx, default_value)
```

```c
ADC_DT_SPEC_GET_BY_IDX_OR(DT_DRV_INST(inst), idx, default_value)
```

### ADC_DT_SPEC_INST_GET_BY_NAME

根据 `DT_DRV_COMPAT` 的实例编号 `inst` 和通道名称 `name` 获取 ADC 通道信息，返回 `struct adc_dt_spec` 静态初始化器。参见 [`ADC_DT_SPEC_GET_BY_NAME()`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#ga058dbc619b7bbf624cd48518b429bb58)。

```c
#define ADC_DT_SPEC_INST_GET_BY_NAME(inst, name)
```

```c
ADC_DT_SPEC_GET_BY_NAME(DT_DRV_INST(inst), name)
```

### ADC_DT_SPEC_INST_GET_BY_NAME_OR

与 [`ADC_DT_SPEC_INST_GET_BY_NAME()`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#ga48139728bd2cec25208ef37d9bbcc34f) 相同，但支持通过 `default_value` 指定后备值。另见 [`ADC_DT_SPEC_GET_BY_NAME_OR`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#ga3522baaa63a00ab672d7ee35a634017c)。 返回对应属性的 `struct adc_dt_spec` 静态初始化器；节点或属性不存在时返回 `default_value`。具体索引/名称存在性测试保留在展开式中。

```c
#define ADC_DT_SPEC_INST_GET_BY_NAME_OR(inst, name, default_value)
```

```c
ADC_DT_SPEC_GET_BY_NAME_OR(DT_DRV_INST(inst), name, default_value)
```

### ADC_DT_SPEC_INST_GET_OR

等价于取实例中索引 0 的 `ADC_DT_SPEC_INST_GET_BY_IDX_OR(inst, 0, default_value)`。参见 [`ADC_DT_SPEC_GET_OR()`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#ga9525d07f52b7e25fa65bdff8865260c9)。译注：原摘要把最后一个参数简写为 `default`；实际宏参数与展开均为 `default_value`。 返回对应属性的 `struct adc_dt_spec` 静态初始化器；节点或属性不存在时返回 `default_value`。具体索引/名称存在性测试保留在展开式中。

```c
#define ADC_DT_SPEC_INST_GET_OR(inst, default_value)
```

```c
ADC_DT_SPEC_GET_OR(DT_DRV_INST(inst), default_value)
```

### ADC_DT_STREAM_IODEV

定义用于 ADC 流式采样的 RTIO 输入输出设备（I/O Device，IODEV）。宏创建所需静态数据结构，把设备树节点指定的 ADC 控制器、一组 ADC 通道规格和一个或多个触发定义关联起来。

参数 `name` 是生成的 `struct rtio_iodev` 变量名；`dt_node` 为 ADC 控制器节点标识符；[`adc_dt_spec`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__dt__spec.html) 为 [`adc_dt_spec`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__dt__spec.html) 通道规格数组；可变参数 `...` 为一个或多个 [`adc_stream_trigger`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__stream__trigger.html) 初始化器。下面保留原展开和使用示例。

```c
#define ADC_DT_STREAM_IODEV(name, dt_node, adc_dt_spec, ...)
```

```c
static struct adc_stream_trigger _CONCAT(__trigger_array_, name)[] = {__VA_ARGS__};     \
static struct adc_read_config _CONCAT(__adc_read_config_, name) = {                     \
        .adc = DEVICE_DT_GET(dt_node),                                                  \
        .is_streaming = true,                                                           \
        .adc_spec = adc_dt_spec,                                                        \
        .triggers = _CONCAT(__trigger_array_, name),                                    \
        .adc_spec_cnt = ARRAY_SIZE(adc_dt_spec),                                        \
        .trigger_cnt = ARRAY_SIZE(_CONCAT(__trigger_array_, name)),                     \
};                                                                                      \
RTIO_IODEV_DEFINE(name, &__adc_iodev_api, &_CONCAT(__adc_read_config_, name))
```

```c
ADC_DT_STREAM_IODEV(my_iodev, DT_ALIAS(adc0), adc_channels,
                   {ADC_TRIG_FIFO_FULL, ADC_STREAM_DATA_INCLUDE});
```

## 463.3\_原始值转换函数类型

[`adc_raw_to_x_fn`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#ga37d3183c11465aef0890484ffd1f5144) 将 ADC 原始单位转换成具体输出单位，完成从原始测量值到物理电压的换算。

```c
typedef int (*adc_raw_to_x_fn)(int32_t ref_mv, enum adc_gain gain,
                              uint8_t resolution, int32_t *valp);
```

| 参数 | 含义 |
| --- | --- |
| `ref_mv` | 测量所用参考电压，单位为毫伏（Millivolt）；可以来自 [`adc_ref_get()`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#ga7a4d12848b6ffb948b60f080abe3ac4d)、[`adc_ref_internal()`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#gad11845f5621d0b0d03da4b6484d79aa4) 或已知外部参考源 |
| `gain` | 输入采样使用的增益配置 |
| `resolution` | 样本绝对值所占的位数；差分采样时，比 [`adc_sequence`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__sequence.html) 中的分辨率少 1 |
| `valp` | 输入时指向原始测量值，成功时写入换算后的值；失败时保持原值不变 |

转换成功返回 0；增益不可逆时返回 `-EINVAL`（无效参数，Invalid Argument）。

## 463.4\_采样完成回调类型

[`adc_sequence_callback`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#ga9150eb6dc53d1c62b9fa225c0a371d6d) 定义请求的一次采样完成后可选调用的回调（Callback）。

```c
typedef enum adc_action (*adc_sequence_callback)(
    const struct device *dev, const struct adc_sequence *sequence,
    uint16_t sampling_index);
```

`dev` 指向驱动实例的设备结构；`sampling_index` 为已完成采样的索引，范围 0—65535。返回值为驱动接下来应执行的 [`adc_action`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#ga8f6df993405679f852ae4cd8c63c6917)。

**`sequence` 指向启动采样时传入结构的副本。**因此，不能用 [`CONTAINER_OF()`](../util_reference/P001_通用工具公共接口.md#gac5bc561d1bfd1bf68877fe577779bd2f) 宏通过它找回关联的其他数据，应使用 [`adc_sequence_options::user_data`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__sequence__options.html#a262fd6daefb22df02c726aafcddc6d47) 字段。

## 463.5\_枚举类型

以下保留枚举项及原有显式赋值，未显式赋值的项按 C 枚举规则取值。VDD 表示供电电压（Supply Voltage），VDD/2、VDD/3、VDD/4 分别取其二分之一、三分之一和四分之一。

### adc_gain

| 枚举项及显式赋值 | 含义 |
| --- | --- |
| [`ADC_GAIN_1_6`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#gga306f882323c66b263d3797124ca5f3a0abb26700162bfc68a2beadc1e78b758c1) | 增益乘以 1/6。 |
| [`ADC_GAIN_1_5`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#gga306f882323c66b263d3797124ca5f3a0a198c40369bddfc3c0eaa8ae3bb1be0c9) | 增益乘以 1/5。 |
| [`ADC_GAIN_1_4`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#gga306f882323c66b263d3797124ca5f3a0afa55c5a94bfebb9a70638e9ab32eabf8) | 增益乘以 1/4。 |
| [`ADC_GAIN_2_7`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#gga306f882323c66b263d3797124ca5f3a0a30cf06d8c6d323a8bfef3a508f2c3388) | 增益乘以 2/7。 |
| [`ADC_GAIN_1_3`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#gga306f882323c66b263d3797124ca5f3a0af896fe01119930815ac78a4ee87635ee) | 增益乘以 1/3。 |
| [`ADC_GAIN_2_5`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#gga306f882323c66b263d3797124ca5f3a0a4a59d3dd1e2e2fbe2ec593291ca307e0) | 增益乘以 2/5。 |
| [`ADC_GAIN_1_2`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#gga306f882323c66b263d3797124ca5f3a0a2d36559128c21834d1188aed43d236d2) | 增益乘以 1/2。 |
| [`ADC_GAIN_2_3`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#gga306f882323c66b263d3797124ca5f3a0ac720b0730cfef7c55f97777fec75dc62) | 增益乘以 2/3。 |
| [`ADC_GAIN_4_5`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#gga306f882323c66b263d3797124ca5f3a0ad0ee4a6bfc749a3213f0c44d30e8e6df) | 增益乘以 4/5。 |
| [`ADC_GAIN_1`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#gga306f882323c66b263d3797124ca5f3a0a76b3097b0b38d33266d36f5a5d534e54) | 增益乘以 1。 |
| [`ADC_GAIN_2`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#gga306f882323c66b263d3797124ca5f3a0aff4b7cc577e333a3a684e4e56b124868) | 增益乘以 2。 |
| [`ADC_GAIN_3`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#gga306f882323c66b263d3797124ca5f3a0a113a3324782a4517bb71fc3b03aeef5e) | 增益乘以 3。 |
| [`ADC_GAIN_4`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#gga306f882323c66b263d3797124ca5f3a0a12756ff0f6a345ff3fee2077e1153300) | 增益乘以 4。 |
| [`ADC_GAIN_6`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#gga306f882323c66b263d3797124ca5f3a0aba255a08f5ff25388778057d725a77c8) | 增益乘以 6。 |
| [`ADC_GAIN_8`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#gga306f882323c66b263d3797124ca5f3a0ae9a429f8b69dd0e5cae0e1ab7dbe7dc3) | 增益乘以 8。 |
| [`ADC_GAIN_12`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#gga306f882323c66b263d3797124ca5f3a0a3ff31845095f2b0fe7e62b2b826411e8) | 增益乘以 12。 |
| [`ADC_GAIN_16`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#gga306f882323c66b263d3797124ca5f3a0a4b18ba08d86e630f2deeeea5b329f970) | 增益乘以 16。 |
| [`ADC_GAIN_24`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#gga306f882323c66b263d3797124ca5f3a0a5d19226b1d1728180101e65b8386ff33) | 增益乘以 24。 |
| [`ADC_GAIN_32`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#gga306f882323c66b263d3797124ca5f3a0ac693403ea0f70f5723a98fe11967c13f) | 增益乘以 32。 |
| [`ADC_GAIN_64`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#gga306f882323c66b263d3797124ca5f3a0a064c567978a50dd58d48d481388dd6eb) | 增益乘以 64。 |
| [`ADC_GAIN_128`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#gga306f882323c66b263d3797124ca5f3a0a1b3c6d80db15acf962192341d4754829) | 增益乘以 128。 |

### adc_reference

| 枚举项及显式赋值 | 含义 |
| --- | --- |
| [`ADC_REF_VDD_1`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#gga91b0f997d73739cf9f7349b7581e1f56ae41651d9d2ba0d3c2a976177fc6ed1b3) | 供电电压 VDD。 |
| [`ADC_REF_VDD_1_2`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#gga91b0f997d73739cf9f7349b7581e1f56a5f47fb0b239da79577887baf2576eb0d) | VDD/2。 |
| [`ADC_REF_VDD_1_3`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#gga91b0f997d73739cf9f7349b7581e1f56a8e5dfe37c3993e118d6e316c9fa0aad1) | VDD/3。 |
| [`ADC_REF_VDD_1_4`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#gga91b0f997d73739cf9f7349b7581e1f56a93d4dc4332b3346a7332383ecf745d2c) | VDD/4。 |
| [`ADC_REF_INTERNAL`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#gga91b0f997d73739cf9f7349b7581e1f56a239921743b35d32a558a43deee2ce709) | 内部参考源。 |
| [`ADC_REF_EXTERNAL0`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#gga91b0f997d73739cf9f7349b7581e1f56afc15362bdf426f412e150ae9f8d224e6) | 外部参考源，输入 0。 |
| [`ADC_REF_EXTERNAL1`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#gga91b0f997d73739cf9f7349b7581e1f56a2733819da753b01a8116d076498fe52a) | 外部参考源，输入 1。 |

### adc_action

| 枚举项及显式赋值 | 含义 |
| --- | --- |
| `ADC_ACTION_CONTINUE = 0` | 正常继续序列。 |
| [`ADC_ACTION_REPEAT`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#gga8f6df993405679f852ae4cd8c63c6917a8efc10c77ea616d568f88d3ef88b1715) | 重复本次采样；把新的一个或多个样本写入最近一次样本所在的相同位置。 |
| [`ADC_ACTION_FINISH`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#gga8f6df993405679f852ae4cd8c63c6917a68a21759522a3d584417fa12359b4dc9) | 立即结束序列。 |

### adc_trigger_type

| 枚举项及显式赋值 | 含义 |
| --- | --- |
| [`ADC_TRIG_DATA_READY`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#gga795f234592e67078c9aad07e1ea099bba404443c7498b487cf965724b2373390a) | 每次新数据就绪时触发。 |
| [`ADC_TRIG_FIFO_WATERMARK`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#gga795f234592e67078c9aad07e1ea099bba69627e59fb6945590cd5c6df1441b2d9) | 达到 FIFO 水位（Watermark）时触发。 |
| [`ADC_TRIG_FIFO_FULL`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#gga795f234592e67078c9aad07e1ea099bbad0d7c8e307a73cc34c58d7e2199d8808) | FIFO 满时触发。 |
| [`ADC_TRIG_COMMON_COUNT`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#gga795f234592e67078c9aad07e1ea099bbaf5fa3757acf5098c21a43208c87888ee) | 全部公共 ADC 触发类型的数量。 |
| `ADC_TRIG_PRIV_START = ADC_TRIG_COMMON_COUNT` | 从此值开始是 ADC 专用类型，参见相应 ADC 头文件。 |
| `ADC_TRIG_MAX = INT16_MAX` | 描述 ADC 触发类型的最大值。 |

### adc_stream_data_opt

| 枚举项及显式赋值 | 含义 |
| --- | --- |
| `ADC_STREAM_DATA_INCLUDE = 0` | 包含该触发关联的全部数据。 |
| `ADC_STREAM_DATA_NOP = 1` | 不处理关联触发数据，数据可以稍后消费。 |
| `ADC_STREAM_DATA_DROP = 2` | 刷新/清除关联的全部触发数据。 |

## 463.6\_adc_channel_setup

配置 ADC 通道。**每个通道在被读取请求选中之前，都必须先调用此函数配置。**

`dev` 指向驱动实例设备结构，`channel_cfg` 为通道配置。成功返回 0；参数值无效时返回 `-EINVAL`。

```c
int adc_channel_setup( const struct device * dev, const struct adc_channel_cfg * channel_cfg );
```

## 463.7\_adc_channel_setup_dt

根据 `struct adc_dt_spec` 配置 ADC 通道，输入 `spec` 为设备树 ADC 规格。返回 [`adc_channel_setup()`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#ga7bc0488b2d08ae2ee4996c0eed11f0bf) 的结果；设备树信息无效时返回 `-ENOTSUP`（不支持，Not Supported）。

```c
static inline int adc_channel_setup_dt( const struct adc_dt_spec * spec);
```

## 463.8\_adc_gain_invert

撤销测量值中已经应用的增益。`gain` 为放大输入所用增益，`value` 指向待处理数值；成功后去除增益影响，无法逆转时保持原值不变。

例如增益为 `ADC_GAIN_1_6`、初值为 10，函数返回后数值为 60。成功返回 0；无法解释增益时返回 `-EINVAL`。

```c
int adc_gain_invert( enum adc_gain gain, int32_t * value );
```

## 463.9\_adc_gain_invert_64

撤销测量值中已经应用的增益。`gain` 为放大输入所用增益，`value` 指向待处理数值；成功后去除增益影响，无法逆转时保持原值不变。

例如增益为 `ADC_GAIN_1_6`、初值为 10，函数返回后数值为 60。成功返回 0；无法解释增益时返回 `-EINVAL`。

```c
int adc_gain_invert_64( enum adc_gain gain, int64_t * value );
```

## 463.10\_adc_get_decoder

获取设备的解码器 API。**仅在启用 [`CONFIG_ADC_STREAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_STREAM) 时可用。**输入 `dev` 指向驱动实例，输出参数 `api` 在成功时接收解码器指针。成功返回 0，否则返回负错误码。

```c
int adc_get_decoder( const struct device * dev, const struct adc_decoder_api ** api );
```

## 463.11\_adc_is_ready_dt

检查设备树规格 `spec` 对应的 ADC 是否已就绪。可以使用时返回 `true`，否则返回 `false`。

```c
static inline bool adc_is_ready_dt( const struct adc_dt_spec * spec);
```

## 463.12\_adc_raw_to_microvolts

把 ADC 原始值转换成微伏（Microvolt）。参数与返回规则参见本页 [`adc_raw_to_x_fn`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#ga37d3183c11465aef0890484ffd1f5144)。

```c
static inline int adc_raw_to_microvolts( int32_t ref_mv, enum adc_gain gain, uint8_t resolution, int32_t * valp );
```

## 463.13\_adc_raw_to_microvolts_dt

利用设备树 `spec` 中的信息把原始 ADC 值转换为微伏。`spec` 为输入规格，`valp` 为输入/输出原始值指针：转换成功后保存微伏值，失败时原值不变。

返回 [`adc_raw_to_microvolts()`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#ga443772e29554fb289032c3b0b7d2fe8d) 的结果；设备树信息无效时返回 `-ENOTSUP`。

```c
static inline int adc_raw_to_microvolts_dt( const struct adc_dt_spec * spec, int32_t * valp );
```

## 463.14\_adc_raw_to_millivolts

把 ADC 原始值转换成毫伏（Millivolt）。参数与返回规则参见本页 [`adc_raw_to_x_fn`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#ga37d3183c11465aef0890484ffd1f5144)。

```c
static inline int adc_raw_to_millivolts( int32_t ref_mv, enum adc_gain gain, uint8_t resolution, int32_t * valp );
```

## 463.15\_adc_raw_to_millivolts_dt

利用设备树 `spec` 中的信息把原始 ADC 值转换为毫伏。`spec` 为输入规格，`valp` 为输入/输出原始值指针：转换成功后保存毫伏值，失败时原值不变。

返回 [`adc_raw_to_millivolts()`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#gaef98dabea3e0dc1cef8add298171a950) 的结果；设备树信息无效时返回 `-ENOTSUP`。

```c
static inline int adc_raw_to_millivolts_dt( const struct adc_dt_spec * spec, int32_t * valp );
```

## 463.16\_adc_raw_to_x_dt_chan

把 ADC 原始值转换成任意输出单位。

| 参数 | 方向 | 含义 |
| --- | --- | --- |
| `conv_func` | 输入 | 转换到最终输出单位的函数 |
| `spec` | 输入 | 设备树 ADC 规格 |
| `channel_cfg` | 输入 | 实际采样使用的通道配置，可以是 `spec` 中的配置，也可以基于它修改，例如使用不同增益 |
| `valp` | 输入/输出 | 原始测量值，成功时改为换算结果，失败时原值不变 |

返回转换函数 [`adc_raw_to_x_fn`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#ga37d3183c11465aef0890484ffd1f5144) 的结果；设备树信息无效时返回 `-ENOTSUP`。

```c
static inline int adc_raw_to_x_dt_chan( adc_raw_to_x_fn conv_func, const struct adc_dt_spec * spec, const struct adc_channel_cfg * channel_cfg, int32_t * valp );
```

## 463.17\_adc_read

设置读取请求。`dev` 指向驱动实例设备结构，`sequence` 指定请求的采样序列。**从用户模式（User Mode）调用时，序列选项中的回调必须为 `NULL`。**

| 返回值 | 含义 |
| --- | --- |
| `0` | 成功 |
| `-EINVAL` | 参数值无效 |
| `-ENOMEM` | 提供的缓冲区不足以保存全部请求采样结果 |
| `-ENOTSUP` | 不支持请求的工作模式 |
| `-EBUSY` | 上一次采样仍在执行时触发下一次采样，仅可能出现在按间隔采样时，说明所选间隔太小 |

对于上述 `-EBUSY` 情形，**所有请求样本仍写入缓冲区，但至少部分样本比计划时刻额外延迟**，不能把此错误简单理解为完全没有采到数据。

```c
int adc_read( const struct device * dev, const struct adc_sequence * sequence );
```

## 463.18\_adc_read_async

设置异步读取请求。**仅在选择 [`CONFIG_ADC_ASYNC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_ASYNC) 时可用；从用户模式调用时，序列选项中的回调必须为 `NULL`。**

`dev` 指向驱动实例设备结构，`sequence` 指定请求的采样序列。`async` 指向有效且已准备好接收通知的 `struct k_poll_signal` 轮询信号（Poll Signal）；如果为 `NULL`，函数不会通知事务何时结束或是否成功。

成功返回 0，否则返回负错误码；可能的错误码见 [`adc_read()`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#ga7567ce3b03ebb294620b4e32b7561ab3)。

```c
int adc_read_async( const struct device * dev, const struct adc_sequence * sequence, struct k_poll_signal * async );
```

## 463.19\_adc_read_async_dt

设置异步读取请求。**仅在选择 [`CONFIG_ADC_ASYNC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_ASYNC) 时可用；从用户模式调用时，序列选项中的回调必须为 `NULL`。**

`spec` 是设备树 ADC 规格，`sequence` 指定请求的采样序列。`async` 指向有效且已准备好接收通知的 `struct k_poll_signal` 轮询信号（Poll Signal）；如果为 `NULL`，函数不会通知事务何时结束或是否成功。

原文将返回值列为 [`adc_read()`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#ga7567ce3b03ebb294620b4e32b7561ab3) 的结果，参见该函数。

```c
static inline int adc_read_async_dt( const struct adc_dt_spec * spec, const struct adc_sequence * sequence, struct k_poll_signal * async );
```

## 463.20\_adc_read_dt

使用设备树规格 `spec` 设置读取请求，`sequence` 指定采样序列。返回 [`adc_read()`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#ga7567ce3b03ebb294620b4e32b7561ab3) 的结果，参见该函数的限制和错误码。

```c
static inline int adc_read_dt( const struct adc_dt_spec * spec, const struct adc_sequence * sequence );
```

## 463.21\_adc_ref_get

获取设备 `dev` 的所选参考源 `ref` 对应的毫伏电压，输出到 `vref_mv`。

驱动提供 `ref_get` 回调时调用该回调；否则，[`ADC_REF_INTERNAL`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#gga91b0f997d73739cf9f7349b7581e1f56a239921743b35d32a558a43deee2ce709) 回退使用静态 `ref_internal` 字段，其他参考源返回 `-ENOTSUP`。实现了 `ref_get` 的驱动自行负责内部参考源的设备树或 `ref_internal` 后备处理。

| 返回值 | 含义 |
| --- | --- |
| `0` | 成功，`vref_mv` 保存毫伏值 |
| `-EINVAL` | `vref_mv` 为 `NULL` |
| `-ENOTSUP` | 不支持该参考源，或不存在数值来源 |
| `-ENODATA` | 支持该参考源，但目前没有已知毫伏值 |

```c
static inline int adc_ref_get( const struct device * dev, enum adc_reference ref, uint16_t * vref_mv );
```

## 463.22\_adc_ref_internal

获取设备 `dev` 的内部参考电压，以毫伏表示，是 [`adc_ref_get()`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#ga7a4d12848b6ffb948b60f080abe3ac4d) 对 [`ADC_REF_INTERNAL`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#gga91b0f997d73739cf9f7349b7581e1f56a239921743b35d32a558a43deee2ce709) 的便捷封装。

实现 `ref_get` 的驱动可以随时间更新该值，例如硬件校准后；函数签名不因此变化。正返回值为参考电压，无法获取参考电压信息时返回 0。

```c
static inline uint16_t adc_ref_internal( const struct device * dev);
```

## 463.23\_adc_sequence_init_dt

使用设备树规格 `spec` 初始化输出序列 `seq`。**只初始化 `channels`、`resolution` 和 `oversampling` 三个字段；其他字段由调用方初始化。**

成功返回 0；`spec` 不包含有效通道配置时返回 `-ENOTSUP`。

```c
static inline int adc_sequence_init_dt( const struct adc_dt_spec * spec, struct adc_sequence * seq );
```

## 463.24\_adc_stream

启动连续 ADC 流式会话。向给定输入输出设备关联的 RTIO 上下文提交多次完成读取请求（Multishot Read）。**仅在启用 [`CONFIG_ADC_STREAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_STREAM) 时可用。**

随着样本就绪，驱动持续产生完成队列项（Completion Queue Entry，CQE），可通过 [`rtio_cqe_consume_block()`](../rtio_core_reference/P001_RTIO公共接口.md#gaf617d05d9b59ce1f1d0697617ef6f249) 消费。实际样本存储在内存池（Memory Pool），应用必须先通过 [`rtio_cqe_get_mempool_buffer()`](../rtio_core_reference/P001_RTIO公共接口.md#gaedbf9386a36ed99baa290ef6c318ded1) 取得缓冲区，再用驱动的 [`adc_decoder_api`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__decoder__api.html) 解码。**处理完成后必须释放缓冲区和 CQE。**

| 参数 | 方向 | 含义 |
| --- | --- | --- |
| `iodev` | 输入 | 由 [`ADC_DT_STREAM_IODEV`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#gabe7d699fba7b663c4b5be5068b9d0a15) 创建的 RTIO 输入输出设备 |
| `ctx` | 输入 | 接收流式数据的 RTIO 上下文，带内存池 |
| `userdata` | 输入 | 可选用户数据，传递到 CQE |
| `handle` | 输出 | 可选输出指针；非 `NULL` 时接收可用于取消流的提交队列项（Submission Queue Entry，SQE） |

成功返回 0；无法从 RTIO 上下文取得 SQE 时返回 `-ENOMEM`。

```c
static inline int adc_stream( struct rtio_iodev * iodev, struct rtio * ctx, void * userdata, struct rtio_sqe ** handle );
```

## 463.25\_内部解码器声明与设备API对象

官方页面还列出内部宏调用和常量接口对象，没有额外文字说明：

```c
DT_FOREACH_STATUS_OKAY_NODE(Z_MAYBE_ADC_DECODER_DECLARE_INTERNAL)
extern const struct rtio_iodev_api __adc_iodev_api;
```

译注：前者遍历状态为 okay 的设备树节点，为可用解码器生成内部声明；后者是 ADC RTIO 输入输出设备所用的接口对象，流设备宏引用它。它们不是需要应用像普通函数一样调用的 ADC 采样入口。


---

[上一章：ADC分压器设备树规格](P462_ADC分压器设备树规格.md) · [下一章：ADC模拟器接口](P464_ADC模拟器接口.md) · [返回大纲](大纲.md)
