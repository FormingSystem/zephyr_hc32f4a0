---
id: learning.zephyr-docs.api-source-supplement-reference.page-237
title: usb_hid.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/usb__hid_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第237章\_usb\_hid.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/usb__hid_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/usb__hid_8h.html)。

## 237.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
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
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="foldopen00047"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00141"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="agroup__usb__hid__device__api_html_ga04ec088255198d1597df8d70db6257ee"></a>
<a id="agroup__usb__hid__device__api_html_ga61b4facfbfb729159135f5c7534ca593"></a>
<a id="agroup__usb__hid__device__api_html_ga7d1b97dd70c25c816a2c78447be13c84"></a>
<a id="agroup__usb__hid__device__api_html_ga88c23fc42f45f4ac05d9b2c1f6d7ec9b"></a>
<a id="agroup__usb__hid__device__api_html_ga8b08b633472ceb1323f09ef81176520f"></a>
<a id="agroup__usb__hid__device__api_html_ga9d82d48c9c6c94ad90e01f44c1f0e72b"></a>
<a id="agroup__usb__hid__device__api_html_gae3d308c55f5594cc0c926b52aaa28fc7"></a>
<a id="agroup__usb__hid__device__api_html_gaed433e24f8487d4e451d9f9daa08c5b0"></a>
<a id="agroup__usb__hid__device__api_html_gafb6073889bf17eb6a93bb8f182cd3f79"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructhid__ops_html"></a>
<a id="astructhid__ops_html_a1acc7f77f6896d2925e63402f1b9ffdd"></a>
<a id="astructhid__ops_html_a42f454cc1ea1e7ae75e6fa4073111f48"></a>
<a id="astructhid__ops_html_a4ec029d8a0bc2acb1dd89a4ccdc4d652"></a>
<a id="astructhid__ops_html_a5ab9c3bbb1d42b7557682ce4f9fc5de5"></a>
<a id="astructhid__ops_html_acc04ebec1deb335ef60bd3a01c6058d6"></a>
<a id="astructhid__ops_html_af1eda81d93e935f9560a26344076f65e"></a>
<a id="astructusb__setup__packet_html"></a>
<a id="ausb_2class_2hid_8h_html"></a>
<a id="ausb__ch9_8h_html"></a>

```c
/*
 * Copyright (c) 2018 Intel Corporation
 * Copyright (c) 2018,2021 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_USB_HID_CLASS_DEVICE_H_
#define ZEPHYR_INCLUDE_USB_HID_CLASS_DEVICE_H_

#include <zephyr/usb/class/hid.h>
#include <zephyr/usb/usb_ch9.h>

#ifdef __cplusplus
extern "C" {
#endif



typedef int (*hid_cb_t)(const struct device *dev,
                        struct usb_setup_packet *setup, int32_t *len,
                        uint8_t **data);
typedef void (*hid_int_ready_callback)(const struct device *dev);
typedef void (*hid_protocol_cb_t)(const struct device *dev, uint8_t protocol);
typedef void (*hid_idle_cb_t)(const struct device *dev, uint16_t report_id);

struct hid_ops {
        hid_cb_t get_report;
        hid_cb_t set_report;
        hid_protocol_cb_t protocol_change;
        hid_idle_cb_t on_idle;
        /*
         * int_in_ready is an optional callback that is called when
         * the current interrupt IN transfer has completed.  This can
         * be used to wait for the endpoint to go idle or to trigger
         * the next transfer.
         */
        hid_int_ready_callback int_in_ready;
        hid_int_ready_callback int_out_ready;
};

__deprecated void usb_hid_register_device(const struct device *dev,
                             const uint8_t *desc,
                             size_t size,
                             const struct hid_ops *op);

__deprecated int hid_int_ep_write(const struct device *dev,
                     const uint8_t *data,
                     uint32_t data_len,
                     uint32_t *bytes_ret);

__deprecated int hid_int_ep_read(const struct device *dev,
                    uint8_t *data,
                    uint32_t max_data_len,
                    uint32_t *ret_bytes);

__deprecated int usb_hid_set_proto_code(const struct device *dev, uint8_t proto_code);

__deprecated int usb_hid_init(const struct device *dev);



#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_USB_HID_CLASS_DEVICE_H_ */
```

