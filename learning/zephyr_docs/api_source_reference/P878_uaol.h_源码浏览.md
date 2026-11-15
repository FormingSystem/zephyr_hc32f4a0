---
id: learning.zephyr-docs.api-source-reference.page-878
title: uaol.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/uaol_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第878章\_uaol.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/uaol_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/uaol_8h.html)。

## 878.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="foldopen00019"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="foldopen00028"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="foldopen00034"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="foldopen00051"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00083"></a>
<a id="foldopen00093"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="foldopen00106"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="foldopen00119"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="foldopen00134"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="foldopen00148"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="astdbool_8h_html_abb452686968e48b67397da5f97445f5b"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructuaol__capabilities_html"></a>
<a id="astructuaol__capabilities_html_a62591bcea71bcdd7f38df544fdc5d86b"></a>
<a id="astructuaol__capabilities_html_a8ee3dd123ad8c5b5569d71a9051bb7ba"></a>
<a id="astructuaol__capabilities_html_a905a3ce47be7b6209734fb9db81a323c"></a>
<a id="astructuaol__capabilities_html_ab3206e9baa93edd745b041a2e8ae540b"></a>
<a id="astructuaol__capabilities_html_ad6bf2b46af3b8820a7ecc35e8085e6dd"></a>
<a id="astructuaol__config_html"></a>
<a id="astructuaol__config_html_a1339eb8254650486eaef38d6723555fb"></a>
<a id="astructuaol__config_html_a32f0a6ea54d32ffd51b4bfacb0cbcd4b"></a>
<a id="astructuaol__config_html_a46bb8d4d8abb45c5a0880a7c54a20570"></a>
<a id="astructuaol__config_html_a766781a2e8d45094ec12431ddbc89870"></a>
<a id="astructuaol__config_html_a7be4b2a7f215424a2a7fe19f7242c6ef"></a>
<a id="astructuaol__config_html_a9e0b745c13341828e542710bacb7b0d9"></a>
<a id="astructuaol__config_html_aaacde851401667b86919604e592ac417"></a>
<a id="astructuaol__config_html_ab4e1601f84eb1d2a2e741b99dd157dc4"></a>
<a id="astructuaol__config_html_ab85e93022ffde5f65b30c67d2ff0c082"></a>
<a id="astructuaol__config_html_abf3c127ea505f9d8e877fc5e6adc320a"></a>
<a id="astructuaol__config_html_ae08eb150aef59a2fc373021e2b5c79f6"></a>
<a id="astructuaol__config_html_ae7d46d04d57ad186ddb5875f336037b3"></a>
<a id="astructuaol__config_html_af9d87bfb5f1ba99b1ad59f19fa0edc90"></a>
<a id="astructuaol__ep__table__entry_html"></a>
<a id="astructuaol__ep__table__entry_html_a3bc142e34d341ae58cbe87a9d2eaf614"></a>
<a id="astructuaol__ep__table__entry_html_adcafe865df5890562a1bd91e3fd6117b"></a>
<a id="astructuaol__ep__table__entry_html_af78fdd9cf09d756cfecfe5527b84d7ff"></a>
<a id="auaol_8h_html_a282748f7d70638f48223093fdee7ca3d"></a>
<a id="auaol_8h_html_a6c3e2c3cad9764baa4271237cf493eb3"></a>
<a id="auaol_8h_html_a6e466003dc004e341d726cd528c0db84"></a>
<a id="auaol_8h_html_ab5a0787faab515bbc7b91972590c1ae8"></a>
<a id="auaol_8h_html_ab698e232c95fedfb9a8e53ee1d99111c"></a>
<a id="auaol_8h_html_abf3c266455b0dc363cf2b81fedc07f12"></a>
<a id="auaol_8h_html_afeaa6e0eee46713a5161fd2873ed58be"></a>
<a id="auaol_8h_html_afeaa6e0eee46713a5161fd2873ed58bea218584a3855ec83ec440aa3321743bad"></a>
<a id="auaol_8h_html_afeaa6e0eee46713a5161fd2873ed58bea373ab76b5d7dcfce76b11d8258055c92"></a>

