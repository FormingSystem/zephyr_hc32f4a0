---
id: learning.zephyr-docs.api-source-reference.page-156
title: protocol.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2protocol_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第156章\_protocol.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2protocol_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2protocol_8h.html)。

## 156.1\_原始可见代码（Source Code）

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
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="foldopen00047"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="foldopen00076"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="foldopen00088"></a>
<a id="l00088"></a>
<a id="l00090"></a>
<a id="l00092"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00100"></a>
<a id="l00102"></a>
<a id="l00104"></a>
<a id="l00106"></a>
<a id="l00108"></a>
<a id="l00110"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="foldopen00120"></a>
<a id="l00120"></a>
<a id="l00122"></a>
<a id="l00124"></a>
<a id="l00126"></a>
<a id="l00128"></a>
<a id="l00130"></a>
<a id="l00132"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="foldopen00156"></a>
<a id="l00156"></a>
<a id="l00158"></a>
<a id="l00160"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="foldopen00175"></a>
<a id="l00175"></a>
<a id="l00177"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00182"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="foldopen00194"></a>
<a id="l00194"></a>
<a id="l00196"></a>
<a id="l00198"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="l00291"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="adevice_8h_html"></a>
<a id="adrivers_2firmware_2scmi_2util_8h_html"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__scmi__interface_html_ga0c1b38acb21bc918714720c781e50d77"></a>
<a id="agroup__scmi__interface_html_ga0f5d5c4382c41a507b21741e88cbcac0"></a>
<a id="agroup__scmi__interface_html_ga451a39b7d2f3ffafa9d69b21c7e249b2"></a>
<a id="agroup__scmi__interface_html_ga8430a8fd8a2f84d0f5613a88b8d86650"></a>
<a id="agroup__scmi__interface_html_gaa97701c4c038fa5403e5696ac84e6149"></a>
<a id="agroup__scmi__interface_html_gac6afb98180e88ade7d235a96e72b7ca6"></a>
<a id="agroup__scmi__interface_html_gacba26fb193852024636dda1e4ef0ee53"></a>
<a id="agroup__scmi__interface_html_gae5326d8ffd8fc7ed76ba73a0aee95d49"></a>
<a id="agroup__scmi__interface_html_gae58fdab329d4f0d2a4b16c6f2a668fe6"></a>
<a id="agroup__scmi__interface_html_gaec0ffd1352d0106633fd15be8fc20aa2"></a>
<a id="agroup__scmi__interface_html_gga0c1b38acb21bc918714720c781e50d77a3f8a2a47929b4de637a158dd1c401e04"></a>
<a id="agroup__scmi__interface_html_gga0c1b38acb21bc918714720c781e50d77ae7a8eede3c6a972ad74fc98697b36668"></a>
<a id="agroup__scmi__interface_html_gga0c1b38acb21bc918714720c781e50d77af5bbe670cc662bb4fe577d3b4c43acb8"></a>
<a id="agroup__scmi__interface_html_gga451a39b7d2f3ffafa9d69b21c7e249b2a000bdbba75d33395490777f1955069c4"></a>
<a id="agroup__scmi__interface_html_gga451a39b7d2f3ffafa9d69b21c7e249b2a2b12279fd4910a2bb349fe26d51772b0"></a>
<a id="agroup__scmi__interface_html_gga451a39b7d2f3ffafa9d69b21c7e249b2a31062d59e627c538943d9b180f2bbdaa"></a>
<a id="agroup__scmi__interface_html_gga451a39b7d2f3ffafa9d69b21c7e249b2a39691c371b8f8c309522ddfe217ec763"></a>
<a id="agroup__scmi__interface_html_gga451a39b7d2f3ffafa9d69b21c7e249b2a5b133193f0ad79541b3c7ca7ff7086b6"></a>
<a id="agroup__scmi__interface_html_gga451a39b7d2f3ffafa9d69b21c7e249b2a7ec843eac30888df53a4142c8a4fb18e"></a>
<a id="agroup__scmi__interface_html_gga451a39b7d2f3ffafa9d69b21c7e249b2a7f05e2ce40670eac59c9d66913f6f0d4"></a>
<a id="agroup__scmi__interface_html_gga451a39b7d2f3ffafa9d69b21c7e249b2a86b3facf8608f0a1a50a15702a81abcc"></a>
<a id="agroup__scmi__interface_html_gga451a39b7d2f3ffafa9d69b21c7e249b2abf54857fe736374a01ec720f595b38bf"></a>
<a id="agroup__scmi__interface_html_gga451a39b7d2f3ffafa9d69b21c7e249b2ad9a7e0568754ed38d498f95b56af4a60"></a>
<a id="agroup__scmi__interface_html_gga451a39b7d2f3ffafa9d69b21c7e249b2adcd09f6ee2b372fe3d854b632dad8089"></a>
<a id="agroup__scmi__interface_html_gga451a39b7d2f3ffafa9d69b21c7e249b2aec1bdf1af231aaf8fecf1cbfdf80ee8d"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructscmi__channel_html"></a>
<a id="astructscmi__message_html"></a>
<a id="astructscmi__message_html_a4b329136651a527d51310af82dc24795"></a>
<a id="astructscmi__message_html_aad4f7713d97765414e21a4cb6ed4b01f"></a>
<a id="astructscmi__message_html_ae868ec173129a6f81c895279e95bb52d"></a>
<a id="astructscmi__protocol__events_html"></a>
<a id="astructscmi__protocol__events_html_a33fb7a3e095fb1ad5267080130277578"></a>
<a id="astructscmi__protocol__events_html_a5ea92cc3ee5da51882568cc464378a7b"></a>
<a id="astructscmi__protocol__events_html_ac04442b926499369d7c89d8aacf0da41"></a>
<a id="astructscmi__protocol__version_html"></a>
<a id="astructscmi__protocol__version_html_a03bf7fd19968bd6e976c948d29f83326"></a>
<a id="astructscmi__protocol__version_html_a602f109457cb0e481a0446cb40f81fab"></a>
<a id="astructscmi__protocol__version_html_a978b1c6f10fd87e5f538e840e4e71470"></a>
<a id="astructscmi__protocol_html"></a>
<a id="astructscmi__protocol_html_a1b414028a899b5bef9c4df38352c5928"></a>
<a id="astructscmi__protocol_html_a4580aabc67a32be7dc9e914dd863a90b"></a>
<a id="astructscmi__protocol_html_a809979e1c761c8486d62a4af6a21b4ad"></a>
<a id="astructscmi__protocol_html_a9081097c7aa12c407ec1d837c541d666"></a>
<a id="astructscmi__protocol_html_aa2a78f57d21a573c6091fba89a757a52"></a>
<a id="astructscmi__protocol_html_ad6c1e08eebc96ff76ae656510d04a9d5"></a>
<a id="astructscmi__protocol_html_ae2c2026eeaad8c5bf73be885fdd6315c"></a>

