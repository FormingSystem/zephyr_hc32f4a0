---
id: learning.zephyr-docs.peripheral-bus-storage-source-reference.page-23
title: zephyr__drivers__psi5__psi5.h_头文件源码
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/psi5_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第23章\_zephyr__drivers__psi5__psi5.h_头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/psi5_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应头文件参考](../peripheral_bus_storage_header_reference/P023_zephyr__drivers__psi5__psi5.h_头文件参考.md)。

## 23.1\_原始可见代码（Source Code）

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
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00030"></a>
<a id="foldopen00034"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="foldopen00046"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00069"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00101"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="foldopen00124"></a>
<a id="l00124"></a>
<a id="l00126"></a>
<a id="l00128"></a>
<a id="l00130"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="foldopen00138"></a>
<a id="l00138"></a>
<a id="l00140"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="foldopen00155"></a>
<a id="l00155"></a>
<a id="l00157"></a>
<a id="l00159"></a>
<a id="l00161"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00167"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="agroup__psi5__interface__backend_html_ga1ddcb06317f425a9d97defb1e4ccd677"></a>
<a id="agroup__psi5__interface__backend_html_ga44a73fc30fb29d688d761b8d23eb0da6"></a>
<a id="agroup__psi5__interface__backend_html_gae9b98f6b16ed1364364e1d63f18bb479"></a>
<a id="agroup__psi5__interface__backend_html_gaf86804dd3befe78878ed2d9b3bad9a49"></a>
<a id="agroup__psi5__interface_html_ga37b0fcdecd4629c5f2657b1cc2e227b4"></a>
<a id="agroup__psi5__interface_html_ga3a27606e2828206608a79ada7238466d"></a>
<a id="agroup__psi5__interface_html_ga5cb0ef3be35e9ff2d05c39cc17f2659f"></a>
<a id="agroup__psi5__interface_html_ga5f43079d704d882ae014c7a15bde6406"></a>
<a id="agroup__psi5__interface_html_gaac8c99036369b14d639cfb82f3b9cd32"></a>
<a id="agroup__psi5__interface_html_gabbc2a744edf1ab01e7bd9321054cf32b"></a>
<a id="agroup__psi5__interface_html_gacebce085be1e554e3faa7b69fd8da61f"></a>
<a id="agroup__psi5__interface_html_gga5cb0ef3be35e9ff2d05c39cc17f2659fa456be16421eb918370e6e50c8367d3ff"></a>
<a id="agroup__psi5__interface_html_gga5cb0ef3be35e9ff2d05c39cc17f2659fa8d7f6f8699ded09880c3febd44375c8f"></a>
<a id="agroup__psi5__interface_html_gga5cb0ef3be35e9ff2d05c39cc17f2659fad1bbb5de03efb0be1075766a396d009a"></a>
<a id="agroup__system__errno_html_ga43785b9969e0bd1af532dbde06c5540b"></a>
<a id="akernel_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructdevice_html_a27573cbd10ee145f8bb1396242b27a3e"></a>
<a id="astructk__timeout__t_html"></a>
<a id="astructpsi5__driver__api_html"></a>
<a id="astructpsi5__driver__api_html_a195bc96d912854955b591b5e2911cb98"></a>
<a id="astructpsi5__driver__api_html_a50bf202d1bea4c2bf17b2ba3b0668cf8"></a>
<a id="astructpsi5__driver__api_html_a5ca6bfb70c91a39fb5aadc9194371383"></a>
<a id="astructpsi5__driver__api_html_adf7ff27e095d3d81e7a25ce5ad3e575f"></a>
<a id="astructpsi5__frame_html"></a>
<a id="astructpsi5__frame_html_a04a7d9d8d1238c823d787543ba2188c3"></a>
<a id="astructpsi5__frame_html_a159d66a7eeee3ffc6714f5058ddeefe9"></a>
<a id="astructpsi5__frame_html_a3b7f3b38ab831e2789c326a327a05e53"></a>
<a id="astructpsi5__frame_html_a975b56a545604103687679c2cb0561eb"></a>
<a id="astructpsi5__frame_html_abd146305031fa97378b96d46e3e6e97d"></a>
<a id="astructpsi5__frame_html_ad32ba54088b03cbd4b91e77d9adadec8"></a>
<a id="astructpsi5__frame_html_aec97ec5f2ebef6903fd0b98d8fd2bec4"></a>
<a id="astructpsi5__rx__callback__config_html"></a>
<a id="astructpsi5__rx__callback__config_html_a53035b05d9e60b090d6329487af27541"></a>
<a id="astructpsi5__rx__callback__config_html_a97356b621ae2c142104320c588fa316f"></a>
<a id="astructpsi5__rx__callback__config_html_ad2b224c07eaaf7aef22c94a0e78353c1"></a>
<a id="astructpsi5__rx__callback__config_html_ad7811862b9f6f7f010eb232fc319bcfb"></a>
<a id="astructpsi5__rx__callback__configs_html"></a>
<a id="astructpsi5__rx__callback__configs_html_a0c72a2df8fbbfc9353b37a79ae4f5e6e"></a>
<a id="astructpsi5__rx__callback__configs_html_a600f5e9d7d28b9a5882252765be51307"></a>

