---
id: learning.zephyr-docs.api-source-reference.page-269
title: fota_http.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/fota__http_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第269章\_fota\_http.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/fota__http_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/fota__http_8h.html)。

## 269.1\_原始可见代码（Source Code）

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
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="foldopen00036"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="foldopen00067"></a>
<a id="l00067"></a>
<a id="l00072"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00092"></a>
<a id="l00094"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00104"></a>
<a id="l00106"></a>
<a id="l00108"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="l00310"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="agroup__fota__http_html_ga511dd696af7bd7b61a9924ca64964f32"></a>
<a id="agroup__fota__http_html_ga56ce2026ec720e06f67ae8d7f780609c"></a>
<a id="agroup__fota__http_html_ga7f0b137c19a30942725406abdcf89497"></a>
<a id="agroup__fota__http_html_ga7f4caeac9e7f14e24da6d403b4730ded"></a>
<a id="agroup__fota__http_html_ga8aa13892a735e7f2826c00dab36b0a08"></a>
<a id="agroup__fota__http_html_gaad1653d95d0d798c63e2d4b3f9ff9324"></a>
<a id="agroup__fota__http_html_gab3d4aa4a5842bf739e4554a40e8b4db5"></a>
<a id="agroup__fota__http_html_gac35f904d1a5c2c337dee9db35e2b13d2"></a>
<a id="agroup__fota__http_html_gac3f298c4501aa85afa63dc08a6ddf1bf"></a>
<a id="agroup__fota__http_html_gac67bbc767cf189830d071651b6b5d986"></a>
<a id="agroup__fota__http_html_gacdeabce6009b1b1b9b10cfe6fe9fd9d9"></a>
<a id="agroup__fota__http_html_gae4f16d5d2769d9af9ba219e69d1bea75"></a>
<a id="agroup__fota__http_html_gaf730ea430346720f05dd7f290eef69c6"></a>
<a id="agroup__tls__credentials_html_gaadfe9694309e473f7be74ed98dfb36d3"></a>
<a id="amcuboot_8h_html"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructfota__http__download__params_html"></a>
<a id="astructfota__http__download__params_html_a24a9783b671cc173c5e4704d134c1b8f"></a>
<a id="astructfota__http__download__params_html_a5022adf6e6b66b202e3a0cb1621be3e3"></a>
<a id="astructfota__http__download__params_html_a57c60cd60cf5b7371d1d890a6b66e07a"></a>
<a id="astructfota__http__download__params_html_a67991bb1e14d5d56a75336f808f383be"></a>
<a id="astructfota__http__download__params_html_a6a643a234324abe04b8a0aeea9e36767"></a>
<a id="astructfota__http__download__params_html_a8e5885ce7f80d1d2a8894a04c27ac2b3"></a>
<a id="astructfota__http__download__params_html_ac8daa467618d47f66f9426e15ab30601"></a>
<a id="astructfota__http__download__params_html_adb810f2566bdf8666f82d6c8a4876856"></a>
<a id="astructfota__http__download__params_html_aebc938e3d275f107b558ea1c27551e32"></a>
<a id="astructfota__http__download__params_html_af867c3301e8911d1c4105515f3546515"></a>
<a id="astructfota__http__progress_html"></a>
<a id="astructfota__http__progress_html_a4fde85b0d24bf84c7a5695acd69c7c97"></a>
<a id="astructfota__http__progress_html_a9bc76de1cc1df4105a5ddb23a3968b50"></a>
<a id="astructfota__http__progress_html_ab93fb2eddbcf59556e92688dca0c6132"></a>
<a id="astructmcuboot__img__header_html"></a>
<a id="atls__credentials_8h_html"></a>

