---
id: learning.zephyr-docs.api-source-network-reference.page-4
title: edac.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/edac_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_edac.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/edac_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/edac_8h.html)。

## 4.1\_原始可见代码（Source Code）

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
<a id="l00032"></a>
<a id="foldopen00036"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
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
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00084"></a>
<a id="l00091"></a>
<a id="foldopen00103"></a>
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
<a id="foldopen00126"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="foldopen00150"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="foldopen00171"></a>
<a id="l00171"></a>
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
<a id="foldopen00194"></a>
<a id="l00194"></a>
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
<a id="foldopen00217"></a>
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
<a id="foldopen00239"></a>
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
<a id="l00251"></a>
<a id="l00258"></a>
<a id="foldopen00270"></a>
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
<a id="foldopen00292"></a>
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
<a id="foldopen00314"></a>
<a id="l00314"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="foldopen00336"></a>
<a id="l00336"></a>
<a id="l00337"></a>
<a id="l00338"></a>
<a id="l00339"></a>
<a id="l00340"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="l00343"></a>
<a id="l00344"></a>
<a id="l00345"></a>
<a id="l00346"></a>
<a id="foldopen00355"></a>
<a id="l00355"></a>
<a id="l00356"></a>
<a id="l00357"></a>
<a id="l00358"></a>
<a id="l00359"></a>
<a id="l00360"></a>
<a id="l00361"></a>
<a id="l00362"></a>
<a id="l00363"></a>
<a id="l00364"></a>
<a id="l00365"></a>
<a id="foldopen00374"></a>
<a id="l00374"></a>
<a id="l00375"></a>
<a id="l00376"></a>
<a id="l00377"></a>
<a id="l00378"></a>
<a id="l00379"></a>
<a id="l00380"></a>
<a id="l00381"></a>
<a id="l00382"></a>
<a id="l00383"></a>
<a id="l00384"></a>
<a id="foldopen00396"></a>
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
<a id="l00408"></a>
<a id="l00410"></a>
<a id="l00412"></a>
<a id="l00413"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__edac__interface_html_ga2b0ea084501faf52aeec5af33a1ca97b"></a>
<a id="agroup__edac__interface_html_ga2def500f72a06271d9a10243bfdf6527"></a>
<a id="agroup__edac__interface_html_ga37e097d550f91072b890d6c2d4b215fa"></a>
<a id="agroup__edac__interface_html_ga3eb3da4d056d8e6167083301eb1276d6"></a>
<a id="agroup__edac__interface_html_ga905539bb96ff8c9f6f6a9fde6b3928e2"></a>
<a id="agroup__edac__interface_html_ga9817f47eeaf532e3789816e412eb5077"></a>
<a id="agroup__edac__interface_html_ga9ed608245ba68aee6b235752a87a5c39"></a>
<a id="agroup__edac__interface_html_gaa6cba09e19de241ed045387c85cc3f1c"></a>
<a id="agroup__edac__interface_html_gaa8c798b60b3b99ae6b8f8358253d1385"></a>
<a id="agroup__edac__interface_html_gab60aa37ba86e2038fe979481cc6134c2"></a>
<a id="agroup__edac__interface_html_gad058d74c811e77b00730e25f2060cce5"></a>
<a id="agroup__edac__interface_html_gaea2915b6c3c4eef2c94c6f60e788dcfe"></a>
<a id="agroup__edac__interface_html_gaec79969648e56e98031d46abe73c2b82"></a>
<a id="agroup__edac__interface_html_gaf02830c2e621e73a7c4add38a92f6d7c"></a>
<a id="agroup__edac__interface_html_gafb0cbc5082e88250a1e5955dd7d1770c"></a>
<a id="agroup__edac__interface_html_gga3eb3da4d056d8e6167083301eb1276d6a5b03fd27f37f01171e50c2997bc29a2f"></a>
<a id="agroup__edac__interface_html_gga3eb3da4d056d8e6167083301eb1276d6a941e09125e6040d7114ee17328fd4b02"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="agroup__system__errno_html_ga43785b9969e0bd1af532dbde06c5540b"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astructdevice_html"></a>
<a id="astructdevice_html_a27573cbd10ee145f8bb1396242b27a3e"></a>

