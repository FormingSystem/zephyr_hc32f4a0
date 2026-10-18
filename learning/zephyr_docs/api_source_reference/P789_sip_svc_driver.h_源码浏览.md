---
id: learning.zephyr-docs.api-source-reference.page-789
title: sip_svc_driver.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__driver_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第789章\_sip\_svc\_driver.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__driver_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__driver_8h.html)。

## 789.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="foldopen00092"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
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
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
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
<a id="l00170"></a>
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
<a id="l00183"></a>
<a id="l00192"></a>
<a id="l00193"></a>
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
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
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
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00295"></a>
<a id="l00309"></a>
<a id="l00310"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="l00313"></a>
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
<a id="l00326"></a>
<a id="l00327"></a>
<a id="l00334"></a>
<a id="l00335"></a>
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
<a id="l00347"></a>
<a id="l00348"></a>
<a id="l00349"></a>
<a id="l00350"></a>
<a id="l00351"></a>
<a id="l00352"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="akernel_8h_html"></a>
<a id="asip__svc__controller_8h_html"></a>
<a id="asip__svc__driver_8h_html_a095123f7aec80a3e51d75ef248990124"></a>
<a id="asip__svc__driver_8h_html_a0a0577249c2a9f470cd6ec0a60b455c8"></a>
<a id="asip__svc__driver_8h_html_a15714e3852882693de6c9c7f2229bcd1"></a>
<a id="asip__svc__driver_8h_html_a3510743d8cf114376b740f3d297c583f"></a>
<a id="asip__svc__driver_8h_html_a35145ddf422e8782b4ec37270b04d98c"></a>
<a id="asip__svc__driver_8h_html_a3cf78c760c6eae2091e92329e54b1a31"></a>
<a id="asip__svc__driver_8h_html_a54293f84f9bc86661f8a4bf717ad4754"></a>
<a id="asip__svc__driver_8h_html_a881e3794f9e29e12c925cb5dbd443420"></a>
<a id="asip__svc__driver_8h_html_a8df36a218cce4c0904c147d498c1322d"></a>
<a id="asip__svc__driver_8h_html_a926eeecea766b2131c03c57111a186f8"></a>
<a id="asip__svc__driver_8h_html_a9d61db0484e2aacce4515290ffb4450c"></a>
<a id="asip__svc__driver_8h_html_aa49a26b4b503e58d23fb5087ed701a0a"></a>
<a id="asip__svc__driver_8h_html_aa4e44eb2af080207821a60f8b3442886"></a>
<a id="asip__svc__driver_8h_html_ab32e31bdba00ff66303fab1b04cd0ebe"></a>
<a id="asip__svc__driver_8h_html_abb9ff6ec7dea6fc4e104db8cc5e7168b"></a>
<a id="asip__svc__driver_8h_html_ac5921c9cdc00604651696e1580f30797"></a>
<a id="asip__svc__driver_8h_html_ad0e52f49e7db8cf51ff8cf95e1283994"></a>
<a id="asip__svc__driver_8h_html_ae52dee0bbba688a73a9726dd4aa482d2"></a>
<a id="asip__svc__proto_8h_html"></a>
<a id="astdbool_8h_html_abb452686968e48b67397da5f97445f5b"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructdevice_html"></a>
<a id="astructsip__svc__request_html"></a>
<a id="astructsvc__driver__api_html"></a>
<a id="astructsvc__driver__api_html_a0ccdebec2a60d32a1767c5e47bc3ae25"></a>
<a id="astructsvc__driver__api_html_a1d94fdfb564caa84e3f18f2139ae4fe0"></a>
<a id="astructsvc__driver__api_html_a30a435265fa828d9fdfcc70664be0945"></a>
<a id="astructsvc__driver__api_html_a484b7c6ef4777a61e8f4f8e6778a7b45"></a>
<a id="astructsvc__driver__api_html_a5f02e921d2a038616fad9d8d6a052f6b"></a>
<a id="astructsvc__driver__api_html_a6435b703d30f462c1ec38e533a9c0817"></a>
<a id="astructsvc__driver__api_html_a79ac1f8410b7f0883ceb0a96823fbdf4"></a>
<a id="astructsvc__driver__api_html_a9f0a7711ef5ba2900d378c0a2805eaf4"></a>
<a id="astructsvc__driver__api_html_ae148bb010e4a0c2913e1c7425565316a"></a>