```c
/*
 * Copyright (c) 2026 Espressif Systems (Shanghai) Co., Ltd.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_MGMT_FOTA_HTTP_H_
#define ZEPHYR_INCLUDE_MGMT_FOTA_HTTP_H_

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

#include <zephyr/dfu/mcuboot.h>
#include <zephyr/net/tls_credentials.h>


#ifdef __cplusplus
extern "C" {
#endif

struct fota_http_progress {
        size_t written;
        size_t total;
        int http_status;
};

typedef void (*fota_http_progress_cb_t)(const struct fota_http_progress *progress, void *user_data);

typedef void (*fota_http_done_cb_t)(int result, void *user_data);

struct fota_http_download_params {
        const char *url;
        const char *const *headers;
#if defined(CONFIG_FOTA_HTTP_SHA256_CHECK) || defined(__DOXYGEN__)
        const uint8_t *sha256;
#endif
#if defined(CONFIG_FOTA_HTTP_TLS) || defined(__DOXYGEN__)
        const sec_tag_t *sec_tags;
        size_t sec_tag_count;
        const char *tls_hostname;
#endif
        fota_http_progress_cb_t progress_cb;
        void *user_data;
        uint8_t image_index;
#if defined(CONFIG_FOTA_HTTP_RESUME) || defined(__DOXYGEN__)
        bool resume;
#endif
};

int fota_http_download(const struct fota_http_download_params *params);

int fota_http_download_async(const struct fota_http_download_params *params,
                             fota_http_done_cb_t done_cb);

int fota_http_cancel(void);

int fota_http_apply(uint8_t image_index, bool permanent);

int fota_http_confirm(uint8_t image_index);

bool fota_http_confirm_pending(void);

int fota_http_get_download_slot(uint8_t image_index);

int fota_http_get_image_header(uint8_t image_index, struct mcuboot_img_header *header);

size_t fota_http_nvm_bytes_written(void);

int fota_http_tls_add_ca(const void *cert, size_t len);

int fota_http_tls_add_client_cert(const void *cert, size_t cert_len, const void *key,
                                  size_t key_len);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_MGMT_FOTA_HTTP_H_ */
```

## 269.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Espressif Systems (Shanghai) Co., Ltd.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 319 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MGMT_FOTA_HTTP_H_`。