```c
/*
 * Copyright (c) 2020 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_EDAC_H_
#define ZEPHYR_INCLUDE_DRIVERS_EDAC_H_

#include <errno.h>

#include <sys/types.h>


enum edac_error_type {
        EDAC_ERROR_TYPE_DRAM_COR = BIT(0),
        EDAC_ERROR_TYPE_DRAM_UC = BIT(1)
};


typedef void (*edac_notify_callback_f)(const struct device *dev, void *data);

__subsystem struct edac_driver_api {
        /* Error Injection API is disabled by default */
        int (*inject_set_param1)(const struct device *dev, uint64_t value);
        int (*inject_get_param1)(const struct device *dev, uint64_t *value);
        int (*inject_set_param2)(const struct device *dev, uint64_t value);
        int (*inject_get_param2)(const struct device *dev, uint64_t *value);
        int (*inject_set_error_type)(const struct device *dev, uint32_t value);
        int (*inject_get_error_type)(const struct device *dev, uint32_t *value);
        int (*inject_error_trigger)(const struct device *dev);

        /* Error Logging  API */
        int (*ecc_error_log_get)(const struct device *dev, uint64_t *value);
        int (*ecc_error_log_clear)(const struct device *dev);
        int (*parity_error_log_get)(const struct device *dev, uint64_t *value);
        int (*parity_error_log_clear)(const struct device *dev);

        /* Error stats API */
        int (*errors_cor_get)(const struct device *dev);
        int (*errors_uc_get)(const struct device *dev);

        /* Notification callback API */
        int (*notify_cb_set)(const struct device *dev,
                             edac_notify_callback_f cb);
};



static inline int edac_inject_set_param1(const struct device *dev,
                                         uint64_t value)
{
        const struct edac_driver_api *api = DEVICE_API_GET(edac, dev);

        if (api->inject_set_param1 == NULL) {
                return -ENOSYS;
        }

        return api->inject_set_param1(dev, value);
}

static inline int edac_inject_get_param1(const struct device *dev,
                                         uint64_t *value)
{
        const struct edac_driver_api *api = DEVICE_API_GET(edac, dev);

        if (api->inject_get_param1 == NULL) {
                return -ENOSYS;
        }

        return api->inject_get_param1(dev, value);

}

static inline int edac_inject_set_param2(const struct device *dev,
                                         uint64_t value)
{
        const struct edac_driver_api *api = DEVICE_API_GET(edac, dev);

        if (api->inject_set_param2 == NULL) {
                return -ENOSYS;
        }

        return api->inject_set_param2(dev, value);
}

static inline int edac_inject_get_param2(const struct device *dev,
                                         uint64_t *value)
{
        const struct edac_driver_api *api = DEVICE_API_GET(edac, dev);

        if (api->inject_get_param2 == NULL) {
                return -ENOSYS;
        }

        return api->inject_get_param2(dev, value);
}

static inline int edac_inject_set_error_type(const struct device *dev,
                                             uint32_t error_type)
{
        const struct edac_driver_api *api = DEVICE_API_GET(edac, dev);

        if (api->inject_set_error_type == NULL) {
                return -ENOSYS;
        }

        return api->inject_set_error_type(dev, error_type);
}

static inline int edac_inject_get_error_type(const struct device *dev,
                                             uint32_t *error_type)
{
        const struct edac_driver_api *api = DEVICE_API_GET(edac, dev);

        if (api->inject_get_error_type == NULL) {
                return -ENOSYS;
        }

        return api->inject_get_error_type(dev, error_type);
}

static inline int edac_inject_error_trigger(const struct device *dev)
{
        const struct edac_driver_api *api = DEVICE_API_GET(edac, dev);

        if (api->inject_error_trigger == NULL) {
                return -ENOSYS;
        }

        return api->inject_error_trigger(dev);
}
 /* End of EDAC Optional Interfaces */


static inline int edac_ecc_error_log_get(const struct device *dev,
                                         uint64_t *value)
{
        const struct edac_driver_api *api = DEVICE_API_GET(edac, dev);

        if (api->ecc_error_log_get == NULL) {
                return -ENOSYS;
        }

        return api->ecc_error_log_get(dev, value);
}

static inline int edac_ecc_error_log_clear(const struct device *dev)
{
        const struct edac_driver_api *api = DEVICE_API_GET(edac, dev);

        if (api->ecc_error_log_clear == NULL) {
                return -ENOSYS;
        }

        return api->ecc_error_log_clear(dev);
}

static inline int edac_parity_error_log_get(const struct device *dev,
                                            uint64_t *value)
{
        const struct edac_driver_api *api = DEVICE_API_GET(edac, dev);

        if (api->parity_error_log_get == NULL) {
                return -ENOSYS;
        }

        return api->parity_error_log_get(dev, value);
}

static inline int edac_parity_error_log_clear(const struct device *dev)
{
        const struct edac_driver_api *api = DEVICE_API_GET(edac, dev);

        if (api->parity_error_log_clear == NULL) {
                return -ENOSYS;
        }

        return api->parity_error_log_clear(dev);
}

static inline int edac_errors_cor_get(const struct device *dev)
{
        const struct edac_driver_api *api = DEVICE_API_GET(edac, dev);

        if (api->errors_cor_get == NULL) {
                return -ENOSYS;
        }

        return api->errors_cor_get(dev);
}

static inline int edac_errors_uc_get(const struct device *dev)
{
        const struct edac_driver_api *api = DEVICE_API_GET(edac, dev);

        if (api->errors_uc_get == NULL) {
                return -ENOSYS;
        }

        return api->errors_uc_get(dev);
}

static inline int edac_notify_callback_set(const struct device *dev,
                                           edac_notify_callback_f cb)
{
        const struct edac_driver_api *api = DEVICE_API_GET(edac, dev);

        if (api->notify_cb_set == NULL) {
                return -ENOSYS;
        }

        return api->notify_cb_set(dev, cb);
}

 /* End of EDAC Mandatory Interfaces */
 /* End of EDAC API */

#endif  /* ZEPHYR_INCLUDE_DRIVERS_EDAC_H_ */
```