```c
/*
 * Copyright (c) 2024 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_UAOL_H_
#define ZEPHYR_INCLUDE_DRIVERS_UAOL_H_

#include <stdint.h>
#include <zephyr/device.h>

struct uaol_capabilities {
        uint32_t input_streams;
        uint32_t output_streams;
        uint32_t bidirectional_streams;
        uint32_t max_tx_fifo_size;
        uint32_t max_rx_fifo_size;
};

enum uaol_direction {
        UAOL_DIR_PLAYBACK = 0,
        UAOL_DIR_CAPTURE  = 1,
};

struct uaol_config {
        uint8_t xhci_bus;
        uint8_t xhci_device;
        uint8_t xhci_function;
        uint16_t art_divider_m;
        uint16_t art_divider_n;
        uint32_t sample_rate;
        uint32_t channels;
        uint32_t sample_bits;
        uint32_t service_interval;
        uint32_t sio_credit_size;
        uint16_t fifo_start_offset;
        uint16_t channel_map;
        enum uaol_direction direction;
};

struct uaol_ep_table_entry {
        uint32_t usb_ep_address     : 5;
        uint32_t device_slot_number : 8;
        uint32_t split_ep           : 1;
};

typedef int (*uaol_api_config)(const struct device *dev, int stream, struct uaol_config *config);

typedef int (*uaol_api_start)(const struct device *dev, int stream);

typedef int (*uaol_api_stop)(const struct device *dev, int stream);

typedef int (*uaol_api_program_ep_table)(const struct device *dev, int stream,
                                         struct uaol_ep_table_entry entry, bool valid);

typedef int (*uaol_api_get_capabilities)(const struct device *dev, struct uaol_capabilities *caps);

__subsystem struct uaol_driver_api {
        uaol_api_config config;
        uaol_api_start start;
        uaol_api_stop stop;
        uaol_api_program_ep_table program_ep_table;
        uaol_api_get_capabilities get_capabilities;
};

static inline int uaol_config(const struct device *dev, int stream, struct uaol_config *cfg)
{
        return DEVICE_API_GET(uaol, dev)->config(dev, stream, cfg);
}

static inline int uaol_start(const struct device *dev, int stream)
{
        return DEVICE_API_GET(uaol, dev)->start(dev, stream);
}

static inline int uaol_stop(const struct device *dev, int stream)
{
        return DEVICE_API_GET(uaol, dev)->stop(dev, stream);
}

static inline int uaol_program_ep_table(const struct device *dev, int stream,
                                        struct uaol_ep_table_entry entry, bool valid)
{
        return DEVICE_API_GET(uaol, dev)->program_ep_table(dev, stream, entry, valid);
}

static inline int uaol_get_capabilities(const struct device *dev, struct uaol_capabilities *caps)
{
        return DEVICE_API_GET(uaol, dev)->get_capabilities(dev, caps);
}

int uaol_get_mapped_hda_link_stream_id(const struct device *dev, int uaol_stream_id);

#endif /* ZEPHYR_INCLUDE_DRIVERS_UAOL_H_ */
```

## 878.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 165 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_UAOL_H_`。