## 269.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/fota__http_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/dfu/mcuboot.h](../boot_control_reference/P002_MCUboot头文件参考.md)
- [zephyr/net/tls_credentials.h](https://docs.zephyrproject.org/latest/doxygen/html/tls__credentials_8h.html)
- [fota_http_progress](../system_service_model_reference/P038_fota_http_progress_结构体.md)
- [written](../system_service_model_reference/P038_fota_http_progress_结构体.md#a9bc76de1cc1df4105a5ddb23a3968b50)
- [total](../system_service_model_reference/P038_fota_http_progress_结构体.md#a4fde85b0d24bf84c7a5695acd69c7c97)
- [http_status](../system_service_model_reference/P038_fota_http_progress_结构体.md#ab93fb2eddbcf59556e92688dca0c6132)
- [fota_http_progress_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html#gac35f904d1a5c2c337dee9db35e2b13d2)
- [fota_http_done_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html#gae4f16d5d2769d9af9ba219e69d1bea75)
- [fota_http_download_params](../system_service_model_reference/P037_fota_http_download_params_结构体.md)
- [url](../system_service_model_reference/P037_fota_http_download_params_结构体.md#a6a643a234324abe04b8a0aeea9e36767)
- [headers](../system_service_model_reference/P037_fota_http_download_params_结构体.md#a8e5885ce7f80d1d2a8894a04c27ac2b3)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [sha256](../system_service_model_reference/P037_fota_http_download_params_结构体.md#adb810f2566bdf8666f82d6c8a4876856)
- [sec_tag_t](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#gaadfe9694309e473f7be74ed98dfb36d3)
- [sec_tags](../system_service_model_reference/P037_fota_http_download_params_结构体.md#a5022adf6e6b66b202e3a0cb1621be3e3)
- [sec_tag_count](../system_service_model_reference/P037_fota_http_download_params_结构体.md#a24a9783b671cc173c5e4704d134c1b8f)
- [tls_hostname](../system_service_model_reference/P037_fota_http_download_params_结构体.md#af867c3301e8911d1c4105515f3546515)
- [progress_cb](../system_service_model_reference/P037_fota_http_download_params_结构体.md#a57c60cd60cf5b7371d1d890a6b66e07a)
- [user_data](../system_service_model_reference/P037_fota_http_download_params_结构体.md#a67991bb1e14d5d56a75336f808f383be)
- [image_index](../system_service_model_reference/P037_fota_http_download_params_结构体.md#ac8daa467618d47f66f9426e15ab30601)
- [resume](../system_service_model_reference/P037_fota_http_download_params_结构体.md#aebc938e3d275f107b558ea1c27551e32)
- [fota_http_download](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html#ga8aa13892a735e7f2826c00dab36b0a08)
- [fota_http_download_async](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html#gaf730ea430346720f05dd7f290eef69c6)
- [fota_http_cancel](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html#gac67bbc767cf189830d071651b6b5d986)
- [fota_http_apply](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html#gaad1653d95d0d798c63e2d4b3f9ff9324)
- [fota_http_confirm](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html#gab3d4aa4a5842bf739e4554a40e8b4db5)
- [fota_http_confirm_pending](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html#ga7f4caeac9e7f14e24da6d403b4730ded)
- [fota_http_get_download_slot](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html#ga7f0b137c19a30942725406abdcf89497)
- [fota_http_get_image_header](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html#ga56ce2026ec720e06f67ae8d7f780609c)
- [mcuboot_img_header](../boot_control_reference/P006_MCUboot镜像头结构.md)
- [fota_http_nvm_bytes_written](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html#gac3f298c4501aa85afa63dc08a6ddf1bf)
- [fota_http_tls_add_ca](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html#ga511dd696af7bd7b61a9924ca64964f32)
- [fota_http_tls_add_client_cert](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html#gacdeabce6009b1b1b9b10cfe6fe9fd9d9)
- [mcuboot.h](../boot_control_reference/P002_MCUboot头文件参考.md)
- [fota_http_download_params::sec_tag_count](../system_service_model_reference/P037_fota_http_download_params_结构体.md#a24a9783b671cc173c5e4704d134c1b8f)
- [fota_http_download_params::sec_tags](../system_service_model_reference/P037_fota_http_download_params_结构体.md#a5022adf6e6b66b202e3a0cb1621be3e3)
- [fota_http_download_params::progress_cb](../system_service_model_reference/P037_fota_http_download_params_结构体.md#a57c60cd60cf5b7371d1d890a6b66e07a)
- [fota_http_download_params::user_data](../system_service_model_reference/P037_fota_http_download_params_结构体.md#a67991bb1e14d5d56a75336f808f383be)
- [fota_http_download_params::url](../system_service_model_reference/P037_fota_http_download_params_结构体.md#a6a643a234324abe04b8a0aeea9e36767)
- [fota_http_download_params::headers](../system_service_model_reference/P037_fota_http_download_params_结构体.md#a8e5885ce7f80d1d2a8894a04c27ac2b3)
- [fota_http_download_params::image_index](../system_service_model_reference/P037_fota_http_download_params_结构体.md#ac8daa467618d47f66f9426e15ab30601)
- [fota_http_download_params::sha256](../system_service_model_reference/P037_fota_http_download_params_结构体.md#adb810f2566bdf8666f82d6c8a4876856)
- [fota_http_download_params::resume](../system_service_model_reference/P037_fota_http_download_params_结构体.md#aebc938e3d275f107b558ea1c27551e32)
- [fota_http_download_params::tls_hostname](../system_service_model_reference/P037_fota_http_download_params_结构体.md#af867c3301e8911d1c4105515f3546515)
- [fota_http_progress::total](../system_service_model_reference/P038_fota_http_progress_结构体.md#a4fde85b0d24bf84c7a5695acd69c7c97)
- [fota_http_progress::written](../system_service_model_reference/P038_fota_http_progress_结构体.md#a9bc76de1cc1df4105a5ddb23a3968b50)
- [fota_http_progress::http_status](../system_service_model_reference/P038_fota_http_progress_结构体.md#ab93fb2eddbcf59556e92688dca0c6132)
- [tls_credentials.h](https://docs.zephyrproject.org/latest/doxygen/html/tls__credentials_8h.html)

---

[上一章](P268_formatter.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P270_frame.h_源码浏览.md)
