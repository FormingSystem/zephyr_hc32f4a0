---
id: learning.zephyr-docs.api-file-protocol-service-reference.page-14
title: zephyr__mgmt__fota_http.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/fota__http_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_zephyr\_\_mgmt\_\_fota\_http.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/fota__http_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

基于HTTP的固件空中升级（Firmware Over-the-Air）。

<a id="details"></a>

```c
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <zephyr/dfu/mcuboot.h>
#include <zephyr/net/tls_credentials.h>
```

查看此文件的源码。

基于HTTP的固件空中升级（Firmware Over-the-Air）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 14.1\_数据结构（Data Structures）

<a id="r_fota_5Fhttp_5Fprogress"></a>

```c
struct fota_http_progress
```

相关声明：[fota_http_progress](../system_service_model_reference/P038_fota_http_progress_结构体.md)。

写入映像（Image）期间报告的传输状态。

<a id="r_fota_5Fhttp_5Fdownload_5Fparams"></a>

```c
struct fota_http_download_params
```

相关声明：[fota_http_download_params](../system_service_model_reference/P037_fota_http_download_params_结构体.md)。

下载（Download）的参数。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 14.2\_类型定义（Typedefs）

<a id="r_gac35f904d1a5c2c337dee9db35e2b13d2"></a>

```c
typedef void(* fota_http_progress_cb_t) (const struct fota_http_progress *progress, void *user_data)
```

