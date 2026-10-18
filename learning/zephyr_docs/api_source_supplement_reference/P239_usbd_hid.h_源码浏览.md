---
id: learning.zephyr-docs.api-source-supplement-reference.page-239
title: usbd_hid.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/usbd__hid_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第239章\_usbd\_hid.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/usbd__hid_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/usbd__hid_8h.html)。

## 239.1\_原始可见代码（Source Code）

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
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
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
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="foldopen00096"></a>
<a id="l00096"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__usbd__hid__device_html_ga547f99b1089a4d65a297faa5d6e8edd8"></a>
<a id="agroup__usbd__hid__device_html_gaa5d319acba8a671537f1ee6a2ea7559e"></a>
<a id="agroup__usbd__hid__device_html_gabb4502a7c3ab5d2400c039549577f4d0"></a>
<a id="agroup__usbd__hid__device_html_gac5b27822922030734341db4b41435cb6"></a>
<a id="agroup__usbd__hid__device_html_ggabfdd923d3dea1fc17d6c21f4ad7dab1da451c0c5bb29aa79f5ce554ac9a914acd"></a>
<a id="agroup__usbd__hid__device_html_ggabfdd923d3dea1fc17d6c21f4ad7dab1dac019f1ccb72d64b8ce9dc5c5d952f8a3"></a>
<a id="agroup__usbd__hid__device_html_ggabfdd923d3dea1fc17d6c21f4ad7dab1dadb047f4ed99575941ca9d857244f5aea"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructdevice_html_ab6d65f3402e67afb9810a8356b915071"></a>
<a id="astructhid__device__ops_html"></a>
<a id="astructhid__device__ops_html_a0043b6bf005785274de2b65f341cb588"></a>
<a id="astructhid__device__ops_html_a3632e4f1247bdd3395a3f470b75dca43"></a>
<a id="astructhid__device__ops_html_a48e03408d693d4d9d9dacf6513a36828"></a>
<a id="astructhid__device__ops_html_a8d96a142b963dd257b2dbb64df82181d"></a>
<a id="astructhid__device__ops_html_ac58785fc2a44be7c46e0c950fc09f0ac"></a>
<a id="astructhid__device__ops_html_ace79e5ef79606daf22b8f39794e9d19e"></a>
<a id="astructhid__device__ops_html_add555b9782b763d5b411909d07d952b8"></a>
<a id="astructhid__device__ops_html_ae9290b806b57c9595fad3ec0a65fdca2"></a>
<a id="astructhid__device__ops_html_aee855ba756e584cefa09ff4caba09c66"></a>
<a id="astructhid__device__ops_html_afd8c16e1256945bc15c70439051deb26"></a>
<a id="astructhid__device__ops_html_aff034989bee801c143384464eb6a5a9d"></a>
<a id="ausb_2class_2hid_8h_html"></a>

