---
id: learning.zephyr-docs.api-file-service-reference.page-40
title: zephyr__psa__ps_ids.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ps__ids_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第40章\_zephyr\_\_psa\_\_ps\_ids.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ps__ids_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

此文件定义PSA受保护存储（PS）API现有使用者的UID范围。

查看此文件的源码。

<a id="details"></a>

本文件定义 PSA 受保护存储 API（PSA PS API）现有使用者的唯一标识范围（UID Ranges）。另请参见（See Also）`zephyr/psa/key_ids.h`。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 40.1\_宏定义（Macros）

<a id="r_ad539bfba58f6ce5e81e92ee9e1ba656f"></a>

```c
#define ZEPHYR_PSA_SETTINGS_TFM_PS_UID_RANGE_BEGIN 0x2C000000
```

相关声明：[ZEPHYR_PSA_SETTINGS_TFM_PS_UID_RANGE_BEGIN](#ad539bfba58f6ce5e81e92ee9e1ba656f)。

供 TF-M PSA PS 设置后端（Settings Backend）使用的唯一标识范围（UID Range）。

<a id="r_a1419b6eac22ee96e74913fd4d448eff7"></a>

```c
#define ZEPHYR_PSA_SETTINGS_TFM_PS_UID_RANGE_SIZE 0x10000
```

相关声明：[ZEPHYR_PSA_SETTINGS_TFM_PS_UID_RANGE_SIZE](#a1419b6eac22ee96e74913fd4d448eff7)。

64 Ki（64 × 1024）。

<a id="r_a55e471f3a2c38989162d838d2e79a4f9"></a>

```c
#define ZEPHYR_PSA_TLS_CREDENTIALS_PS_UID_RANGE_BEGIN 0xC2E0000000000000
```

相关声明：[ZEPHYR_PSA_TLS_CREDENTIALS_PS_UID_RANGE_BEGIN](#a55e471f3a2c38989162d838d2e79a4f9)。

供传输层安全凭据的受保护存储后端（TLS Credentials PS Backend）使用的唯一标识范围（UID Range）。

<a id="r_a3bd964fda5fdf6abdbc42308dfd98de7"></a>

```c
#define ZEPHYR_PSA_TLS_CREDENTIALS_PS_UID_RANGE_SIZE 0x0001000000000000
```

相关声明：[ZEPHYR_PSA_TLS_CREDENTIALS_PS_UID_RANGE_SIZE](#a3bd964fda5fdf6abdbc42308dfd98de7)。

数值（Value）：`2^48`。

## 40.2\_详细说明（Detailed Documentation）

<a id="ad539bfba58f6ce5e81e92ee9e1ba656f"></a>

### `ZEPHYR_PSA_SETTINGS_TFM_PS_UID_RANGE_BEGIN`

```c
#define ZEPHYR_PSA_SETTINGS_TFM_PS_UID_RANGE_BEGIN 0x2C000000
```

供 TF-M PSA PS 设置后端（Settings Backend）使用的唯一标识范围（UID Range）。

<a id="a1419b6eac22ee96e74913fd4d448eff7"></a>

### `ZEPHYR_PSA_SETTINGS_TFM_PS_UID_RANGE_SIZE`

```c
#define ZEPHYR_PSA_SETTINGS_TFM_PS_UID_RANGE_SIZE 0x10000
```

64 Ki（64 × 1024）。

<a id="a55e471f3a2c38989162d838d2e79a4f9"></a>

### `ZEPHYR_PSA_TLS_CREDENTIALS_PS_UID_RANGE_BEGIN`

```c
#define ZEPHYR_PSA_TLS_CREDENTIALS_PS_UID_RANGE_BEGIN 0xC2E0000000000000
```

供传输层安全凭据的受保护存储后端（TLS Credentials PS Backend）使用的唯一标识范围（UID Range）。

<a id="a3bd964fda5fdf6abdbc42308dfd98de7"></a>

### `ZEPHYR_PSA_TLS_CREDENTIALS_PS_UID_RANGE_SIZE`

```c
#define ZEPHYR_PSA_TLS_CREDENTIALS_PS_UID_RANGE_SIZE 0x0001000000000000
```

数值（Value）：`2^48`。


## 40.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P678_ps_ids.h_源码浏览.md)
- [zephyr/psa/key_ids.h](https://docs.zephyrproject.org/latest/doxygen/html/key__ids_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P039_zephyr__net__promiscuous.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P041_zephyr__net__ptp.h_文件参考.md)