相关声明：[fota_http_progress_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html#gac35f904d1a5c2c337dee9db35e2b13d2)、[fota_http_progress](../system_service_model_reference/P038_fota_http_progress_结构体.md)。

进度回调（Progress Callback）。

<a id="r_gae4f16d5d2769d9af9ba219e69d1bea75"></a>

```c
typedef void(* fota_http_done_cb_t) (int result, void *user_data)
```

相关声明：[fota_http_done_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html#gae4f16d5d2769d9af9ba219e69d1bea75)。

`fota_http_download_async()` 的完成回调（Completion Callback）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 14.3\_函数（Functions）

<a id="r_ga8aa13892a735e7f2826c00dab36b0a08"></a>

```c
int fota_http_download (const struct fota_http_download_params *params)
```

相关声明：[fota_http_download](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html#ga8aa13892a735e7f2826c00dab36b0a08)、[fota_http_download_params](../system_service_model_reference/P037_fota_http_download_params_结构体.md)。

将固件镜像（Firmware Image）下载到 MCUboot 次级槽（Secondary Slot）。

<a id="r_gaf730ea430346720f05dd7f290eef69c6"></a>

```c
int fota_http_download_async (const struct fota_http_download_params *params, fota_http_done_cb_t done_cb)
```

相关声明：[fota_http_download_async](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html#gaf730ea430346720f05dd7f290eef69c6)、[fota_http_download_params](../system_service_model_reference/P037_fota_http_download_params_结构体.md)、[fota_http_done_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html#gae4f16d5d2769d9af9ba219e69d1bea75)。

在库线程（Library Thread）中下载固件镜像（Firmware Image）。

<a id="r_gac67bbc767cf189830d071651b6b5d986"></a>

```c
int fota_http_cancel (void)
```

相关声明：[fota_http_cancel](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html#gac67bbc767cf189830d071651b6b5d986)。

中止正在进行的下载（Download）。

<a id="r_gaad1653d95d0d798c63e2d4b3f9ff9324"></a>

```c
int fota_http_apply (uint8_t image_index, bool permanent)
```

相关声明：[fota_http_apply](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html#gaad1653d95d0d798c63e2d4b3f9ff9324)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

请求 MCUboot 在下次复位（Reset）时引导已下载的镜像（Downloaded Image）。

<a id="r_gab3d4aa4a5842bf739e4554a40e8b4db5"></a>

```c
int fota_http_confirm (uint8_t image_index)
```

相关声明：[fota_http_confirm](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html#gab3d4aa4a5842bf739e4554a40e8b4db5)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

确认正在运行的镜像（Running Image），使引导加载程序（Bootloader）停止回退该镜像。

<a id="r_ga7f4caeac9e7f14e24da6d403b4730ded"></a>

```c
bool fota_http_confirm_pending (void)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[fota_http_confirm_pending](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html#ga7f4caeac9e7f14e24da6d403b4730ded)。

检查正在运行的镜像（Running Image）是否仍需确认。

<a id="r_ga7f0b137c19a30942725406abdcf89497"></a>

```c
int fota_http_get_download_slot (uint8_t image_index)
```

相关声明：[fota_http_get_download_slot](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html#ga7f0b137c19a30942725406abdcf89497)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

下载写入槽的闪存区域标识符（Flash Area Identifier）。

<a id="r_ga56ce2026ec720e06f67ae8d7f780609c"></a>

```c
int fota_http_get_image_header (uint8_t image_index, struct mcuboot_img_header *header)
```

相关声明：[fota_http_get_image_header](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html#ga56ce2026ec720e06f67ae8d7f780609c)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mcuboot_img_header](../boot_control_reference/P006_MCUboot镜像头结构.md)。

读取次级槽（Secondary Slot）中镜像的 MCUboot 头（Header）。

<a id="r_gac3f298c4501aa85afa63dc08a6ddf1bf"></a>

```c
size_t fota_http_nvm_bytes_written (void)
```

相关声明：[fota_http_nvm_bytes_written](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html#gac3f298c4501aa85afa63dc08a6ddf1bf)。

最近一次下载写入非易失性存储器（Non-volatile Memory）的字节数。

<a id="r_ga511dd696af7bd7b61a9924ca64964f32"></a>

```c
int fota_http_tls_add_ca (const void *cert, size_t len)
```

相关声明：[fota_http_tls_add_ca](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html#ga511dd696af7bd7b61a9924ca64964f32)。

注册用于认证 HTTPS 服务器的 CA 证书（CA Certificate）。

<a id="r_gacdeabce6009b1b1b9b10cfe6fe9fd9d9"></a>

```c
int fota_http_tls_add_client_cert (const void *cert, size_t cert_len, const void *key, size_t key_len)
```

相关声明：[fota_http_tls_add_client_cert](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html#gacdeabce6009b1b1b9b10cfe6fe9fd9d9)。

注册双向 TLS（Mutual TLS）使用的客户端证书和密钥（Client Certificate and Key）。


## 14.4\_原页交叉引用（Cross References）

- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/dfu/mcuboot.h](../boot_control_reference/P003_MCUboot头文件源码.md)
- [zephyr/net/tls_credentials.h](../api_source_reference/P870_tls_credentials.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P269_fota_http.h_源码浏览.md)
- [fota_http_progress](../system_service_model_reference/P038_fota_http_progress_结构体.md)
- [fota_http_download_params](../system_service_model_reference/P037_fota_http_download_params_结构体.md)
- [fota_http_progress_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html#gac35f904d1a5c2c337dee9db35e2b13d2)
- [fota_http_done_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html#gae4f16d5d2769d9af9ba219e69d1bea75)
- [fota_http_download_async()](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html#gaf730ea430346720f05dd7f290eef69c6)
- [fota_http_download](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html#ga8aa13892a735e7f2826c00dab36b0a08)
- [fota_http_cancel](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html#gac67bbc767cf189830d071651b6b5d986)
- [fota_http_apply](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html#gaad1653d95d0d798c63e2d4b3f9ff9324)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [fota_http_confirm](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html#gab3d4aa4a5842bf739e4554a40e8b4db5)
- [fota_http_confirm_pending](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html#ga7f4caeac9e7f14e24da6d403b4730ded)
- [fota_http_get_download_slot](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html#ga7f0b137c19a30942725406abdcf89497)
- [fota_http_get_image_header](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html#ga56ce2026ec720e06f67ae8d7f780609c)
- [mcuboot_img_header](../boot_control_reference/P006_MCUboot镜像头结构.md)
- [fota_http_nvm_bytes_written](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html#gac3f298c4501aa85afa63dc08a6ddf1bf)
- [fota_http_tls_add_ca](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html#ga511dd696af7bd7b61a9924ca64964f32)
- [fota_http_tls_add_client_cert](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html#gacdeabce6009b1b1b9b10cfe6fe9fd9d9)

<a id="header-details"></a>

---

[上一章](P013_zephyr__drivers__pcie__controller.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P015_zephyr__debug__gcov.h_文件参考.md)
