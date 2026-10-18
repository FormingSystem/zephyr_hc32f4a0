---
id: learning.zephyr-docs.api-source-supplement-reference.page-43
title: mipi_dsi.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mipi__dsi_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第43章\_mipi\_dsi.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mipi__dsi_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mipi__dsi_8h.html)。

## 43.1\_原始可见代码（Source Code）

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
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="foldopen00035"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00085"></a>
<a id="foldopen00087"></a>
<a id="l00087"></a>
<a id="l00089"></a>
<a id="l00091"></a>
<a id="l00093"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="foldopen00105"></a>
<a id="l00105"></a>
<a id="l00107"></a>
<a id="l00109"></a>
<a id="l00111"></a>
<a id="l00113"></a>
<a id="l00115"></a>
<a id="l00117"></a>
<a id="l00119"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00128"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="foldopen00153"></a>
<a id="l00153"></a>
<a id="l00155"></a>
<a id="l00157"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00165"></a>
<a id="foldopen00175"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="foldopen00191"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="foldopen00265"></a>
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
<a id="l00285"></a>
<a id="l00286"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="adt-bindings_2mipi__dsi_2mipi__dsi_8h_html"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__ft8xx__reference__api_html_gacde1ca3945cbe6c828f65051c5c3a615"></a>
<a id="agroup__mipi__dsi__interface__backend_html_ga9abb63e5c7cdb7597376a237a420c2b5"></a>
<a id="agroup__mipi__dsi__interface__backend_html_ga9ebc67e63c629c75ff61fa220a2787a0"></a>
<a id="agroup__mipi__dsi__interface__backend_html_gaf5e12800d2a80e8a78da16cb5a71b008"></a>
<a id="agroup__mipi__dsi__interface_html_ga121633e8e379e7d1ebd749328f2014fd"></a>
<a id="agroup__mipi__dsi__interface_html_ga18689fac223fddc10b23b6bc6712944e"></a>
<a id="agroup__mipi__dsi__interface_html_ga5442f45c7c827d1dd8c3fa21da49c560"></a>
<a id="agroup__mipi__dsi__interface_html_ga7b5f52bcd51821bf120c5ac67b4c2fa5"></a>
<a id="agroup__mipi__dsi__interface_html_gace5bb52f483634baa185f46ac61efb71"></a>
<a id="agroup__mipi__dsi__interface_html_gace728ac82d30e15868298facd6df0228"></a>
<a id="agroup__mipi__dsi__interface_html_gad0f324e32191469bc0d24ba203286237"></a>
<a id="agroup__system__errno_html_ga43785b9969e0bd1af532dbde06c5540b"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html_a5c5d83d87790efd59ea916c2b99f9118"></a>
<a id="amipi__display_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructmipi__dsi__device_html"></a>
<a id="astructmipi__dsi__device_html_a729dd69843ee3eaf6bd5cbd2e725fdea"></a>
<a id="astructmipi__dsi__device_html_ae2e6fddb1651a71c1b969ecec295e1c0"></a>
<a id="astructmipi__dsi__device_html_af22eab1f95d8865fe7a67e49d6e36f8c"></a>
<a id="astructmipi__dsi__device_html_af9ec42cd1fcb16cf63060b0097180f3f"></a>
<a id="astructmipi__dsi__driver__api_html"></a>
<a id="astructmipi__dsi__driver__api_html_a246757a8c84029b7c2f75962558dd4dd"></a>
<a id="astructmipi__dsi__driver__api_html_a264e060eb462dc4b125cfbb1480cb2fd"></a>
<a id="astructmipi__dsi__driver__api_html_af8d27427074067a34938600d58c53df4"></a>
<a id="astructmipi__dsi__msg_html"></a>
<a id="astructmipi__dsi__msg_html_a45ee5101f773a600e116d41a247cdcf4"></a>
<a id="astructmipi__dsi__msg_html_a4cb0756c8cffa6acc10fee77ba6d4b17"></a>
<a id="astructmipi__dsi__msg_html_a73e62f4c7e45f0553fd0deeec06356a2"></a>
<a id="astructmipi__dsi__msg_html_a92dc0767c36f31cb23207a0581d3355f"></a>
<a id="astructmipi__dsi__msg_html_a9bc57ad1617fec4bd42560c6133fd774"></a>
<a id="astructmipi__dsi__msg_html_aa21b5be5cdfac9411601c83f72e58405"></a>
<a id="astructmipi__dsi__msg_html_ab17fda1dbb330bc8e66597ef816f413f"></a>
<a id="astructmipi__dsi__msg_html_ac93016853da47dc07094e7fe44e4625f"></a>
<a id="astructmipi__dsi__timings_html"></a>
<a id="astructmipi__dsi__timings_html_a3a91e874a7da6c37bf9b06944a3d658a"></a>
<a id="astructmipi__dsi__timings_html_a535e0177862b753ef9f4af011ed483a4"></a>
<a id="astructmipi__dsi__timings_html_a58f985d9c43cd149959dad7f12fcff8e"></a>
<a id="astructmipi__dsi__timings_html_ac44c32c7d150ddd4b327308196169578"></a>
<a id="astructmipi__dsi__timings_html_acc8077892efa4977fd667680d63f5c7c"></a>
<a id="astructmipi__dsi__timings_html_ad1b00493166d0276eb66d73be4b6968d"></a>
<a id="astructmipi__dsi__timings_html_afb4451d7767a911ea6a92a9fbba5e935"></a>
<a id="astructmipi__dsi__timings_html_afff80261d02253b76a872ee805a4cd46"></a>

