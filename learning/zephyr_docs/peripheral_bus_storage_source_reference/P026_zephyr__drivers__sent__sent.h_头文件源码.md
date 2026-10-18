---
id: learning.zephyr-docs.peripheral-bus-storage-source-reference.page-26
title: zephyr__drivers__sent__sent.h_头文件源码
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sent_2sent_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第26章\_zephyr__drivers__sent__sent.h_头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sent_2sent_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应头文件参考](../peripheral_bus_storage_header_reference/P026_zephyr__drivers__sent__sent.h_头文件参考.md)。

## 26.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00031"></a>
<a id="foldopen00035"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="foldopen00054"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00102"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="foldopen00118"></a>
<a id="l00118"></a>
<a id="l00120"></a>
<a id="l00122"></a>
<a id="l00124"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="foldopen00132"></a>
<a id="l00132"></a>
<a id="l00134"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="foldopen00149"></a>
<a id="l00149"></a>
<a id="l00151"></a>
<a id="l00153"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00161"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="agroup__sent__interface__backend_html_ga3b72c0fafbb177264d20df089ff5c38c"></a>
<a id="agroup__sent__interface__backend_html_ga4d4cc8870210e37bdac56d15f5979a32"></a>
<a id="agroup__sent__interface__backend_html_gad13f1bbd1eb6b6300780596b94bff6ac"></a>
<a id="agroup__sent__interface_html_ga069232b79943be845df411539ef04993"></a>
<a id="agroup__sent__interface_html_ga19bb6e9149dfb7af97ca90289e33bdac"></a>
<a id="agroup__sent__interface_html_ga227aafdbe8f93dbdb97f3969517e6c63"></a>
<a id="agroup__sent__interface_html_ga47d05656177dae0a388e1155be82494f"></a>
<a id="agroup__sent__interface_html_ga9deb810297f7d42159187bbb8dddb8d2"></a>
<a id="agroup__sent__interface_html_gae1eacde97297c97e27b67a7ae7e121cb"></a>
<a id="agroup__sent__interface_html_gga069232b79943be845df411539ef04993a44b400409bb8a00ba23022490a6e6e73"></a>
<a id="agroup__sent__interface_html_gga069232b79943be845df411539ef04993adbbb93e3efeeb6d2330bc4c9cb0ae4d5"></a>
<a id="agroup__sent__interface_html_gga069232b79943be845df411539ef04993aeef9ade678a8b59d7a8e0d0154f9b137"></a>
<a id="agroup__sent__interface_html_gga069232b79943be845df411539ef04993afb15bcda86b0faef89c8dc1662f060a1"></a>
<a id="agroup__system__errno_html_ga43785b9969e0bd1af532dbde06c5540b"></a>
<a id="akernel_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructsent__driver__api_html"></a>
<a id="astructsent__driver__api_html_a0be794c9fb93ff9e04fa22cf2aeea4b9"></a>
<a id="astructsent__driver__api_html_a355a318c08625c99bb1b2adf193bf577"></a>
<a id="astructsent__driver__api_html_a832b061c8e6ae38199d54f9702fb39a7"></a>
<a id="astructsent__frame_html"></a>
<a id="astructsent__frame_html_a1c02dabd2b0605b77683daf17fc7980b"></a>
<a id="astructsent__frame_html_a43d52380608b7683534dc31873a396af"></a>
<a id="astructsent__frame_html_a4bef9a0871e8ecd86b6753e5bb46c6a0"></a>
<a id="astructsent__frame_html_a648203dab36ae27e874a171c71d92fe8"></a>
<a id="astructsent__frame_html_a689cb24f6c8049e6282ca30939430c8f"></a>
<a id="astructsent__frame_html_aae185d5b024a3d9afc135ecc19c9410f"></a>
<a id="astructsent__frame_html_aafd880b826c351481b384b5fef106068"></a>
<a id="astructsent__frame_html_ab39f8ecf19e198ca4818fb13d522c6f4"></a>
<a id="astructsent__rx__callback__config_html"></a>
<a id="astructsent__rx__callback__config_html_a251257c08668ced3773bec6895fbd467"></a>
<a id="astructsent__rx__callback__config_html_a45b6353ae6f2177d2267cc343c798726"></a>
<a id="astructsent__rx__callback__config_html_a67e2cd95a91793a1cfbb73f86862ff04"></a>
<a id="astructsent__rx__callback__config_html_afcf63b8116f8dca5839c5b44b5fd1b39"></a>
<a id="astructsent__rx__callback__configs_html"></a>
<a id="astructsent__rx__callback__configs_html_a0f4d0261c97b21430de9782e20d1c244"></a>
<a id="astructsent__rx__callback__configs_html_a631882e363de3c8cc693336028561c1b"></a>