```c
/*
 * Copyright (c) 2023 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_USBD_HID_CLASS_DEVICE_H_
#define ZEPHYR_INCLUDE_USBD_HID_CLASS_DEVICE_H_

#include <stdint.h>
#include <zephyr/device.h>
#include <zephyr/usb/class/hid.h>

#ifdef __cplusplus
extern "C" {
#endif


/*
 * HID Device overview:
 *
 *         +---------------------+
 *         |                     |
 *         |                     |
 *         |     HID Device      |
 *         |  User "top half"    |
 *         |  of the device that +-------+
 *         |  deals with input   |       |
 *         |     sampling        |       |
 *         |                     |       |
 *         |                     |       |
 *         | ------------------- |       |
 *         |                     |       |
 *         |   HID Device user   |       |
 *         |      callbacks      |       |
 *         |      handlers       |       |
 *         +---------------------+       |
 *                    ^                  |  HID Device Driver API:
 *                    |                  |
 *  set_protocol()    |                  |  hid_device_register()
 *  get_report()      |                  |  hid_device_submit_report(
 *  ....              |                  |  ...
 *                    v                  |
 *         +---------------------+       |
 *         |                     |       |
 *         |      HID Device     |       |
 *         |     "bottom half"   |<------+
 *         |    USB HID class    |
 *         |    implementation   |
 *         |                     |
 *         |                     |
 *         +---------------------+
 *                    ^
 *                    v
 *          +--------------------+
 *          |                    |
 *          |     USB Device     |
 *          |       Support      |
 *          |                    |
 *          +--------------------+
 */

enum {
        HID_REPORT_TYPE_INPUT = 1,
        HID_REPORT_TYPE_OUTPUT,
        HID_REPORT_TYPE_FEATURE,
};

struct hid_device_ops {
        void (*iface_ready)(const struct device *dev, const bool ready);

        int (*get_report_size)(const struct device *dev,
                               const uint8_t type, const uint8_t id);

        int (*get_report)(const struct device *dev,
                          const uint8_t type, const uint8_t id,
                          const uint16_t len, uint8_t *const buf);

        int (*verify_set_report)(const struct device *dev,
                                 const uint8_t type, const uint8_t id,
                                 const uint16_t len);

        int (*set_report)(const struct device *dev,
                          const uint8_t type, const uint8_t id,
                          const uint16_t len, const uint8_t *const buf);

        void (*set_idle)(const struct device *dev,
                         const uint8_t id, const uint32_t duration);

        uint32_t (*get_idle)(const struct device *dev, const uint8_t id);

        void (*set_protocol)(const struct device *dev, const uint8_t proto);

        void (*input_report_done)(const struct device *dev,
                                  const uint8_t *const report);

        void (*output_report)(const struct device *dev, const uint16_t len,
                              const uint8_t *const buf);
        void (*sof)(const struct device *dev);
};

int hid_device_register(const struct device *dev,
                        const uint8_t *const rdesc, const uint16_t rsize,
                        const struct hid_device_ops *const ops);

int hid_device_submit_report(const struct device *dev,
                             const uint16_t size, const uint8_t *const report);

int hid_device_set_in_polling(const struct device *dev, const unsigned int period_us);

int hid_device_set_out_polling(const struct device *dev, const unsigned int period_us);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_USBD_HID_CLASS_DEVICE_H_ */
```

## 239.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 32 行

HID 设备概览（HID Device overview）。上方原始代码注释保留了完整字符图。图中各部分及连接关系如下：

- HID 设备的用户“上半部”（User top half）负责输入采样（Input sampling）。
- 同一用户侧还提供 HID 设备用户回调处理程序（User callbacks handlers）。USB HID 类通过 `set_protocol()`、`get_report()` 等接口与这些回调交互。
- HID 设备驱动 API（HID Device Driver API）包括 `hid_device_register()`、`hid_device_submit_report(...)` 等，将用户上半部连接到设备“下半部”（Bottom half）。
- HID 设备“下半部”是 USB HID 类实现（USB HID class implementation）。
- USB HID 类实现与 USB 设备支持层（USB Device Support）双向交互。

### 注释 3：原第 282 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_USBD_HID_CLASS_DEVICE_H_`。