```c
/*
 * Copyright (c) 2020 Teslabs Engineering S.L.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_MIPI_DSI_H_
#define ZEPHYR_INCLUDE_DRIVERS_MIPI_DSI_H_

#include <errno.h>
#include <sys/types.h>
#include <zephyr/device.h>
#include <zephyr/display/mipi_display.h>
#include <zephyr/dt-bindings/mipi_dsi/mipi_dsi.h>

#ifdef __cplusplus
extern "C" {
#endif

struct mipi_dsi_timings {
        uint32_t hactive;
        uint32_t hfp;
        uint32_t hbp;
        uint32_t hsync;
        uint32_t vactive;
        uint32_t vfp;
        uint32_t vbp;
        uint32_t vsync;
};


#define MIPI_DSI_MODE_VIDEO             BIT(0)
#define MIPI_DSI_MODE_VIDEO_BURST       BIT(1)
#define MIPI_DSI_MODE_VIDEO_SYNC_PULSE  BIT(2)
#define MIPI_DSI_MODE_VIDEO_AUTO_VERT   BIT(3)
#define MIPI_DSI_MODE_VIDEO_HSE         BIT(4)
#define MIPI_DSI_MODE_VIDEO_HFP         BIT(5)
#define MIPI_DSI_MODE_VIDEO_HBP         BIT(6)
#define MIPI_DSI_MODE_VIDEO_HSA         BIT(7)
#define MIPI_DSI_MODE_VSYNC_FLUSH       BIT(8)
#define MIPI_DSI_MODE_EOT_PACKET        BIT(9)
#define MIPI_DSI_CLOCK_NON_CONTINUOUS   BIT(10)
#define MIPI_DSI_MODE_LPM               BIT(11)


struct mipi_dsi_device {
        uint8_t data_lanes;
        struct mipi_dsi_timings timings;
        uint32_t pixfmt;
        uint32_t mode_flags;
};

/*
 * Per message flag to indicate the message must be sent
 * using Low Power Mode instead of controller default.
 */
#define MIPI_DSI_MSG_USE_LPM BIT(0x0)

struct mipi_dsi_msg {
        uint8_t type;
        uint16_t flags;
        uint8_t cmd;
        size_t tx_len;
        const void *tx_buf;
        size_t rx_len;
        void *rx_buf;
        void *user_data;
};


typedef int (*mipi_dsi_api_attach_t)(const struct device *dev, uint8_t channel,
                                     const struct mipi_dsi_device *mdev);

typedef ssize_t (*mipi_dsi_api_transfer_t)(const struct device *dev, uint8_t channel,
                                           struct mipi_dsi_msg *msg);

typedef int (*mipi_dsi_api_detach_t)(const struct device *dev, uint8_t channel,
                                     const struct mipi_dsi_device *mdev);

__subsystem struct mipi_dsi_driver_api {
        mipi_dsi_api_attach_t attach;
        mipi_dsi_api_transfer_t transfer;
        mipi_dsi_api_detach_t detach;
};


static inline int mipi_dsi_attach(const struct device *dev,
                                  uint8_t channel,
                                  const struct mipi_dsi_device *mdev)
{
        return DEVICE_API_GET(mipi_dsi, dev)->attach(dev, channel, mdev);
}

static inline ssize_t mipi_dsi_transfer(const struct device *dev,
                                        uint8_t channel,
                                        struct mipi_dsi_msg *msg)
{
        return DEVICE_API_GET(mipi_dsi, dev)->transfer(dev, channel, msg);
}

ssize_t mipi_dsi_generic_read(const struct device *dev, uint8_t channel,
                              const void *params, size_t nparams,
                              void *buf, size_t len);

ssize_t mipi_dsi_generic_write(const struct device *dev, uint8_t channel,
                               const void *buf, size_t len);

ssize_t mipi_dsi_dcs_read(const struct device *dev, uint8_t channel,
                          uint8_t cmd, void *buf, size_t len);

ssize_t mipi_dsi_dcs_write(const struct device *dev, uint8_t channel,
                           uint8_t cmd, const void *buf, size_t len);


static inline int mipi_dsi_detach(const struct device *dev,
                                  uint8_t channel,
                                  const struct mipi_dsi_device *mdev)
{
        const struct mipi_dsi_driver_api *api = DEVICE_API_GET(mipi_dsi, dev);

        if (api->detach == NULL) {
                return -ENOSYS;
        }

        return api->detach(dev, channel, mdev);
}

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DRIVERS_MIPI_DSI_H_ */
```