```c
/*
 * Copyright 2024,2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_FIRMWARE_SCMI_PROTOCOL_H_
#define ZEPHYR_INCLUDE_DRIVERS_FIRMWARE_SCMI_PROTOCOL_H_


#include <zephyr/device.h>
#include <zephyr/drivers/firmware/scmi/util.h>
#include <stdint.h>
#include <errno.h>

#define SCMI_SHORT_NAME_MAX_SIZE 16

#define SCMI_MESSAGE_HDR_MAKE(id, type, proto, token)                                              \
        (SCMI_FIELD_MAKE(id, GENMASK(7, 0), 0) | SCMI_FIELD_MAKE(type, GENMASK(1, 0), 8) |         \
         SCMI_FIELD_MAKE(proto, GENMASK(7, 0), 10) | SCMI_FIELD_MAKE(token, GENMASK(9, 0), 18))

#define SCMI_MESSAGE_HDR_TAKE_MSGID(hdr)    FIELD_GET(GENMASK(7, 0), (hdr))

#define SCMI_MESSAGE_HDR_TAKE_TYPE(hdr)     FIELD_GET(GENMASK(9, 8), (hdr))

#define SCMI_MESSAGE_HDR_TAKE_PROTOCOL(hdr) FIELD_GET(GENMASK(17, 10), (hdr))

#define SCMI_MESSAGE_HDR_TAKE_TOKEN(hdr)    FIELD_GET(GENMASK(27, 18), (hdr))

struct scmi_channel;

enum scmi_message_type {
        SCMI_COMMAND = 0x0,
        SCMI_DELAYED_REPLY = 0x2,
        SCMI_NOTIFICATION = 0x3,
};

enum scmi_status_code {
        SCMI_SUCCESS = 0,
        SCMI_NOT_SUPPORTED = -1,
        SCMI_INVALID_PARAMETERS = -2,
        SCMI_DENIED = -3,
        SCMI_NOT_FOUND = -4,
        SCMI_OUT_OF_RANGE = -5,
        SCMI_BUSY = -6,
        SCMI_COMMS_ERROR = -7,
        SCMI_GENERIC_ERROR = -8,
        SCMI_HARDWARE_ERROR = -9,
        SCMI_PROTOCOL_ERROR = -10,
        SCMI_IN_USE = -11,
};

struct scmi_protocol {
        uint32_t id;
        struct scmi_channel *tx;
        struct scmi_channel *rx;
        const struct device *transport;
        void *data;
        uint32_t version;
        const struct scmi_protocol_events *events;
};

typedef void (*scmi_protocol_event_callback)(struct scmi_protocol *proto, uint32_t msg_id);

struct scmi_protocol_events {
        const uint32_t *evts;
        uint32_t num_events;
        scmi_protocol_event_callback cb;
};

struct scmi_protocol_version {
        union {
                uint32_t raw;
                struct {
                        uint16_t minor;
                        uint16_t major;
                };
        };
};

struct scmi_message {
        uint32_t hdr;
        uint32_t len;
        void *content;
};

int scmi_status_to_errno(int scmi_status);

int scmi_send_message(struct scmi_protocol *proto, struct scmi_message *msg,
                      struct scmi_message *reply, bool use_polling);

int scmi_protocol_get_version(struct scmi_protocol *proto, uint32_t *version);

int scmi_protocol_attributes_get(struct scmi_protocol *proto, uint32_t *attributes);

int scmi_protocol_message_attributes_get(struct scmi_protocol *proto, uint32_t message_id,
                                         uint32_t *attributes);

int scmi_protocol_version_negotiate(struct scmi_protocol *proto, uint32_t version);

int scmi_read_message(struct scmi_protocol *proto, struct scmi_message *msg);



#endif /* ZEPHYR_INCLUDE_DRIVERS_FIRMWARE_SCMI_PROTOCOL_H_ */
```

