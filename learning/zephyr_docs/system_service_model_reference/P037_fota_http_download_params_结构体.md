---
id: learning.zephyr-docs.system-service-model-reference.page-37
title: fota_http_download_params_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structfota__http__download__params.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第37章\_fota\_http\_download\_params\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structfota__http__download__params.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

下载（Download）的参数。

```c
#include <zephyr/mgmt/fota_http.h>
```

<a id="details"></a>

下载（Download）的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 37.1\_数据成员（Data Fields）

<a id="r_a6a643a234324abe04b8a0aeea9e36767"></a>

```c
const char * url
```

相关声明：[url](#a6a643a234324abe04b8a0aeea9e36767)。

形式为 `http://host[:port]/path` 的完整 URL；启用 `CONFIG_FOTA_HTTP_TLS` 时使用 `https`。

<a id="r_a8e5885ce7f80d1d2a8894a04c27ac2b3"></a>

```c
const char *const * headers
```

相关声明：[headers](#a8e5885ce7f80d1d2a8894a04c27ac2b3)。

可选的附加请求头列表，以 `NULL` 终止。

<a id="r_adb810f2566bdf8666f82d6c8a4876856"></a>

```c
const uint8_t * sha256
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sha256](#adb810f2566bdf8666f82d6c8a4876856)。

可选的预期映像 SHA-256 摘要（digest），长度为 32 字节。

<a id="r_a5022adf6e6b66b202e3a0cb1621be3e3"></a>

```c
const sec_tag_t * sec_tags
```

相关声明：[sec_tag_t](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#gaadfe9694309e473f7be74ed98dfb36d3)、[sec_tags](#a5022adf6e6b66b202e3a0cb1621be3e3)。

可选的 TLS 安全标签（security tags），用于代替 `CONFIG_FOTA_HTTP_TLS_SEC_TAG`。

<a id="r_a24a9783b671cc173c5e4704d134c1b8f"></a>

```c
size_t sec_tag_count
```

相关声明：[sec_tag_count](#a24a9783b671cc173c5e4704d134c1b8f)。

`sec_tags` 中的条目数量。

<a id="r_af867c3301e8911d1c4105515f3546515"></a>

```c
const char * tls_hostname
```

相关声明：[tls_hostname](#af867c3301e8911d1c4105515f3546515)。

可选的主机名；当它与 URL 中的主机不同，用于验证服务器证书。

<a id="r_a57c60cd60cf5b7371d1d890a6b66e07a"></a>

```c
fota_http_progress_cb_t progress_cb
```

相关声明：[fota_http_progress_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html#gac35f904d1a5c2c337dee9db35e2b13d2)、[progress_cb](#a57c60cd60cf5b7371d1d890a6b66e07a)。

可选的进度回调（progress callback）。

<a id="r_a67991bb1e14d5d56a75336f808f383be"></a>

```c
void * user_data
```

相关声明：[user_data](#a67991bb1e14d5d56a75336f808f383be)。

原样传给各回调。

<a id="r_ac8daa467618d47f66f9426e15ab30601"></a>

```c
uint8_t image_index
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[image_index](#ac8daa467618d47f66f9426e15ab30601)。

多映像布局中要更新的映像；只有一个映像时为 0。

<a id="r_aebc938e3d275f107b558ea1c27551e32"></a>

```c
bool resume
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[resume](#aebc938e3d275f107b558ea1c27551e32)。

继续之前中断的下载。

## 37.2\_详细说明（Detailed Documentation）

<a id="a8e5885ce7f80d1d2a8894a04c27ac2b3"></a>

### `headers`

```c
const char* const* fota_http_download_params::headers
```

可选的附加请求头列表，以 `NULL` 终止。

每个条目都是以 `"\r\n"` 结尾的完整请求头行，例如 `"Authorization: Bearer token\r\n"`。

<a id="ac8daa467618d47f66f9426e15ab30601"></a>

### `image_index`

```c
uint8_t fota_http_download_params::image_index
```

多映像布局中要更新的映像；只有一个映像时为 0。

<a id="a57c60cd60cf5b7371d1d890a6b66e07a"></a>

### `progress_cb`

```c
fota_http_progress_cb_t fota_http_download_params::progress_cb
```

可选的进度回调（progress callback）。

<a id="aebc938e3d275f107b558ea1c27551e32"></a>

### `resume`

```c
bool fota_http_download_params::resume
```

继续之前中断的下载。

只有 URL 和映像索引与中断的下载相匹配时，才使用保存的偏移量。如果服务器此前发送过 `ETag` 或 `Last-Modified` 头，请求会携带 `If-Range`，因此服务器上的文件若发生变化，就会重新从头下载。仅在启用 `CONFIG_FOTA_HTTP_RESUME` 时存在。

<a id="a24a9783b671cc173c5e4704d134c1b8f"></a>

### `sec_tag_count`

```c
size_t fota_http_download_params::sec_tag_count
```

`sec_tags` 中的条目数量。

<a id="a5022adf6e6b66b202e3a0cb1621be3e3"></a>

### `sec_tags`

```c
const sec_tag_t* fota_http_download_params::sec_tags
```

可选的 TLS 安全标签（security tags），用于代替 `CONFIG_FOTA_HTTP_TLS_SEC_TAG`。

仅在启用 `CONFIG_FOTA_HTTP_TLS` 时存在。

<a id="adb810f2566bdf8666f82d6c8a4876856"></a>

### `sha256`

```c
const uint8_t* fota_http_download_params::sha256
```

可选的预期映像 SHA-256 摘要（digest），长度为 32 字节。

仅在启用 `CONFIG_FOTA_HTTP_SHA256_CHECK` 时存在。

<a id="af867c3301e8911d1c4105515f3546515"></a>

### `tls_hostname`

```c
const char* fota_http_download_params::tls_hostname
```

可选的主机名；当它与 URL 中的主机不同，用于验证服务器证书。

当 URL 使用 IP 地址，而证书中没有匹配的 IP 条目时需要此项。仅在启用 `CONFIG_FOTA_HTTP_TLS` 时存在。

<a id="a6a643a234324abe04b8a0aeea9e36767"></a>

### `url`

```c
const char* fota_http_download_params::url
```

形式为 `http://host[:port]/path` 的完整 URL；启用 `CONFIG_FOTA_HTTP_TLS` 时使用 `https`。

<a id="a67991bb1e14d5d56a75336f808f383be"></a>

### `user_data`

```c
void* fota_http_download_params::user_data
```

原样传给各回调。

本数据类型文档由以下文件生成：

- `zephyr/mgmt/fota_http.h`

## 37.3\_原页交叉引用（Cross References）

- [zephyr/mgmt/fota_http.h](https://docs.zephyrproject.org/latest/doxygen/html/fota__http_8h_source.html)
- [CONFIG_FOTA_HTTP_TLS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FOTA_HTTP_TLS)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [sec_tag_t](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#gaadfe9694309e473f7be74ed98dfb36d3)
- [CONFIG_FOTA_HTTP_TLS_SEC_TAG](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FOTA_HTTP_TLS_SEC_TAG)
- [fota_http_progress_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html#gac35f904d1a5c2c337dee9db35e2b13d2)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [CONFIG_FOTA_HTTP_RESUME](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FOTA_HTTP_RESUME)
- [CONFIG_FOTA_HTTP_SHA256_CHECK](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FOTA_HTTP_SHA256_CHECK)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P036_flash_stm32_ex_op_sector_wp_out_结构体.md) · [返回大纲](大纲.md) · [下一章](P038_fota_http_progress_结构体.md)