## 43.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2020 Teslabs Engineering S.L.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 98 行

逐消息标志（Per message flag），指示该消息必须使用低功耗模式（Low Power Mode）发送，而非采用控制器默认模式。

### 注释 3：原第 286 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_MIPI_DSI_H_`。

## 43.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mipi__dsi_8h.html)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [sys/types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/display/mipi_display.h](https://docs.zephyrproject.org/latest/doxygen/html/mipi__display_8h.html)
- [zephyr/dt-bindings/mipi_dsi/mipi_dsi.h](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2mipi__dsi_2mipi__dsi_8h.html)
- [mipi_dsi_timings](../hardware/P248_MIPI显示串行时序.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [hactive](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__timings.html#a3a91e874a7da6c37bf9b06944a3d658a)
- [hfp](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__timings.html#ad1b00493166d0276eb66d73be4b6968d)
- [hbp](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__timings.html#afb4451d7767a911ea6a92a9fbba5e935)
- [hsync](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__timings.html#a58f985d9c43cd149959dad7f12fcff8e)
- [vactive](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__timings.html#acc8077892efa4977fd667680d63f5c7c)
- [vfp](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__timings.html#ac44c32c7d150ddd4b327308196169578)
- [vbp](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__timings.html#afff80261d02253b76a872ee805a4cd46)
- [vsync](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__timings.html#a535e0177862b753ef9f4af011ed483a4)
- [mipi_dsi_device](../hardware/P249_MIPI显示串行设备.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [data_lanes](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__device.html#ae2e6fddb1651a71c1b969ecec295e1c0)
- [timings](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__device.html#af9ec42cd1fcb16cf63060b0097180f3f)
- [pixfmt](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__device.html#a729dd69843ee3eaf6bd5cbd2e725fdea)
- [mode_flags](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__device.html#af22eab1f95d8865fe7a67e49d6e36f8c)
- [mipi_dsi_msg](../hardware/P250_MIPI显示串行消息.md)
- [type](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__msg.html#a92dc0767c36f31cb23207a0581d3355f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__msg.html#ac93016853da47dc07094e7fe44e4625f)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__msg.html#a45ee5101f773a600e116d41a247cdcf4)
- [tx_len](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__msg.html#a4cb0756c8cffa6acc10fee77ba6d4b17)
- [tx_buf](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__msg.html#a73e62f4c7e45f0553fd0deeec06356a2)
- [rx_len](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__msg.html#ab17fda1dbb330bc8e66597ef816f413f)
- [rx_buf](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__msg.html#aa21b5be5cdfac9411601c83f72e58405)
- [user_data](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__msg.html#a9bc57ad1617fec4bd42560c6133fd774)
- [mipi_dsi_api_attach_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface__backend.html#ga9abb63e5c7cdb7597376a237a420c2b5)
- [device](../device_reference/P002_设备对象结构.md)
- [ssize_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a5c5d83d87790efd59ea916c2b99f9118)
- [mipi_dsi_api_transfer_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface__backend.html#ga9ebc67e63c629c75ff61fa220a2787a0)
- [mipi_dsi_api_detach_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface__backend.html#gaf5e12800d2a80e8a78da16cb5a71b008)
- [mipi_dsi_driver_api](../hardware/P254_MIPI显示串行函数表.md)
- [attach](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__driver__api.html#a246757a8c84029b7c2f75962558dd4dd)
- [transfer](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__driver__api.html#af8d27427074067a34938600d58c53df4)
- [detach](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__driver__api.html#a264e060eb462dc4b125cfbb1480cb2fd)
- [mipi_dsi_attach](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#ga18689fac223fddc10b23b6bc6712944e)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [mipi_dsi_transfer](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#gace5bb52f483634baa185f46ac61efb71)
- [mipi_dsi_generic_read](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#ga121633e8e379e7d1ebd749328f2014fd)
- [mipi_dsi_generic_write](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#ga5442f45c7c827d1dd8c3fa21da49c560)
- [mipi_dsi_dcs_read](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#ga7b5f52bcd51821bf120c5ac67b4c2fa5)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)
- [mipi_dsi_dcs_write](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#gad0f324e32191469bc0d24ba203286237)
- [mipi_dsi_detach](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#gace728ac82d30e15868298facd6df0228)
- [ENOSYS](../error_reference/P003_系统错误号公共接口.md#ga43785b9969e0bd1af532dbde06c5540b)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [mipi_dsi.h](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2mipi__dsi_2mipi__dsi_8h.html)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)
- [mipi_display.h](https://docs.zephyrproject.org/latest/doxygen/html/mipi__display_8h.html)
- [mipi_dsi_device::pixfmt](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__device.html#a729dd69843ee3eaf6bd5cbd2e725fdea)
- [mipi_dsi_device::data_lanes](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__device.html#ae2e6fddb1651a71c1b969ecec295e1c0)
- [mipi_dsi_device::mode_flags](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__device.html#af22eab1f95d8865fe7a67e49d6e36f8c)
- [mipi_dsi_device::timings](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__device.html#af9ec42cd1fcb16cf63060b0097180f3f)
- [mipi_dsi_driver_api::attach](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__driver__api.html#a246757a8c84029b7c2f75962558dd4dd)
- [mipi_dsi_driver_api::detach](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__driver__api.html#a264e060eb462dc4b125cfbb1480cb2fd)
- [mipi_dsi_driver_api::transfer](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__driver__api.html#af8d27427074067a34938600d58c53df4)
- [mipi_dsi_msg::cmd](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__msg.html#a45ee5101f773a600e116d41a247cdcf4)
- [mipi_dsi_msg::tx_len](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__msg.html#a4cb0756c8cffa6acc10fee77ba6d4b17)
- [mipi_dsi_msg::tx_buf](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__msg.html#a73e62f4c7e45f0553fd0deeec06356a2)
- [mipi_dsi_msg::type](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__msg.html#a92dc0767c36f31cb23207a0581d3355f)
- [mipi_dsi_msg::user_data](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__msg.html#a9bc57ad1617fec4bd42560c6133fd774)
- [mipi_dsi_msg::rx_buf](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__msg.html#aa21b5be5cdfac9411601c83f72e58405)
- [mipi_dsi_msg::rx_len](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__msg.html#ab17fda1dbb330bc8e66597ef816f413f)
- [mipi_dsi_msg::flags](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__msg.html#ac93016853da47dc07094e7fe44e4625f)
- [mipi_dsi_timings::hactive](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__timings.html#a3a91e874a7da6c37bf9b06944a3d658a)
- [mipi_dsi_timings::vsync](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__timings.html#a535e0177862b753ef9f4af011ed483a4)
- [mipi_dsi_timings::hsync](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__timings.html#a58f985d9c43cd149959dad7f12fcff8e)
- [mipi_dsi_timings::vfp](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__timings.html#ac44c32c7d150ddd4b327308196169578)
- [mipi_dsi_timings::vactive](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__timings.html#acc8077892efa4977fd667680d63f5c7c)
- [mipi_dsi_timings::hfp](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__timings.html#ad1b00493166d0276eb66d73be4b6968d)
- [mipi_dsi_timings::hbp](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__timings.html#afb4451d7767a911ea6a92a9fbba5e935)
- [mipi_dsi_timings::vbp](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__timings.html#afff80261d02253b76a872ee805a4cd46)

---

[上一章](P042_led.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P044_mcp9600.h_源码浏览.md)