```c
/*
 * Copyright 2025 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_PSI5_H_
#define ZEPHYR_INCLUDE_DRIVERS_PSI5_H_

#include <zephyr/kernel.h>
#include <zephyr/device.h>

#ifdef __cplusplus
extern "C" {
#endif


enum psi5_frame_type {
        PSI5_SERIAL_FRAME_4_BIT_ID,
        PSI5_SERIAL_FRAME_8_BIT_ID,
        PSI5_DATA_FRAME
};

struct psi5_frame {
        enum psi5_frame_type type;

        union {
                uint32_t data;

                struct {
                        uint8_t id;
                        uint16_t data;
                } serial;
        };

        uint32_t timestamp;
        uint8_t crc;
        uint8_t slot_number;
};

typedef void (*psi5_tx_callback_t)(const struct device *dev, uint8_t channel, int status,
                                   void *user_data);

typedef void (*psi5_rx_frame_callback_t)(const struct device *dev, uint8_t channel,
                                         uint32_t num_frame, void *user_data);


typedef int (*psi5_start_sync_t)(const struct device *dev, uint8_t channel);

typedef int (*psi5_stop_sync_t)(const struct device *dev, uint8_t channel);

typedef int (*psi5_send_t)(const struct device *dev, uint8_t channel, const uint64_t data,
                           k_timeout_t timeout, psi5_tx_callback_t callback, void *user_data);

struct psi5_rx_callback_config {
        psi5_rx_frame_callback_t callback;
        struct psi5_frame *frame;
        uint32_t max_num_frame;
        void *user_data;
};

struct psi5_rx_callback_configs {
        struct psi5_rx_callback_config *serial_frame;
        struct psi5_rx_callback_config *data_frame;
};

typedef int (*psi5_register_callback_t)(const struct device *dev, uint8_t channel,
                                        struct psi5_rx_callback_configs callback_configs);

__subsystem struct psi5_driver_api {
        psi5_start_sync_t start_sync;
        psi5_stop_sync_t stop_sync;
        psi5_send_t send;
        psi5_register_callback_t register_callback;
};


__syscall int psi5_start_sync(const struct device *dev, uint8_t channel);

static inline int z_impl_psi5_start_sync(const struct device *dev, uint8_t channel)
{
        const struct psi5_driver_api *api = DEVICE_API_GET(psi5, dev);

        if (api->start_sync) {
                return api->start_sync(dev, channel);
        }

        return -ENOSYS;
}

__syscall int psi5_stop_sync(const struct device *dev, uint8_t channel);

static inline int z_impl_psi5_stop_sync(const struct device *dev, uint8_t channel)
{
        const struct psi5_driver_api *api = DEVICE_API_GET(psi5, dev);

        if (api->stop_sync) {
                return api->stop_sync(dev, channel);
        }

        return -ENOSYS;
}

__syscall int psi5_send(const struct device *dev, uint8_t channel, const uint64_t data,
                        k_timeout_t timeout, psi5_tx_callback_t callback, void *user_data);

static inline int z_impl_psi5_send(const struct device *dev, uint8_t channel, const uint64_t data,
                                   k_timeout_t timeout, psi5_tx_callback_t callback,
                                   void *user_data)
{
        const struct psi5_driver_api *api = DEVICE_API_GET(psi5, dev);

        if (api->send) {
                return api->send(dev, channel, data, timeout, callback, user_data);
        }

        return -ENOSYS;
}

__syscall int psi5_register_callback(const struct device *dev, uint8_t channel,
                                     struct psi5_rx_callback_configs callback_configs);

static inline int z_impl_psi5_register_callback(const struct device *dev, uint8_t channel,
                                                struct psi5_rx_callback_configs callback_configs)
{
        const struct psi5_driver_api *api = DEVICE_API_GET(psi5, dev);

        if (api->register_callback) {
                return api->register_callback(dev, channel, callback_configs);
        }

        return -ENOSYS;
}

#ifdef __cplusplus
}
#endif


#include <zephyr/syscalls/psi5.h>

#endif /* ZEPHYR_INCLUDE_DRIVERS_PSI5_H_ */
```