```c
/*
 * Copyright 2025 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_SENT_H_
#define ZEPHYR_INCLUDE_DRIVERS_SENT_H_

#include <zephyr/kernel.h>
#include <zephyr/device.h>

#ifdef __cplusplus
extern "C" {
#endif


enum sent_frame_type {
        SENT_SHORT_SERIAL_FRAME,
        SENT_ENHANCED_SERIAL_FRAME_4_BIT_ID,
        SENT_ENHANCED_SERIAL_FRAME_8_BIT_ID,
        SENT_FAST_FRAME
};

#define SENT_MAX_DATA_NIBBLES 8

struct sent_frame {
        enum sent_frame_type type;

        union {
                struct {
                        uint8_t id;

                        uint16_t data;
                } serial;

                struct {
                        uint8_t data_nibbles[SENT_MAX_DATA_NIBBLES];
                } fast;
        };

        uint32_t timestamp;

        uint8_t crc;
};

typedef void (*sent_rx_frame_callback_t)(const struct device *dev, uint8_t channel,
                                         uint32_t num_frame, void *user_data);


typedef int (*sent_start_listening_t)(const struct device *dev, uint8_t channel);

typedef int (*sent_stop_listening_t)(const struct device *dev, uint8_t channel);

struct sent_rx_callback_config {
        sent_rx_frame_callback_t callback;
        struct sent_frame *frame;
        uint32_t max_num_frame;
        void *user_data;
};

struct sent_rx_callback_configs {
        struct sent_rx_callback_config *serial;
        struct sent_rx_callback_config *fast;
};

typedef int (*sent_register_callback_t)(const struct device *dev, uint8_t channel,
                                        struct sent_rx_callback_configs callback_configs);

__subsystem struct sent_driver_api {
        sent_start_listening_t start_listening;
        sent_stop_listening_t stop_listening;
        sent_register_callback_t register_callback;
};


__syscall int sent_start_listening(const struct device *dev, uint8_t channel);

static inline int z_impl_sent_start_listening(const struct device *dev, uint8_t channel)
{
        const struct sent_driver_api *api = DEVICE_API_GET(sent, dev);

        if (api->start_listening) {
                return api->start_listening(dev, channel);
        }

        return -ENOSYS;
}

__syscall int sent_stop_listening(const struct device *dev, uint8_t channel);

static inline int z_impl_sent_stop_listening(const struct device *dev, uint8_t channel)
{
        const struct sent_driver_api *api = DEVICE_API_GET(sent, dev);

        if (api->stop_listening) {
                return api->stop_listening(dev, channel);
        }

        return -ENOSYS;
}

__syscall int sent_register_callback(const struct device *dev, uint8_t channel,
                                     struct sent_rx_callback_configs callback_configs);

static inline int z_impl_sent_register_callback(const struct device *dev, uint8_t channel,
                                                struct sent_rx_callback_configs callback_configs)
{
        const struct sent_driver_api *api = DEVICE_API_GET(sent, dev);

        if (api->register_callback) {
                return api->register_callback(dev, channel, callback_configs);
        }

        return -ENOSYS;
}

#ifdef __cplusplus
}
#endif


#include <zephyr/syscalls/sent.h>

#endif /* ZEPHYR_INCLUDE_DRIVERS_SENT_H_ */
```

## 26.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2025 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 242 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_SENT_H_`。