## 237.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2018 Intel Corporation。

版权（Copyright）：© 2018,2021 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 52 行

`int_in_ready` 是一个可选回调，在当前中断 IN 传输（Interrupt IN transfer）完成时调用。它可用于等待端点进入空闲状态，或触发下一次传输。

### 注释 3：原第 150 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_USB_HID_CLASS_DEVICE_H_`。

## 237.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/usb__hid_8h.html)
- [zephyr/usb/class/hid.h](https://docs.zephyrproject.org/latest/doxygen/html/usb_2class_2hid_8h.html)
- [zephyr/usb/usb_ch9.h](../usb/P172_USB标准请求与描述符常量.md)
- [hid_cb_t](../usb/P046_旧版HID设备接口API.md#ga04ec088255198d1597df8d70db6257ee)
- [device](../device_reference/P002_设备对象结构.md)
- [usb_setup_packet](../usb/P160_USB控制请求包.md)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [hid_int_ready_callback](../usb/P046_旧版HID设备接口API.md#gaed433e24f8487d4e451d9f9daa08c5b0)
- [hid_protocol_cb_t](../usb/P046_旧版HID设备接口API.md#gae3d308c55f5594cc0c926b52aaa28fc7)
- [hid_idle_cb_t](../usb/P046_旧版HID设备接口API.md#ga61b4facfbfb729159135f5c7534ca593)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [hid_ops](../usb/P047_旧版HID回调接口.md)
- [get_report](../usb/P047_旧版HID回调接口.md#a4ec029d8a0bc2acb1dd89a4ccdc4d652)
- [set_report](../usb/P047_旧版HID回调接口.md#a5ab9c3bbb1d42b7557682ce4f9fc5de5)
- [protocol_change](../usb/P047_旧版HID回调接口.md#acc04ebec1deb335ef60bd3a01c6058d6)
- [on_idle](../usb/P047_旧版HID回调接口.md#a1acc7f77f6896d2925e63402f1b9ffdd)
- [int_in_ready](../usb/P047_旧版HID回调接口.md#af1eda81d93e935f9560a26344076f65e)
- [int_out_ready](../usb/P047_旧版HID回调接口.md#a42f454cc1ea1e7ae75e6fa4073111f48)
- [usb_hid_register_device](../usb/P046_旧版HID设备接口API.md#ga8b08b633472ceb1323f09ef81176520f)
- [hid_int_ep_write](../usb/P046_旧版HID设备接口API.md#ga9d82d48c9c6c94ad90e01f44c1f0e72b)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [hid_int_ep_read](../usb/P046_旧版HID设备接口API.md#ga7d1b97dd70c25c816a2c78447be13c84)
- [usb_hid_set_proto_code](../usb/P046_旧版HID设备接口API.md#gafb6073889bf17eb6a93bb8f182cd3f79)
- [usb_hid_init](../usb/P046_旧版HID设备接口API.md#ga88c23fc42f45f4ac05d9b2c1f6d7ec9b)
- [hid_ops::on_idle](../usb/P047_旧版HID回调接口.md#a1acc7f77f6896d2925e63402f1b9ffdd)
- [hid_ops::int_out_ready](../usb/P047_旧版HID回调接口.md#a42f454cc1ea1e7ae75e6fa4073111f48)
- [hid_ops::get_report](../usb/P047_旧版HID回调接口.md#a4ec029d8a0bc2acb1dd89a4ccdc4d652)
- [hid_ops::set_report](../usb/P047_旧版HID回调接口.md#a5ab9c3bbb1d42b7557682ce4f9fc5de5)
- [hid_ops::protocol_change](../usb/P047_旧版HID回调接口.md#acc04ebec1deb335ef60bd3a01c6058d6)
- [hid_ops::int_in_ready](../usb/P047_旧版HID回调接口.md#af1eda81d93e935f9560a26344076f65e)
- [hid.h](https://docs.zephyrproject.org/latest/doxygen/html/usb_2class_2hid_8h.html)
- [usb_ch9.h](../usb/P172_USB标准请求与描述符常量.md)

---

[上一章](P236_usb_dc.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P238_usbc_ppc.h_源码浏览.md)