```c
/*
 * Copyright (c) 2023, Intel Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_SIP_SVC_DRIVER_H_
#define ZEPHYR_INCLUDE_SIP_SVC_DRIVER_H_

#include <zephyr/device.h>
#include <zephyr/kernel.h>
#include <zephyr/arch/arm64/arm-smccc.h>
#include <zephyr/drivers/sip_svc/sip_svc_proto.h>
#include <zephyr/sip_svc/sip_svc_controller.h>

#define SVC_CONDUIT_NAME_LENGTH (4)

typedef void (*sip_supervisory_call_t)(const struct device *dev, unsigned long function_id,
                                       unsigned long arg0, unsigned long arg1, unsigned long arg2,
                                       unsigned long arg3, unsigned long arg4, unsigned long arg5,
                                       unsigned long arg6, struct arm_smccc_res *res);

typedef bool (*sip_svc_plat_func_id_valid_t)(const struct device *dev, uint32_t command,
                                             uint32_t func_id);

typedef uint32_t (*sip_svc_plat_format_trans_id_t)(const struct device *dev, uint32_t client_idx,
                                                   uint32_t trans_idx);

typedef uint32_t (*sip_svc_plat_get_trans_idx_t)(const struct device *dev, uint32_t trans_id);

typedef void (*sip_svc_plat_update_trans_id_t)(const struct device *dev,
                                               struct sip_svc_request *request, uint32_t trans_id);

typedef void (*sip_svc_plat_free_async_memory_t)(const struct device *dev,
                                                 struct sip_svc_request *request);

typedef int (*sip_svc_plat_async_res_req_t)(const struct device *dev, unsigned long *a0,
                                            unsigned long *a1, unsigned long *a2, unsigned long *a3,
                                            unsigned long *a4, unsigned long *a5, unsigned long *a6,
                                            unsigned long *a7, char *buf, size_t size);

typedef int (*sip_svc_plat_async_res_res_t)(const struct device *dev, struct arm_smccc_res *res,
                                            char *buf, size_t *size, uint32_t *trans_id);

typedef uint32_t (*sip_svc_plat_get_error_code_t)(const struct device *dev,
                                                  struct arm_smccc_res *res);

__subsystem struct svc_driver_api {
        sip_supervisory_call_t sip_supervisory_call;
        sip_svc_plat_func_id_valid_t sip_svc_plat_func_id_valid;
        sip_svc_plat_format_trans_id_t sip_svc_plat_format_trans_id;
        sip_svc_plat_get_trans_idx_t sip_svc_plat_get_trans_idx;
        sip_svc_plat_update_trans_id_t sip_svc_plat_update_trans_id;
        sip_svc_plat_free_async_memory_t sip_svc_plat_free_async_memory;
        sip_svc_plat_async_res_req_t sip_svc_plat_async_res_req;
        sip_svc_plat_async_res_res_t sip_svc_plat_async_res_res;
        sip_svc_plat_get_error_code_t sip_svc_plat_get_error_code;
};

__syscall void sip_supervisory_call(const struct device *dev, unsigned long function_id,
                                    unsigned long arg0, unsigned long arg1, unsigned long arg2,
                                    unsigned long arg3, unsigned long arg4, unsigned long arg5,
                                    unsigned long arg6, struct arm_smccc_res *res);
static inline void z_impl_sip_supervisory_call(const struct device *dev, unsigned long function_id,
                                               unsigned long arg0, unsigned long arg1,
                                               unsigned long arg2, unsigned long arg3,
                                               unsigned long arg4, unsigned long arg5,
                                               unsigned long arg6, struct arm_smccc_res *res)
{
        __ASSERT(dev, "dev shouldn't be NULL");
        const struct svc_driver_api *api = DEVICE_API_GET(svc, dev);

        __ASSERT(api->sip_supervisory_call, "sip_supervisory_call shouldn't be NULL");
        __ASSERT(res, "response pointer shouldn't be NULL");

        api->sip_supervisory_call(dev, function_id, arg0, arg1, arg2, arg3, arg4, arg5, arg6, res);
}

__syscall bool sip_svc_plat_func_id_valid(const struct device *dev, uint32_t command,
                                          uint32_t func_id);
static inline bool z_impl_sip_svc_plat_func_id_valid(const struct device *dev, uint32_t command,
                                                     uint32_t func_id)
{
        __ASSERT(dev, "dev shouldn't be NULL");
        const struct svc_driver_api *api = DEVICE_API_GET(svc, dev);

        __ASSERT(api->sip_svc_plat_func_id_valid,
                 "sip_svc_plat_func_id_valid func shouldn't be NULL");

        return api->sip_svc_plat_func_id_valid(dev, command, func_id);
}

__syscall uint32_t sip_svc_plat_format_trans_id(const struct device *dev, uint32_t client_idx,
                                                uint32_t trans_idx);
static inline uint32_t z_impl_sip_svc_plat_format_trans_id(const struct device *dev,
                                                           uint32_t client_idx, uint32_t trans_idx)
{
        __ASSERT(dev, "dev shouldn't be NULL");
        const struct svc_driver_api *api = DEVICE_API_GET(svc, dev);

        __ASSERT(api->sip_svc_plat_format_trans_id,
                 "sip_svc_plat_format_trans_id func shouldn't be NULL");

        return api->sip_svc_plat_format_trans_id(dev, client_idx, trans_idx);
}

__syscall uint32_t sip_svc_plat_get_trans_idx(const struct device *dev, uint32_t trans_id);
static inline uint32_t z_impl_sip_svc_plat_get_trans_idx(const struct device *dev,
                                                         uint32_t trans_id)
{
        __ASSERT(dev, "dev shouldn't be NULL");
        const struct svc_driver_api *api = DEVICE_API_GET(svc, dev);

        __ASSERT(api->sip_svc_plat_get_trans_idx,
                 "sip_svc_plat_get_trans_idx func shouldn't be NULL");

        return api->sip_svc_plat_get_trans_idx(dev, trans_id);
}

__syscall void sip_svc_plat_update_trans_id(const struct device *dev,
                                            struct sip_svc_request *request, uint32_t trans_id);
static inline void z_impl_sip_svc_plat_update_trans_id(const struct device *dev,
                                                       struct sip_svc_request *request,
                                                       uint32_t trans_id)
{
        __ASSERT(dev, "dev shouldn't be NULL");
        const struct svc_driver_api *api = DEVICE_API_GET(svc, dev);

        __ASSERT(api->sip_svc_plat_update_trans_id,
                 "sip_svc_plat_update_trans_id func shouldn't be NULL");
        __ASSERT(request, "request shouldn't be NULL");

        api->sip_svc_plat_update_trans_id(dev, request, trans_id);
}

__syscall uint32_t sip_svc_plat_get_error_code(const struct device *dev, struct arm_smccc_res *res);
static inline uint32_t z_impl_sip_svc_plat_get_error_code(const struct device *dev,
                                                          struct arm_smccc_res *res)
{
        __ASSERT(dev, "dev shouldn't be NULL");
        const struct svc_driver_api *api = DEVICE_API_GET(svc, dev);

        __ASSERT(api->sip_svc_plat_get_error_code,
                 "sip_svc_plat_get_error_code func shouldn't be NULL");
        __ASSERT(res, "res shouldn't be NULL");

        return api->sip_svc_plat_get_error_code(dev, res);
}

__syscall int sip_svc_plat_async_res_req(const struct device *dev, unsigned long *a0,
                                         unsigned long *a1, unsigned long *a2, unsigned long *a3,
                                         unsigned long *a4, unsigned long *a5, unsigned long *a6,
                                         unsigned long *a7, char *buf, size_t size);
static inline int z_impl_sip_svc_plat_async_res_req(const struct device *dev, unsigned long *a0,
                                                    unsigned long *a1, unsigned long *a2,
                                                    unsigned long *a3, unsigned long *a4,
                                                    unsigned long *a5, unsigned long *a6,
                                                    unsigned long *a7, char *buf, size_t size)
{
        __ASSERT(dev, "dev shouldn't be NULL");
        const struct svc_driver_api *api = DEVICE_API_GET(svc, dev);

        __ASSERT(api->sip_svc_plat_async_res_req,
                 "sip_svc_plat_async_res_req func shouldn't be NULL");
        __ASSERT(a0, "a0 shouldn't be NULL");
        __ASSERT(a1, "a1 shouldn't be NULL");
        __ASSERT(a2, "a2 shouldn't be NULL");
        __ASSERT(a3, "a3 shouldn't be NULL");
        __ASSERT(a4, "a4 shouldn't be NULL");
        __ASSERT(a5, "a5 shouldn't be NULL");
        __ASSERT(a6, "a6 shouldn't be NULL");
        __ASSERT(a7, "a7 shouldn't be NULL");
        __ASSERT(((buf == NULL && size == 0) || (buf != NULL && size != 0)),
                 "buf and size should represent a buffer");
        return api->sip_svc_plat_async_res_req(dev, a0, a1, a2, a3, a4, a5, a6, a7, buf, size);
}

__syscall int sip_svc_plat_async_res_res(const struct device *dev, struct arm_smccc_res *res,
                                         char *buf, size_t *size, uint32_t *trans_id);
static inline int z_impl_sip_svc_plat_async_res_res(const struct device *dev,
                                                    struct arm_smccc_res *res, char *buf,
                                                    size_t *size, uint32_t *trans_id)
{
        __ASSERT(dev, "dev shouldn't be NULL");
        const struct svc_driver_api *api = DEVICE_API_GET(svc, dev);

        __ASSERT(api->sip_svc_plat_async_res_res,
                 "sip_svc_plat_async_res_res func shouldn't be NULL");
        __ASSERT(res, "res shouldn't be NULL");
        __ASSERT(buf, "buf shouldn't be NULL");
        __ASSERT(size, "size shouldn't be NULL");
        __ASSERT(trans_id, "buf shouldn't be NULL");

        return api->sip_svc_plat_async_res_res(dev, res, buf, size, trans_id);
}

__syscall void sip_svc_plat_free_async_memory(const struct device *dev,
                                              struct sip_svc_request *request);
static inline void z_impl_sip_svc_plat_free_async_memory(const struct device *dev,
                                                         struct sip_svc_request *request)
{
        __ASSERT(dev, "dev shouldn't be NULL");
        const struct svc_driver_api *api = DEVICE_API_GET(svc, dev);

        __ASSERT(api->sip_svc_plat_free_async_memory,
                 "sip_svc_plat_free_async_memory func shouldn't be NULL");
        __ASSERT(request, "request shouldn't be NULL");

        api->sip_svc_plat_free_async_memory(dev, request);
}


#include <zephyr/syscalls/sip_svc_driver.h>

#endif /* ZEPHYR_INCLUDE_SIP_SVC_DRIVER_H_ */
```