## 878.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/uaol_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [uaol_capabilities](../audio_video_model_reference/P048_uaol_capabilities_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [input_streams](../audio_video_model_reference/P048_uaol_capabilities_结构体.md#a8ee3dd123ad8c5b5569d71a9051bb7ba)
- [output_streams](../audio_video_model_reference/P048_uaol_capabilities_结构体.md#ad6bf2b46af3b8820a7ecc35e8085e6dd)
- [bidirectional_streams](../audio_video_model_reference/P048_uaol_capabilities_结构体.md#a905a3ce47be7b6209734fb9db81a323c)
- [max_tx_fifo_size](../audio_video_model_reference/P048_uaol_capabilities_结构体.md#ab3206e9baa93edd745b041a2e8ae540b)
- [max_rx_fifo_size](../audio_video_model_reference/P048_uaol_capabilities_结构体.md#a62591bcea71bcdd7f38df544fdc5d86b)
- [uaol_direction](https://docs.zephyrproject.org/latest/doxygen/html/uaol_8h.html#afeaa6e0eee46713a5161fd2873ed58be)
- [UAOL_DIR_PLAYBACK](https://docs.zephyrproject.org/latest/doxygen/html/uaol_8h.html#afeaa6e0eee46713a5161fd2873ed58bea218584a3855ec83ec440aa3321743bad)
- [UAOL_DIR_CAPTURE](https://docs.zephyrproject.org/latest/doxygen/html/uaol_8h.html#afeaa6e0eee46713a5161fd2873ed58bea373ab76b5d7dcfce76b11d8258055c92)
- [uaol_config](../audio_video_model_reference/P049_uaol_config_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [xhci_bus](../audio_video_model_reference/P049_uaol_config_结构体.md#ab4e1601f84eb1d2a2e741b99dd157dc4)
- [xhci_device](../audio_video_model_reference/P049_uaol_config_结构体.md#abf3c127ea505f9d8e877fc5e6adc320a)
- [xhci_function](../audio_video_model_reference/P049_uaol_config_结构体.md#aaacde851401667b86919604e592ac417)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [art_divider_m](../audio_video_model_reference/P049_uaol_config_结构体.md#a1339eb8254650486eaef38d6723555fb)
- [art_divider_n](../audio_video_model_reference/P049_uaol_config_结构体.md#ab85e93022ffde5f65b30c67d2ff0c082)
- [sample_rate](../audio_video_model_reference/P049_uaol_config_结构体.md#a46bb8d4d8abb45c5a0880a7c54a20570)
- [channels](../audio_video_model_reference/P049_uaol_config_结构体.md#a9e0b745c13341828e542710bacb7b0d9)
- [sample_bits](../audio_video_model_reference/P049_uaol_config_结构体.md#ae08eb150aef59a2fc373021e2b5c79f6)
- [service_interval](../audio_video_model_reference/P049_uaol_config_结构体.md#af9d87bfb5f1ba99b1ad59f19fa0edc90)
- [sio_credit_size](../audio_video_model_reference/P049_uaol_config_结构体.md#a7be4b2a7f215424a2a7fe19f7242c6ef)
- [fifo_start_offset](../audio_video_model_reference/P049_uaol_config_结构体.md#a766781a2e8d45094ec12431ddbc89870)
- [channel_map](../audio_video_model_reference/P049_uaol_config_结构体.md#ae7d46d04d57ad186ddb5875f336037b3)
- [direction](../audio_video_model_reference/P049_uaol_config_结构体.md#a32f0a6ea54d32ffd51b4bfacb0cbcd4b)
- [uaol_ep_table_entry](../audio_video_model_reference/P050_uaol_ep_table_entry_结构体.md)
- [usb_ep_address](../audio_video_model_reference/P050_uaol_ep_table_entry_结构体.md#adcafe865df5890562a1bd91e3fd6117b)
- [device_slot_number](../audio_video_model_reference/P050_uaol_ep_table_entry_结构体.md#af78fdd9cf09d756cfecfe5527b84d7ff)
- [split_ep](../audio_video_model_reference/P050_uaol_ep_table_entry_结构体.md#a3bc142e34d341ae58cbe87a9d2eaf614)
- [device](../device_reference/P002_设备对象结构.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [uaol_config](https://docs.zephyrproject.org/latest/doxygen/html/uaol_8h.html#ab5a0787faab515bbc7b91972590c1ae8)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [uaol_start](https://docs.zephyrproject.org/latest/doxygen/html/uaol_8h.html#abf3c266455b0dc363cf2b81fedc07f12)
- [uaol_stop](https://docs.zephyrproject.org/latest/doxygen/html/uaol_8h.html#ab698e232c95fedfb9a8e53ee1d99111c)
- [uaol_program_ep_table](https://docs.zephyrproject.org/latest/doxygen/html/uaol_8h.html#a282748f7d70638f48223093fdee7ca3d)
- [uaol_get_capabilities](https://docs.zephyrproject.org/latest/doxygen/html/uaol_8h.html#a6e466003dc004e341d726cd528c0db84)
- [uaol_get_mapped_hda_link_stream_id](https://docs.zephyrproject.org/latest/doxygen/html/uaol_8h.html#a6c3e2c3cad9764baa4271237cf493eb3)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [uaol_capabilities::max_rx_fifo_size](../audio_video_model_reference/P048_uaol_capabilities_结构体.md#a62591bcea71bcdd7f38df544fdc5d86b)
- [uaol_capabilities::input_streams](../audio_video_model_reference/P048_uaol_capabilities_结构体.md#a8ee3dd123ad8c5b5569d71a9051bb7ba)
- [uaol_capabilities::bidirectional_streams](../audio_video_model_reference/P048_uaol_capabilities_结构体.md#a905a3ce47be7b6209734fb9db81a323c)
- [uaol_capabilities::max_tx_fifo_size](../audio_video_model_reference/P048_uaol_capabilities_结构体.md#ab3206e9baa93edd745b041a2e8ae540b)
- [uaol_capabilities::output_streams](../audio_video_model_reference/P048_uaol_capabilities_结构体.md#ad6bf2b46af3b8820a7ecc35e8085e6dd)
- [uaol_config::art_divider_m](../audio_video_model_reference/P049_uaol_config_结构体.md#a1339eb8254650486eaef38d6723555fb)
- [uaol_config::direction](../audio_video_model_reference/P049_uaol_config_结构体.md#a32f0a6ea54d32ffd51b4bfacb0cbcd4b)
- [uaol_config::sample_rate](../audio_video_model_reference/P049_uaol_config_结构体.md#a46bb8d4d8abb45c5a0880a7c54a20570)
- [uaol_config::fifo_start_offset](../audio_video_model_reference/P049_uaol_config_结构体.md#a766781a2e8d45094ec12431ddbc89870)
- [uaol_config::sio_credit_size](../audio_video_model_reference/P049_uaol_config_结构体.md#a7be4b2a7f215424a2a7fe19f7242c6ef)
- [uaol_config::channels](../audio_video_model_reference/P049_uaol_config_结构体.md#a9e0b745c13341828e542710bacb7b0d9)
- [uaol_config::xhci_function](../audio_video_model_reference/P049_uaol_config_结构体.md#aaacde851401667b86919604e592ac417)
- [uaol_config::xhci_bus](../audio_video_model_reference/P049_uaol_config_结构体.md#ab4e1601f84eb1d2a2e741b99dd157dc4)
- [uaol_config::art_divider_n](../audio_video_model_reference/P049_uaol_config_结构体.md#ab85e93022ffde5f65b30c67d2ff0c082)
- [uaol_config::xhci_device](../audio_video_model_reference/P049_uaol_config_结构体.md#abf3c127ea505f9d8e877fc5e6adc320a)
- [uaol_config::sample_bits](../audio_video_model_reference/P049_uaol_config_结构体.md#ae08eb150aef59a2fc373021e2b5c79f6)
- [uaol_config::channel_map](../audio_video_model_reference/P049_uaol_config_结构体.md#ae7d46d04d57ad186ddb5875f336037b3)
- [uaol_config::service_interval](../audio_video_model_reference/P049_uaol_config_结构体.md#af9d87bfb5f1ba99b1ad59f19fa0edc90)
- [uaol_ep_table_entry::split_ep](../audio_video_model_reference/P050_uaol_ep_table_entry_结构体.md#a3bc142e34d341ae58cbe87a9d2eaf614)
- [uaol_ep_table_entry::usb_ep_address](../audio_video_model_reference/P050_uaol_ep_table_entry_结构体.md#adcafe865df5890562a1bd91e3fd6117b)
- [uaol_ep_table_entry::device_slot_number](../audio_video_model_reference/P050_uaol_ep_table_entry_结构体.md#af78fdd9cf09d756cfecfe5527b84d7ff)

---

[上一章](P877_trickle.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P879_uart_bridge.h_源码浏览.md)
