---
id: learning.zephyr-docs.api-source-reference.page-876
title: transport.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/transport_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第876章\_transport.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/transport_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/transport_8h.html)。

## 876.1\_原始可见代码（Source Code）

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
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="foldopen00053"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00062"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="foldopen00097"></a>
<a id="l00097"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00203"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
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
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00295"></a>
<a id="l00296"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00302"></a>
<a id="l00303"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="l00314"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__scmi__transport_html_ga4c6cccb4e76fef22ec9f3527a96a8de5"></a>
<a id="agroup__system__errno_html_ga43785b9969e0bd1af532dbde06c5540b"></a>
<a id="akernel_8h_html"></a>
<a id="astdbool_8h_html_abb452686968e48b67397da5f97445f5b"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructdevice_html"></a>
<a id="astructdevice_html_a4a2e6a2cfeb6efed7d5383c33458f46d"></a>
<a id="astructk__mutex_html"></a>
<a id="astructk__sem_html"></a>
<a id="astructscmi__channel_html"></a>
<a id="astructscmi__channel_html_a1b69c9d0c6b49f5496ad59270ab8f157"></a>
<a id="astructscmi__channel_html_a81065fcba9755ccf88c3ce372ded5d56"></a>
<a id="astructscmi__channel_html_ad049e30d6a1806232e2f0adf19e472c9"></a>
<a id="astructscmi__message_html"></a>
<a id="astructscmi__transport__api_html"></a>
<a id="astructscmi__transport__api_html_a2d90efd745ef78a07482c51a5748fef4"></a>
<a id="astructscmi__transport__api_html_a452deceb4eb343b19adf720eae7fb602"></a>
<a id="astructscmi__transport__api_html_a517cb99fc369eec024d4a4acf66865e3"></a>
<a id="astructscmi__transport__api_html_a52c33e80eda1ac892d2e04e3692ced58"></a>
<a id="astructscmi__transport__api_html_a8cc80f631a74b7cf253140fa1a7707d9"></a>
<a id="astructscmi__transport__api_html_ac5eb66a8b0d25c17ef6bf36da23c06ae"></a>

```c
/*
 * Copyright 2024 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_FIRMWARE_SCMI_TRANSPORT_H_
#define ZEPHYR_INCLUDE_DRIVERS_FIRMWARE_SCMI_TRANSPORT_H_

#include <zephyr/device.h>
#include <zephyr/kernel.h>


struct scmi_message;
struct scmi_channel;

typedef void (*scmi_channel_cb)(struct scmi_channel *chan, uint32_t hdr);

struct scmi_channel {
        void *data;
        scmi_channel_cb cb;
        struct k_mutex lock;

        struct k_sem sem;

        bool ready;
        bool polling_only;
};

struct scmi_transport_api {
        int (*init)(const struct device *transport);

        int (*send_message)(const struct device *transport,
                            struct scmi_channel *chan,
                            struct scmi_message *msg,
                            bool use_polling);

        int (*setup_chan)(const struct device *transport,
                          struct scmi_channel *chan,
                          bool tx);

        int (*read_message)(const struct device *transport,
                            struct scmi_channel *chan,
                            struct scmi_message *msg);

        bool (*channel_is_free)(const struct device *transport,
                                struct scmi_channel *chan);

        struct scmi_channel *(*request_channel)(const struct device *transport,
                                                uint32_t proto, bool tx);
};


static inline struct scmi_channel *
scmi_transport_request_channel(const struct device *transport,
                               uint32_t proto, bool tx)
{
        const struct scmi_transport_api *api =
                (const struct scmi_transport_api *)transport->api;

        if (api->request_channel) {
                return api->request_channel(transport, proto, tx);
        }

        return NULL;
}

static inline int scmi_transport_init(const struct device *transport)
{
        const struct scmi_transport_api *api =
                (const struct scmi_transport_api *)transport->api;

        if (api->init) {
                return api->init(transport);
        }

        return 0;
}

static inline int scmi_transport_setup_chan(const struct device *transport,
                                            struct scmi_channel *chan,
                                            bool tx)
{
        const struct scmi_transport_api *api =
                (const struct scmi_transport_api *)transport->api;

        if (!api || !api->setup_chan) {
                return -ENOSYS;
        }

        return api->setup_chan(transport, chan, tx);
}

static inline int scmi_transport_send_message(const struct device *transport,
                                              struct scmi_channel *chan,
                                              struct scmi_message *msg,
                                              bool use_polling)
{
        const struct scmi_transport_api *api =
                (const struct scmi_transport_api *)transport->api;

        if (!api || !api->send_message) {
                return -ENOSYS;
        }

        return api->send_message(transport, chan, msg, use_polling);
}

static inline int scmi_transport_read_message(const struct device *transport,
                                              struct scmi_channel *chan,
                                              struct scmi_message *msg)
{
        const struct scmi_transport_api *api =
                (const struct scmi_transport_api *)transport->api;

        if (!api || !api->read_message) {
                return -ENOSYS;
        }

        return api->read_message(transport, chan, msg);
}

static inline bool scmi_transport_channel_is_free(const struct device *transport,
                                                  struct scmi_channel *chan)
{
        const struct scmi_transport_api *api =
                (const struct scmi_transport_api *)transport->api;

        if (!api || !api->channel_is_free) {
                return -ENOSYS;
        }

        return api->channel_is_free(transport, chan);
}

int scmi_core_transport_init(const struct device *transport);



#endif /* ZEPHYR_INCLUDE_DRIVERS_FIRMWARE_SCMI_TRANSPORT_H_ */
```