## 789.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023, Intel Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 352 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_SIP_SVC_DRIVER_H_`。

## 789.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__driver_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/drivers/sip_svc/sip_svc_proto.h](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__proto_8h.html)
- [zephyr/sip_svc/sip_svc_controller.h](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__controller_8h.html)
- [sip_supervisory_call_t](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__driver_8h.html#a15714e3852882693de6c9c7f2229bcd1)
- [device](../device_reference/P002_设备对象结构.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [sip_svc_plat_func_id_valid_t](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__driver_8h.html#ac5921c9cdc00604651696e1580f30797)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [sip_svc_plat_format_trans_id_t](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__driver_8h.html#a3cf78c760c6eae2091e92329e54b1a31)
- [sip_svc_plat_get_trans_idx_t](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__driver_8h.html#a35145ddf422e8782b4ec37270b04d98c)
- [sip_svc_plat_update_trans_id_t](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__driver_8h.html#a9d61db0484e2aacce4515290ffb4450c)
- [sip_svc_request](../platform_security_model_reference/P056_sip_svc_request_结构体.md)
- [sip_svc_plat_free_async_memory_t](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__driver_8h.html#ab32e31bdba00ff66303fab1b04cd0ebe)
- [sip_svc_plat_async_res_req_t](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__driver_8h.html#aa49a26b4b503e58d23fb5087ed701a0a)
- [sip_svc_plat_async_res_res_t](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__driver_8h.html#a54293f84f9bc86661f8a4bf717ad4754)
- [sip_svc_plat_get_error_code_t](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__driver_8h.html#a926eeecea766b2131c03c57111a186f8)
- [svc_driver_api](../device_power_control_model_reference/P092_svc_driver_api_结构体.md)
- [sip_supervisory_call](../device_power_control_model_reference/P092_svc_driver_api_结构体.md#a5f02e921d2a038616fad9d8d6a052f6b)
- [sip_svc_plat_func_id_valid](../device_power_control_model_reference/P092_svc_driver_api_结构体.md#a9f0a7711ef5ba2900d378c0a2805eaf4)
- [sip_svc_plat_format_trans_id](../device_power_control_model_reference/P092_svc_driver_api_结构体.md#a6435b703d30f462c1ec38e533a9c0817)
- [sip_svc_plat_get_trans_idx](../device_power_control_model_reference/P092_svc_driver_api_结构体.md#a30a435265fa828d9fdfcc70664be0945)
- [sip_svc_plat_update_trans_id](../device_power_control_model_reference/P092_svc_driver_api_结构体.md#a0ccdebec2a60d32a1767c5e47bc3ae25)
- [sip_svc_plat_free_async_memory](../device_power_control_model_reference/P092_svc_driver_api_结构体.md#a484b7c6ef4777a61e8f4f8e6778a7b45)
- [sip_svc_plat_async_res_req](../device_power_control_model_reference/P092_svc_driver_api_结构体.md#a79ac1f8410b7f0883ceb0a96823fbdf4)
- [sip_svc_plat_async_res_res](../device_power_control_model_reference/P092_svc_driver_api_结构体.md#a1d94fdfb564caa84e3f18f2139ae4fe0)
- [sip_svc_plat_get_error_code](../device_power_control_model_reference/P092_svc_driver_api_结构体.md#ae148bb010e4a0c2913e1c7425565316a)
- [sip_supervisory_call](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__driver_8h.html#a881e3794f9e29e12c925cb5dbd443420)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [sip_svc_plat_func_id_valid](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__driver_8h.html#a8df36a218cce4c0904c147d498c1322d)
- [sip_svc_plat_format_trans_id](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__driver_8h.html#ae52dee0bbba688a73a9726dd4aa482d2)
- [sip_svc_plat_get_trans_idx](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__driver_8h.html#ad0e52f49e7db8cf51ff8cf95e1283994)
- [sip_svc_plat_update_trans_id](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__driver_8h.html#a095123f7aec80a3e51d75ef248990124)
- [sip_svc_plat_get_error_code](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__driver_8h.html#a3510743d8cf114376b740f3d297c583f)
- [sip_svc_plat_async_res_req](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__driver_8h.html#abb9ff6ec7dea6fc4e104db8cc5e7168b)
- [sip_svc_plat_async_res_res](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__driver_8h.html#a0a0577249c2a9f470cd6ec0a60b455c8)
- [sip_svc_plat_free_async_memory](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__driver_8h.html#aa4e44eb2af080207821a60f8b3442886)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [sip_svc_controller.h](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__controller_8h.html)
- [sip_svc_proto.h](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__proto_8h.html)
- [svc_driver_api::sip_svc_plat_update_trans_id](../device_power_control_model_reference/P092_svc_driver_api_结构体.md#a0ccdebec2a60d32a1767c5e47bc3ae25)
- [svc_driver_api::sip_svc_plat_async_res_res](../device_power_control_model_reference/P092_svc_driver_api_结构体.md#a1d94fdfb564caa84e3f18f2139ae4fe0)
- [svc_driver_api::sip_svc_plat_get_trans_idx](../device_power_control_model_reference/P092_svc_driver_api_结构体.md#a30a435265fa828d9fdfcc70664be0945)
- [svc_driver_api::sip_svc_plat_free_async_memory](../device_power_control_model_reference/P092_svc_driver_api_结构体.md#a484b7c6ef4777a61e8f4f8e6778a7b45)
- [svc_driver_api::sip_supervisory_call](../device_power_control_model_reference/P092_svc_driver_api_结构体.md#a5f02e921d2a038616fad9d8d6a052f6b)
- [svc_driver_api::sip_svc_plat_format_trans_id](../device_power_control_model_reference/P092_svc_driver_api_结构体.md#a6435b703d30f462c1ec38e533a9c0817)
- [svc_driver_api::sip_svc_plat_async_res_req](../device_power_control_model_reference/P092_svc_driver_api_结构体.md#a79ac1f8410b7f0883ceb0a96823fbdf4)
- [svc_driver_api::sip_svc_plat_func_id_valid](../device_power_control_model_reference/P092_svc_driver_api_结构体.md#a9f0a7711ef5ba2900d378c0a2805eaf4)
- [svc_driver_api::sip_svc_plat_get_error_code](../device_power_control_model_reference/P092_svc_driver_api_结构体.md#ae148bb010e4a0c2913e1c7425565316a)

---

[上一章](P788_sip_svc_agilex_mailbox.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P790_sip_svc_proto.h_源码浏览.md)