## 26.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../peripheral_bus_storage_header_reference/P026_zephyr__drivers__sent__sent.h_头文件参考.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [sent_frame_type](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html#ga069232b79943be845df411539ef04993)
- [SENT_SHORT_SERIAL_FRAME](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html#gga069232b79943be845df411539ef04993adbbb93e3efeeb6d2330bc4c9cb0ae4d5)
- [SENT_ENHANCED_SERIAL_FRAME_4_BIT_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html#gga069232b79943be845df411539ef04993a44b400409bb8a00ba23022490a6e6e73)
- [SENT_ENHANCED_SERIAL_FRAME_8_BIT_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html#gga069232b79943be845df411539ef04993aeef9ade678a8b59d7a8e0d0154f9b137)
- [SENT_FAST_FRAME](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html#gga069232b79943be845df411539ef04993afb15bcda86b0faef89c8dc1662f060a1)
- [sent_frame](../peripheral_bus_storage_model_reference/P088_sent_frame_结构体.md)
- [type](../peripheral_bus_storage_model_reference/P088_sent_frame_结构体.md#aafd880b826c351481b384b5fef106068)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [id](../peripheral_bus_storage_model_reference/P088_sent_frame_结构体.md#a689cb24f6c8049e6282ca30939430c8f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [data](../peripheral_bus_storage_model_reference/P088_sent_frame_结构体.md#a43d52380608b7683534dc31873a396af)
- [serial](../peripheral_bus_storage_model_reference/P088_sent_frame_结构体.md#ab39f8ecf19e198ca4818fb13d522c6f4)
- [data_nibbles](../peripheral_bus_storage_model_reference/P088_sent_frame_结构体.md#a4bef9a0871e8ecd86b6753e5bb46c6a0)
- [SENT_MAX_DATA_NIBBLES](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html#ga19bb6e9149dfb7af97ca90289e33bdac)
- [fast](../peripheral_bus_storage_model_reference/P088_sent_frame_结构体.md#a1c02dabd2b0605b77683daf17fc7980b)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [timestamp](../peripheral_bus_storage_model_reference/P088_sent_frame_结构体.md#aae185d5b024a3d9afc135ecc19c9410f)
- [crc](../peripheral_bus_storage_model_reference/P088_sent_frame_结构体.md#a648203dab36ae27e874a171c71d92fe8)
- [sent_rx_frame_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html#ga47d05656177dae0a388e1155be82494f)
- [device](../device_reference/P002_设备对象结构.md)
- [sent_start_listening_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface__backend.html#ga4d4cc8870210e37bdac56d15f5979a32)
- [sent_stop_listening_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface__backend.html#gad13f1bbd1eb6b6300780596b94bff6ac)
- [sent_rx_callback_config](../peripheral_bus_storage_model_reference/P089_sent_rx_callback_config_结构体.md)
- [callback](../peripheral_bus_storage_model_reference/P089_sent_rx_callback_config_结构体.md#afcf63b8116f8dca5839c5b44b5fd1b39)
- [frame](../peripheral_bus_storage_model_reference/P089_sent_rx_callback_config_结构体.md#a251257c08668ced3773bec6895fbd467)
- [max_num_frame](../peripheral_bus_storage_model_reference/P089_sent_rx_callback_config_结构体.md#a45b6353ae6f2177d2267cc343c798726)
- [user_data](../peripheral_bus_storage_model_reference/P089_sent_rx_callback_config_结构体.md#a67e2cd95a91793a1cfbb73f86862ff04)
- [sent_rx_callback_configs](../peripheral_bus_storage_model_reference/P090_sent_rx_callback_configs_结构体.md)
- [serial](../peripheral_bus_storage_model_reference/P090_sent_rx_callback_configs_结构体.md#a631882e363de3c8cc693336028561c1b)
- [fast](../peripheral_bus_storage_model_reference/P090_sent_rx_callback_configs_结构体.md#a0f4d0261c97b21430de9782e20d1c244)
- [sent_register_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface__backend.html#ga3b72c0fafbb177264d20df089ff5c38c)
- [sent_driver_api](../peripheral_bus_storage_model_reference/P087_sent_driver_api_结构体.md)
- [start_listening](../peripheral_bus_storage_model_reference/P087_sent_driver_api_结构体.md#a832b061c8e6ae38199d54f9702fb39a7)
- [stop_listening](../peripheral_bus_storage_model_reference/P087_sent_driver_api_结构体.md#a355a318c08625c99bb1b2adf193bf577)
- [register_callback](../peripheral_bus_storage_model_reference/P087_sent_driver_api_结构体.md#a0be794c9fb93ff9e04fa22cf2aeea4b9)
- [sent_start_listening](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html#ga227aafdbe8f93dbdb97f3969517e6c63)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [ENOSYS](../error_reference/P003_系统错误号公共接口.md#ga43785b9969e0bd1af532dbde06c5540b)
- [sent_stop_listening](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html#gae1eacde97297c97e27b67a7ae7e121cb)
- [sent_register_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html#ga9deb810297f7d42159187bbb8dddb8d2)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [sent_driver_api::register_callback](../peripheral_bus_storage_model_reference/P087_sent_driver_api_结构体.md#a0be794c9fb93ff9e04fa22cf2aeea4b9)
- [sent_driver_api::stop_listening](../peripheral_bus_storage_model_reference/P087_sent_driver_api_结构体.md#a355a318c08625c99bb1b2adf193bf577)
- [sent_driver_api::start_listening](../peripheral_bus_storage_model_reference/P087_sent_driver_api_结构体.md#a832b061c8e6ae38199d54f9702fb39a7)
- [sent_frame::fast](../peripheral_bus_storage_model_reference/P088_sent_frame_结构体.md#a1c02dabd2b0605b77683daf17fc7980b)
- [sent_frame::data](../peripheral_bus_storage_model_reference/P088_sent_frame_结构体.md#a43d52380608b7683534dc31873a396af)
- [sent_frame::data_nibbles](../peripheral_bus_storage_model_reference/P088_sent_frame_结构体.md#a4bef9a0871e8ecd86b6753e5bb46c6a0)
- [sent_frame::crc](../peripheral_bus_storage_model_reference/P088_sent_frame_结构体.md#a648203dab36ae27e874a171c71d92fe8)
- [sent_frame::id](../peripheral_bus_storage_model_reference/P088_sent_frame_结构体.md#a689cb24f6c8049e6282ca30939430c8f)
- [sent_frame::timestamp](../peripheral_bus_storage_model_reference/P088_sent_frame_结构体.md#aae185d5b024a3d9afc135ecc19c9410f)
- [sent_frame::type](../peripheral_bus_storage_model_reference/P088_sent_frame_结构体.md#aafd880b826c351481b384b5fef106068)
- [sent_frame::serial](../peripheral_bus_storage_model_reference/P088_sent_frame_结构体.md#ab39f8ecf19e198ca4818fb13d522c6f4)
- [sent_rx_callback_config::frame](../peripheral_bus_storage_model_reference/P089_sent_rx_callback_config_结构体.md#a251257c08668ced3773bec6895fbd467)
- [sent_rx_callback_config::max_num_frame](../peripheral_bus_storage_model_reference/P089_sent_rx_callback_config_结构体.md#a45b6353ae6f2177d2267cc343c798726)
- [sent_rx_callback_config::user_data](../peripheral_bus_storage_model_reference/P089_sent_rx_callback_config_结构体.md#a67e2cd95a91793a1cfbb73f86862ff04)
- [sent_rx_callback_config::callback](../peripheral_bus_storage_model_reference/P089_sent_rx_callback_config_结构体.md#afcf63b8116f8dca5839c5b44b5fd1b39)
- [sent_rx_callback_configs::fast](../peripheral_bus_storage_model_reference/P090_sent_rx_callback_configs_结构体.md#a0f4d0261c97b21430de9782e20d1c244)
- [sent_rx_callback_configs::serial](../peripheral_bus_storage_model_reference/P090_sent_rx_callback_configs_结构体.md#a631882e363de3c8cc693336028561c1b)

---

[上一章](P025_zephyr__drivers__sdhc.h_头文件源码.md) · [返回大纲](大纲.md) · [下一章](P027_zephyr__drivers__smbus.h_头文件源码.md)