## 23.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2025 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 289 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_PSI5_H_`。

## 23.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../peripheral_bus_storage_header_reference/P023_zephyr__drivers__psi5__psi5.h_头文件参考.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [psi5_frame_type](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface.html#ga5cb0ef3be35e9ff2d05c39cc17f2659f)
- [PSI5_SERIAL_FRAME_4_BIT_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface.html#gga5cb0ef3be35e9ff2d05c39cc17f2659fa456be16421eb918370e6e50c8367d3ff)
- [PSI5_SERIAL_FRAME_8_BIT_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface.html#gga5cb0ef3be35e9ff2d05c39cc17f2659fad1bbb5de03efb0be1075766a396d009a)
- [PSI5_DATA_FRAME](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface.html#gga5cb0ef3be35e9ff2d05c39cc17f2659fa8d7f6f8699ded09880c3febd44375c8f)
- [psi5_frame](../peripheral_bus_storage_model_reference/P071_psi5_frame_结构体.md)
- [type](../peripheral_bus_storage_model_reference/P071_psi5_frame_结构体.md#a975b56a545604103687679c2cb0561eb)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [data](../peripheral_bus_storage_model_reference/P071_psi5_frame_结构体.md#a159d66a7eeee3ffc6714f5058ddeefe9)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [id](../peripheral_bus_storage_model_reference/P071_psi5_frame_结构体.md#ad32ba54088b03cbd4b91e77d9adadec8)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [serial](../peripheral_bus_storage_model_reference/P071_psi5_frame_结构体.md#a04a7d9d8d1238c823d787543ba2188c3)
- [timestamp](../peripheral_bus_storage_model_reference/P071_psi5_frame_结构体.md#a3b7f3b38ab831e2789c326a327a05e53)
- [crc](../peripheral_bus_storage_model_reference/P071_psi5_frame_结构体.md#abd146305031fa97378b96d46e3e6e97d)
- [slot_number](../peripheral_bus_storage_model_reference/P071_psi5_frame_结构体.md#aec97ec5f2ebef6903fd0b98d8fd2bec4)
- [psi5_tx_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface.html#gaac8c99036369b14d639cfb82f3b9cd32)
- [device](../device_reference/P002_设备对象结构.md)
- [psi5_rx_frame_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface.html#ga5f43079d704d882ae014c7a15bde6406)
- [psi5_start_sync_t](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface__backend.html#gaf86804dd3befe78878ed2d9b3bad9a49)
- [psi5_stop_sync_t](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface__backend.html#ga44a73fc30fb29d688d761b8d23eb0da6)
- [psi5_send_t](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface__backend.html#ga1ddcb06317f425a9d97defb1e4ccd677)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [psi5_rx_callback_config](../peripheral_bus_storage_model_reference/P072_psi5_rx_callback_config_结构体.md)
- [callback](../peripheral_bus_storage_model_reference/P072_psi5_rx_callback_config_结构体.md#ad7811862b9f6f7f010eb232fc319bcfb)
- [frame](../peripheral_bus_storage_model_reference/P072_psi5_rx_callback_config_结构体.md#a97356b621ae2c142104320c588fa316f)
- [max_num_frame](../peripheral_bus_storage_model_reference/P072_psi5_rx_callback_config_结构体.md#a53035b05d9e60b090d6329487af27541)
- [user_data](../peripheral_bus_storage_model_reference/P072_psi5_rx_callback_config_结构体.md#ad2b224c07eaaf7aef22c94a0e78353c1)
- [psi5_rx_callback_configs](../peripheral_bus_storage_model_reference/P073_psi5_rx_callback_configs_结构体.md)
- [serial_frame](../peripheral_bus_storage_model_reference/P073_psi5_rx_callback_configs_结构体.md#a0c72a2df8fbbfc9353b37a79ae4f5e6e)
- [data_frame](../peripheral_bus_storage_model_reference/P073_psi5_rx_callback_configs_结构体.md#a600f5e9d7d28b9a5882252765be51307)
- [psi5_register_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface__backend.html#gae9b98f6b16ed1364364e1d63f18bb479)
- [psi5_driver_api](../peripheral_bus_storage_model_reference/P070_psi5_driver_api_结构体.md)
- [start_sync](../peripheral_bus_storage_model_reference/P070_psi5_driver_api_结构体.md#a5ca6bfb70c91a39fb5aadc9194371383)
- [stop_sync](../peripheral_bus_storage_model_reference/P070_psi5_driver_api_结构体.md#adf7ff27e095d3d81e7a25ce5ad3e575f)
- [send](../peripheral_bus_storage_model_reference/P070_psi5_driver_api_结构体.md#a50bf202d1bea4c2bf17b2ba3b0668cf8)
- [register_callback](../peripheral_bus_storage_model_reference/P070_psi5_driver_api_结构体.md#a195bc96d912854955b591b5e2911cb98)
- [psi5_start_sync](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface.html#gabbc2a744edf1ab01e7bd9321054cf32b)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [ENOSYS](../error_reference/P003_系统错误号公共接口.md#ga43785b9969e0bd1af532dbde06c5540b)
- [psi5_stop_sync](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface.html#gacebce085be1e554e3faa7b69fd8da61f)
- [psi5_send](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface.html#ga3a27606e2828206608a79ada7238466d)
- [psi5_register_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface.html#ga37b0fcdecd4629c5f2657b1cc2e227b4)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [device::data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [psi5_driver_api::register_callback](../peripheral_bus_storage_model_reference/P070_psi5_driver_api_结构体.md#a195bc96d912854955b591b5e2911cb98)
- [psi5_driver_api::send](../peripheral_bus_storage_model_reference/P070_psi5_driver_api_结构体.md#a50bf202d1bea4c2bf17b2ba3b0668cf8)
- [psi5_driver_api::start_sync](../peripheral_bus_storage_model_reference/P070_psi5_driver_api_结构体.md#a5ca6bfb70c91a39fb5aadc9194371383)
- [psi5_driver_api::stop_sync](../peripheral_bus_storage_model_reference/P070_psi5_driver_api_结构体.md#adf7ff27e095d3d81e7a25ce5ad3e575f)
- [psi5_frame::serial](../peripheral_bus_storage_model_reference/P071_psi5_frame_结构体.md#a04a7d9d8d1238c823d787543ba2188c3)
- [psi5_frame::data](../peripheral_bus_storage_model_reference/P071_psi5_frame_结构体.md#a159d66a7eeee3ffc6714f5058ddeefe9)
- [psi5_frame::timestamp](../peripheral_bus_storage_model_reference/P071_psi5_frame_结构体.md#a3b7f3b38ab831e2789c326a327a05e53)
- [psi5_frame::type](../peripheral_bus_storage_model_reference/P071_psi5_frame_结构体.md#a975b56a545604103687679c2cb0561eb)
- [psi5_frame::crc](../peripheral_bus_storage_model_reference/P071_psi5_frame_结构体.md#abd146305031fa97378b96d46e3e6e97d)
- [psi5_frame::id](../peripheral_bus_storage_model_reference/P071_psi5_frame_结构体.md#ad32ba54088b03cbd4b91e77d9adadec8)
- [psi5_frame::slot_number](../peripheral_bus_storage_model_reference/P071_psi5_frame_结构体.md#aec97ec5f2ebef6903fd0b98d8fd2bec4)
- [psi5_rx_callback_config::max_num_frame](../peripheral_bus_storage_model_reference/P072_psi5_rx_callback_config_结构体.md#a53035b05d9e60b090d6329487af27541)
- [psi5_rx_callback_config::frame](../peripheral_bus_storage_model_reference/P072_psi5_rx_callback_config_结构体.md#a97356b621ae2c142104320c588fa316f)
- [psi5_rx_callback_config::user_data](../peripheral_bus_storage_model_reference/P072_psi5_rx_callback_config_结构体.md#ad2b224c07eaaf7aef22c94a0e78353c1)
- [psi5_rx_callback_config::callback](../peripheral_bus_storage_model_reference/P072_psi5_rx_callback_config_结构体.md#ad7811862b9f6f7f010eb232fc319bcfb)
- [psi5_rx_callback_configs::serial_frame](../peripheral_bus_storage_model_reference/P073_psi5_rx_callback_configs_结构体.md#a0c72a2df8fbbfc9353b37a79ae4f5e6e)
- [psi5_rx_callback_configs::data_frame](../peripheral_bus_storage_model_reference/P073_psi5_rx_callback_configs_结构体.md#a600f5e9d7d28b9a5882252765be51307)

---

[上一章](P022_zephyr__drivers__ps2.h_头文件源码.md) · [返回大纲](大纲.md) · [下一章](P024_zephyr__sd__sd.h_头文件源码.md)
