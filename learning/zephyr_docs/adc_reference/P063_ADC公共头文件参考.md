---
id: learning.zephyr-docs.adc_reference.adcmainheader-63
title: ADC公共头文件参考
kind: reference
status: maintained
domains: [zephyr, adc_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2adc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第63章\_ADC公共头文件参考

原文：[drivers_2adc_8h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2adc_8h.html)。读取日期：2026-10-13，`latest`。

`zephyr/drivers/adc.h` 是模数转换器（Analog-to-Digital Converter，ADC）驱动应用程序接口（Application Programming Interface，API）的主头文件。它汇集通道配置、设备树规格、采样序列、读取、流式处理和数值换算的声明。

本页完整翻译官方“文件参考”列出的结构、宏、类型、枚举和函数简述；详细参数、执行约束及错误码沿[ADC公共接口参考](../hardware/P463_ADC公共接口参考.md)和各结构页阅读。完整可见源码另存于[下一章](P064_ADC公共头文件源码.md)，不会用本页的声明列表代替源码。

## 63.1\_头文件依赖

```c
#include <zephyr/device.h>
#include <zephyr/dt-bindings/adc/adc.h>
#include <zephyr/kernel.h>
#include <zephyr/rtio/rtio.h>
#include <zephyr/dsp/types.h>
#include <zephyr/syscalls/adc.h>
```

它们依次涉及设备、ADC设备树（Devicetree）常量、内核、实时输入输出（Real-Time Input/Output，RTIO）、数字信号处理（Digital Signal Processing，DSP）类型和系统调用（System Calls）。通用采集时间常量见[本册第1章](P001_ADC通用设备树常量参考.md)。原源码把系统调用头放在文件末尾，以上是文件参考页的依赖列表。

## 63.2\_数据结构

表中对象均为结构体（Structure）；未附加简述的项目保留入口，并链接已有完整字段译文。

| 结构 | 中文说明与字段入口 |
| --- | --- |
| `struct adc_channel_cfg` | [指定ADC通道配置的结构](../hardware/P443_ADC通道配置结构.md) |
| `struct adc_dt_spec` | [保存设备树中指定的ADC通道信息](../hardware/P444_ADC设备树规格.md) |
| `struct adc_sequence_options` | [定义ADC采样序列的附加选项](../hardware/P446_ADC采样序列选项.md) |
| `struct adc_sequence` | [定义ADC采样序列](../hardware/P445_ADC采样序列结构.md) |
| `struct adc_data_header` | [ADC数据头；本文件参考页未附加简述](../hardware/P450_ADC数据头.md) |
| `struct adc_data` | [ADC通道的数据](../hardware/P452_ADC解码数据.md) |
| `struct adc_data::adc_sample_data` | [嵌套样本数据结构；本文件参考页未附加简述](../hardware/P453_ADC样本数据.md) |
| `struct adc_stream_trigger` | [流触发配置；本文件参考页未附加简述](../hardware/P449_ADC流触发配置.md) |
| `struct adc_chan_spec` | [ADC通道规格（Channel Specification）](../hardware/P447_ADC通道规格.md) |
| `struct adc_read_config` | [ADC读取配置；本文件参考页未附加简述](../hardware/P448_ADC读取配置.md) |
| `struct adc_decoder_api` | [解码单个原始数据缓冲区（Raw Data Buffer）](../hardware/P455_ADC解码器API结构.md) |
| `struct adc_driver_api` | [ADC驱动操作（Driver Operations）](../hardware/P454_ADC驱动API结构.md) |
| `struct adc_data_generic_header` | [编码后的ADC流式帧（Streaming Frame）的通用头部](../hardware/P451_ADC通用数据头.md) |

## 63.3\_设备树与解码器宏

宏（Macro）的 `node_id` 参数为设备树节点标识，`inst` 为实例号，`name` 为名称，`idx` 为索引，`default_value` 为后备默认值。`DT_DRV_COMPAT` 表示当前驱动使用的设备树兼容标识。输入输出通道（I/O Channel）在设备树中写作 `io-channels`。

| 宏签名 | 中文说明 |
| --- | --- |
| `ADC_CHANNEL_CFG_DT(node_id)` | 从给定设备树节点取得ADC通道配置 |
| `ADC_DT_SPEC_GET_BY_NAME(node_id, name)` | 按名称取得ADC输入输出通道信息 |
| `ADC_DT_SPEC_GET_BY_NAME_OR(node_id, name, default_value)` | 与按名称取得规格相同，但提供后备默认值 |
| `ADC_DT_SPEC_INST_GET_BY_NAME(inst, name)` | 从DT_DRV_COMPAT对应实例按名称取得通道信息 |
| `ADC_DT_SPEC_INST_GET_BY_NAME_OR(inst, name, default_value)` | 实例按名称取得规格，并提供后备默认值 |
| `ADC_DT_SPEC_GET_BY_IDX(node_id, idx)` | 从设备树按索引取得ADC通道信息 |
| `ADC_DT_SPEC_GET_BY_IDX_OR(node_id, idx, default_value)` | 按索引取得规格，并提供后备默认值 |
| `ADC_DT_SPEC_INST_GET_BY_IDX(inst, idx)` | 从DT_DRV_COMPAT对应实例按索引取得通道信息 |
| `ADC_DT_SPEC_INST_GET_BY_IDX_OR(inst, idx, default_value)` | 实例按索引取得规格，并提供后备默认值 |
| `ADC_DT_SPEC_GET(node_id)` | 等价于 `ADC_DT_SPEC_GET_BY_IDX(node_id, 0)` |
| `ADC_DT_SPEC_GET_OR(node_id, default_value)` | 等价于 `ADC_DT_SPEC_GET_BY_IDX_OR(node_id, 0, default_value)` |
| `ADC_DT_SPEC_INST_GET(inst)` | 等价于 `ADC_DT_SPEC_INST_GET_BY_IDX(inst, 0)` |
| `ADC_DT_SPEC_INST_GET_OR(inst, default_value)` | 实例的索引0规格，并提供后备默认值；见下方译注 |
| `ADC_DECODER_NAME()` | 取得当前驱动的解码器（Decoder）名称 |
| `ADC_DECODER_DT_GET(node_id)` | 静态取得给定节点的解码器 |
| `ADC_DECODER_API_DT_DEFINE()` | 定义解码器API |
| `ADC_DT_STREAM_IODEV(name, dt_node, adc_dt_spec, ...)` | 为ADC流式处理定义RTIO输入输出设备（I/O Device） |

译注：原文把 `ADC_DT_SPEC_INST_GET_OR(inst, default_value)` 的等价式写成 `ADC_DT_SPEC_INST_GET_BY_IDX_OR(inst, 0, default)`，末项使用了 `default`；源码实际转交的形参名为 `default_value`。这里记录原文差异，使用时应保持源码的 `default_value` 形参关系。

## 63.4\_枚举类型

枚举（Enumeration）包括通道增益（Gain）、参考源（Reference）、采样后动作、触发类型和流数据处置。下表不为隐式枚举项额外编造赋值；只有源码显式写出的等号值才出现在“原声明”列。详细行为见[ADC公共接口](../hardware/P463_ADC公共接口参考.md)。

枚举类型 `enum adc_gain`：

| 原声明 | 中文含义 |
| --- | --- |
| `ADC_GAIN_1_6` | 增益1/6 |
| `ADC_GAIN_1_5` | 增益1/5 |
| `ADC_GAIN_1_4` | 增益1/4 |
| `ADC_GAIN_2_7` | 增益2/7 |
| `ADC_GAIN_1_3` | 增益1/3 |
| `ADC_GAIN_2_5` | 增益2/5 |
| `ADC_GAIN_1_2` | 增益1/2 |
| `ADC_GAIN_2_3` | 增益2/3 |
| `ADC_GAIN_4_5` | 增益4/5 |
| `ADC_GAIN_1` | 增益1 |
| `ADC_GAIN_2` | 增益2 |
| `ADC_GAIN_3` | 增益3 |
| `ADC_GAIN_4` | 增益4 |
| `ADC_GAIN_6` | 增益6 |
| `ADC_GAIN_8` | 增益8 |
| `ADC_GAIN_12` | 增益12 |
| `ADC_GAIN_16` | 增益16 |
| `ADC_GAIN_24` | 增益24 |
| `ADC_GAIN_32` | 增益32 |
| `ADC_GAIN_64` | 增益64 |
| `ADC_GAIN_128` | 增益128 |

枚举类型 `enum adc_reference`：

| 原声明 | 中文含义 |
| --- | --- |
| `ADC_REF_VDD_1` | VDD参考 |
| `ADC_REF_VDD_1_2` | VDD的1/2参考 |
| `ADC_REF_VDD_1_3` | VDD的1/3参考 |
| `ADC_REF_VDD_1_4` | VDD的1/4参考 |
| `ADC_REF_INTERNAL` | 内部参考（Internal Reference） |
| `ADC_REF_EXTERNAL0` | 外部参考0（External Reference 0） |
| `ADC_REF_EXTERNAL1` | 外部参考1 |

枚举类型 `enum adc_action`：

| 原声明 | 中文含义 |
| --- | --- |
| `ADC_ACTION_CONTINUE = 0` | 继续采样（Continue） |
| `ADC_ACTION_REPEAT` | 重复采样（Repeat） |
| `ADC_ACTION_FINISH` | 结束采样（Finish） |

枚举类型 `enum adc_trigger_type`：

| 原声明 | 中文含义 |
| --- | --- |
| `ADC_TRIG_DATA_READY` | 数据就绪触发（Data Ready） |
| `ADC_TRIG_FIFO_WATERMARK` | 先入先出队列（First In, First Out，FIFO）水位触发（Watermark） |
| `ADC_TRIG_FIFO_FULL` | FIFO满触发 |
| `ADC_TRIG_COMMON_COUNT` | 公共触发类型数量 |
| `ADC_TRIG_PRIV_START = ADC_TRIG_COMMON_COUNT` | 私有触发类型起点 |
| `ADC_TRIG_MAX = INT16_MAX` | 触发类型最大值 |

枚举类型 `enum adc_stream_data_opt`：

| 原声明 | 中文含义 |
| --- | --- |
| `ADC_STREAM_DATA_INCLUDE = 0` | 包含关联触发的全部数据（Include） |
| `ADC_STREAM_DATA_NOP = 1` | 不处理关联数据（No Operation），可稍后消费 |
| `ADC_STREAM_DATA_DROP = 2` | 清除关联触发的全部数据（Drop） |

## 63.5\_回调与驱动函数类型

下列8个类型为函数指针（Function Pointer）类型定义。`uint8_t`、`uint16_t` 表示8位、16位无符号整数，`int32_t`、`int64_t` 表示32位、64位有符号整数。设备指针 `dev`、通道配置 `channel_cfg`、采样序列 `sequence` 和解码器接口 `api` 对应前述结构。

### adc_sequence_callback

```c
typedef enum adc_action (*adc_sequence_callback)(const struct device *dev,
                                                 const struct adc_sequence *sequence,
                                                 uint16_t sampling_index);
```

可选的采样完成回调（Sampling Callback）：每次请求的采样完成后调用，返回采样后动作。

### adc_api_channel_setup

```c
typedef int (*adc_api_channel_setup)(const struct device *dev,
                                     const struct adc_channel_cfg *channel_cfg);
```

配置通道的ADC API函数类型。

### adc_api_read

```c
typedef int (*adc_api_read)(const struct device *dev,
                            const struct adc_sequence *sequence);
```

设置读取请求（Read Request）的ADC API函数类型。

### adc_api_submit

```c
typedef void (*adc_api_submit)(const struct device *dev,
                                  struct rtio_iodev_sqe *sqe);
```

提交流请求（Stream Request）的ADC API函数类型。`rtio_iodev_sqe` 为RTIO设备提交队列项（Submission Queue Entry）。

### adc_api_get_decoder

```c
typedef int (*adc_api_get_decoder)(const struct device *dev,
                                    const struct adc_decoder_api **api);
```

取得给定设备关联解码器的函数类型。

### adc_api_read_async

```c
typedef int (*adc_api_read_async)(const struct device *dev,
                                  const struct adc_sequence *sequence,
                                  struct k_poll_signal *async);
```

设置异步读取请求（Asynchronous Read Request）的ADC API函数类型。`k_poll_signal` 为轮询信号（Poll Signal）。

### adc_api_ref_get

```c
typedef int (*adc_api_ref_get)(const struct device *dev, enum adc_reference ref,
                               uint16_t *vref_mv);
```

取得参考电压的ADC API函数类型，电压单位为毫伏（Millivolt，mV）。

### adc_raw_to_x_fn

```c
typedef int (*adc_raw_to_x_fn)(int32_t ref_mv, enum adc_gain gain, uint8_t resolution,
                               int32_t *valp);
```

将ADC原始单位转换为指定输出单位的函数类型。

## 63.6\_通道配置与读取

这组函数配置通道并发起采样读取，分别提供设备指针入口和设备树规格入口；异步入口通过轮询信号参数返回完成通知。

### adc_channel_setup

```c
int adc_channel_setup(const struct device *dev,
                                const struct adc_channel_cfg *channel_cfg);
```

配置ADC通道。

### adc_channel_setup_dt

```c
static int adc_channel_setup_dt(const struct adc_dt_spec *spec);
```

使用 `struct adc_dt_spec` 中的信息配置ADC通道。

### adc_read

```c
int adc_read(const struct device *dev,
                       const struct adc_sequence *sequence);
```

设置读取请求。

### adc_read_dt

```c
static int adc_read_dt(const struct adc_dt_spec *spec,
                              const struct adc_sequence *sequence);
```

通过 `struct adc_dt_spec` 设置读取请求。

### adc_read_async

```c
int adc_read_async(const struct device *dev,
                             const struct adc_sequence *sequence,
                             struct k_poll_signal *async);
```

设置异步读取请求。

### adc_read_async_dt

```c
static int adc_read_async_dt(const struct adc_dt_spec *spec,
                                    const struct adc_sequence *sequence,
                                    struct k_poll_signal *async);
```

通过 `struct adc_dt_spec` 设置异步读取请求。

## 63.7\_流式处理与参考电压

这组函数取得解码器、启动连续流会话，或查询选定参考源的电压，供后续数据处理使用。

### adc_get_decoder

```c
int adc_get_decoder(const struct device *dev,
                                const struct adc_decoder_api **api);
```

取得该设备的解码器API。

### adc_stream

```c
static int adc_stream(struct rtio_iodev *iodev, struct rtio *ctx, void *userdata,
                                struct rtio_sqe **handle);
```

启动连续ADC流式会话（Continuous Streaming Session）。

### adc_ref_get

```c
static int adc_ref_get(const struct device *dev, enum adc_reference ref,
                              uint16_t *vref_mv);
```

取得所选ADC参考源的电压。

### adc_ref_internal

```c
static uint16_t adc_ref_internal(const struct device *dev);
```

取得内部参考电压。

## 63.8\_增益逆运算与原始值转换

这组函数撤销增益并转换采样单位；直接入口显式传入参考电压、增益和分辨率，设备树入口从规格结构取得相关信息。

### adc_gain_invert

```c
int adc_gain_invert(enum adc_gain gain, int32_t *value);
```

对测量值撤销增益作用。

### adc_gain_invert_64

```c
int adc_gain_invert_64(enum adc_gain gain, int64_t *value);
```

对64位测量值撤销增益作用。

### adc_raw_to_millivolts

```c
static int adc_raw_to_millivolts(int32_t ref_mv, enum adc_gain gain, uint8_t resolution,
                                        int32_t *valp);
```

将原始ADC值转换为毫伏。

### adc_raw_to_microvolts

```c
static int adc_raw_to_microvolts(int32_t ref_mv, enum adc_gain gain, uint8_t resolution,
                                        int32_t *valp);
```

将原始ADC值转换为微伏（Microvolt，µV）。

### adc_raw_to_x_dt_chan

```c
static int adc_raw_to_x_dt_chan(adc_raw_to_x_fn conv_func,
                                       const struct adc_dt_spec *spec,
                                       const struct adc_channel_cfg *channel_cfg,
                                       int32_t *valp);
```

将原始ADC值转换为任意指定的输出单位。

### adc_raw_to_millivolts_dt

```c
static int adc_raw_to_millivolts_dt(const struct adc_dt_spec *spec, int32_t *valp);
```

使用 `struct adc_dt_spec` 保存的信息，把原始值转换为毫伏。

### adc_raw_to_microvolts_dt

```c
static int adc_raw_to_microvolts_dt(const struct adc_dt_spec *spec, int32_t *valp);
```

使用 `struct adc_dt_spec` 保存的信息，把原始值转换为微伏。

## 63.9\_序列初始化与就绪检查

这组辅助函数从设备树规格初始化序列，或检查所关联的ADC设备是否就绪；完整初始化范围见公共接口说明。

### adc_sequence_init_dt

```c
static int adc_sequence_init_dt(const struct adc_dt_spec *spec,
                                       struct adc_sequence *seq);
```

使用 `struct adc_dt_spec` 中的信息初始化 `struct adc_sequence`。

### adc_is_ready_dt

```c
static bool adc_is_ready_dt(const struct adc_dt_spec *spec);
```

验证ADC设备是否就绪（Ready）。

## 63.10\_解码器声明与默认输入输出接口

文件参考页还列出遍历设备树节点的宏调用及默认ADC输入输出设备API声明。源码中的两行分别为：

```c
DT_FOREACH_STATUS_OKAY_NODE(Z_MAYBE_ADC_DECODER_DECLARE_INTERNAL)
extern const struct rtio_iodev_api __adc_iodev_api;
```

译注：前一行遍历状态为okay的设备树节点，按节点兼容标识声明解码器；后一行声明默认ADC输入输出设备API。原文件参考页面把这两项连续显示，这里按源码分行保留。后端操作类型说明另见[ADC驱动后端](../hardware/P456_ADC驱动后端.md)。

---

[上一章：ADC仿真器头文件源码](P062_ADC仿真器头文件源码.md) · [下一章：ADC公共头文件源码](P064_ADC公共头文件源码.md) · [返回大纲](大纲.md)
