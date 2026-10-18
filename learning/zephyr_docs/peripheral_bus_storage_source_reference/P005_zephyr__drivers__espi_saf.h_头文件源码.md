---
id: learning.zephyr-docs.peripheral-bus-storage-source-reference.page-5
title: zephyr__drivers__espi_saf.h_头文件源码
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/espi__saf_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_zephyr__drivers__espi_saf.h_头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/espi__saf_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应头文件参考](../peripheral_bus_storage_header_reference/P005_zephyr__drivers__espi_saf.h_头文件参考.md)。

## 5.1\_原始可见代码（Source Code）

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
<a id="l00022"></a>
<a id="l00032"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00097"></a>
<a id="foldopen00104"></a>
<a id="l00104"></a>
<a id="l00106"></a>
<a id="l00108"></a>
<a id="l00110"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="foldopen00122"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="foldopen00131"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00147"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="foldopen00210"></a>
<a id="l00210"></a>
<a id="l00212"></a>
<a id="l00214"></a>
<a id="l00216"></a>
<a id="l00218"></a>
<a id="l00220"></a>
<a id="l00222"></a>
<a id="l00224"></a>
<a id="l00226"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00232"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="l00310"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="l00327"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00333"></a>
<a id="l00344"></a>
<a id="l00345"></a>
<a id="l00346"></a>
<a id="l00347"></a>
<a id="l00348"></a>
<a id="l00349"></a>
<a id="l00350"></a>
<a id="l00351"></a>
<a id="l00365"></a>
<a id="l00366"></a>
<a id="l00367"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="l00372"></a>
<a id="l00373"></a>
<a id="l00374"></a>
<a id="l00375"></a>
<a id="l00376"></a>
<a id="l00377"></a>
<a id="l00378"></a>
<a id="l00379"></a>
<a id="l00393"></a>
<a id="l00394"></a>
<a id="l00395"></a>
<a id="l00396"></a>
<a id="l00397"></a>
<a id="l00398"></a>
<a id="l00399"></a>
<a id="l00400"></a>
<a id="l00401"></a>
<a id="l00402"></a>
<a id="l00403"></a>
<a id="l00404"></a>
<a id="l00405"></a>
<a id="l00406"></a>
<a id="l00407"></a>
<a id="l00421"></a>
<a id="l00422"></a>
<a id="l00423"></a>
<a id="l00424"></a>
<a id="l00425"></a>
<a id="l00426"></a>
<a id="l00427"></a>
<a id="l00428"></a>
<a id="l00429"></a>
<a id="l00430"></a>
<a id="l00431"></a>
<a id="l00432"></a>
<a id="l00433"></a>
<a id="l00434"></a>
<a id="l00435"></a>
<a id="l00449"></a>
<a id="l00450"></a>
<a id="l00451"></a>
<a id="l00452"></a>
<a id="l00453"></a>
<a id="l00454"></a>
<a id="l00455"></a>
<a id="l00456"></a>
<a id="l00457"></a>
<a id="l00458"></a>
<a id="l00459"></a>
<a id="l00460"></a>
<a id="l00461"></a>
<a id="l00462"></a>
<a id="l00463"></a>
<a id="l00525"></a>
<a id="foldopen00534"></a>
<a id="l00534"></a>
<a id="l00535"></a>
<a id="l00536"></a>
<a id="l00537"></a>
<a id="l00538"></a>
<a id="l00539"></a>
<a id="l00540"></a>
<a id="l00541"></a>
<a id="l00542"></a>
<a id="l00543"></a>
<a id="l00544"></a>
<a id="foldopen00557"></a>
<a id="l00557"></a>
<a id="l00558"></a>
<a id="l00559"></a>
<a id="l00560"></a>
<a id="l00561"></a>
<a id="l00562"></a>
<a id="l00563"></a>
<a id="l00564"></a>
<a id="l00565"></a>
<a id="l00566"></a>
<a id="l00567"></a>
<a id="l00568"></a>
<a id="foldopen00585"></a>
<a id="l00585"></a>
<a id="l00586"></a>
<a id="l00587"></a>
<a id="l00588"></a>
<a id="l00589"></a>
<a id="l00590"></a>
<a id="l00591"></a>
<a id="l00592"></a>
<a id="l00593"></a>
<a id="l00594"></a>
<a id="l00595"></a>
<a id="l00596"></a>
<a id="l00597"></a>
<a id="l00598"></a>
<a id="l00599"></a>
<a id="l00600"></a>
<a id="l00604"></a>
<a id="l00605"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="agroup__espi__interface_html_ga36ac3fbf9813f78bad90f047e1eb1128"></a>
<a id="agroup__espi__interface_html_ga9d848c7e367cf277230f365f73c15c46"></a>
<a id="agroup__espi__saf__interface__backend_html_ga03a72ef8a19738d90681114f478ff068"></a>
<a id="agroup__espi__saf__interface__backend_html_ga20ae708179a104c9334fe8fd554e5e05"></a>
<a id="agroup__espi__saf__interface__backend_html_ga24498afe1639bd7c5192215dc8bbbed9"></a>
<a id="agroup__espi__saf__interface__backend_html_ga4e8a12a1311d6604a61d1a9e57573e17"></a>
<a id="agroup__espi__saf__interface__backend_html_ga5f422a48cf008d7a737ec6a3fd0f0400"></a>
<a id="agroup__espi__saf__interface__backend_html_ga6154711885b4edc54db016ba9826c176"></a>
<a id="agroup__espi__saf__interface__backend_html_ga6ac9186c5b022f79dd8671594450efff"></a>
<a id="agroup__espi__saf__interface__backend_html_ga7c1aef03f238ced4e64c6e3be7ad643c"></a>
<a id="agroup__espi__saf__interface__backend_html_gaeb3c1ee73f50fd05737f28a75013c2a8"></a>
<a id="agroup__espi__saf__interface_html_ga0f5017eac05f928e635fec8e5f877c7d"></a>
<a id="agroup__espi__saf__interface_html_ga104175f74019e58b8b7901f3dae245db"></a>
<a id="agroup__espi__saf__interface_html_ga15855a2ac593b97dc1a3e83ac9eda300"></a>
<a id="agroup__espi__saf__interface_html_ga273a9707f3ca501ed2dd3019cdeaa363"></a>
<a id="agroup__espi__saf__interface_html_ga324283c28e6a33be112571621d1568e8"></a>
<a id="agroup__espi__saf__interface_html_ga34b0f6336aec45016d97528767b09434"></a>
<a id="agroup__espi__saf__interface_html_ga66bd7ad63051eefa407df554d5241d9e"></a>
<a id="agroup__espi__saf__interface_html_ga6c54d9274b1a8e883484bd892f606fd5"></a>
<a id="agroup__espi__saf__interface_html_ga8b53a93559f0c67953e283f59107aa22"></a>
<a id="agroup__espi__saf__interface_html_gaafe30738c18a16b056ed8dcf8638eb84"></a>
<a id="agroup__espi__saf__interface_html_gadb881f847082f713bb0159d1e474980a"></a>
<a id="agroup__espi__saf__interface_html_gaf987842bc7dad310c7270aed50086af9"></a>
<a id="agroup__espi__saf__interface_html_gga66bd7ad63051eefa407df554d5241d9ea79df8d5856d2f0d818cb511d9ae41b74"></a>
<a id="agroup__espi__saf__interface_html_gga66bd7ad63051eefa407df554d5241d9ea7bbb878224b80bfa133655879bcb8607"></a>
<a id="agroup__espi__saf__interface_html_gga66bd7ad63051eefa407df554d5241d9ea875a93d6e2f4ed68b0355d71d68674b2"></a>
<a id="agroup__espi__saf__interface_html_gga66bd7ad63051eefa407df554d5241d9ea9041f596e78d9443c7368b46527f49f1"></a>
<a id="agroup__system__errno_html_ga91457bbf35f0f1085619a99423bb1f33"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="astdbool_8h_html_abb452686968e48b67397da5f97445f5b"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructdevice_html"></a>
<a id="astructespi__saf__cfg_html"></a>
<a id="astructespi__saf__cfg_html_a20da4ce3549c53adb038dab7a5bed8a8"></a>
<a id="astructespi__saf__cfg_html_a99d90bcf04f3f09ac5fb739b390a42c8"></a>
<a id="astructespi__saf__cfg_html_ab07ab3b33980f6865cbadbbcb5e203c0"></a>
<a id="astructespi__saf__driver__api_html"></a>
<a id="astructespi__saf__driver__api_html_a088327a328a6007a08d46a657b5eb559"></a>
<a id="astructespi__saf__driver__api_html_a2e8edf284a31c4a64df5e6a663e0a237"></a>
<a id="astructespi__saf__driver__api_html_a3c6cebf1dec4d5335f9a063369f5668f"></a>
<a id="astructespi__saf__driver__api_html_a40236a94bc0381a2c24ac2a7ea313df7"></a>
<a id="astructespi__saf__driver__api_html_a4deef8ca71ecf0f602069b00110433d7"></a>
<a id="astructespi__saf__driver__api_html_a8b6ce9775a5852c8ca9bd495f809598c"></a>
<a id="astructespi__saf__driver__api_html_aa8e94dd0a6e7fadaddadf98395b8e592"></a>
<a id="astructespi__saf__driver__api_html_aabb50eb69906fe5b37b68981899de3c0"></a>
<a id="astructespi__saf__driver__api_html_ab6a07068dc41aa04087d56fa3b70deea"></a>
<a id="astructespi__saf__packet_html"></a>
<a id="astructespi__saf__packet_html_a00bfcab9fe2b928be3ea3485c5e91401"></a>
<a id="astructespi__saf__packet_html_a8ee8a45b3490746f893f6b17fb96b815"></a>
<a id="astructespi__saf__packet_html_af88017b76b64b77c95d9684981f48482"></a>