## 4.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2020 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 57 行

错误注入 API（Error Injection API）默认禁用。

### 注释 3：原第 66 行

错误日志 API（Error Logging API）。

### 注释 4：原第 72 行

错误统计 API（Error Stats API）。

### 注释 5：原第 76 行

通知回调 API（Notification Callback API）。

### 注释 6：原第 249 行

错误检测与纠正可选接口（EDAC Optional Interfaces）结束。

### 注释 7：原第 408 行

错误检测与纠正必需接口（EDAC Mandatory Interfaces）结束。

### 注释 8：原第 410 行

错误检测与纠正 API（EDAC API）结束。

### 注释 9：原第 413 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_EDAC_H_`。

## 4.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/edac_8h.html)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [sys/types.h](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md)
- [edac_error_type](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html#ga3eb3da4d056d8e6167083301eb1276d6)
- [EDAC_ERROR_TYPE_DRAM_COR](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html#gga3eb3da4d056d8e6167083301eb1276d6a941e09125e6040d7114ee17328fd4b02)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [EDAC_ERROR_TYPE_DRAM_UC](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html#gga3eb3da4d056d8e6167083301eb1276d6a5b03fd27f37f01171e50c2997bc29a2f)
- [device](../device_reference/P002_设备对象结构.md)
- [data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [edac_inject_set_param1](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html#gad058d74c811e77b00730e25f2060cce5)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [ENOSYS](../error_reference/P003_系统错误号公共接口.md#ga43785b9969e0bd1af532dbde06c5540b)
- [edac_inject_get_param1](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html#ga9817f47eeaf532e3789816e412eb5077)
- [edac_inject_set_param2](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html#ga9ed608245ba68aee6b235752a87a5c39)
- [edac_inject_get_param2](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html#ga37e097d550f91072b890d6c2d4b215fa)
- [edac_inject_set_error_type](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html#ga2b0ea084501faf52aeec5af33a1ca97b)
- [edac_inject_get_error_type](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html#gafb0cbc5082e88250a1e5955dd7d1770c)
- [edac_inject_error_trigger](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html#gaf02830c2e621e73a7c4add38a92f6d7c)
- [edac_ecc_error_log_get](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html#ga905539bb96ff8c9f6f6a9fde6b3928e2)
- [edac_ecc_error_log_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html#gaa8c798b60b3b99ae6b8f8358253d1385)
- [edac_parity_error_log_get](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html#gaa6cba09e19de241ed045387c85cc3f1c)
- [edac_parity_error_log_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html#gab60aa37ba86e2038fe979481cc6134c2)
- [edac_errors_cor_get](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html#gaea2915b6c3c4eef2c94c6f60e788dcfe)
- [edac_errors_uc_get](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html#gaec79969648e56e98031d46abe73c2b82)
- [edac_notify_callback_set](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html#ga2def500f72a06271d9a10243bfdf6527)
- [types.h](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md)
- [device::data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)

---

[上一章](P003_cr.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P005_em32_clock.h_源码浏览.md)
