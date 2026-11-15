---
id: learning.zephyr-docs.device-power-control-model-reference.page-92
title: svc_driver_api_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsvc__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第92章\_svc\_driver\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsvc__driver__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

sip_svc驱动的API结构。

```c
#include <zephyr/drivers/sip_svc/sip_svc_driver.h>
```

<a id="details"></a>

sip_svc驱动的API结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 92.1\_数据成员（Data Fields）

<a id="r_a5f02e921d2a038616fad9d8d6a052f6b"></a>

```c
sip_supervisory_call_t sip_supervisory_call
```

相关声明：[sip_supervisory_call_t](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__driver_8h.html#a15714e3852882693de6c9c7f2229bcd1)、[sip_supervisory_call](#a5f02e921d2a038616fad9d8d6a052f6b)。

<a id="r_a9f0a7711ef5ba2900d378c0a2805eaf4"></a>

```c
sip_svc_plat_func_id_valid_t sip_svc_plat_func_id_valid
```

相关声明：[sip_svc_plat_func_id_valid_t](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__driver_8h.html#ac5921c9cdc00604651696e1580f30797)、[sip_svc_plat_func_id_valid](#a9f0a7711ef5ba2900d378c0a2805eaf4)。

<a id="r_a6435b703d30f462c1ec38e533a9c0817"></a>

```c
sip_svc_plat_format_trans_id_t sip_svc_plat_format_trans_id
```

相关声明：[sip_svc_plat_format_trans_id_t](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__driver_8h.html#a3cf78c760c6eae2091e92329e54b1a31)、[sip_svc_plat_format_trans_id](#a6435b703d30f462c1ec38e533a9c0817)。

<a id="r_a30a435265fa828d9fdfcc70664be0945"></a>

```c
sip_svc_plat_get_trans_idx_t sip_svc_plat_get_trans_idx
```

相关声明：[sip_svc_plat_get_trans_idx_t](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__driver_8h.html#a35145ddf422e8782b4ec37270b04d98c)、[sip_svc_plat_get_trans_idx](#a30a435265fa828d9fdfcc70664be0945)。

<a id="r_a0ccdebec2a60d32a1767c5e47bc3ae25"></a>

```c
sip_svc_plat_update_trans_id_t sip_svc_plat_update_trans_id
```

相关声明：[sip_svc_plat_update_trans_id_t](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__driver_8h.html#a9d61db0484e2aacce4515290ffb4450c)、[sip_svc_plat_update_trans_id](#a0ccdebec2a60d32a1767c5e47bc3ae25)。

<a id="r_a484b7c6ef4777a61e8f4f8e6778a7b45"></a>

```c
sip_svc_plat_free_async_memory_t sip_svc_plat_free_async_memory
```

相关声明：[sip_svc_plat_free_async_memory_t](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__driver_8h.html#ab32e31bdba00ff66303fab1b04cd0ebe)、[sip_svc_plat_free_async_memory](#a484b7c6ef4777a61e8f4f8e6778a7b45)。

<a id="r_a79ac1f8410b7f0883ceb0a96823fbdf4"></a>

```c
sip_svc_plat_async_res_req_t sip_svc_plat_async_res_req
```

相关声明：[sip_svc_plat_async_res_req_t](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__driver_8h.html#aa49a26b4b503e58d23fb5087ed701a0a)、[sip_svc_plat_async_res_req](#a79ac1f8410b7f0883ceb0a96823fbdf4)。

<a id="r_a1d94fdfb564caa84e3f18f2139ae4fe0"></a>

```c
sip_svc_plat_async_res_res_t sip_svc_plat_async_res_res
```

相关声明：[sip_svc_plat_async_res_res_t](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__driver_8h.html#a54293f84f9bc86661f8a4bf717ad4754)、[sip_svc_plat_async_res_res](#a1d94fdfb564caa84e3f18f2139ae4fe0)。

<a id="r_ae148bb010e4a0c2913e1c7425565316a"></a>

```c
sip_svc_plat_get_error_code_t sip_svc_plat_get_error_code
```

相关声明：[sip_svc_plat_get_error_code_t](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__driver_8h.html#a926eeecea766b2131c03c57111a186f8)、[sip_svc_plat_get_error_code](#ae148bb010e4a0c2913e1c7425565316a)。

## 92.2\_详细说明（Detailed Documentation）

<a id="a5f02e921d2a038616fad9d8d6a052f6b"></a>

### `sip_supervisory_call`

```c
sip_supervisory_call_t svc_driver_api::sip_supervisory_call
```

<a id="a79ac1f8410b7f0883ceb0a96823fbdf4"></a>

### `sip_svc_plat_async_res_req`

```c
sip_svc_plat_async_res_req_t svc_driver_api::sip_svc_plat_async_res_req
```

<a id="a1d94fdfb564caa84e3f18f2139ae4fe0"></a>

### `sip_svc_plat_async_res_res`

```c
sip_svc_plat_async_res_res_t svc_driver_api::sip_svc_plat_async_res_res
```

<a id="a6435b703d30f462c1ec38e533a9c0817"></a>

### `sip_svc_plat_format_trans_id`

```c
sip_svc_plat_format_trans_id_t svc_driver_api::sip_svc_plat_format_trans_id
```

<a id="a484b7c6ef4777a61e8f4f8e6778a7b45"></a>

### `sip_svc_plat_free_async_memory`

```c
sip_svc_plat_free_async_memory_t svc_driver_api::sip_svc_plat_free_async_memory
```

<a id="a9f0a7711ef5ba2900d378c0a2805eaf4"></a>

### `sip_svc_plat_func_id_valid`

```c
sip_svc_plat_func_id_valid_t svc_driver_api::sip_svc_plat_func_id_valid
```

<a id="ae148bb010e4a0c2913e1c7425565316a"></a>

### `sip_svc_plat_get_error_code`

```c
sip_svc_plat_get_error_code_t svc_driver_api::sip_svc_plat_get_error_code
```

<a id="a30a435265fa828d9fdfcc70664be0945"></a>

### `sip_svc_plat_get_trans_idx`

```c
sip_svc_plat_get_trans_idx_t svc_driver_api::sip_svc_plat_get_trans_idx
```

<a id="a0ccdebec2a60d32a1767c5e47bc3ae25"></a>

### `sip_svc_plat_update_trans_id`

```c
sip_svc_plat_update_trans_id_t svc_driver_api::sip_svc_plat_update_trans_id
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/sip_svc/sip_svc_driver.h`

## 92.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sip_svc/sip_svc_driver.h](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__driver_8h_source.html)
- [sip_supervisory_call_t](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__driver_8h.html#a15714e3852882693de6c9c7f2229bcd1)
- [sip_svc_plat_func_id_valid_t](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__driver_8h.html#ac5921c9cdc00604651696e1580f30797)
- [sip_svc_plat_format_trans_id_t](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__driver_8h.html#a3cf78c760c6eae2091e92329e54b1a31)
- [sip_svc_plat_get_trans_idx_t](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__driver_8h.html#a35145ddf422e8782b4ec37270b04d98c)
- [sip_svc_plat_update_trans_id_t](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__driver_8h.html#a9d61db0484e2aacce4515290ffb4450c)
- [sip_svc_plat_free_async_memory_t](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__driver_8h.html#ab32e31bdba00ff66303fab1b04cd0ebe)
- [sip_svc_plat_async_res_req_t](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__driver_8h.html#aa49a26b4b503e58d23fb5087ed701a0a)
- [sip_svc_plat_async_res_res_t](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__driver_8h.html#a54293f84f9bc86661f8a4bf717ad4754)
- [sip_svc_plat_get_error_code_t](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__driver_8h.html#a926eeecea766b2131c03c57111a186f8)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P091_st_transfer_properties_结构体.md) · [返回大纲](大纲.md) · [下一章](P093_tcpc_chip_info_结构体.md)
