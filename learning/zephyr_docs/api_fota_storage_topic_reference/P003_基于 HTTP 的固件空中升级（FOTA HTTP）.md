---
id: learning.zephyr-docs.api-fota-storage-topic-reference.page-3
title: 基于 HTTP 的固件空中升级（FOTA HTTP）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_基于 HTTP 的固件空中升级（FOTA HTTP）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

基于HTTP的固件空中升级（Firmware Over-the-Air）。

<a id="details"></a>

通过 HTTP 进行固件无线升级（Firmware Over-the-Air，FOTA）。自（Since）4.5 起提供，版本（Version）0.1.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 3.1\_数据结构（Data Structures）

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

## 3.2\_类型定义（Typedefs）

<a id="r_gac35f904d1a5c2c337dee9db35e2b13d2"></a>

```c
typedef void(* fota_http_progress_cb_t) (const struct fota_http_progress *progress, void *user_data)
```

相关声明：[fota_http_progress_cb_t](#gac35f904d1a5c2c337dee9db35e2b13d2)、[fota_http_progress](../system_service_model_reference/P038_fota_http_progress_结构体.md)。

进度回调（Progress Callback）。

<a id="r_gae4f16d5d2769d9af9ba219e69d1bea75"></a>

```c
typedef void(* fota_http_done_cb_t) (int result, void *user_data)
```

相关声明：[fota_http_done_cb_t](#gae4f16d5d2769d9af9ba219e69d1bea75)。

`fota_http_download_async()` 的完成回调（Completion Callback）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 3.3\_函数（Functions）

<a id="r_ga8aa13892a735e7f2826c00dab36b0a08"></a>

```c
int fota_http_download (const struct fota_http_download_params *params)
```

相关声明：[fota_http_download](#ga8aa13892a735e7f2826c00dab36b0a08)、[fota_http_download_params](../system_service_model_reference/P037_fota_http_download_params_结构体.md)。

将固件镜像（Firmware Image）下载到 MCUboot 次级槽（Secondary Slot）。

<a id="r_gaf730ea430346720f05dd7f290eef69c6"></a>

```c
int fota_http_download_async (const struct fota_http_download_params *params, fota_http_done_cb_t done_cb)
```

相关声明：[fota_http_download_async](#gaf730ea430346720f05dd7f290eef69c6)、[fota_http_download_params](../system_service_model_reference/P037_fota_http_download_params_结构体.md)、[fota_http_done_cb_t](#gae4f16d5d2769d9af9ba219e69d1bea75)。

在库线程（Library Thread）中下载固件镜像（Firmware Image）。

<a id="r_gac67bbc767cf189830d071651b6b5d986"></a>

```c
int fota_http_cancel (void)
```

相关声明：[fota_http_cancel](#gac67bbc767cf189830d071651b6b5d986)。

中止正在进行的下载（Download）。

<a id="r_gaad1653d95d0d798c63e2d4b3f9ff9324"></a>

```c
int fota_http_apply (uint8_t image_index, bool permanent)
```

相关声明：[fota_http_apply](#gaad1653d95d0d798c63e2d4b3f9ff9324)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

请求 MCUboot 在下次复位（Reset）时引导已下载的镜像（Downloaded Image）。

<a id="r_gab3d4aa4a5842bf739e4554a40e8b4db5"></a>

```c
int fota_http_confirm (uint8_t image_index)
```

相关声明：[fota_http_confirm](#gab3d4aa4a5842bf739e4554a40e8b4db5)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

确认正在运行的镜像（Running Image），使引导加载程序（Bootloader）停止回退该镜像。

<a id="r_ga7f4caeac9e7f14e24da6d403b4730ded"></a>

```c
bool fota_http_confirm_pending (void)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[fota_http_confirm_pending](#ga7f4caeac9e7f14e24da6d403b4730ded)。

检查正在运行的镜像（Running Image）是否仍需确认。

<a id="r_ga7f0b137c19a30942725406abdcf89497"></a>

```c
int fota_http_get_download_slot (uint8_t image_index)
```

相关声明：[fota_http_get_download_slot](#ga7f0b137c19a30942725406abdcf89497)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

下载写入槽的闪存区域标识符（Flash Area Identifier）。

<a id="r_ga56ce2026ec720e06f67ae8d7f780609c"></a>

```c
int fota_http_get_image_header (uint8_t image_index, struct mcuboot_img_header *header)
```

相关声明：[fota_http_get_image_header](#ga56ce2026ec720e06f67ae8d7f780609c)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mcuboot_img_header](../boot_control_reference/P006_MCUboot镜像头结构.md)。

读取次级槽（Secondary Slot）中镜像的 MCUboot 头（Header）。

<a id="r_gac3f298c4501aa85afa63dc08a6ddf1bf"></a>

```c
size_t fota_http_nvm_bytes_written (void)
```

相关声明：[fota_http_nvm_bytes_written](#gac3f298c4501aa85afa63dc08a6ddf1bf)。

最近一次下载写入非易失性存储器（Non-volatile Memory）的字节数。

<a id="r_ga511dd696af7bd7b61a9924ca64964f32"></a>

```c
int fota_http_tls_add_ca (const void *cert, size_t len)
```

相关声明：[fota_http_tls_add_ca](#ga511dd696af7bd7b61a9924ca64964f32)。

注册用于认证 HTTPS 服务器的 CA 证书（CA Certificate）。

<a id="r_gacdeabce6009b1b1b9b10cfe6fe9fd9d9"></a>

```c
int fota_http_tls_add_client_cert (const void *cert, size_t cert_len, const void *key, size_t key_len)
```

相关声明：[fota_http_tls_add_client_cert](#gacdeabce6009b1b1b9b10cfe6fe9fd9d9)。

注册双向 TLS（Mutual TLS）使用的客户端证书和密钥（Client Certificate and Key）。

## 3.4\_详细说明（Detailed Documentation）

<a id="gae4f16d5d2769d9af9ba219e69d1bea75"></a>

### `fota_http_done_cb_t`

```c
typedef void(* fota_http_done_cb_t) (int result, void *user_data)
```

```c
#include <zephyr/mgmt/fota_http.h>
```

`fota_http_download_async()` 的完成回调（Completion Callback）。

下载完成后，由库线程（Library Thread）调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `result` | 下载返回值；成功时为 0。 |
| `user_data` | 来自 `fota_http_download_params` 的指针。 |

<a id="gac35f904d1a5c2c337dee9db35e2b13d2"></a>

### `fota_http_progress_cb_t`

```c
typedef void(* fota_http_progress_cb_t) (const struct fota_http_progress *progress, void *user_data)
```

```c
#include <zephyr/mgmt/fota_http.h>
```

进度回调（Progress Callback）。

每次将一个响应体片段（Body Fragment）写入闪存后，由下载线程调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `progress` | 当前传输状态（Transfer State）。 |
| `user_data` | 来自 `fota_http_download_params` 的指针。 |

<a id="gaad1653d95d0d798c63e2d4b3f9ff9324"></a>

### `fota_http_apply()`

```c
int fota_http_apply ( uint8_t image_index, bool permanent )
```

```c
#include <zephyr/mgmt/fota_http.h>
```

请求 MCUboot 在下次复位（Reset）时引导已下载的镜像（Downloaded Image）。

次级槽位（Secondary Slot）必须包含具有有效 MCUboot 头部的镜像；如果自启动以来曾向该槽位下载，则最近一次下载必须成功。签名仅由引导加载程序（Bootloader）自身检查。

多个镜像必须一起更新时，应先下载并应用每个镜像，再重启：MCUboot 验证整个镜像集合并一次性交换（Swap），因此若仅应用了集合的一部分便重启，只会交换已标记的镜像。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `image_index` | 要启动的镜像；只有一个镜像时为 0。 |
| `permanent` | 为 `true` 时立即将镜像标记为已确认（Confirmed）。为 `false` 时，镜像先试启动一次以供评估；除非在下一次复位前调用 `fota_http_confirm()`，否则引导加载程序会回退到当前镜像。回退（Revert）需要 MCUboot 使用支持此功能的模式，例如 `swap-using-move` 或 `swap-using-offset`。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 已请求升级（Upgrade）。 |
| `-ENODEV` | `image_index` 对应的槽位不存在。 |
| `-EBUSY` | 正在下载。 |
| `-ENOEXEC` | 次级槽位（Secondary Slot）中没有有效镜像，或最近一次向其下载失败。 |
| `-errno` | 任何闪存（Flash）或引导加载程序（Bootloader）错误。 |

<a id="gac67bbc767cf189830d071651b6b5d986"></a>

### `fota_http_cancel()`

```c
int fota_http_cancel ( void )
```

```c
#include <zephyr/mgmt/fota_http.h>
```

中止正在进行的下载（Download）。

下一个片段到达或请求超时时，传输停止并报告 `-ECANCELED`。

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 此前有下载正在运行，并将停止。 |
| `-EALREADY` | 没有下载正在运行。 |

<a id="gab3d4aa4a5842bf739e4554a40e8b4db5"></a>

### `fota_http_confirm()`

```c
int fota_http_confirm ( uint8_t image_index)
```

```c
#include <zephyr/mgmt/fota_http.h>
```

确认正在运行的镜像（Running Image），使引导加载程序（Bootloader）停止回退该镜像。

只确认 `image_index` 指定的镜像。因此，若布局中还存有第二个设备的固件，则仅确认本设备已验证的部分。对于必须一起运行的镜像集合，应确认其中每个镜像。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `image_index` | 要确认的镜像；只有一个镜像时为 0。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 镜像已确认（Confirmed）。 |
| `-ENODEV` | `image_index` 对应的槽位不存在。 |
| `-errno` | 任何闪存（Flash）或引导加载程序（Bootloader）错误。 |

<a id="ga7f4caeac9e7f14e24da6d403b4730ded"></a>

### `fota_http_confirm_pending()`

```c
bool fota_http_confirm_pending ( void )
```

```c
#include <zephyr/mgmt/fota_http.h>
```

检查正在运行的镜像（Running Image）是否仍需确认。

仅报告镜像 0 的状态，因为引导加载程序接口不支持按镜像查询。更新多个镜像的应用须自行跟踪其他镜像。

**返回（Returns）**：返回值（Returns）：执行测试升级（Test Upgrade）后、调用 `fota_http_confirm()` 前为 `true`。

<a id="ga8aa13892a735e7f2826c00dab36b0a08"></a>

### `fota_http_download()`

```c
int fota_http_download ( const struct fota_http_download_params * params)
```

```c
#include <zephyr/mgmt/fota_http.h>
```

将固件镜像（Firmware Image）下载到 MCUboot 次级槽（Secondary Slot）。

阻塞至整个镜像写入完成或传输失败。下载失败会使槽位仅被部分写入，MCUboot 将拒绝该镜像；在后续一次下载成功之前，`fota_http_apply()` 也会拒绝它。因 SHA-256 或降级检查（Downgrade Check）而被拒绝的镜像将被擦除。

这里只存储镜像。调用 `fota_http_apply()` 才会安排启动该镜像。

当运行中的镜像为测试镜像（Test Image）时，次级槽位保存 MCUboot 用于回退的镜像。因此，在调用 `fota_http_confirm()` 之前，将拒绝下载。

调用者的栈必须足以容纳 HTTP 客户端，以及使用 HTTPS 时的 TLS 握手（Handshake）；`fota_http_download_async()` 则使用库线程。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `params` | 下载参数（Download Parameters）。所指向的数据必须保持有效，直到调用返回。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 镜像已写入，且头部有效。 |
| `-EINVAL` | URL 无法解析，或超过缓冲区大小限制。 |
| `-ENOTSUP` | 不支持该 URL 方案（Scheme）。 |
| `-ENODEV` | `image_index` 对应的槽位不存在。 |
| `-EBUSY` | 另一个下载正在进行。 |
| `-EBADMSG` | 服务器返回了非预期的状态。 |
| `-ELOOP` | 重定向次数超过 `CONFIG_FOTA_HTTP_MAX_REDIRECTS`。 |
| `-ENODATA` | 服务器发送了空响应体（Body）。 |
| `-EMSGSIZE` | 收到的字节数少于服务器声明的数量。 |
| `-ECANCELED` | 调用了 `fota_http_cancel()`。 |
| `-EILSEQ` | SHA-256 摘要（Digest）不匹配，镜像已擦除。 |
| `-ENOEXEC` | 写入的数据不是 MCUboot 镜像。 |
| `-EPERM` | 运行中的镜像尚未确认，或者下载的镜像比运行中的镜像更旧且已被擦除。 |
| `-errno` | 任何套接字（Socket）、HTTP 客户端或闪存错误。 |

<a id="gaf730ea430346720f05dd7f290eef69c6"></a>

### `fota_http_download_async()`

```c
int fota_http_download_async ( const struct fota_http_download_params * params, fota_http_done_cb_t done_cb )
```

```c
#include <zephyr/mgmt/fota_http.h>
```

在库线程（Library Thread）中下载固件镜像（Firmware Image）。

传输加入队列后立即返回。将调用 `done_cb`，并传入 `fota_http_download()` 本应返回的结果。

要求启用 `CONFIG_FOTA_HTTP_ASYNC`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `params` | 下载参数（Download Parameters）。结构体与 URL 会被复制；结构体所指向的其他数据必须保持有效，直到 `done_cb` 执行。 |
| `done_cb` | 完成回调（Completion Callback），可为 `NULL`。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 下载已加入队列。 |
| `-EINVAL` | `params` 或其 URL 为 `NULL`，或者 URL 过长。 |
| `-ENOTSUP` | `CONFIG_FOTA_HTTP_ASYNC` 未启用。 |
| `-EPERM` | 运行中的镜像尚未确认（Confirmed）。 |
| `-EBUSY` | 另一个下载正在进行。 |

<a id="ga7f0b137c19a30942725406abdcf89497"></a>

### `fota_http_get_download_slot()`

```c
int fota_http_get_download_slot ( uint8_t image_index)
```

```c
#include <zephyr/mgmt/fota_http.h>
```

下载写入槽的闪存区域标识符（Flash Area Identifier）。

对于直接原地执行（Direct-XIP）的引导加载程序，槽位在链接时已经固定，因此调用者必须获取针对该槽位构建的镜像变体。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `image_index` | 要查询其次级槽位（Secondary Slot）的镜像。 |

**返回（Returns）**：返回值（Returns）：闪存区域标识符（Flash Area Identifier）；镜像没有次级槽位时，返回负 `errno` 错误码。

<a id="ga56ce2026ec720e06f67ae8d7f780609c"></a>

### `fota_http_get_image_header()`

```c
int fota_http_get_image_header ( uint8_t image_index, struct mcuboot_img_header * header )
```

```c
#include <zephyr/mgmt/fota_http.h>
```

读取次级槽（Secondary Slot）中镜像的 MCUboot 头（Header）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `image_index` | 要读取其次级槽位（Secondary Slot）的镜像。 |
| `header` | 输出头部（Output Header）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 读取到了有效头部。 |
| `-EIO` | 槽位中没有有效镜像。 |
| `-errno` | 任何闪存（Flash）错误。 |

<a id="gac3f298c4501aa85afa63dc08a6ddf1bf"></a>

### `fota_http_nvm_bytes_written()`

```c
size_t fota_http_nvm_bytes_written ( void )
```

```c
#include <zephyr/mgmt/fota_http.h>
```

最近一次下载写入非易失性存储器（Non-volatile Memory）的字节数。

**返回（Returns）**：返回值（Returns）：槽位内的字节数；未执行过下载时为 0。

<a id="ga511dd696af7bd7b61a9924ca64964f32"></a>

### `fota_http_tls_add_ca()`

```c
int fota_http_tls_add_ca ( const void * cert, size_t len )
```

```c
#include <zephyr/mgmt/fota_http.h>
```

注册用于认证 HTTPS 服务器的 CA 证书（CA Certificate）。

证书存储在 `CONFIG_FOTA_HTTP_TLS_SEC_TAG` 指定的安全标签下。应用若已通过 `tls_credential_add()` 在该标签下注册了证书，就无需调用此函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cert` | DER 或 PEM 编码的证书（Certificate）。不会复制证书，因此只要还会执行 HTTPS 下载，证书就必须保持有效。 |
| `len` | `cert` 的大小，单位为字节。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="gacdeabce6009b1b1b9b10cfe6fe9fd9d9"></a>

### `fota_http_tls_add_client_cert()`

```c
int fota_http_tls_add_client_cert ( const void * cert, size_t cert_len, const void * key, size_t key_len )
```

```c
#include <zephyr/mgmt/fota_http.h>
```

注册双向 TLS（Mutual TLS）使用的客户端证书和密钥（Client Certificate and Key）。

二者均存储在 `CONFIG_FOTA_HTTP_TLS_SEC_TAG` 指定的安全标签下，且均不会被复制。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cert` | DER 或 PEM 编码的客户端证书（Client Certificate）。 |
| `cert_len` | `cert` 的大小，单位为字节。 |
| `key` | DER 或 PEM 编码的私钥（Private Key）。 |
| `key_len` | `key` 的大小，单位为字节。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。


## 3.5\_原页交叉引用（Cross References）

- [fota_http_progress](../system_service_model_reference/P038_fota_http_progress_结构体.md)
- [fota_http_download_params](../system_service_model_reference/P037_fota_http_download_params_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [mcuboot_img_header](../boot_control_reference/P006_MCUboot镜像头结构.md)
- [zephyr/mgmt/fota_http.h](../api_file_protocol_service_reference/P014_zephyr__mgmt__fota_http.h_文件参考.md)
- [CONFIG_FOTA_HTTP_MAX_REDIRECTS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FOTA_HTTP_MAX_REDIRECTS)
- [CONFIG_FOTA_HTTP_ASYNC](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FOTA_HTTP_ASYNC)
- [CONFIG_FOTA_HTTP_TLS_SEC_TAG](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FOTA_HTTP_TLS_SEC_TAG)
- [tls_credential_add()](../api_memory_timer_topic_reference/P011_传输层安全（TLS）的凭据管理。.md#ga640ff6dd3eb4d5017feaab6fab2bb2f7)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P002_协调集标识配置文件（Coordinated Set Identification Profile，CSIP）.md) · [返回大纲](大纲.md) · [下一章](P004_HTTP响应状态码（Response Status Codes）。.md)