## 239.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/usbd__hid_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/usb/class/hid.h](https://docs.zephyrproject.org/latest/doxygen/html/usb_2class_2hid_8h.html)
- [HID_REPORT_TYPE_INPUT](../usb/P042_新版HID设备API.md#ggabfdd923d3dea1fc17d6c21f4ad7dab1da451c0c5bb29aa79f5ce554ac9a914acd)
- [HID_REPORT_TYPE_OUTPUT](../usb/P042_新版HID设备API.md#ggabfdd923d3dea1fc17d6c21f4ad7dab1dac019f1ccb72d64b8ce9dc5c5d952f8a3)
- [HID_REPORT_TYPE_FEATURE](../usb/P042_新版HID设备API.md#ggabfdd923d3dea1fc17d6c21f4ad7dab1dadb047f4ed99575941ca9d857244f5aea)
- [hid_device_ops](../usb/P043_HID设备回调接口.md)
- [iface_ready](../usb/P043_HID设备回调接口.md#a8d96a142b963dd257b2dbb64df82181d)
- [device](../device_reference/P002_设备对象结构.md)
- [get_report_size](../usb/P043_HID设备回调接口.md#a3632e4f1247bdd3395a3f470b75dca43)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [get_report](../usb/P043_HID设备回调接口.md#aff034989bee801c143384464eb6a5a9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [verify_set_report](../usb/P043_HID设备回调接口.md#aee855ba756e584cefa09ff4caba09c66)
- [set_report](../usb/P043_HID设备回调接口.md#add555b9782b763d5b411909d07d952b8)
- [set_idle](../usb/P043_HID设备回调接口.md#a48e03408d693d4d9d9dacf6513a36828)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [get_idle](../usb/P043_HID设备回调接口.md#afd8c16e1256945bc15c70439051deb26)
- [set_protocol](../usb/P043_HID设备回调接口.md#ae9290b806b57c9595fad3ec0a65fdca2)
- [input_report_done](../usb/P043_HID设备回调接口.md#ace79e5ef79606daf22b8f39794e9d19e)
- [output_report](../usb/P043_HID设备回调接口.md#ac58785fc2a44be7c46e0c950fc09f0ac)
- [sof](../usb/P043_HID设备回调接口.md#a0043b6bf005785274de2b65f341cb588)
- [hid_device_register](../usb/P042_新版HID设备API.md#gabb4502a7c3ab5d2400c039549577f4d0)
- [ops](../device_reference/P002_设备对象结构.md#ab6d65f3402e67afb9810a8356b915071)
- [hid_device_submit_report](../usb/P042_新版HID设备API.md#ga547f99b1089a4d65a297faa5d6e8edd8)
- [hid_device_set_in_polling](../usb/P042_新版HID设备API.md#gaa5d319acba8a671537f1ee6a2ea7559e)
- [hid_device_set_out_polling](../usb/P042_新版HID设备API.md#gac5b27822922030734341db4b41435cb6)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [device::ops](../device_reference/P002_设备对象结构.md#ab6d65f3402e67afb9810a8356b915071)
- [hid_device_ops::sof](../usb/P043_HID设备回调接口.md#a0043b6bf005785274de2b65f341cb588)
- [hid_device_ops::get_report_size](../usb/P043_HID设备回调接口.md#a3632e4f1247bdd3395a3f470b75dca43)
- [hid_device_ops::set_idle](../usb/P043_HID设备回调接口.md#a48e03408d693d4d9d9dacf6513a36828)
- [hid_device_ops::iface_ready](../usb/P043_HID设备回调接口.md#a8d96a142b963dd257b2dbb64df82181d)
- [hid_device_ops::output_report](../usb/P043_HID设备回调接口.md#ac58785fc2a44be7c46e0c950fc09f0ac)
- [hid_device_ops::input_report_done](../usb/P043_HID设备回调接口.md#ace79e5ef79606daf22b8f39794e9d19e)
- [hid_device_ops::set_report](../usb/P043_HID设备回调接口.md#add555b9782b763d5b411909d07d952b8)
- [hid_device_ops::set_protocol](../usb/P043_HID设备回调接口.md#ae9290b806b57c9595fad3ec0a65fdca2)
- [hid_device_ops::verify_set_report](../usb/P043_HID设备回调接口.md#aee855ba756e584cefa09ff4caba09c66)
- [hid_device_ops::get_idle](../usb/P043_HID设备回调接口.md#afd8c16e1256945bc15c70439051deb26)
- [hid_device_ops::get_report](../usb/P043_HID设备回调接口.md#aff034989bee801c143384464eb6a5a9d)
- [hid.h](https://docs.zephyrproject.org/latest/doxygen/html/usb_2class_2hid_8h.html)

---

[上一章](P238_usbc_ppc.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P240_usbh.h_源码浏览.md)