## 876.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2024 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 319 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_FIRMWARE_SCMI_TRANSPORT_H_`。

## 876.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/transport_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [scmi_message](../platform_security_model_reference/P037_scmi_message_结构体.md)
- [scmi_channel](../platform_security_model_reference/P033_scmi_channel_结构体.md)
- [scmi_channel_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__transport.html#ga4c6cccb4e76fef22ec9f3527a96a8de5)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [data](../platform_security_model_reference/P033_scmi_channel_结构体.md#a1b69c9d0c6b49f5496ad59270ab8f157)
- [cb](../platform_security_model_reference/P033_scmi_channel_结构体.md#a81065fcba9755ccf88c3ce372ded5d56)
- [k_mutex](../synchronization_reference/P007_内核互斥量结构.md)
- [k_sem](../synchronization_reference/P009_内核信号量结构.md)
- [polling_only](../platform_security_model_reference/P033_scmi_channel_结构体.md#ad049e30d6a1806232e2f0adf19e472c9)
- [scmi_transport_api](../platform_security_model_reference/P052_scmi_transport_api_结构体.md)
- [init](../platform_security_model_reference/P052_scmi_transport_api_结构体.md#a2d90efd745ef78a07482c51a5748fef4)
- [device](../device_reference/P002_设备对象结构.md)
- [send_message](../platform_security_model_reference/P052_scmi_transport_api_结构体.md#ac5eb66a8b0d25c17ef6bf36da23c06ae)
- [setup_chan](../platform_security_model_reference/P052_scmi_transport_api_结构体.md#a452deceb4eb343b19adf720eae7fb602)
- [read_message](../platform_security_model_reference/P052_scmi_transport_api_结构体.md#a8cc80f631a74b7cf253140fa1a7707d9)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [channel_is_free](../platform_security_model_reference/P052_scmi_transport_api_结构体.md#a52c33e80eda1ac892d2e04e3692ced58)
- [api](../device_reference/P002_设备对象结构.md#a4a2e6a2cfeb6efed7d5383c33458f46d)
- [request_channel](../platform_security_model_reference/P052_scmi_transport_api_结构体.md#a517cb99fc369eec024d4a4acf66865e3)
- [ENOSYS](../error_reference/P003_系统错误号公共接口.md#ga43785b9969e0bd1af532dbde06c5540b)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [device::api](../device_reference/P002_设备对象结构.md#a4a2e6a2cfeb6efed7d5383c33458f46d)
- [scmi_channel::data](../platform_security_model_reference/P033_scmi_channel_结构体.md#a1b69c9d0c6b49f5496ad59270ab8f157)
- [scmi_channel::cb](../platform_security_model_reference/P033_scmi_channel_结构体.md#a81065fcba9755ccf88c3ce372ded5d56)
- [scmi_channel::polling_only](../platform_security_model_reference/P033_scmi_channel_结构体.md#ad049e30d6a1806232e2f0adf19e472c9)
- [scmi_transport_api::init](../platform_security_model_reference/P052_scmi_transport_api_结构体.md#a2d90efd745ef78a07482c51a5748fef4)
- [scmi_transport_api::setup_chan](../platform_security_model_reference/P052_scmi_transport_api_结构体.md#a452deceb4eb343b19adf720eae7fb602)
- [scmi_transport_api::request_channel](../platform_security_model_reference/P052_scmi_transport_api_结构体.md#a517cb99fc369eec024d4a4acf66865e3)
- [scmi_transport_api::channel_is_free](../platform_security_model_reference/P052_scmi_transport_api_结构体.md#a52c33e80eda1ac892d2e04e3692ced58)
- [scmi_transport_api::read_message](../platform_security_model_reference/P052_scmi_transport_api_结构体.md#a8cc80f631a74b7cf253140fa1a7707d9)
- [scmi_transport_api::send_message](../platform_security_model_reference/P052_scmi_transport_api_结构体.md#ac5eb66a8b0d25c17ef6bf36da23c06ae)

---

[上一章](P875_transform.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P877_trickle.h_源码浏览.md)