```c
/*
 * Copyright (c) 2019 Intel Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_ESPI_SAF_H_
#define ZEPHYR_INCLUDE_ESPI_SAF_H_

#include <zephyr/sys/__assert.h>
#include <zephyr/types.h>
#include <zephyr/device.h>

#ifdef __cplusplus
extern "C" {
#endif







enum espi_taf_event {
        ESPI_TAF_EVENT_NO_REQUEST = 0,
        ESPI_TAF_EVENT_HOST_REQUEST,
        ESPI_TAF_EVENT_EC0_REQUEST,
        ESPI_TAF_EVENT_MAX_REQUEST,
};

struct espi_saf_hw_cfg;
struct espi_saf_flash_cfg;
struct espi_saf_pr;

struct espi_saf_cfg {
        uint8_t nflash_devices;
        struct espi_saf_hw_cfg hwcfg;
        struct espi_saf_flash_cfg *flash_cfgs;
};

struct espi_saf_packet {
        uint32_t flash_addr;
        uint8_t *buf;
        uint32_t len;
};

/*
 *defined in espi.h
 * struct espi_callback
 * typedef void (*espi_callback_handler_t)()
 */


typedef int (*espi_saf_api_config)(const struct device *dev,
                                   const struct espi_saf_cfg *cfg);

typedef int (*espi_saf_api_set_protection_regions)(
                                const struct device *dev,
                                const struct espi_saf_protection *pr);

typedef int (*espi_saf_api_activate)(const struct device *dev);

typedef bool (*espi_saf_api_get_channel_status)(const struct device *dev);

typedef int (*espi_saf_api_flash_read)(const struct device *dev,
                                       struct espi_saf_packet *pckt);
typedef int (*espi_saf_api_flash_write)(const struct device *dev,
                                        struct espi_saf_packet *pckt);
typedef int (*espi_saf_api_flash_erase)(const struct device *dev,
                                        struct espi_saf_packet *pckt);
typedef int (*espi_saf_api_flash_unsuccess)(const struct device *dev,
                                        struct espi_saf_packet *pckt);
typedef int (*espi_saf_api_manage_callback)(const struct device *dev,
                                            struct espi_callback *callback,
                                            bool set);

__subsystem struct espi_saf_driver_api {
        espi_saf_api_config config;
        espi_saf_api_set_protection_regions set_protection_regions;
        espi_saf_api_activate activate;
        espi_saf_api_get_channel_status get_channel_status;
        espi_saf_api_flash_read flash_read;
        espi_saf_api_flash_write flash_write;
        espi_saf_api_flash_erase flash_erase;
        espi_saf_api_flash_unsuccess flash_unsuccess;
        espi_saf_api_manage_callback manage_callback;
};


__syscall int espi_saf_config(const struct device *dev,
                              const struct espi_saf_cfg *cfg);

static inline int z_impl_espi_saf_config(const struct device *dev,
                                         const struct espi_saf_cfg *cfg)
{
        return DEVICE_API_GET(espi_saf, dev)->config(dev, cfg);
}

__syscall int espi_saf_set_protection_regions(
                                const struct device *dev,
                                const struct espi_saf_protection *pr);

static inline int z_impl_espi_saf_set_protection_regions(
                                        const struct device *dev,
                                        const struct espi_saf_protection *pr)
{
        return DEVICE_API_GET(espi_saf, dev)->set_protection_regions(dev, pr);
}

__syscall int espi_saf_activate(const struct device *dev);

static inline int z_impl_espi_saf_activate(const struct device *dev)
{
        return DEVICE_API_GET(espi_saf, dev)->activate(dev);
}

__syscall bool espi_saf_get_channel_status(const struct device *dev);

static inline bool z_impl_espi_saf_get_channel_status(
                                        const struct device *dev)
{
        return DEVICE_API_GET(espi_saf, dev)->get_channel_status(dev);
}

__syscall int espi_saf_flash_read(const struct device *dev,
                                  struct espi_saf_packet *pckt);

static inline int z_impl_espi_saf_flash_read(const struct device *dev,
                                             struct espi_saf_packet *pckt)
{
        const struct espi_saf_driver_api *api = DEVICE_API_GET(espi_saf, dev);

        if (!api->flash_read) {
                return -ENOTSUP;
        }

        return api->flash_read(dev, pckt);
}

__syscall int espi_saf_flash_write(const struct device *dev,
                                   struct espi_saf_packet *pckt);

static inline int z_impl_espi_saf_flash_write(const struct device *dev,
                                              struct espi_saf_packet *pckt)
{
        const struct espi_saf_driver_api *api = DEVICE_API_GET(espi_saf, dev);

        if (!api->flash_write) {
                return -ENOTSUP;
        }

        return api->flash_write(dev, pckt);
}

__syscall int espi_saf_flash_erase(const struct device *dev,
                                   struct espi_saf_packet *pckt);

static inline int z_impl_espi_saf_flash_erase(const struct device *dev,
                                              struct espi_saf_packet *pckt)
{
        const struct espi_saf_driver_api *api = DEVICE_API_GET(espi_saf, dev);

        if (!api->flash_erase) {
                return -ENOTSUP;
        }

        return api->flash_erase(dev, pckt);
}

__syscall int espi_saf_flash_unsuccess(const struct device *dev,
                                       struct espi_saf_packet *pckt);

static inline int z_impl_espi_saf_flash_unsuccess(const struct device *dev,
                                                  struct espi_saf_packet *pckt)
{
        const struct espi_saf_driver_api *api = DEVICE_API_GET(espi_saf, dev);

        if (!api->flash_unsuccess) {
                return -ENOTSUP;
        }

        return api->flash_unsuccess(dev, pckt);
}


static inline void espi_saf_init_callback(struct espi_callback *callback,
                                          espi_callback_handler_t handler,
                                          enum espi_bus_event evt_type)
{
        __ASSERT(callback, "Callback pointer should not be NULL");
        __ASSERT(handler, "Callback handler pointer should not be NULL");

        callback->handler = handler;
        callback->evt_type = evt_type;
}

static inline int espi_saf_add_callback(const struct device *dev,
                                        struct espi_callback *callback)
{
        const struct espi_saf_driver_api *api = DEVICE_API_GET(espi_saf, dev);

        if (!api->manage_callback) {
                return -ENOTSUP;
        }

        return api->manage_callback(dev, callback, true);
}

static inline int espi_saf_remove_callback(const struct device *dev,
                                           struct espi_callback *callback)
{
        const struct espi_saf_driver_api *api = DEVICE_API_GET(espi_saf, dev);

        if (!api->manage_callback) {
                return -ENOTSUP;
        }

        return api->manage_callback(dev, callback, false);
}

#ifdef __cplusplus
}
#endif

#include <zephyr/syscalls/espi_saf.h>
#endif /* ZEPHYR_INCLUDE_ESPI_SAF_H_ */
```

