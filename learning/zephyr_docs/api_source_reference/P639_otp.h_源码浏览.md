---
id: learning.zephyr-docs.api-source-reference.page-639
title: otp.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/otp_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第639章\_otp.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/otp_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/otp_8h.html)。

## 639.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00037"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="foldopen00052"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00067"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="agroup__otp__interface__backend_html_ga2dd11aba59cbe417973d98503d67b343"></a>
<a id="agroup__otp__interface__backend_html_gae4eff2ba1959c2817f684a3306427e09"></a>
<a id="agroup__otp__interface_html_ga067683279ab5d0e9b5f32f83c6b12630"></a>
<a id="agroup__otp__interface_html_gacaba6f85fb9ba7c0683417b9a2a81a6a"></a>
<a id="agroup__system__errno_html_ga43785b9969e0bd1af532dbde06c5540b"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html_a98a5cc5f4a350bf5652565021a2f239f"></a>
<a id="astructdevice_html"></a>
<a id="astructdevice_html_a27573cbd10ee145f8bb1396242b27a3e"></a>
<a id="astructotp__driver__api_html"></a>
<a id="astructotp__driver__api_html_a5372b65914f5d9d02b7a1f9db3bcde5d"></a>
<a id="astructotp__driver__api_html_ac3bf2e91c385c713739e8be04ae0264d"></a>

```c
/*
 * Copyright (c) 2025 STMicroelectronics
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_OTP_H_
#define ZEPHYR_INCLUDE_DRIVERS_OTP_H_


#include <stddef.h>
#include <sys/types.h>
#include <zephyr/device.h>
#include <zephyr/types.h>

#ifdef __cplusplus
extern "C" {
#endif


typedef int (*otp_api_read)(const struct device *dev, off_t offset, void *data, size_t len);

typedef int (*otp_api_program)(const struct device *dev, off_t offset, const void *data,
                               size_t len);

__subsystem struct otp_driver_api {
        otp_api_read read;
#if defined(CONFIG_OTP_PROGRAM) || defined(__DOXYGEN__)
        otp_api_program program;
#endif
};


__syscall int otp_read(const struct device *dev, off_t offset, void *data, size_t len);

static inline int z_impl_otp_read(const struct device *dev, off_t offset, void *data, size_t len)
{
        return DEVICE_API_GET(otp, dev)->read(dev, offset, data, len);
}

#if defined(CONFIG_OTP_PROGRAM) || defined(__DOXYGEN__)
__syscall int otp_program(const struct device *dev, off_t offset, const void *data, size_t len);

static inline int z_impl_otp_program(const struct device *dev, off_t offset, const void *data,
                                      size_t len)
{
        const struct otp_driver_api *api = DEVICE_API_GET(otp, dev);

        if (api->program == NULL) {
                return -ENOSYS;
        }

        return api->program(dev, offset, data, len);
}
#endif

#ifdef __cplusplus
}
#endif


#include <zephyr/syscalls/otp.h>

#endif /* ZEPHYR_INCLUDE_DRIVERS_OTP_H_ */
```

## 639.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 STMicroelectronics。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 121 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_OTP_H_`。

## 639.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/otp_8h.html)
- [sys/types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [otp_api_read](https://docs.zephyrproject.org/latest/doxygen/html/group__otp__interface__backend.html#ga2dd11aba59cbe417973d98503d67b343)
- [device](../device_reference/P002_设备对象结构.md)
- [off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)
- [data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [otp_api_program](https://docs.zephyrproject.org/latest/doxygen/html/group__otp__interface__backend.html#gae4eff2ba1959c2817f684a3306427e09)
- [otp_driver_api](../platform_security_model_reference/P024_otp_driver_api_结构体.md)
- [read](../platform_security_model_reference/P024_otp_driver_api_结构体.md#a5372b65914f5d9d02b7a1f9db3bcde5d)
- [program](../platform_security_model_reference/P024_otp_driver_api_结构体.md#ac3bf2e91c385c713739e8be04ae0264d)
- [otp_read](https://docs.zephyrproject.org/latest/doxygen/html/group__otp__interface.html#ga067683279ab5d0e9b5f32f83c6b12630)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [otp_program](https://docs.zephyrproject.org/latest/doxygen/html/group__otp__interface.html#gacaba6f85fb9ba7c0683417b9a2a81a6a)
- [ENOSYS](../error_reference/P003_系统错误号公共接口.md#ga43785b9969e0bd1af532dbde06c5540b)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)
- [device::data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [otp_driver_api::read](../platform_security_model_reference/P024_otp_driver_api_结构体.md#a5372b65914f5d9d02b7a1f9db3bcde5d)
- [otp_driver_api::program](../platform_security_model_reference/P024_otp_driver_api_结构体.md#ac3bf2e91c385c713739e8be04ae0264d)

---

[上一章](P638_os_mgmt_client.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P640_packet.h_源码浏览.md)