## 156.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2024,2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 298 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_FIRMWARE_SCMI_PROTOCOL_H_`。

## 156.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2protocol_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/drivers/firmware/scmi/util.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2util_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [scmi_channel](../platform_security_model_reference/P033_scmi_channel_结构体.md)
- [scmi_message_type](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#ga0c1b38acb21bc918714720c781e50d77)
- [SCMI_COMMAND](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gga0c1b38acb21bc918714720c781e50d77af5bbe670cc662bb4fe577d3b4c43acb8)
- [SCMI_DELAYED_REPLY](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gga0c1b38acb21bc918714720c781e50d77ae7a8eede3c6a972ad74fc98697b36668)
- [SCMI_NOTIFICATION](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gga0c1b38acb21bc918714720c781e50d77a3f8a2a47929b4de637a158dd1c401e04)
- [scmi_status_code](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#ga451a39b7d2f3ffafa9d69b21c7e249b2)
- [SCMI_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gga451a39b7d2f3ffafa9d69b21c7e249b2a000bdbba75d33395490777f1955069c4)
- [SCMI_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gga451a39b7d2f3ffafa9d69b21c7e249b2adcd09f6ee2b372fe3d854b632dad8089)
- [SCMI_INVALID_PARAMETERS](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gga451a39b7d2f3ffafa9d69b21c7e249b2a2b12279fd4910a2bb349fe26d51772b0)
- [SCMI_DENIED](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gga451a39b7d2f3ffafa9d69b21c7e249b2abf54857fe736374a01ec720f595b38bf)
- [SCMI_NOT_FOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gga451a39b7d2f3ffafa9d69b21c7e249b2a86b3facf8608f0a1a50a15702a81abcc)
- [SCMI_OUT_OF_RANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gga451a39b7d2f3ffafa9d69b21c7e249b2a7ec843eac30888df53a4142c8a4fb18e)
- [SCMI_BUSY](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gga451a39b7d2f3ffafa9d69b21c7e249b2a31062d59e627c538943d9b180f2bbdaa)
- [SCMI_COMMS_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gga451a39b7d2f3ffafa9d69b21c7e249b2aec1bdf1af231aaf8fecf1cbfdf80ee8d)
- [SCMI_GENERIC_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gga451a39b7d2f3ffafa9d69b21c7e249b2a39691c371b8f8c309522ddfe217ec763)
- [SCMI_HARDWARE_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gga451a39b7d2f3ffafa9d69b21c7e249b2a5b133193f0ad79541b3c7ca7ff7086b6)
- [SCMI_PROTOCOL_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gga451a39b7d2f3ffafa9d69b21c7e249b2a7f05e2ce40670eac59c9d66913f6f0d4)
- [SCMI_IN_USE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gga451a39b7d2f3ffafa9d69b21c7e249b2ad9a7e0568754ed38d498f95b56af4a60)
- [scmi_protocol](../platform_security_model_reference/P047_scmi_protocol_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [id](../platform_security_model_reference/P047_scmi_protocol_结构体.md#ae2c2026eeaad8c5bf73be885fdd6315c)
- [tx](../platform_security_model_reference/P047_scmi_protocol_结构体.md#aa2a78f57d21a573c6091fba89a757a52)
- [rx](../platform_security_model_reference/P047_scmi_protocol_结构体.md#a4580aabc67a32be7dc9e914dd863a90b)
- [device](../device_reference/P002_设备对象结构.md)
- [transport](../platform_security_model_reference/P047_scmi_protocol_结构体.md#a9081097c7aa12c407ec1d837c541d666)
- [data](../platform_security_model_reference/P047_scmi_protocol_结构体.md#ad6c1e08eebc96ff76ae656510d04a9d5)
- [version](../platform_security_model_reference/P047_scmi_protocol_结构体.md#a809979e1c761c8486d62a4af6a21b4ad)
- [scmi_protocol_events](../platform_security_model_reference/P048_scmi_protocol_events_结构体.md)
- [events](../platform_security_model_reference/P047_scmi_protocol_结构体.md#a1b414028a899b5bef9c4df38352c5928)
- [scmi_protocol_event_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#ga8430a8fd8a2f84d0f5613a88b8d86650)
- [evts](../platform_security_model_reference/P048_scmi_protocol_events_结构体.md#ac04442b926499369d7c89d8aacf0da41)
- [num_events](../platform_security_model_reference/P048_scmi_protocol_events_结构体.md#a33fb7a3e095fb1ad5267080130277578)
- [cb](../platform_security_model_reference/P048_scmi_protocol_events_结构体.md#a5ea92cc3ee5da51882568cc464378a7b)
- [scmi_protocol_version](../platform_security_model_reference/P049_scmi_protocol_version_结构体.md)
- [raw](../platform_security_model_reference/P049_scmi_protocol_version_结构体.md#a978b1c6f10fd87e5f538e840e4e71470)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [minor](../platform_security_model_reference/P049_scmi_protocol_version_结构体.md#a602f109457cb0e481a0446cb40f81fab)
- [major](../platform_security_model_reference/P049_scmi_protocol_version_结构体.md#a03bf7fd19968bd6e976c948d29f83326)
- [scmi_message](../platform_security_model_reference/P037_scmi_message_结构体.md)
- [hdr](../platform_security_model_reference/P037_scmi_message_结构体.md#a4b329136651a527d51310af82dc24795)
- [len](../platform_security_model_reference/P037_scmi_message_结构体.md#aad4f7713d97765414e21a4cb6ed4b01f)
- [content](../platform_security_model_reference/P037_scmi_message_结构体.md#ae868ec173129a6f81c895279e95bb52d)
- [scmi_status_to_errno](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gaec0ffd1352d0106633fd15be8fc20aa2)
- [scmi_send_message](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gacba26fb193852024636dda1e4ef0ee53)
- [scmi_protocol_get_version](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gaa97701c4c038fa5403e5696ac84e6149)
- [scmi_protocol_attributes_get](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gac6afb98180e88ade7d235a96e72b7ca6)
- [scmi_protocol_message_attributes_get](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#ga0f5d5c4382c41a507b21741e88cbcac0)
- [scmi_protocol_version_negotiate](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gae58fdab329d4f0d2a4b16c6f2a668fe6)
- [scmi_read_message](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gae5326d8ffd8fc7ed76ba73a0aee95d49)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [util.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2util_8h.html)
- [scmi_message::hdr](../platform_security_model_reference/P037_scmi_message_结构体.md#a4b329136651a527d51310af82dc24795)
- [scmi_message::len](../platform_security_model_reference/P037_scmi_message_结构体.md#aad4f7713d97765414e21a4cb6ed4b01f)
- [scmi_message::content](../platform_security_model_reference/P037_scmi_message_结构体.md#ae868ec173129a6f81c895279e95bb52d)
- [scmi_protocol_events::num_events](../platform_security_model_reference/P048_scmi_protocol_events_结构体.md#a33fb7a3e095fb1ad5267080130277578)
- [scmi_protocol_events::cb](../platform_security_model_reference/P048_scmi_protocol_events_结构体.md#a5ea92cc3ee5da51882568cc464378a7b)
- [scmi_protocol_events::evts](../platform_security_model_reference/P048_scmi_protocol_events_结构体.md#ac04442b926499369d7c89d8aacf0da41)
- [scmi_protocol_version::major](../platform_security_model_reference/P049_scmi_protocol_version_结构体.md#a03bf7fd19968bd6e976c948d29f83326)
- [scmi_protocol_version::minor](../platform_security_model_reference/P049_scmi_protocol_version_结构体.md#a602f109457cb0e481a0446cb40f81fab)
- [scmi_protocol_version::raw](../platform_security_model_reference/P049_scmi_protocol_version_结构体.md#a978b1c6f10fd87e5f538e840e4e71470)
- [scmi_protocol::events](../platform_security_model_reference/P047_scmi_protocol_结构体.md#a1b414028a899b5bef9c4df38352c5928)
- [scmi_protocol::rx](../platform_security_model_reference/P047_scmi_protocol_结构体.md#a4580aabc67a32be7dc9e914dd863a90b)
- [scmi_protocol::version](../platform_security_model_reference/P047_scmi_protocol_结构体.md#a809979e1c761c8486d62a4af6a21b4ad)
- [scmi_protocol::transport](../platform_security_model_reference/P047_scmi_protocol_结构体.md#a9081097c7aa12c407ec1d837c541d666)
- [scmi_protocol::tx](../platform_security_model_reference/P047_scmi_protocol_结构体.md#aa2a78f57d21a573c6091fba89a757a52)
- [scmi_protocol::data](../platform_security_model_reference/P047_scmi_protocol_结构体.md#ad6c1e08eebc96ff76ae656510d04a9d5)
- [scmi_protocol::id](../platform_security_model_reference/P047_scmi_protocol_结构体.md#ae2c2026eeaad8c5bf73be885fdd6315c)

---

[上一章](P155_pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P157_devicetree.h_源码浏览.md)