## 5.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2019 Intel Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 137 行

以下内容定义于 `espi.h`：`struct espi_callback` 和 `typedef void (*espi_callback_handler_t)()`。

### 注释 3：原第 605 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_ESPI_SAF_H_`。

## 5.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../peripheral_bus_storage_header_reference/P005_zephyr__drivers__espi_saf.h_头文件参考.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [espi_taf_event](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#ga66bd7ad63051eefa407df554d5241d9e)
- [ESPI_TAF_EVENT_NO_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#gga66bd7ad63051eefa407df554d5241d9ea7bbb878224b80bfa133655879bcb8607)
- [ESPI_TAF_EVENT_HOST_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#gga66bd7ad63051eefa407df554d5241d9ea79df8d5856d2f0d818cb511d9ae41b74)
- [ESPI_TAF_EVENT_EC0_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#gga66bd7ad63051eefa407df554d5241d9ea875a93d6e2f4ed68b0355d71d68674b2)
- [ESPI_TAF_EVENT_MAX_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#gga66bd7ad63051eefa407df554d5241d9ea9041f596e78d9443c7368b46527f49f1)
- [espi_saf_cfg](../peripheral_bus_storage_model_reference/P015_espi_saf_cfg_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [nflash_devices](../peripheral_bus_storage_model_reference/P015_espi_saf_cfg_结构体.md#ab07ab3b33980f6865cbadbbcb5e203c0)
- [hwcfg](../peripheral_bus_storage_model_reference/P015_espi_saf_cfg_结构体.md#a20da4ce3549c53adb038dab7a5bed8a8)
- [flash_cfgs](../peripheral_bus_storage_model_reference/P015_espi_saf_cfg_结构体.md#a99d90bcf04f3f09ac5fb739b390a42c8)
- [espi_saf_packet](../peripheral_bus_storage_model_reference/P017_espi_saf_packet_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [flash_addr](../peripheral_bus_storage_model_reference/P017_espi_saf_packet_结构体.md#a8ee8a45b3490746f893f6b17fb96b815)
- [buf](../peripheral_bus_storage_model_reference/P017_espi_saf_packet_结构体.md#a00bfcab9fe2b928be3ea3485c5e91401)
- [len](../peripheral_bus_storage_model_reference/P017_espi_saf_packet_结构体.md#af88017b76b64b77c95d9684981f48482)
- [espi_saf_api_config](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface__backend.html#ga5f422a48cf008d7a737ec6a3fd0f0400)
- [device](../device_reference/P002_设备对象结构.md)
- [espi_saf_api_set_protection_regions](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface__backend.html#gaeb3c1ee73f50fd05737f28a75013c2a8)
- [espi_saf_api_activate](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface__backend.html#ga03a72ef8a19738d90681114f478ff068)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [espi_saf_api_get_channel_status](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface__backend.html#ga6ac9186c5b022f79dd8671594450efff)
- [espi_saf_api_flash_read](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface__backend.html#ga6154711885b4edc54db016ba9826c176)
- [espi_saf_api_flash_write](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface__backend.html#ga24498afe1639bd7c5192215dc8bbbed9)
- [espi_saf_api_flash_erase](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface__backend.html#ga4e8a12a1311d6604a61d1a9e57573e17)
- [espi_saf_api_flash_unsuccess](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface__backend.html#ga7c1aef03f238ced4e64c6e3be7ad643c)
- [espi_saf_api_manage_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface__backend.html#ga20ae708179a104c9334fe8fd554e5e05)
- [espi_saf_driver_api](../peripheral_bus_storage_model_reference/P016_espi_saf_driver_api_结构体.md)
- [config](../peripheral_bus_storage_model_reference/P016_espi_saf_driver_api_结构体.md#a4deef8ca71ecf0f602069b00110433d7)
- [set_protection_regions](../peripheral_bus_storage_model_reference/P016_espi_saf_driver_api_结构体.md#a40236a94bc0381a2c24ac2a7ea313df7)
- [activate](../peripheral_bus_storage_model_reference/P016_espi_saf_driver_api_结构体.md#a2e8edf284a31c4a64df5e6a663e0a237)
- [get_channel_status](../peripheral_bus_storage_model_reference/P016_espi_saf_driver_api_结构体.md#a088327a328a6007a08d46a657b5eb559)
- [flash_read](../peripheral_bus_storage_model_reference/P016_espi_saf_driver_api_结构体.md#a3c6cebf1dec4d5335f9a063369f5668f)
- [flash_write](../peripheral_bus_storage_model_reference/P016_espi_saf_driver_api_结构体.md#a8b6ce9775a5852c8ca9bd495f809598c)
- [flash_erase](../peripheral_bus_storage_model_reference/P016_espi_saf_driver_api_结构体.md#aa8e94dd0a6e7fadaddadf98395b8e592)
- [flash_unsuccess](../peripheral_bus_storage_model_reference/P016_espi_saf_driver_api_结构体.md#aabb50eb69906fe5b37b68981899de3c0)
- [manage_callback](../peripheral_bus_storage_model_reference/P016_espi_saf_driver_api_结构体.md#ab6a07068dc41aa04087d56fa3b70deea)
- [espi_saf_config](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#ga34b0f6336aec45016d97528767b09434)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [espi_saf_set_protection_regions](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#ga273a9707f3ca501ed2dd3019cdeaa363)
- [espi_saf_activate](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#gaafe30738c18a16b056ed8dcf8638eb84)
- [espi_saf_get_channel_status](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#ga8b53a93559f0c67953e283f59107aa22)
- [espi_saf_flash_read](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#ga0f5017eac05f928e635fec8e5f877c7d)
- [ENOTSUP](../error_reference/P003_系统错误号公共接口.md#ga91457bbf35f0f1085619a99423bb1f33)
- [espi_saf_flash_write](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#ga104175f74019e58b8b7901f3dae245db)
- [espi_saf_flash_erase](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#ga15855a2ac593b97dc1a3e83ac9eda300)
- [espi_saf_flash_unsuccess](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#ga6c54d9274b1a8e883484bd892f606fd5)
- [espi_saf_init_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#ga324283c28e6a33be112571621d1568e8)
- [espi_callback_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga9d848c7e367cf277230f365f73c15c46)
- [espi_bus_event](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga36ac3fbf9813f78bad90f047e1eb1128)
- [espi_saf_add_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#gadb881f847082f713bb0159d1e474980a)
- [espi_saf_remove_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#gaf987842bc7dad310c7270aed50086af9)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [espi_saf_cfg::hwcfg](../peripheral_bus_storage_model_reference/P015_espi_saf_cfg_结构体.md#a20da4ce3549c53adb038dab7a5bed8a8)
- [espi_saf_cfg::flash_cfgs](../peripheral_bus_storage_model_reference/P015_espi_saf_cfg_结构体.md#a99d90bcf04f3f09ac5fb739b390a42c8)
- [espi_saf_cfg::nflash_devices](../peripheral_bus_storage_model_reference/P015_espi_saf_cfg_结构体.md#ab07ab3b33980f6865cbadbbcb5e203c0)
- [espi_saf_driver_api::get_channel_status](../peripheral_bus_storage_model_reference/P016_espi_saf_driver_api_结构体.md#a088327a328a6007a08d46a657b5eb559)
- [espi_saf_driver_api::activate](../peripheral_bus_storage_model_reference/P016_espi_saf_driver_api_结构体.md#a2e8edf284a31c4a64df5e6a663e0a237)
- [espi_saf_driver_api::flash_read](../peripheral_bus_storage_model_reference/P016_espi_saf_driver_api_结构体.md#a3c6cebf1dec4d5335f9a063369f5668f)
- [espi_saf_driver_api::set_protection_regions](../peripheral_bus_storage_model_reference/P016_espi_saf_driver_api_结构体.md#a40236a94bc0381a2c24ac2a7ea313df7)
- [espi_saf_driver_api::config](../peripheral_bus_storage_model_reference/P016_espi_saf_driver_api_结构体.md#a4deef8ca71ecf0f602069b00110433d7)
- [espi_saf_driver_api::flash_write](../peripheral_bus_storage_model_reference/P016_espi_saf_driver_api_结构体.md#a8b6ce9775a5852c8ca9bd495f809598c)
- [espi_saf_driver_api::flash_erase](../peripheral_bus_storage_model_reference/P016_espi_saf_driver_api_结构体.md#aa8e94dd0a6e7fadaddadf98395b8e592)
- [espi_saf_driver_api::flash_unsuccess](../peripheral_bus_storage_model_reference/P016_espi_saf_driver_api_结构体.md#aabb50eb69906fe5b37b68981899de3c0)
- [espi_saf_driver_api::manage_callback](../peripheral_bus_storage_model_reference/P016_espi_saf_driver_api_结构体.md#ab6a07068dc41aa04087d56fa3b70deea)
- [espi_saf_packet::buf](../peripheral_bus_storage_model_reference/P017_espi_saf_packet_结构体.md#a00bfcab9fe2b928be3ea3485c5e91401)
- [espi_saf_packet::flash_addr](../peripheral_bus_storage_model_reference/P017_espi_saf_packet_结构体.md#a8ee8a45b3490746f893f6b17fb96b815)
- [espi_saf_packet::len](../peripheral_bus_storage_model_reference/P017_espi_saf_packet_结构体.md#af88017b76b64b77c95d9684981f48482)

---

[上一章](P004_zephyr__drivers__espi.h_头文件源码.md) · [返回大纲](大纲.md) · [下一章](P006_zephyr__drivers__fpga.h_头文件源码.md)
