---
id: learning.zephyr-docs.adc_reference.adcmainheader-64
title: ADC公共头文件源码
kind: reference
status: maintained
domains: [zephyr, adc_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2adc_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第64章\_ADC公共头文件源码

原文：[drivers_2adc_8h_source](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2adc_8h_source.html)。读取日期：2026-10-13，`latest`。

本页保留官方源码浏览器显示的 `zephyr/drivers/adc.h`。模数转换器（Analog-to-Digital Converter，ADC）的文件参考见[上一章](P063_ADC公共头文件参考.md)，完整接口契约见[ADC公共接口](../hardware/P463_ADC公共接口参考.md)。

## 64.1\_原始可见源码

以下只去除网页展示行号和行末空白；版权、许可证、条件编译、全部声明、内联函数实现、宏展开及可见注释完整保留。Doxygen会隐藏部分文档注释，所以本段对应网页可见内容，不声称是原仓库文件的逐字节副本。

```c
/*
 * Copyright (c) 2018 Nordic Semiconductor ASA
 * Copyright (c) 2015 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_ADC_H_
#define ZEPHYR_INCLUDE_DRIVERS_ADC_H_

#include <zephyr/device.h>
#include <zephyr/dt-bindings/adc/adc.h>
#include <zephyr/kernel.h>
#include <zephyr/rtio/rtio.h>
#include <zephyr/dsp/types.h>

#ifdef __cplusplus
extern "C" {
#endif


enum adc_gain {
        ADC_GAIN_1_6,
        ADC_GAIN_1_5,
        ADC_GAIN_1_4,
        ADC_GAIN_2_7,
        ADC_GAIN_1_3,
        ADC_GAIN_2_5,
        ADC_GAIN_1_2,
        ADC_GAIN_2_3,
        ADC_GAIN_4_5,
        ADC_GAIN_1,
        ADC_GAIN_2,
        ADC_GAIN_3,
        ADC_GAIN_4,
        ADC_GAIN_6,
        ADC_GAIN_8,
        ADC_GAIN_12,
        ADC_GAIN_16,
        ADC_GAIN_24,
        ADC_GAIN_32,
        ADC_GAIN_64,
        ADC_GAIN_128,
};

int adc_gain_invert(enum adc_gain gain, int32_t *value);

int adc_gain_invert_64(enum adc_gain gain, int64_t *value);

enum adc_reference {
        ADC_REF_VDD_1,
        ADC_REF_VDD_1_2,
        ADC_REF_VDD_1_3,
        ADC_REF_VDD_1_4,
        ADC_REF_INTERNAL,
        ADC_REF_EXTERNAL0,
        ADC_REF_EXTERNAL1,
};

struct adc_channel_cfg {
        enum adc_gain gain;

        enum adc_reference reference;

        uint16_t acquisition_time;

        uint8_t channel_id   : 5;

        uint8_t differential : 1;

#ifdef CONFIG_ADC_CONFIGURABLE_INPUTS
        uint8_t input_positive;

        uint8_t input_negative;
#endif /* CONFIG_ADC_CONFIGURABLE_INPUTS */

#ifdef CONFIG_ADC_CONFIGURABLE_EXCITATION_CURRENT_SOURCE_PIN
        uint8_t current_source_pin_set : 1;
        uint8_t current_source_pin[2];
#endif /* CONFIG_ADC_CONFIGURABLE_EXCITATION_CURRENT_SOURCE_PIN */

#ifdef CONFIG_ADC_CONFIGURABLE_VBIAS_PIN
        uint32_t vbias_pins;
#endif /* CONFIG_ADC_CONFIGURABLE_VBIAS_PIN */
};

#define ADC_CHANNEL_CFG_DT(node_id) { \
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

struct adc_dt_spec {
        const struct device *dev;

        uint8_t channel_id;

        bool channel_cfg_dt_node_exists;

        struct adc_channel_cfg channel_cfg;

        uint16_t vref_mv;

        uint8_t resolution;

        uint8_t oversampling;
};


#define ADC_DT_SPEC_STRUCT(ctlr, input) { \
                .dev = DEVICE_DT_GET(ctlr), \
                .channel_id = input, \
                ADC_CHANNEL_CFG_FROM_DT_NODE(\
                        ADC_CHANNEL_DT_NODE(ctlr, input)) \
        }

#define ADC_CHANNEL_DT_NODE(ctlr, input) \
        DT_CHILD_BY_UNIT_ADDR_INT(ctlr, input)

#define ADC_CHANNEL_CFG_FROM_DT_NODE(node_id) \
        IF_ENABLED(DT_NODE_EXISTS(node_id), \
                (.channel_cfg_dt_node_exists = true, \
                 .channel_cfg  = ADC_CHANNEL_CFG_DT(node_id), \
                 .vref_mv      = DT_PROP_OR(node_id, zephyr_vref_mv, 0), \
                 .resolution   = DT_PROP_OR(node_id, zephyr_resolution, 0), \
                 .oversampling = DT_PROP_OR(node_id, zephyr_oversampling, 0),))


#define ADC_DT_SPEC_GET_BY_NAME(node_id, name) \
        ADC_DT_SPEC_STRUCT(DT_IO_CHANNELS_CTLR_BY_NAME(node_id, name), \
                           DT_IO_CHANNELS_INPUT_BY_NAME(node_id, name))

#define ADC_DT_SPEC_GET_BY_NAME_OR(node_id, name, default_value) \
        COND_CODE_1(DT_PROP_HAS_NAME(node_id, io_channels, name), \
                    (ADC_DT_SPEC_GET_BY_NAME(node_id, name)), (default_value))

#define ADC_DT_SPEC_INST_GET_BY_NAME(inst, name) \
        ADC_DT_SPEC_GET_BY_NAME(DT_DRV_INST(inst), name)

#define ADC_DT_SPEC_INST_GET_BY_NAME_OR(inst, name, default_value) \
        ADC_DT_SPEC_GET_BY_NAME_OR(DT_DRV_INST(inst), name, default_value)

#define ADC_DT_SPEC_GET_BY_IDX(node_id, idx) \
        ADC_DT_SPEC_STRUCT(DT_IO_CHANNELS_CTLR_BY_IDX(node_id, idx), \
                           DT_IO_CHANNELS_INPUT_BY_IDX(node_id, idx))

#define ADC_DT_SPEC_GET_BY_IDX_OR(node_id, idx, default_value) \
        COND_CODE_1(DT_PROP_HAS_IDX(node_id, io_channels, idx), \
                    (ADC_DT_SPEC_GET_BY_IDX(node_id, idx)), (default_value))

#define ADC_DT_SPEC_INST_GET_BY_IDX(inst, idx) \
        ADC_DT_SPEC_GET_BY_IDX(DT_DRV_INST(inst), idx)

#define ADC_DT_SPEC_INST_GET_BY_IDX_OR(inst, idx, default_value) \
        ADC_DT_SPEC_GET_BY_IDX_OR(DT_DRV_INST(inst), idx, default_value)

#define ADC_DT_SPEC_GET(node_id) ADC_DT_SPEC_GET_BY_IDX(node_id, 0)

#define ADC_DT_SPEC_GET_OR(node_id, default_value) \
        ADC_DT_SPEC_GET_BY_IDX_OR(node_id, 0, default_value)

#define ADC_DT_SPEC_INST_GET(inst) ADC_DT_SPEC_GET(DT_DRV_INST(inst))

#define ADC_DT_SPEC_INST_GET_OR(inst, default_value) \
        ADC_DT_SPEC_GET_OR(DT_DRV_INST(inst), default_value)

/* Forward declaration of the adc_sequence structure. */
struct adc_sequence;

enum adc_action {
        ADC_ACTION_CONTINUE = 0,

        ADC_ACTION_REPEAT,

        ADC_ACTION_FINISH,
};

typedef enum adc_action (*adc_sequence_callback)(const struct device *dev,
                                                 const struct adc_sequence *sequence,
                                                 uint16_t sampling_index);

struct adc_sequence_options {
        uint32_t interval_us;

        adc_sequence_callback callback;

        void *user_data;

        uint16_t extra_samplings;
};

struct adc_sequence {
        const struct adc_sequence_options *options;

        uint32_t channels;

        void *buffer;

        size_t buffer_size;

#if defined(CONFIG_ADC_SEQUENCE_PRIORITY) || defined(__DOXYGEN__)
        uint32_t priority;
#endif

        uint8_t resolution;

        uint8_t oversampling;

        bool calibrate;
};

struct adc_data_header {
        uint64_t base_timestamp_ns;
        uint16_t reading_count;
};

struct adc_data {
        struct adc_data_header header;
        int8_t shift;
        struct adc_sample_data {
                uint32_t timestamp_delta;
                union {
                        q31_t value;
                };
        } readings[1];
};

enum adc_trigger_type {
        ADC_TRIG_DATA_READY,

        ADC_TRIG_FIFO_WATERMARK,

        ADC_TRIG_FIFO_FULL,

        ADC_TRIG_COMMON_COUNT,

        ADC_TRIG_PRIV_START = ADC_TRIG_COMMON_COUNT,

        ADC_TRIG_MAX = INT16_MAX,
};

enum adc_stream_data_opt {
        ADC_STREAM_DATA_INCLUDE = 0,
        ADC_STREAM_DATA_NOP = 1,
        ADC_STREAM_DATA_DROP = 2,
};

struct adc_stream_trigger {
        enum adc_trigger_type trigger;
        enum adc_stream_data_opt opt;
};

struct adc_chan_spec {
        uint8_t chan_idx;
        uint8_t chan_resolution;
};

/*
 * Internal data structure used to store information about the IODevice for async reading and
 * streaming adc data.
 */
struct adc_read_config {
        const struct device *adc;
        const bool is_streaming;
        const struct adc_dt_spec *adc_spec;
        const struct adc_stream_trigger *triggers;
        struct adc_sequence *sequence;
        uint16_t fifo_watermark_lvl;
        uint16_t fifo_mode;
        size_t adc_spec_cnt;
        size_t trigger_cnt;
};

struct adc_decoder_api {
        int (*get_frame_count)(const uint8_t *buffer, uint32_t channel,
                               uint16_t *frame_count);

        int (*get_size_info)(struct adc_dt_spec adc_spec, uint32_t channel, size_t *base_size,
                             size_t *frame_size);

        int (*decode)(const uint8_t *buffer, uint32_t channel, uint32_t *fit,
                      uint16_t max_count, void *data_out);

        bool (*has_trigger)(const uint8_t *buffer, enum adc_trigger_type trigger);
};


typedef int (*adc_api_channel_setup)(const struct device *dev,
                                     const struct adc_channel_cfg *channel_cfg);

typedef int (*adc_api_read)(const struct device *dev,
                            const struct adc_sequence *sequence);

typedef void (*adc_api_submit)(const struct device *dev,
                                  struct rtio_iodev_sqe *sqe);

typedef int (*adc_api_get_decoder)(const struct device *dev,
                                    const struct adc_decoder_api **api);


typedef int (*adc_api_read_async)(const struct device *dev,
                                  const struct adc_sequence *sequence,
                                  struct k_poll_signal *async);

typedef int (*adc_api_ref_get)(const struct device *dev, enum adc_reference ref,
                               uint16_t *vref_mv);

__subsystem struct adc_driver_api {
        adc_api_channel_setup channel_setup;
        adc_api_read          read;
#if defined(CONFIG_ADC_ASYNC) || defined(__DOXYGEN__)
        adc_api_read_async    read_async;
#endif
#if defined(CONFIG_ADC_STREAM) || defined(__DOXYGEN__)
        adc_api_submit    submit;
        adc_api_get_decoder get_decoder;
#endif
        uint16_t ref_internal;
        adc_api_ref_get ref_get;
};


__syscall int adc_channel_setup(const struct device *dev,
                                const struct adc_channel_cfg *channel_cfg);

static inline int z_impl_adc_channel_setup(const struct device *dev,
                                           const struct adc_channel_cfg *channel_cfg)
{
        return DEVICE_API_GET(adc, dev)->channel_setup(dev, channel_cfg);
}

static inline int adc_channel_setup_dt(const struct adc_dt_spec *spec)
{
        if (!spec->channel_cfg_dt_node_exists) {
                return -ENOTSUP;
        }

        return adc_channel_setup(spec->dev, &spec->channel_cfg);
}

__syscall int adc_read(const struct device *dev,
                       const struct adc_sequence *sequence);

static inline int z_impl_adc_read(const struct device *dev,
                                  const struct adc_sequence *sequence)
{
        return DEVICE_API_GET(adc, dev)->read(dev, sequence);
}

static inline int adc_read_dt(const struct adc_dt_spec *spec,
                              const struct adc_sequence *sequence)
{
        return adc_read(spec->dev, sequence);
}

__syscall int adc_read_async(const struct device *dev,
                             const struct adc_sequence *sequence,
                             struct k_poll_signal *async);

#ifdef CONFIG_ADC_ASYNC
static inline int z_impl_adc_read_async(const struct device *dev,
                                        const struct adc_sequence *sequence,
                                        struct k_poll_signal *async)
{
        return DEVICE_API_GET(adc, dev)->read_async(dev, sequence, async);
}
#endif /* CONFIG_ADC_ASYNC */

static inline int adc_read_async_dt(const struct adc_dt_spec *spec,
                                    const struct adc_sequence *sequence,
                                    struct k_poll_signal *async)
{
        return adc_read_async(spec->dev, sequence, async);
}

__syscall int adc_get_decoder(const struct device *dev,
                                const struct adc_decoder_api **api);

struct __attribute__((__packed__)) adc_data_generic_header {
        uint64_t timestamp_ns;

        uint8_t num_channels;

        int8_t shift;

        /* This padding is needed to make sure that the 'channels' field is aligned */
        int16_t _padding;

        struct adc_chan_spec channels[0];
};

static inline int adc_stream(struct rtio_iodev *iodev, struct rtio *ctx, void *userdata,
                                struct rtio_sqe **handle)
{
        if (IS_ENABLED(CONFIG_USERSPACE)) {
                struct rtio_sqe sqe;

                rtio_sqe_prep_read_multishot(&sqe, iodev, RTIO_PRIO_NORM, userdata);
                rtio_sqe_copy_in_get_handles(ctx, &sqe, handle, 1);
        } else {
                struct rtio_sqe *sqe = rtio_sqe_acquire(ctx);

                if (sqe == NULL) {
                        return -ENOMEM;
                }
                if (handle != NULL) {
                        *handle = sqe;
                }
                rtio_sqe_prep_read_multishot(sqe, iodev, RTIO_PRIO_NORM, userdata);
        }
        rtio_submit(ctx, 0);
        return 0;
}

#ifdef CONFIG_ADC_STREAM
static inline int z_impl_adc_get_decoder(const struct device *dev,
                                            const struct adc_decoder_api **decoder)
{
        const struct adc_driver_api *api = DEVICE_API_GET(adc, dev);

        __ASSERT_NO_MSG(api != NULL);

        if (api->get_decoder == NULL) {
                *decoder = NULL;
                return -1;
        }

        return api->get_decoder(dev, decoder);
}
#endif /* CONFIG_ADC_STREAM */

static inline int adc_ref_get(const struct device *dev, enum adc_reference ref,
                              uint16_t *vref_mv)
{
        const struct adc_driver_api *api;

        if (vref_mv == NULL) {
                return -EINVAL;
        }

        api = DEVICE_API_GET(adc, dev);

        if (api->ref_get != NULL) {
                return api->ref_get(dev, ref, vref_mv);
        }

        if (ref != ADC_REF_INTERNAL) {
                return -ENOTSUP;
        }

        *vref_mv = api->ref_internal;
        return (*vref_mv == 0U) ? -ENODATA : 0;
}

static inline uint16_t adc_ref_internal(const struct device *dev)
{
        uint16_t vref_mv;
        int ret;

        ret = adc_ref_get(dev, ADC_REF_INTERNAL, &vref_mv);

        return ret == 0 ? vref_mv : 0U;
}

typedef int (*adc_raw_to_x_fn)(int32_t ref_mv, enum adc_gain gain, uint8_t resolution,
                               int32_t *valp);

static inline int adc_raw_to_millivolts(int32_t ref_mv, enum adc_gain gain, uint8_t resolution,
                                        int32_t *valp)
{
        int64_t adc_mv = (int64_t)*valp * (int64_t)ref_mv;
        int ret = adc_gain_invert_64(gain, &adc_mv);

        if (ret == 0) {
                adc_mv = adc_mv >> resolution;
                if (adc_mv > INT32_MAX || adc_mv < INT32_MIN) {
                        __ASSERT(false, "conversion result is out of range");
                }

                *valp = (int32_t)adc_mv;
        }

        return ret;
}

static inline int adc_raw_to_microvolts(int32_t ref_mv, enum adc_gain gain, uint8_t resolution,
                                        int32_t *valp)
{
        int64_t adc_uv = (int64_t)*valp * ref_mv * 1000;
        int ret = adc_gain_invert_64(gain, &adc_uv);

        if (ret == 0) {
                *valp = (int32_t)(adc_uv >> resolution);
        }

        return ret;
}

static inline int adc_raw_to_x_dt_chan(adc_raw_to_x_fn conv_func,
                                       const struct adc_dt_spec *spec,
                                       const struct adc_channel_cfg *channel_cfg,
                                       int32_t *valp)
{
        int32_t vref_mv;
        uint16_t vref_mv_u16;
        uint8_t resolution;

        if (!spec->channel_cfg_dt_node_exists) {
                return -ENOTSUP;
        }

        if (adc_ref_get(spec->dev, channel_cfg->reference, &vref_mv_u16) == 0) {
                vref_mv = (int32_t)vref_mv_u16;
        } else {
                vref_mv = spec->vref_mv;
        }

        resolution = spec->resolution;

        /*
         * For differential channels, one bit less needs to be specified
         * for resolution to achieve correct conversion.
         */
        if (channel_cfg->differential) {
                resolution -= 1U;
        }

        return conv_func(vref_mv, channel_cfg->gain, resolution, valp);
}


static inline int adc_raw_to_millivolts_dt(const struct adc_dt_spec *spec, int32_t *valp)
{
        return adc_raw_to_x_dt_chan(adc_raw_to_millivolts, spec, &spec->channel_cfg, valp);
}

static inline int adc_raw_to_microvolts_dt(const struct adc_dt_spec *spec, int32_t *valp)
{
        return adc_raw_to_x_dt_chan(adc_raw_to_microvolts, spec, &spec->channel_cfg, valp);
}

static inline int adc_sequence_init_dt(const struct adc_dt_spec *spec,
                                       struct adc_sequence *seq)
{
        if (!spec->channel_cfg_dt_node_exists) {
                return -ENOTSUP;
        }

        seq->channels = BIT(spec->channel_id);
        seq->resolution = spec->resolution;
        seq->oversampling = spec->oversampling;

        return 0;
}

static inline bool adc_is_ready_dt(const struct adc_dt_spec *spec)
{
        return device_is_ready(spec->dev);
}

#define ADC_DECODER_NAME() UTIL_CAT(DT_DRV_COMPAT, __adc_decoder_api)

#define ADC_DECODER_DT_GET(node_id)                                                             \
        &UTIL_CAT(DT_STRING_TOKEN_BY_IDX(node_id, compatible, 0), __adc_decoder_api)

#define ADC_DECODER_API_DT_DEFINE()                                                             \
        COND_CODE_1(DT_HAS_COMPAT_STATUS_OKAY(DT_DRV_COMPAT), (), (static))                     \
        const STRUCT_SECTION_ITERABLE(adc_decoder_api, ADC_DECODER_NAME())

#define Z_MAYBE_ADC_DECODER_DECLARE_INTERNAL_IDX(node_id, prop, idx)                            \
        extern const struct adc_decoder_api UTIL_CAT(                                           \
                DT_STRING_TOKEN_BY_IDX(node_id, prop, idx), __adc_decoder_api);

#define Z_MAYBE_ADC_DECODER_DECLARE_INTERNAL(node_id)                                           \
        COND_CODE_1(DT_NODE_HAS_PROP(node_id, compatible),                                      \
                        (DT_FOREACH_PROP_ELEM(node_id, compatible,                              \
                                          Z_MAYBE_ADC_DECODER_DECLARE_INTERNAL_IDX)),           \
                                                ())

DT_FOREACH_STATUS_OKAY_NODE(Z_MAYBE_ADC_DECODER_DECLARE_INTERNAL)

/* The default adc iodev API */
extern const struct rtio_iodev_api __adc_iodev_api;

#define ADC_DT_STREAM_IODEV(name, dt_node, adc_dt_spec, ...)                                    \
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


#ifdef __cplusplus
}
#endif

#include <zephyr/syscalls/adc.h>

#endif  /* ZEPHYR_INCLUDE_DRIVERS_ADC_H_ */
```

## 64.2\_可见注释译文

可见的英文说明注释按原出现顺序翻译如下：

1. 对 `adc_sequence` 结构进行前置声明（Forward Declaration）。
2. 内部结构 `adc_read_config` 保存异步读取（Asynchronous Reading）和流式ADC数据（Streaming ADC Data）所用输入输出设备（I/O Device）的信息。
3. `_padding` 填充字段用于确保 `channels` 字段对齐（Alignment）。
4. 对差分通道（Differential Channel），换算时需要把分辨率（Resolution）减少一位，才能得到正确的转换结果。
5. `__adc_iodev_api` 为默认ADC输入输出设备API。

原版权与 `SPDX-License-Identifier: Apache-2.0` 作为法律标识保持原样。条件编译指令旁的配置宏名注释同样保留。

## 64.3\_源码阅读定位

译注：`CONFIG_ADC_CONFIGURABLE_INPUTS`、`CONFIG_ADC_CONFIGURABLE_EXCITATION_CURRENT_SOURCE_PIN`、`CONFIG_ADC_CONFIGURABLE_VBIAS_PIN` 决定部分通道字段是否存在；`CONFIG_ADC_ASYNC` 和 `CONFIG_ADC_STREAM` 分别控制异步读取和流接口的相关实现。阅读结构布局时应保留这些条件，而不能把网页显示的全部字段视为任何构建都具有的固定布局。

设备树辅助函数在缺少通道配置节点时可能返回 `-ENOTSUP`（不支持，Not Supported）。参考电压获取先尝试驱动 `ref_get`；未提供该回调时只回退到内部参考值，且零参考值返回 `-ENODATA`（无数据，No Data）。差分通道的减一位处理位于 `adc_raw_to_x_dt_chan()`，它会先尝试读取参考电压，失败后使用设备树规格中的参考毫伏值。

这些定位说明用于帮助对照原始实现，不能替代完整参数、错误码和调用条件的接口译文；相关入口均在前一章。

---

[上一章：ADC公共头文件参考](P063_ADC公共头文件参考.md) · [下一章：ADC驱动头文件目录](P065_ADC驱动头文件目录.md) · [返回大纲](大纲.md)
